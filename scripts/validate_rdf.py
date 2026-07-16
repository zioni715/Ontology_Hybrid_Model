"""Parse all PCPO Turtle inputs and perform baseline RDF checks."""

from __future__ import annotations

import sys

from rdflib import Graph, Namespace, RDF, RDFS, XSD

from common import (
    INVALID_DATA_FILE,
    ONTOLOGY_FILES,
    VALID_DATA_FILE,
    ProjectError,
    invalid_overlay_graph,
    relative,
    valid_graph,
)


FORBIDDEN_NAMESPACES = (
    Namespace("http://www.w3.org/2002/07/owl#"),
    Namespace("http://www.w3.org/ns/shacl#"),
    Namespace("http://www.w3.org/2003/11/swrl#"),
)

PCPO = Namespace("https://example.org/pcpo#")
DECIMAL_PROPERTIES = {
    PCPO[name]
    for name in (
        "contractQuantityValue",
        "contractUnitPriceValue",
        "contractAmountValue",
        "previousCumulativeQuantityValue",
        "currentProgressQuantityValue",
        "cumulativeQuantityValue",
        "remainingQuantityValue",
        "appliedContractUnitPriceValue",
        "previousCumulativeAmountValue",
        "currentProgressAmountValue",
        "cumulativeAmountValue",
        "aggregatedCurrentAmountValue",
        "quantityToleranceValue",
        "amountToleranceValue",
        "barDiameterValue",
        "barLengthValue",
        "baseLengthValue",
        "spliceLengthValue",
        "anchorageLengthValue",
        "totalBarLengthValue",
        "unitWeightValue",
        "rebarWeightValue",
        "designStrengthValue",
        "maxAggregateSizeValue",
        "slumpValue",
        "dimensionLengthValue",
        "dimensionWidthValue",
        "dimensionHeightValue",
        "grossVolumeValue",
        "deductionVolumeValue",
        "netVolumeValue",
        "contactLengthValue",
        "contactHeightValue",
        "grossContactAreaValue",
        "openingDeductionAreaValue",
        "netContactAreaValue",
        "installationHeightValue",
        "supportAreaValue",
        "supportVolumeValue",
    )
}


def parse_individually() -> None:
    """Parse every PCPO Turtle source separately for file-specific errors."""

    for path in (*ONTOLOGY_FILES, VALID_DATA_FILE, INVALID_DATA_FILE):
        graph = Graph()
        graph.parse(path, format="turtle")
        print(f"[OK] {relative(path)}: {len(graph)} triples")


def check_forbidden_terms(graph: Graph) -> None:
    """Ensure the requested RDF/RDFS/SPARQL core does not use excluded vocabularies."""

    violations: list[str] = []
    for subject, predicate, obj in graph:
        for term in (subject, predicate, obj):
            text = str(term)
            if any(text.startswith(str(namespace)) for namespace in FORBIDDEN_NAMESPACES):
                violations.append(text)
    if violations:
        unique = ", ".join(sorted(set(violations)))
        raise ProjectError(f"Excluded OWL/SHACL/SWRL terms found in PCPO graph: {unique}")


def check_schema_documentation(graph: Graph) -> None:
    """Require core schema terms to have the requested RDFS metadata."""

    issues: list[str] = []
    for class_uri in graph.subjects(RDF.type, RDFS.Class):
        labels = list(graph.objects(class_uri, RDFS.label))
        languages = {label.language for label in labels}
        if not {"ko", "en"}.issubset(languages):
            issues.append(f"{class_uri} needs Korean and English labels")
        if not any(graph.objects(class_uri, RDFS.comment)):
            issues.append(f"{class_uri} needs an rdfs:comment")

    for property_uri in graph.subjects(RDF.type, RDF.Property):
        labels = list(graph.objects(property_uri, RDFS.label))
        languages = {label.language for label in labels}
        if not {"ko", "en"}.issubset(languages):
            issues.append(f"{property_uri} needs Korean and English labels")
        if not any(graph.objects(property_uri, RDFS.comment)):
            issues.append(f"{property_uri} needs an rdfs:comment")
        if not any(graph.objects(property_uri, RDFS.domain)):
            issues.append(f"{property_uri} needs an rdfs:domain")
        if not any(graph.objects(property_uri, RDFS.range)):
            issues.append(f"{property_uri} needs an rdfs:range")

    if issues:
        raise ProjectError("Schema documentation errors:\n- " + "\n- ".join(issues))


def check_decimal_datatypes(graph: Graph) -> None:
    """Ensure quantity, unit-price, and amount values are numeric literals."""

    issues: list[str] = []
    for property_uri in DECIMAL_PROPERTIES:
        for subject, value in graph.subject_objects(property_uri):
            if value.datatype != XSD.decimal:
                issues.append(f"{subject} {property_uri} {value!r} is not xsd:decimal")
    if issues:
        raise ProjectError("Numeric datatype errors:\n- " + "\n- ".join(issues))


def main() -> int:
    try:
        parse_individually()
        valid = valid_graph()
        invalid = invalid_overlay_graph()
        check_forbidden_terms(valid)
        check_schema_documentation(valid)
        check_decimal_datatypes(invalid)
        print(f"[OK] PCPO valid graph loaded: {len(valid)} triples")
        print(f"[OK] PCPO invalid overlay graph loaded: {len(invalid)} triples")
        print("[OK] Class/property documentation and numeric datatypes verified")
        print("RDF validation completed successfully.")
        return 0
    except Exception as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
