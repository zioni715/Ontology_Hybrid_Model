"""Create a formal class/property visualization from the hand-authored ontology."""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

from rdflib import Graph, Literal, Namespace, RDF, RDFS, URIRef


ROOT = Path(__file__).resolve().parents[1]
ONTOLOGY_FILES = (
    ROOT / "ontology" / "schema.ttl",
    ROOT / "ontology" / "classes.ttl",
    ROOT / "ontology" / "properties.ttl",
    ROOT / "ontology" / "code-lists.ttl",
)
OUTPUT_FILE = Path(__file__).resolve().parent / "ontology_data.js"
HTML_FILE = Path(__file__).resolve().parent / "ontology_graph.html"
EMBED_START = "/* RCPP_DATA_START */"
EMBED_END = "/* RCPP_DATA_END */"

RCPP = Namespace("https://example.org/rcpp#")
XSD = Namespace("http://www.w3.org/2001/XMLSchema#")
PREFIXES = (
    (str(RCPP), "rcpp:"),
    (str(RDF), "rdf:"),
    (str(RDFS), "rdfs:"),
    (str(XSD), "xsd:"),
)

DOCUMENT_Y = {
    RCPP.QuantityCalculationSheet: 100,
    RCPP.ContractStatement: 260,
    RCPP.WorkTypeDetailStatement: 420,
    RCPP.WorkTypeSummaryStatement: 580,
    RCPP.PreviousProgressStatement: 740,
    RCPP.CurrentProgressQuantitySheet: 900,
    RCPP.SupportingReferenceDocument: 1060,
    RCPP.CurrentProgressStatement: 1240,
}

SCHEMA_POSITIONS = {
    "Project": (70, 80),
    "ProgressPaymentRound": (280, 80),
    "ProgressDocument": (70, 500),
    "SourceDocument": (250, 400),
    "OutputDocument": (250, 970),
    "QuantityCalculationSheet": (450, 80),
    "ContractStatement": (450, 190),
    "WorkTypeDetailStatement": (450, 300),
    "WorkTypeSummaryStatement": (450, 410),
    "PreviousProgressStatement": (450, 520),
    "CurrentProgressQuantitySheet": (450, 630),
    "SupportingReferenceDocument": (450, 760),
    "UnitPriceAnalysisStatement": (650, 690),
    "PriceCalculationStatement": (650, 800),
    "CostStatement": (650, 910),
    "CurrentProgressStatement": (450, 970),
    "DocumentRole": (850, 1000),
    "DocumentItem": (900, 520),
    "DetailCostItem": (1060, 420),
    "SummaryCostItem": (1060, 690),
    "QuantityCalculationItem": (1240, 80),
    "ContractStatementItem": (1240, 190),
    "WorkTypeDetailItem": (1240, 300),
    "WorkTypeSummaryItem": (1240, 690),
    "PreviousProgressStatementItem": (1240, 410),
    "CurrentProgressQuantityItem": (1240, 520),
    "SupportingReferenceItem": (1060, 830),
    "CurrentProgressStatementItem": (1240, 830),
    "CurrentProgressDetailItem": (1430, 610),
    "CurrentProgressSummaryItem": (1430, 760),
    "DocumentItemMatching": (1400, 260),
    "ProgressQuantityRollupCalculation": (1430, 500),
    "ProgressAmountCalculation": (1570, 320),
    "CurrentProgressAmountCalculation": (1790, 250),
    "ProgressSummaryCalculation": (1790, 420),
    "ConsistencyRule": (2010, 520),
    "CostItem": (2280, 300),
    "WorkCategory": (2280, 760),
    "Unit": (2500, 760),
    "RebarCostItem": (2500, 80),
    "ConcreteCostItem": (2500, 245),
    "FormworkCostItem": (2500, 410),
    "ShoringCostItem": (2500, 575),
    "ControlledSpecificationValue": (2280, 930),
    "RebarGrade": (2500, 900),
    "RebarWorkType": (2700, 900),
    "FormworkType": (2900, 900),
    "ComplexityLevel": (3110, 900),
    "ShoringType": (2500, 1030),
    "InstallationEnvironment": (2760, 1030),
    "PlacementMethod": (3060, 1030),
}

# The complete-class view contains substantially more nodes and links than the
# focused views below.  Stretch its vertical lanes and slightly compress its
# horizontal span so that the initial SVG fit uses the available panel height
# instead of rendering a very wide, small graph.
SCHEMA_X_SCALE = 0.90
SCHEMA_Y_SCALE = 1.55
SCHEMA_X_OFFSET = 50
SCHEMA_Y_OFFSET = 60

SPECIFICATION_POSITIONS = {
    "CostItem": (150, 380),
    "RebarCostItem": (560, 80),
    "ConcreteCostItem": (560, 260),
    "ReadyMixedConcreteCostItem": (900, 200),
    "ConcretePlacementCostItem": (900, 330),
    "FormworkCostItem": (560, 500),
    "ShoringCostItem": (560, 680),
}

DOCUMENT_FLOW_POSITIONS = {
    "QuantityCalculationSheet": (100, 170),
    "ContractStatement": (360, 170),
    "WorkTypeDetailStatement": (620, 170),
    "WorkTypeSummaryStatement": (880, 170),
    "PreviousProgressStatement": (100, 470),
    "CurrentProgressQuantitySheet": (500, 470),
    "CurrentProgressStatement": (1240, 320),
}

ITEM_MATCHING_POSITIONS = {
    "QuantityCalculationItem": (110, 130),
    "ContractStatementItem": (400, 130),
    "WorkTypeDetailItem": (690, 130),
    "WorkTypeSummaryItem": (1030, 130),
    "PreviousProgressStatementItem": (110, 440),
    "ProgressQuantityDetailItem": (340, 600),
    "CurrentProgressQuantityItem": (580, 440),
    "DocumentItemMatching": (590, 285),
    "CurrentProgressDetailItem": (720, 420),
    "CurrentProgressSummaryItem": (1050, 440),
}

AMOUNT_CALCULATION_POSITIONS = {
    "contractUnitPrice": (100, 150),
    "progressCurrentQuantity": (100, 410),
    "outputContractUnitPrice": (390, 150),
    "outputCurrentQuantity": (390, 410),
    "CalculationPolicy": (620, 80),
    "UnitConversionRule": (650, 470),
    "CurrentProgressAmountCalculation": (840, 280),
    "CalculationActivity": (1070, 440),
    "outputCurrentAmount": (1120, 280),
    "CurrentProgressStatement": (1420, 280),
}

FLOW_CLASS_POSITIONS = {
    "Project": (70, 80),
    "ProgressPaymentRound": (250, 80),
    "ProgressDocument": (70, 700),
    "SourceDocument": (250, 580),
    "OutputDocument": (250, 1240),
    "QuantityCalculationSheet": (450, 100),
    "ContractStatement": (450, 260),
    "WorkTypeDetailStatement": (450, 420),
    "WorkTypeSummaryStatement": (450, 580),
    "PreviousProgressStatement": (450, 740),
    "CurrentProgressQuantitySheet": (450, 900),
    "SupportingReferenceDocument": (450, 1060),
    "CurrentProgressStatement": (450, 1240),
    "QuantityCalculationItem": (650, 100),
    "ContractStatementItem": (650, 260),
    "WorkTypeDetailItem": (650, 420),
    "WorkTypeSummaryItem": (650, 580),
    "PreviousProgressStatementItem": (650, 740),
    "CurrentProgressQuantityItem": (650, 900),
    "SupportingReferenceItem": (650, 1060),
    "CurrentProgressStatementItem": (650, 1240),
    "CurrentProgressDetailItem": (830, 1190),
    "CurrentProgressSummaryItem": (830, 1290),
    "DocumentItemMatching": (1135, 250),
    "ProgressAmountCalculation": (1135, 690),
    "ProgressSummaryCalculation": (1135, 940),
    "ConsistencyRule": (1135, 1080),
    "ProgressQuantityRollupCalculation": (1135, 530),
    "WorkTypeDetailStatement": (360, 1245),
    "WorkTypeSummaryStatement": (550, 1245),
    "UnitPriceAnalysisStatement": (740, 1245),
    "PriceCalculationStatement": (930, 1245),
    "CostStatement": (1120, 1245),
    "ControlledSpecificationValue": (1360, 760),
    "RebarGrade": (1570, 560),
    "RebarWorkType": (1770, 560),
    "PlacementMethod": (1970, 560),
    "FormworkType": (1570, 700),
    "ComplexityLevel": (1770, 700),
    "ShoringType": (1970, 700),
    "InstallationEnvironment": (2170, 700),
}

FIELD_RELATIONS = {
    RCPP.mapsDirectlyTo: ("direct", "그대로 전달"),
    RCPP.matchesWithField: ("matching", "매칭 기준"),
    RCPP.calculationInputFor: ("calculation", "산식 입력"),
    RCPP.consistencyComparedWith: ("consistency", "일관성 비교"),
    RCPP.aggregatesTo: ("aggregation", "집계 전달"),
    RCPP.groupsByField: ("grouping", "그룹 기준"),
}

CLASS_RELATIONS = {
    RCPP.typicalNextDocumentClass: ("document-flow", "대표 서류 흐름"),
    RCPP.schemaFlowsTo: ("object", "스키마상 다음 단계"),
    RCPP.expectedItemClass: ("object", "예상 서류 내역 클래스"),
    RCPP.producesField: ("calculation", "산출항목 생성"),
    RCPP.expectedCostItemClass: ("object", "예상 표준 비용항목"),
    RCPP.expectedWorkCategoryClass: ("object", "예상 표준 공종"),
    RCPP.expectedUnitClass: ("object", "예상 표준 단위"),
    RCPP.expectedAmountCalculationClass: ("calculation", "예상 금액 계산"),
    RCPP.expectedCorrespondingItemClass: ("matching", "예상 동일 내역 대응"),
    RCPP.expectedUnitPriceSourceClass: ("calculation", "예상 계약단가 출처"),
    RCPP.expectedSourceItemClass: ("direct", "예상 내역값 파생 근거"),
    RCPP.expectedIdentificationReferenceClass: ("matching", "예상 품목식별 참고"),
    RCPP.expectedQuantityBasisClass: ("direct", "예상 계약수량 근거"),
    RCPP.expectedPreviousQuantitySourceClass: ("direct", "예상 전회누계 출처"),
    RCPP.expectedAggregationTargetClass: ("aggregation", "예상 집계 대상"),
    RCPP.inputQuantityProperty: ("calculation", "금회수량 입력속성"),
    RCPP.inputUnitPriceProperty: ("calculation", "계약단가 입력속성"),
    RCPP.inputToCalculationClass: ("calculation", "금액계산 입력 전달"),
    RCPP.expectedRequirementTargetClass: ("object", "필드요구 대상"),
}

CLASS_SIGNATURE_RELATIONS = {
    RCPP.belongsToProject: "프로젝트 소속",
    RCPP.belongsToProgressRound: "기성회차 소속",
    RCPP.usesCalculationPolicy: "계산정책 적용",
    RCPP.appliesRule: "실행 계산규칙",
    RCPP.appliesPolicy: "실행 계산정책",
    RCPP.usesUnitConversionRule: "단위변환규칙 사용",
    RCPP.calculationRound: "계산 기성회차",
    RCPP.sourceItem: "매칭 원천항목",
    RCPP.targetItem: "매칭 대상항목",
    RCPP.matchedCostItem: "매칭 표준 비용항목",
    RCPP.quantityAggregatedInto: "기성수량 집계",
    RCPP.hasSourceLocation: "원천위치 연결",
    RCPP.currency: "통화 사용",
    RCPP.roundingMode: "반올림 방식 사용",
    RCPP.hasDocumentRole: "서류역할 사용",
    # These are existing cost-item properties. Their domain/range links keep
    # the controlled-value classes connected in the complete-class view while
    # actual values such as SD400 remain property values, not graph nodes.
    RCPP.rebarGrade: "강종 속성",
    RCPP.rebarWorkType: "철근 작업유형 속성",
    RCPP.placementMethod: "타설방법 속성",
    RCPP.formworkType: "거푸집 종류 속성",
    RCPP.complexityLevel: "복잡도 속성",
    RCPP.shoringType: "동바리 종류 속성",
    RCPP.installationEnvironment: "설치환경 속성",
}


class VisualizationError(RuntimeError):
    """Raised when ontology sources cannot produce visualization data."""


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_ontology() -> Graph:
    graph = Graph()
    for path in ONTOLOGY_FILES:
        if not path.is_file():
            raise VisualizationError(f"Required file does not exist: {relative(path)}")
        try:
            graph.parse(path, format="turtle")
        except Exception as exc:
            raise VisualizationError(f"Failed to parse {relative(path)}: {exc}") from exc
    return graph


def compact(term: object) -> str:
    text = str(term)
    for namespace, prefix in PREFIXES:
        if text.startswith(namespace):
            return prefix + text[len(namespace) :]
    return text


def local_name(term: URIRef) -> str:
    text = str(term)
    return text.rsplit("#", 1)[-1].rsplit("/", 1)[-1]


def localized_literal(
    graph: Graph, subject: URIRef, predicate: URIRef, language: str | None = None
) -> str:
    values = list(graph.objects(subject, predicate))
    if language is not None:
        for value in values:
            if isinstance(value, Literal) and value.language == language:
                return str(value)
    for preferred in ("ko", "en", None):
        for value in values:
            if isinstance(value, Literal) and value.language == preferred:
                return str(value)
    return str(values[0]) if values else ""


def literal_values(graph: Graph, subject: URIRef, predicate: URIRef) -> list[str]:
    return sorted({str(value) for value in graph.objects(subject, predicate)})


def label_for(graph: Graph, subject: URIRef) -> str:
    return localized_literal(graph, subject, RDFS.label, "ko") or local_name(subject)


def graph_level(graph: Graph, subject: URIRef) -> str:
    return localized_literal(graph, subject, RCPP.graphLevel) or "detail"


def ancestors(graph: Graph, class_uri: URIRef) -> list[URIRef]:
    ordered: list[URIRef] = []
    queue = [class_uri]
    while queue:
        current = queue.pop(0)
        if current in ordered:
            continue
        ordered.append(current)
        queue.extend(
            parent
            for parent in graph.objects(current, RDFS.subClassOf)
            if isinstance(parent, URIRef) and str(parent).startswith(str(RCPP))
        )
    return ordered


def property_owners(graph: Graph, property_uri: URIRef) -> set[URIRef]:
    return {
        value
        for predicate in (RDFS.domain, RCPP.appliesToClass)
        for value in graph.objects(property_uri, predicate)
        if isinstance(value, URIRef)
    }


def property_detail(graph: Graph, property_uri: URIRef) -> dict[str, object]:
    owners = sorted(property_owners(graph, property_uri), key=str)
    documents = sorted(graph.objects(property_uri, RCPP.fieldOfDocument), key=str)
    ranges = sorted(graph.objects(property_uri, RDFS.range), key=str)
    required_by = sorted(
        {
            required_class
            for requirement in graph.subjects(RCPP.requiredProperty, property_uri)
            if localized_literal(graph, requirement, RCPP.requirementLevel, "ko")
            == "필수"
            for required_class in graph.objects(requirement, RCPP.requiredForClass)
            if isinstance(required_class, URIRef)
        },
        key=str,
    )
    return {
        "id": str(property_uri),
        "iri": compact(property_uri),
        "label": label_for(graph, property_uri),
        "description": localized_literal(graph, property_uri, RDFS.comment, "ko"),
        "category": localized_literal(graph, property_uri, RCPP.propertyCategory)
        or "기타",
        "range": ", ".join(compact(value) for value in ranges),
        "owners": [label_for(graph, owner) for owner in owners],
        "documents": [label_for(graph, document) for document in documents],
        "required": bool(required_by),
        "requiredForClasses": [label_for(graph, value) for value in required_by],
        "outputColumnGroup": localized_literal(
            graph, property_uri, RCPP.outputColumnGroup
        ),
        "specificationRequirement": localized_literal(
            graph, property_uri, RCPP.specificationRequirement, "ko"
        ),
        "inclusionCondition": localized_literal(
            graph, property_uri, RCPP.inclusionCondition, "ko"
        ),
        "examples": literal_values(graph, property_uri, RCPP.exampleValue),
        "sourceFieldLabels": literal_values(graph, property_uri, RCPP.sourceFieldLabel),
        "superProperties": [
            compact(value)
            for value in sorted(graph.objects(property_uri, RDFS.subPropertyOf), key=str)
            if isinstance(value, URIRef)
        ],
        "formulas": literal_values(graph, property_uri, RCPP.formulaExpression)
        + [
            f"[교차검토] {value}"
            for value in literal_values(
                graph, property_uri, RCPP.crossCheckFormulaExpression
            )
        ],
        "level": graph_level(graph, property_uri),
    }


def details_for_class(
    graph: Graph, class_uri: URIRef, properties: set[URIRef]
) -> list[dict[str, object]]:
    lineage = set(ancestors(graph, class_uri))
    details = []
    for property_uri in properties:
        field_documents = {
            value
            for value in graph.objects(property_uri, RCPP.fieldOfDocument)
            if isinstance(value, URIRef)
        }
        if property_owners(graph, property_uri) & lineage or field_documents & lineage:
            details.append(property_detail(graph, property_uri))
    return sorted(details, key=lambda item: (str(item["category"]), str(item["label"])))


def class_node(
    graph: Graph, class_uri: URIRef, properties: set[URIRef]
) -> dict[str, object]:
    name = local_name(class_uri)
    level = graph_level(graph, class_uri)
    group = localized_literal(graph, class_uri, RCPP.visualizationGroup)
    raw_schema_x, raw_schema_y = SCHEMA_POSITIONS.get(name, (900, 1080))
    schema_x = SCHEMA_X_OFFSET + raw_schema_x * SCHEMA_X_SCALE
    schema_y = SCHEMA_Y_OFFSET + raw_schema_y * SCHEMA_Y_SCALE
    flow_x, flow_y = FLOW_CLASS_POSITIONS.get(name, (900, 1320))
    specification_x, specification_y = SPECIFICATION_POSITIONS.get(
        name, (900, 760)
    )
    document_flow_x, document_flow_y = DOCUMENT_FLOW_POSITIONS.get(name, (900, 720))
    item_matching_x, item_matching_y = ITEM_MATCHING_POSITIONS.get(name, (900, 720))
    amount_x, amount_y = AMOUNT_CALCULATION_POSITIONS.get(name, (900, 620))
    expected_roles = sorted(graph.objects(class_uri, RCPP.expectedDocumentRole), key=str)
    lineage = ancestors(graph, class_uri)
    is_document = RCPP.ProgressDocument in lineage
    is_item = RCPP.DocumentItem in lineage
    node_type = "document" if is_document else "process"
    if is_item:
        node_type = "item"
    if group in {"calculation-type", "amount-calculation", "calculation-rule", "calculation-activity"}:
        node_type = "calculation"
    if group == "context":
        node_type = "context"
    if group == "cost-item":
        node_type = "cost-item"
    if group == "specification":
        node_type = "specification"
    if group == "reference-concept":
        node_type = "reference"
    if RCPP.ControlledSpecificationValue in lineage or class_uri in {
        RCPP.Currency,
        RCPP.RoundingMode,
    }:
        node_type = "code-list"
    if class_uri == RCPP.ProgressDocument:
        node_type = "root"
    return {
        "id": str(class_uri),
        "iri": compact(class_uri),
        "name": name,
        "label": label_for(graph, class_uri),
        "description": localized_literal(graph, class_uri, RDFS.comment, "ko"),
        "stage": localized_literal(graph, class_uri, RCPP.processStage, "ko"),
        "code": localized_literal(graph, class_uri, RCPP.documentCode),
        "role": ", ".join(label_for(graph, role) for role in expected_roles),
        "level": level,
        "group": group,
        "nodeType": node_type,
        "primary": level == "core",
        "parents": [
            label_for(graph, parent)
            for parent in graph.objects(class_uri, RDFS.subClassOf)
            if isinstance(parent, URIRef)
        ],
        "formulas": literal_values(graph, class_uri, RCPP.formulaExpression)
        + [
            f"[교차검토] {value}"
            for value in literal_values(
                graph, class_uri, RCPP.crossCheckFormulaExpression
            )
        ],
        "properties": details_for_class(graph, class_uri, properties),
        "schemaX": schema_x,
        "schemaY": schema_y,
        "flowX": flow_x,
        "flowY": flow_y,
        "specificationX": specification_x,
        "specificationY": specification_y,
        "documentFlowX": document_flow_x,
        "documentFlowY": document_flow_y,
        "itemMatchingX": item_matching_x,
        "itemMatchingY": item_matching_y,
        "amountX": amount_x,
        "amountY": amount_y,
        "x": schema_x,
        "y": schema_y,
    }


def field_position(graph: Graph, property_uri: URIRef, owner: URIRef) -> tuple[float, float]:
    def sort_key(candidate: URIRef) -> tuple[float, str]:
        order_text = localized_literal(graph, candidate, RCPP.fieldOrder)
        return (float(order_text) if order_text else 999.0, str(candidate))

    siblings = sorted(
        (
            candidate
            for candidate in graph.subjects(RCPP.fieldOfDocument, owner)
            if isinstance(candidate, URIRef)
            and graph_level(graph, candidate) in {"core", "extended"}
        ),
        key=sort_key,
    )
    index = siblings.index(property_uri)
    x = 850 + index * 110
    y = DOCUMENT_Y.get(owner, 520)
    return x, y


def field_node(graph: Graph, property_uri: URIRef) -> dict[str, object]:
    detail = property_detail(graph, property_uri)
    owners = [
        value
        for value in graph.objects(property_uri, RCPP.fieldOfDocument)
        if isinstance(value, URIRef)
    ]
    owner = owners[0]
    x, y = field_position(graph, property_uri, owner)
    amount_x, amount_y = AMOUNT_CALCULATION_POSITIONS.get(
        local_name(property_uri), (900, 620)
    )
    return {
        **detail,
        "name": local_name(property_uri),
        "stage": "서류내역 매핑·계산",
        "code": "",
        "role": "필수 데이터 항목" if detail["required"] else "파생·확장 데이터 항목",
        "group": f"field-{local_name(owner)}",
        "nodeType": "field",
        "primary": detail["level"] == "core",
        "parents": [],
        "properties": [],
        "ownerDocument": str(owner),
        "ownerLabel": label_for(graph, owner),
        "schemaX": x,
        "schemaY": y,
        "flowX": x,
        "flowY": y,
        "documentFlowX": x,
        "documentFlowY": y,
        "itemMatchingX": x,
        "itemMatchingY": y,
        "amountX": amount_x,
        "amountY": amount_y,
        "x": x,
        "y": y,
    }


def relation_record(
    graph: Graph,
    source: URIRef,
    target: URIRef,
    predicate: URIRef,
    kind: str,
    label: str,
    primary: bool,
) -> dict[str, object]:
    return {
        "source": str(source),
        "target": str(target),
        "predicate": compact(predicate),
        "label": label,
        "description": localized_literal(graph, predicate, RDFS.comment, "ko"),
        "kind": kind,
        "primary": primary,
    }


def build_payload() -> dict[str, object]:
    graph = load_ontology()
    classes = {
        value
        for value in graph.subjects(RDF.type, RDFS.Class)
        if isinstance(value, URIRef) and str(value).startswith(str(RCPP))
    }
    properties = {
        value
        for value in graph.subjects(RDF.type, RDF.Property)
        if isinstance(value, URIRef) and str(value).startswith(str(RCPP))
    }

    visible_classes = set(classes)
    visible_fields = {
        property_uri
        for property_uri in properties
        if graph_level(graph, property_uri) in {"core", "extended"}
        and any(graph.objects(property_uri, RCPP.fieldOfDocument))
    }

    nodes = [
        class_node(graph, class_uri, properties)
        for class_uri in sorted(visible_classes, key=str)
    ] + [
        field_node(graph, property_uri)
        for property_uri in sorted(visible_fields, key=str)
    ]
    node_ids = {node["id"] for node in nodes}
    level_by_id = {node["id"]: node["level"] for node in nodes}

    links: list[dict[str, object]] = []
    seen: set[tuple[str, str, str]] = set()

    for child, parent in graph.subject_objects(RDFS.subClassOf):
        if child not in visible_classes or parent not in visible_classes:
            continue
        key = (str(child), str(parent), "hierarchy")
        if key in seen:
            continue
        seen.add(key)
        links.append(
            {
                "source": str(child),
                "target": str(parent),
                "predicate": "rdfs:subClassOf",
                "label": "하위 클래스",
                "description": "RDFS 클래스 상속 관계",
                "kind": "hierarchy",
                "primary": True,
            }
        )

    for predicate, (kind, label) in CLASS_RELATIONS.items():
        for source, target in graph.subject_objects(predicate):
            if str(source) not in node_ids or str(target) not in node_ids:
                continue
            key = (str(source), str(target), kind)
            if key in seen:
                continue
            seen.add(key)
            links.append(
                relation_record(
                    graph,
                    source,
                    target,
                    predicate,
                    kind,
                    label,
                    level_by_id[str(source)] == "core"
                    and level_by_id[str(target)] == "core",
                )
            )

    # Show selected object-property schema signatures as class-level links.
    # These relations already exist in the ontology through domain/range or
    # appliesToClass; rendering them prevents context and policy classes from
    # appearing as disconnected process nodes.
    for predicate, label in CLASS_SIGNATURE_RELATIONS.items():
        sources = {
            value
            for schema_predicate in (RDFS.domain, RCPP.appliesToClass)
            for value in graph.objects(predicate, schema_predicate)
            if value in visible_classes
        }
        targets = {
            value
            for value in graph.objects(predicate, RDFS.range)
            if value in visible_classes
        }
        for source in sorted(sources, key=str):
            for target in sorted(targets, key=str):
                if source == target:
                    continue
                key = (str(source), str(target), "object")
                if key in seen:
                    continue
                seen.add(key)
                links.append(
                    relation_record(
                        graph,
                        source,
                        target,
                        predicate,
                        "object",
                        label,
                        graph_level(graph, source) == "core"
                        and graph_level(graph, target) == "core",
                    )
                )

    for predicate, (kind, label) in FIELD_RELATIONS.items():
        symmetric = predicate == RCPP.consistencyComparedWith
        for source, target in graph.subject_objects(predicate):
            if source not in visible_fields or target not in visible_fields:
                continue
            source_id, target_id = str(source), str(target)
            key_source, key_target = (
                sorted((source_id, target_id)) if symmetric else (source_id, target_id)
            )
            key = (key_source, key_target, kind)
            if key in seen:
                continue
            seen.add(key)
            links.append(
                relation_record(
                    graph,
                    source,
                    target,
                    predicate,
                    kind,
                    label,
                    level_by_id[source_id] == "core"
                    and level_by_id[target_id] == "core",
                )
            )

    for property_uri in sorted(visible_fields, key=str):
        for domain in graph.objects(property_uri, RDFS.domain):
            if str(domain) not in node_ids:
                continue
            key = (str(property_uri), str(domain), "domain")
            if key in seen:
                continue
            seen.add(key)
            links.append(
                {
                    "source": str(property_uri),
                    "target": str(domain),
                    "predicate": "rdfs:domain",
                    "label": "적용 항목 클래스",
                    "description": "rdf:Property가 어느 문서항목 클래스에 적용되는지 명시한다.",
                    "kind": "domain",
                    "primary": level_by_id[str(property_uri)] == "core",
                }
            )

    by_node: dict[str, dict[str, list[dict[str, object]]]] = defaultdict(
        lambda: {"outgoing": [], "incoming": []}
    )
    for relation in links:
        by_node[str(relation["source"])]["outgoing"].append(relation)
        by_node[str(relation["target"])]["incoming"].append(relation)
    for node in nodes:
        node["relations"] = by_node[str(node["id"])]

    return {
        "title": "RCPP 핵심 기성금액 온톨로지",
        "description": "프로젝트·기성회차별 서류 역할, 서류 내역, 표준 비용항목, 공종별 속성, 단위 변환과 금회기성액 계산 관계를 표시합니다. 수량산식·산출근거·산출수량은 수량산출서 내역의 속성값으로 표시합니다.",
        "generatedFrom": [relative(path) for path in ONTOLOGY_FILES],
        "viewBox": [0, 0, 3000, 1800],
        "flowViewBox": [0, 0, 4700, 1450],
        "specificationViewBox": [0, 0, 1150, 800],
        "documentFlowViewBox": [0, 0, 1400, 650],
        "itemMatchingViewBox": [0, 0, 1250, 720],
        "amountCalculationViewBox": [0, 0, 1580, 620],
        "nodes": nodes,
        "links": links,
    }


def build_output() -> str:
    return "window.RCPP_GRAPH_DATA = " + json.dumps(
        build_payload(), ensure_ascii=False, indent=2, sort_keys=True
    ) + ";\n"


def html_with_embedded_data(output: str) -> str:
    if not HTML_FILE.is_file():
        raise VisualizationError(f"Missing {relative(HTML_FILE)}")
    html = HTML_FILE.read_text(encoding="utf-8")
    if EMBED_START not in html or EMBED_END not in html:
        raise VisualizationError(
            f"Missing embedded-data markers in {relative(HTML_FILE)}"
        )
    before, remainder = html.split(EMBED_START, 1)
    _, after = remainder.split(EMBED_END, 1)
    return f"{before}{EMBED_START}\n{output.rstrip()}\n{EMBED_END}{after}"


def embedded_output(html: str) -> str:
    if EMBED_START not in html or EMBED_END not in html:
        return ""
    return html.split(EMBED_START, 1)[1].split(EMBED_END, 1)[0].strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail when ontology_data.js is missing or stale",
    )
    args = parser.parse_args()
    try:
        expected = build_output()
        if args.check:
            if not OUTPUT_FILE.is_file():
                raise VisualizationError(f"Missing {relative(OUTPUT_FILE)}")
            if OUTPUT_FILE.read_text(encoding="utf-8") != expected:
                raise VisualizationError(
                    f"Stale {relative(OUTPUT_FILE)}; run "
                    "python visualization/generate_visualization_data.py"
                )
            html = HTML_FILE.read_text(encoding="utf-8") if HTML_FILE.is_file() else ""
            if embedded_output(html) != expected.strip():
                raise VisualizationError(
                    f"Stale embedded data in {relative(HTML_FILE)}; run "
                    "python visualization/generate_visualization_data.py"
                )
            print(
                f"[OK] {relative(OUTPUT_FILE)} and standalone "
                f"{relative(HTML_FILE)} are current"
            )
            return 0

        OUTPUT_FILE.write_text(expected, encoding="utf-8")
        HTML_FILE.write_text(html_with_embedded_data(expected), encoding="utf-8")
        print(
            f"Wrote {relative(OUTPUT_FILE)} and embedded data in "
            f"{relative(HTML_FILE)}"
        )
        return 0
    except Exception as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
