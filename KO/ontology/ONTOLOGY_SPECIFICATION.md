# RCPP 온톨로지 명세서

- 온톨로지 버전: `1.0.0`
- 명세서 생성일: `2026-07-28`
- 네임스페이스: `https://example.org/rcpp#`
- 전체 트리플: **3,260개**
- 클래스: **63개**
- 속성: **246개**
- 기타 명명 자원: **107개**
- 내부 관계 트리플: **867개**

- 구성: `schema.ttl`, `classes.ttl`, `properties.ttl`, `code-lists.ttl`에 선언된 RCPP 온톨로지 용어
- 수록내용: 클래스·속성·규칙·통제값 설명 및 내부 자원 간 관계 트리플

## 1. 적용 범위

- 연구범위: RCPP는 Reinforced Concrete Progress Payment의 약어임. 기성서류를 핵심 업무개념으로 유지하면서 Project와 ProgressPaymentRound를 실제 데이터의 적용 문맥으로 명시함. 연구 범위는 철근콘크리트공종의 철근·콘크리트·거푸집·동바리 수량 및 기성금액 산정이며 실제 시공·검측·품질 판정은 제외함.

- 주요 처리: 확정된 계약내역·전회 누계값·금회기성수량 연결 → 철근·콘크리트·거푸집·동바리 기성금액 계산 → 공사기성부분내역서 구성

## 2. 표기 원칙

- `rcpp:`: 본 온톨로지의 네임스페이스
- 클래스: 개념의 유형
- 속성: 개체의 값 또는 개체 간 관계
- 규칙: 규칙 클래스와 실제 적용 규칙 개체 구분
- 원문·표준값: 서류 원문 문자열과 정규화된 공종·단위·비용항목 개체 병행 보존
- 내부 관계 트리플: 주어와 목적어가 모두 RCPP 명명 자원인 트리플 전체

## 3. 클래스 명세

### 3.1. `CalculationActivity` — 계산 실행

- 설명: 특정 프로젝트와 기성회차에서 계산규칙·정책·입력항목·출력항목을 적용하여 실제 결과를 만든 실행 기록.
- IRI: `rcpp:CalculationActivity`
- 상위 클래스: -
- 적용 속성: `rcpp:appliesPolicy`, `rcpp:appliesRule`, `rcpp:calculationInputItem`, `rcpp:calculationOutputItem`, `rcpp:calculationRound`, `rcpp:calculationStatus`, `rcpp:usesUnitConversionRule`

### 3.2. `CalculationPolicy` — 금액 계산정책

- 설명: 통화, 반올림 방식, 금액 소수점 자릿수와 계산순서를 프로젝트 기성회차에 적용하는 정책.
- IRI: `rcpp:CalculationPolicy`
- 상위 클래스: -
- 적용 속성: `rcpp:amountTolerance`, `rcpp:calculationOrder`, `rcpp:currency`, `rcpp:decimalScale`, `rcpp:quantityTolerance`, `rcpp:roundingMode`

### 3.3. `CalculationRule` — 계산규칙

- 설명: 재사용 가능한 산식 정의와 입력속성·출력속성·적용조건·단위조건·처리단계를 표현하는 규칙의 상위 클래스.
- IRI: `rcpp:CalculationRule`
- 상위 클래스: -
- 적용 속성: `rcpp:applicationCondition`, `rcpp:processingStage`, `rcpp:unitCondition`

### 3.4. `ComplexityLevel` — 복잡도

- 설명: 간단·보통·복잡처럼 계약단가를 구분하는 표준 난이도 코드목록.
- IRI: `rcpp:ComplexityLevel`
- 상위 클래스: `rcpp:ControlledSpecificationValue`
- 적용 속성: -

### 3.5. `ConcreteCostItem` — 콘크리트 비용항목

- 설명: 철근콘크리트공종의 콘크리트 표준 비용항목 상위 클래스. 재료비 성격의 레미콘과 시공비 성격의 콘크리트 타설은 각각 하위 클래스로 구분하고 해당 계약단가 식별속성을 적용함.
- IRI: `rcpp:ConcreteCostItem`
- 상위 클래스: `rcpp:CostItem`
- 적용 속성: -

### 3.6. `ConcretePlacementCostItem` — 콘크리트 타설 비용항목

- 설명: 타설방법·적용부위·물량구간·작업조건 등 시공비 구분요소로 계약단가를 식별하는 콘크리트 타설 비용항목.
- IRI: `rcpp:ConcretePlacementCostItem`
- 상위 클래스: `rcpp:ConcreteCostItem`
- 적용 속성: `rcpp:applicationPart`, `rcpp:maximumQuantityThreshold`, `rcpp:minimumQuantityThreshold`, `rcpp:placementCondition`, `rcpp:placementMethod`, `rcpp:quantityBand`, `rcpp:usesVibrator`

### 3.7. `ConsistencyRule` — 기성데이터 일관성 규칙

- 설명: 별도 검증 결과를 만드는 클래스가 아니라 자동 산정 전에 서류 간 값과 계산 한계를 확인하기 위한 온톨로지 규칙 정의.
- IRI: `rcpp:ConsistencyRule`
- 상위 클래스: -
- 적용 속성: -
- 주요 관계:
  - `rcpp:schemaFlowsTo` → `rcpp:CurrentProgressStatement`

### 3.8. `ContractStatement` — 계약내역서

- 설명: 품목코드, 공종·세부품목, 규격, 단위, 계약수량, 계약단가와 계약금액을 제공하는 산정 근거서류. 도급금액·도급액 같은 원문 표현은 sourceFieldLabel로 보존함.
- IRI: `rcpp:ContractStatement`
- 상위 클래스: `rcpp:SourceDocument`
- 적용 속성: -
- 주요 관계:
  - `rcpp:expectedDocumentRole` → `rcpp:ContractBasisDocumentRole`
  - `rcpp:expectedItemClass` → `rcpp:ContractStatementItem`
  - `rcpp:schemaFlowsTo` → `rcpp:DocumentItemMatching`
  - `rcpp:typicalNextDocumentClass` → `rcpp:WorkTypeDetailStatement`

### 3.9. `ContractStatementItem` — 계약내역 항목

- 설명: 계약 품목코드, 공사내역, 규격, 단위와 도급 조건을 담는 행.
- IRI: `rcpp:ContractStatementItem`
- 상위 클래스: `rcpp:DetailCostItem`
- 적용 속성: `rcpp:contractAmount`, `rcpp:contractItemCode`, `rcpp:contractItemName`, `rcpp:contractQuantity`, `rcpp:contractQuantityBasis`, `rcpp:contractSpecification`, `rcpp:contractUnit`, `rcpp:contractUnitPrice`, `rcpp:contractWorkType`, `rcpp:quantityBasisFrom`
- 주요 관계:
  - `rcpp:expectedCostItemClass` → `rcpp:CostItem`
  - `rcpp:expectedSourceItemClass` → `rcpp:QuantityCalculationItem`

### 3.10. `ControlledSpecificationValue` — 표준 속성값

- 설명: 프로젝트마다 다른 원문 표현을 하나의 계약단가 식별용 표준값으로 정규화하는 코드목록의 상위 클래스.
- IRI: `rcpp:ControlledSpecificationValue`
- 상위 클래스: -
- 적용 속성: `rcpp:codeValue`, `rcpp:sourceValueAlias`

### 3.11. `CostItem` — 표준 비용항목

- 설명: 프로젝트와 기성회차에 독립적으로 품명·공종·정규화 규격속성·표준단위를 식별하는 철근콘크리트공종의 기준 비용항목. 공종별 규격은 별도 노드가 아니라 하위 공종 비용항목에 직접 정의된 속성값으로 기록함. 계약수량·계약단가·기성수량·기성금액은 프로젝트별 서류 내역 개체에 기록함.
- IRI: `rcpp:CostItem`
- 상위 클래스: -
- 적용 속성: `rcpp:belongsToWorkCategory`, `rcpp:costItemCode`, `rcpp:costItemName`, `rcpp:normalizedSpecificationCode`, `rcpp:usesSpecificationRule`, `rcpp:usesUnit`
- 주요 관계:
  - `rcpp:expectedUnitClass` → `rcpp:Unit`
  - `rcpp:expectedWorkCategoryClass` → `rcpp:WorkCategory`
  - `rcpp:schemaFlowsTo` → `rcpp:DocumentItemMatching`

### 3.12. `CostStatement` — 원가계산서

- 설명: 직접공사비·간접비·총공사비 구성의 총괄 근거를 제공함.
- IRI: `rcpp:CostStatement`
- 상위 클래스: `rcpp:SupportingReferenceDocument`
- 적용 속성: -

### 3.13. `Currency` — 통화

- 설명: 기성금액 계산에 사용하는 통화 코드목록.
- IRI: `rcpp:Currency`
- 상위 클래스: -
- 적용 속성: `rcpp:codeValue`

### 3.14. `CurrentProgressAmountCalculation` — 금회기성금액 산정규칙

- 설명: 기성수량산출서의 금회기성수량과 대응 계약 내역의 계약단가를 결합하여 공사기성부분내역서의 금회기성금액을 산출하는 계산규칙 유형.
- IRI: `rcpp:CurrentProgressAmountCalculation`
- 상위 클래스: `rcpp:ProgressAmountCalculation`
- 적용 속성: -
- 주요 관계:
  - `rcpp:inputQuantityProperty` → `rcpp:progressCurrentQuantity`
  - `rcpp:inputUnitPriceProperty` → `rcpp:contractUnitPrice`
  - `rcpp:producesField` → `rcpp:outputCurrentAmount`
  - `rcpp:schemaFlowsTo` → `rcpp:CurrentProgressStatement`

### 3.15. `CurrentProgressDetailItem` — 공사기성 상세항목

- 설명: 공사내역, 규격, 단위, 계약금액, 전회누계기성금액, 금회기성금액과 적요를 구성하는 결과서류의 품목별 상세 행.
- IRI: `rcpp:CurrentProgressDetailItem`
- 상위 클래스: `rcpp:CurrentProgressStatementItem`, `rcpp:DetailCostItem`
- 적용 속성: `rcpp:outputContractAmount`, `rcpp:outputContractQuantity`, `rcpp:outputContractUnitPrice`, `rcpp:outputCumulativeAmount`, `rcpp:outputCumulativeQuantity`, `rcpp:outputCumulativeRate`, `rcpp:outputCurrentAmount`, `rcpp:outputCurrentQuantity`, `rcpp:outputCurrentRate`, `rcpp:outputItemCode`, `rcpp:outputPreviousAmount`, `rcpp:outputPreviousQuantity`, `rcpp:outputPreviousRate`, `rcpp:outputRemainingAmount`, `rcpp:outputRemainingQuantity`, `rcpp:outputRemarks`, `rcpp:outputSpecification`, `rcpp:outputUnit`, `rcpp:outputWorkDescription`, `rcpp:outputWorkType`
- 주요 관계:
  - `rcpp:expectedAggregationTargetClass` → `rcpp:CurrentProgressSummaryItem`
  - `rcpp:expectedCorrespondingItemClass` → `rcpp:ContractStatementItem`
  - `rcpp:expectedCorrespondingItemClass` → `rcpp:CurrentProgressQuantityItem`
  - `rcpp:expectedCorrespondingItemClass` → `rcpp:PreviousProgressStatementItem`
  - `rcpp:expectedCostItemClass` → `rcpp:CostItem`
  - `rcpp:expectedSourceItemClass` → `rcpp:ContractStatementItem`
  - `rcpp:expectedSourceItemClass` → `rcpp:CurrentProgressQuantityItem`
  - `rcpp:expectedSourceItemClass` → `rcpp:PreviousProgressStatementItem`
  - `rcpp:expectedUnitPriceSourceClass` → `rcpp:ContractStatementItem`

### 3.16. `CurrentProgressQuantityItem` — 기성수량 항목

- 설명: 동일 계약 내역의 전회누계값과 비용산정용으로 확정 입력된 금회기성수량을 바탕으로 누계·잔여 기성수량을 담는 행. 수량산출 내역은 계약수량과 품목 식별의 참고자료이며 금회기성수량의 직접 출처가 아니다.
- IRI: `rcpp:CurrentProgressQuantityItem`
- 상위 클래스: `rcpp:DocumentItem`
- 적용 속성: `rcpp:previousQuantityFrom`, `rcpp:progressCumulativeQuantity`, `rcpp:progressCurrentQuantity`, `rcpp:progressPreviousCumulativeQuantity`, `rcpp:progressQuantityItemCode`, `rcpp:progressQuantityItemName`, `rcpp:progressQuantitySpecification`, `rcpp:progressQuantityUnit`, `rcpp:progressQuantityWorkType`, `rcpp:progressRemainingQuantity`
- 주요 관계:
  - `rcpp:expectedCorrespondingItemClass` → `rcpp:ContractStatementItem`
  - `rcpp:expectedCorrespondingItemClass` → `rcpp:PreviousProgressStatementItem`
  - `rcpp:expectedCostItemClass` → `rcpp:CostItem`
  - `rcpp:expectedIdentificationReferenceClass` → `rcpp:ContractStatementItem`
  - `rcpp:expectedIdentificationReferenceClass` → `rcpp:QuantityCalculationItem`
  - `rcpp:expectedPreviousQuantitySourceClass` → `rcpp:PreviousProgressStatementItem`
  - `rcpp:expectedQuantityBasisClass` → `rcpp:QuantityCalculationItem`
  - `rcpp:expectedSourceItemClass` → `rcpp:PreviousProgressStatementItem`
  - `rcpp:expectedSourceItemClass` → `rcpp:ProgressQuantityDetailItem`

### 3.17. `CurrentProgressQuantitySheet` — 기성수량산출서

- 설명: 전회누계기성수량과 비용산정용으로 확정 입력된 금회기성수량을 품목별로 기록하고, 이를 이용하여 누계기성수량과 잔여수량을 계산하여 공사기성부분내역서에 제공하는 서류. 검측 및 실제 시공 여부 판정은 포함하지 않음.
- IRI: `rcpp:CurrentProgressQuantitySheet`
- 상위 클래스: `rcpp:SourceDocument`
- 적용 속성: -
- 주요 관계:
  - `rcpp:expectedDocumentRole` → `rcpp:ProgressQuantityDocumentRole`
  - `rcpp:expectedItemClass` → `rcpp:CurrentProgressQuantityItem`
  - `rcpp:expectedItemClass` → `rcpp:ProgressQuantityDetailItem`
  - `rcpp:schemaFlowsTo` → `rcpp:DocumentItemMatching`
  - `rcpp:schemaFlowsTo` → `rcpp:ProgressQuantityRollupCalculation`
  - `rcpp:typicalNextDocumentClass` → `rcpp:CurrentProgressStatement`

### 3.18. `CurrentProgressStatement` — 공사기성부분내역서

- 설명: 계약내역서의 계약기준정보, 기성수량산출서의 금회수량, 공종별내역서·공종별집계표의 구성근거를 연결하고 금액 산식을 적용하여 작성하는 목표 서류.
- IRI: `rcpp:CurrentProgressStatement`
- 상위 클래스: `rcpp:OutputDocument`
- 적용 속성: -
- 주요 관계:
  - `rcpp:expectedAmountCalculationClass` → `rcpp:CurrentProgressAmountCalculation`
  - `rcpp:expectedDocumentRole` → `rcpp:ProgressStatementDocumentRole`
  - `rcpp:expectedItemClass` → `rcpp:CurrentProgressDetailItem`
  - `rcpp:expectedItemClass` → `rcpp:CurrentProgressSummaryItem`

### 3.19. `CurrentProgressStatementItem` — 공사기성 내역항목

- 설명: 공사기성부분내역서의 상세 행과 결과서류 내부 집계 행을 포괄하는 상위 개념.
- IRI: `rcpp:CurrentProgressStatementItem`
- 상위 클래스: `rcpp:DocumentItem`
- 적용 속성: -

### 3.20. `CurrentProgressSummaryItem` — 공사기성 집계항목

- 설명: 공사기성부분내역서 안에서 품목별 상세금액을 철근·콘크리트·거푸집·동바리 및 철근콘크리트공사 합계로 집계하는 행.
- IRI: `rcpp:CurrentProgressSummaryItem`
- 상위 클래스: `rcpp:CurrentProgressStatementItem`, `rcpp:SummaryCostItem`
- 적용 속성: `rcpp:outputReinforcedConcreteAmount`, `rcpp:outputSummaryContractAmount`, `rcpp:outputSummaryCumulativeAmount`, `rcpp:outputSummaryCurrentAmount`, `rcpp:outputSummaryPreviousAmount`, `rcpp:outputSummaryWorkCategoryText`
- 주요 관계:
  - `rcpp:expectedSourceItemClass` → `rcpp:CurrentProgressDetailItem`

### 3.21. `DetailCostItem` — 품목별 상세항목

- 설명: 품명·규격·단위·수량·단가·금액을 가지며 다른 서류의 동일 표준 비용항목과 대응하는 품목별 상세 행.
- IRI: `rcpp:DetailCostItem`
- 상위 클래스: `rcpp:DocumentItem`
- 적용 속성: `rcpp:aggregatedInto`
- 주요 관계:
  - `rcpp:expectedAggregationTargetClass` → `rcpp:SummaryCostItem`

### 3.22. `DocumentItem` — 서류 항목

- 설명: 서류의 한 행 또는 함께 식별되는 데이터 묶음을 포괄하는 상위 개념. 서류 간 매칭은 내역 식별정보와 개별 필드 관계로 정의함.
- IRI: `rcpp:DocumentItem`
- 상위 클래스: -
- 적용 속성: `rcpp:belongsToWorkCategory`, `rcpp:correspondsToItem`, `rcpp:derivedFrom`, `rcpp:hasAmountValue`, `rcpp:hasItemCode`, `rcpp:hasItemName`, `rcpp:hasQuantityValue`, `rcpp:hasSourceLocation`, `rcpp:hasSourceUnitText`, `rcpp:hasSourceWorkCategoryText`, `rcpp:hasSpecificationText`, `rcpp:hasUnitPriceValue`, `rcpp:identificationReferencedFrom`, `rcpp:representsCostItem`, `rcpp:usesUnit`, `rcpp:usesUnitPriceFrom`
- 주요 관계:
  - `rcpp:expectedUnitClass` → `rcpp:Unit`
  - `rcpp:expectedWorkCategoryClass` → `rcpp:WorkCategory`

### 3.23. `DocumentItemMatching` — 서류내역 매칭

- 설명: 내역코드와 공종을 보조키로 사용하고 품명·정규화된 비용 관련 규격요소·단위를 함께 비교하여 수량산출서·계약내역서·공종별내역서·기성수량산출서·공사기성부분내역서의 동일 표준 비용항목과 계약단가를 연결함.
- IRI: `rcpp:DocumentItemMatching`
- 상위 클래스: -
- 적용 속성: `rcpp:confidenceScore`, `rcpp:matchedCostItem`, `rcpp:matchingEvidence`, `rcpp:matchingMethod`, `rcpp:reviewStatus`, `rcpp:reviewedBy`, `rcpp:sourceItem`, `rcpp:targetItem`
- 주요 관계:
  - `rcpp:schemaFlowsTo` → `rcpp:CurrentProgressAmountCalculation`

### 3.24. `DocumentRole` — 서류 역할

- 설명: 프로젝트마다 파일명과 파일 구성이 달라도 계약기준·수량근거·세부비용·비용집계·기성수량·기성결과 중 어떤 기능을 수행하는지 분류하는 역할 개념. 하나의 실제 서류가 둘 이상의 역할을 수행가능.
- IRI: `rcpp:DocumentRole`
- 상위 클래스: -
- 적용 속성: -

### 3.25. `FieldRequirement` — 항목값 요구조건

- 설명: 필수 여부를 속성 하나에 전역으로 부여하지 않고 요구 속성·적용 클래스·요구수준의 조합으로 표현하는 규칙 개체.
- IRI: `rcpp:FieldRequirement`
- 상위 클래스: -
- 적용 속성: `rcpp:requiredForClass`, `rcpp:requiredProperty`, `rcpp:requirementLevel`, `rcpp:requirementPurpose`
- 주요 관계:
  - `rcpp:expectedRequirementTargetClass` → `rcpp:CalculationActivity`
  - `rcpp:expectedRequirementTargetClass` → `rcpp:DocumentItem`
  - `rcpp:expectedRequirementTargetClass` → `rcpp:DocumentItemMatching`

### 3.26. `FormworkCostItem` — 거푸집 비용항목

- 설명: 거푸집 종류·복잡도·전용횟수·수직고구간·작업유형을 속성값으로 가지고 계약단가를 식별하는 표준 비용항목. 노드를 클릭하면 적용 속성·예시·포함조건을 확인가능.
- IRI: `rcpp:FormworkCostItem`
- 상위 클래스: `rcpp:CostItem`
- 적용 속성: `rcpp:applicationPart`, `rcpp:complexityLevel`, `rcpp:formworkType`, `rcpp:formworkWorkType`, `rcpp:isExposedFinish`, `rcpp:maximumVerticalHeight`, `rcpp:minimumVerticalHeight`, `rcpp:reuseCount`, `rcpp:verticalHeightBand`

### 3.27. `FormworkType` — 거푸집 유형

- 설명: 합판거푸집·유로폼처럼 재료 또는 공법에 따른 거푸집 종류 코드목록.
- IRI: `rcpp:FormworkType`
- 상위 클래스: `rcpp:ControlledSpecificationValue`
- 적용 속성: -

### 3.28. `InstallationEnvironment` — 설치환경

- 설명: 육상·수상처럼 동바리 설치 장소와 환경을 구분하는 코드목록.
- IRI: `rcpp:InstallationEnvironment`
- 상위 클래스: `rcpp:ControlledSpecificationValue`
- 적용 속성: -

### 3.29. `OutputDocument` — 산정 결과서류

- 설명: 산정 근거서류의 항목을 매칭하고 산식을 적용하여 작성하는 결과 서류.
- IRI: `rcpp:OutputDocument`
- 상위 클래스: `rcpp:ProgressDocument`
- 적용 속성: -

### 3.30. `PlacementMethod` — 타설방법

- 설명: 펌프카 타설·인력 타설처럼 콘크리트 타설방식을 구분하는 코드목록.
- IRI: `rcpp:PlacementMethod`
- 상위 클래스: `rcpp:ControlledSpecificationValue`
- 적용 속성: -

### 3.31. `PreviousProgressStatement` — 전회 공사기성부분내역서

- 설명: 전회까지의 누계기성수량·누계기성금액·기성비율을 제공하는 산정 근거서류.
- IRI: `rcpp:PreviousProgressStatement`
- 상위 클래스: `rcpp:SourceDocument`
- 적용 속성: -
- 주요 관계:
  - `rcpp:expectedDocumentRole` → `rcpp:PreviousProgressBasisDocumentRole`
  - `rcpp:expectedItemClass` → `rcpp:PreviousProgressStatementItem`
  - `rcpp:schemaFlowsTo` → `rcpp:DocumentItemMatching`
  - `rcpp:typicalNextDocumentClass` → `rcpp:CurrentProgressQuantitySheet`

### 3.32. `PreviousProgressStatementItem` — 전회 기성항목

- 설명: 전회까지의 누계수량·누계금액·비율을 담는 행.
- IRI: `rcpp:PreviousProgressStatementItem`
- 상위 클래스: `rcpp:DetailCostItem`
- 적용 속성: `rcpp:previousCumulativeAmount`, `rcpp:previousCumulativeQuantity`, `rcpp:previousCumulativeRate`, `rcpp:previousItemCode`, `rcpp:previousSpecification`, `rcpp:previousUnit`, `rcpp:previousWorkDescription`
- 주요 관계:
  - `rcpp:expectedCorrespondingItemClass` → `rcpp:ContractStatementItem`
  - `rcpp:expectedCostItemClass` → `rcpp:CostItem`

### 3.33. `PriceCalculationStatement` — 단가산출서

- 설명: 품목별 계약단가 산정 근거를 제공함.
- IRI: `rcpp:PriceCalculationStatement`
- 상위 클래스: `rcpp:SupportingReferenceDocument`
- 적용 속성: -

### 3.34. `ProgressAmountCalculation` — 기성금액·비율 및 누계 산정규칙

- 설명: 수량 누계·잔여 계산을 중복 수행하지 않고, 매칭된 계약조건·확정 금회기성수량·전회누계금액에 산식을 적용하여 계약·금회·누계·잔여 금액과 기성비율을 계산함.
- IRI: `rcpp:ProgressAmountCalculation`
- 상위 클래스: `rcpp:CalculationRule`
- 적용 속성: -
- 주요 관계:
  - `rcpp:schemaFlowsTo` → `rcpp:ConsistencyRule`
  - `rcpp:schemaFlowsTo` → `rcpp:CurrentProgressStatement`

### 3.35. `ProgressDocument` — 기성서류

- 설명: 기성업무에서 산정 근거·매칭·계산·결과 작성에 사용하는 모든 서류의 최상위 개념. 이 온톨로지의 중심은 프로젝트가 아니라 공사기성부분내역서를 작성하기 위한 기성서류와 서류내역의 데이터 흐름임.
- IRI: `rcpp:ProgressDocument`
- 상위 클래스: -
- 적용 속성: `rcpp:belongsToProgressRound`, `rcpp:belongsToProject`, `rcpp:containsItem`, `rcpp:documentIdentifier`, `rcpp:documentName`, `rcpp:documentReferenceDate`, `rcpp:documentRevision`, `rcpp:hasDocumentRole`, `rcpp:hasSourceLocation`, `rcpp:precedesDocument`

### 3.36. `ProgressPaymentRound` — 기성회차

- 설명: 한 프로젝트 안에서 회차번호·기준일·이전 회차를 묶고 해당 회차에 적용되는 문서와 계산정책을 구분하는 문맥.
- IRI: `rcpp:ProgressPaymentRound`
- 상위 클래스: -
- 적용 속성: `rcpp:belongsToProject`, `rcpp:isFirstProgressRound`, `rcpp:previousProgressRound`, `rcpp:progressRoundNumber`, `rcpp:progressRoundReferenceDate`, `rcpp:usesCalculationPolicy`

### 3.37. `ProgressQuantityDetailItem` — 기성수량 상세항목

- 설명: 기성수량산출서에서 위치·구조물·층·부재 등 최소 구분별로 기록되고 하나의 계약항목 단위 금회기성수량으로 합산되는 상세행.
- IRI: `rcpp:ProgressQuantityDetailItem`
- 상위 클래스: `rcpp:DocumentItem`
- 적용 속성: `rcpp:detailCurrentQuantity`, `rcpp:detailLocationText`, `rcpp:quantityAggregatedInto`
- 주요 관계:
  - `rcpp:expectedAggregationTargetClass` → `rcpp:CurrentProgressQuantityItem`
  - `rcpp:expectedCorrespondingItemClass` → `rcpp:ContractStatementItem`
  - `rcpp:expectedCostItemClass` → `rcpp:CostItem`

### 3.38. `ProgressQuantityRollupCalculation` — 기성수량 누계·잔여 산정규칙

- 설명: 금회기성수량 자체를 결정하지 않음. 동일 표준 비용항목의 계약수량·전회누계수량과 현재 회차에 비용산정용으로 확정 입력된 금회기성수량을 결합하여 누계·잔여 기성수량을 계산함. 검측·품질·시공사실 판단은 수행하지 않음.
- IRI: `rcpp:ProgressQuantityRollupCalculation`
- 상위 클래스: `rcpp:CalculationRule`
- 적용 속성: -
- 주요 관계:
  - `rcpp:inputQuantityProperty` → `rcpp:contractQuantity`
  - `rcpp:inputQuantityProperty` → `rcpp:progressCurrentQuantity`
  - `rcpp:inputQuantityProperty` → `rcpp:progressPreviousCumulativeQuantity`
  - `rcpp:producesField` → `rcpp:progressCumulativeQuantity`
  - `rcpp:producesField` → `rcpp:progressRemainingQuantity`
  - `rcpp:schemaFlowsTo` → `rcpp:ConsistencyRule`
  - `rcpp:schemaFlowsTo` → `rcpp:CurrentProgressAmountCalculation`
  - `rcpp:schemaFlowsTo` → `rcpp:CurrentProgressStatement`

### 3.39. `ProgressSummaryCalculation` — 공종별·전체 기성 집계규칙

- 설명: 기성 상세내역의 품목별 금액을 철근·콘크리트·거푸집·동바리 및 전체 금액으로 집계함.
- IRI: `rcpp:ProgressSummaryCalculation`
- 상위 클래스: `rcpp:CalculationRule`
- 적용 속성: -
- 주요 관계:
  - `rcpp:schemaFlowsTo` → `rcpp:CurrentProgressStatement`

### 3.40. `Project` — 프로젝트

- 설명: 서로 다른 공사 프로젝트의 계약·기성서류와 항목을 분리하는 적용 문맥. 온톨로지의 업무 중심은 기성서류이며 프로젝트는 실제 데이터의 범위를 식별함.
- IRI: `rcpp:Project`
- 상위 클래스: -
- 적용 속성: `rcpp:projectIdentifier`, `rcpp:projectName`

### 3.41. `QuantityCalculationItem` — 수량산출 항목

- 설명: 공종·품명·규격·단위와 서류에 기록된 수량산식·산출근거·산출수량을 담는 수량산출서의 행.
- IRI: `rcpp:QuantityCalculationItem`
- 상위 클래스: `rcpp:DocumentItem`
- 적용 속성: `rcpp:quantityCalculatedQuantity`, `rcpp:quantityCalculationBasis`, `rcpp:quantityCalculationCode`, `rcpp:quantityContractItemCode`, `rcpp:quantityFormula`, `rcpp:quantityItemName`, `rcpp:quantitySpecification`, `rcpp:quantityUnit`, `rcpp:quantityWorkType`
- 주요 관계:
  - `rcpp:expectedCostItemClass` → `rcpp:CostItem`

### 3.42. `QuantityCalculationSheet` — 수량산출서

- 설명: 구조물·위치·규격·산식을 기준으로 철근·콘크리트·거푸집·동바리의 산출수량과 계약수량 산출근거를 제공하는 서류.
- IRI: `rcpp:QuantityCalculationSheet`
- 상위 클래스: `rcpp:SourceDocument`
- 적용 속성: -
- 주요 관계:
  - `rcpp:expectedDocumentRole` → `rcpp:QuantityBasisDocumentRole`
  - `rcpp:expectedItemClass` → `rcpp:QuantityCalculationItem`
  - `rcpp:schemaFlowsTo` → `rcpp:DocumentItemMatching`
  - `rcpp:typicalNextDocumentClass` → `rcpp:ContractStatement`

### 3.43. `ReadyMixedConcreteCostItem` — 레미콘 비용항목

- 설명: 콘크리트 종류·호칭강도·굵은골재 최대치수·슬럼프 등 재료 규격으로 계약단가를 식별하는 레미콘 비용항목.
- IRI: `rcpp:ReadyMixedConcreteCostItem`
- 상위 클래스: `rcpp:ConcreteCostItem`
- 적용 속성: `rcpp:cementType`, `rcpp:concreteType`, `rcpp:maximumAggregateSize`, `rcpp:nominalStrength`, `rcpp:slump`

### 3.44. `RebarCostItem` — 철근 비용항목

- 설명: 철근형태·강종·호칭지름 또는 지름구간·작업유형을 속성값으로 가지고 계약단가를 식별하는 표준 비용항목. 노드를 클릭하면 적용 속성·예시·포함조건을 확인가능.
- IRI: `rcpp:RebarCostItem`
- 상위 클래스: `rcpp:CostItem`
- 적용 속성: `rcpp:diameterCategory`, `rcpp:fabricationMethod`, `rcpp:maximumDiameter`, `rcpp:minimumDiameter`, `rcpp:nominalDiameter`, `rcpp:rebarGrade`, `rcpp:rebarType`, `rcpp:rebarWorkType`, `rcpp:spliceMethod`

### 3.45. `RebarGrade` — 철근 강종

- 설명: SD400·SD500·SD600처럼 철근의 표준 강종을 식별하는 코드목록.
- IRI: `rcpp:RebarGrade`
- 상위 클래스: `rcpp:ControlledSpecificationValue`
- 적용 속성: -

### 3.46. `RebarWorkType` — 철근 작업유형

- 설명: 가공·조립·가공 및 조립의 표준 작업범위를 표현하는 코드목록.
- IRI: `rcpp:RebarWorkType`
- 상위 클래스: `rcpp:ControlledSpecificationValue`
- 적용 속성: -

### 3.47. `RoundingMode` — 반올림 방식

- 설명: 반올림·절사·올림 등 금액 자릿수 처리방식의 코드목록.
- IRI: `rcpp:RoundingMode`
- 상위 클래스: -
- 적용 속성: `rcpp:codeValue`

### 3.48. `ShoringCostItem` — 동바리 비용항목

- 설명: 동바리 종류·설치환경·수직고구간·작업유형을 속성값으로 가지고 계약단가를 식별하는 표준 비용항목. 노드를 클릭하면 적용 속성·예시·포함조건을 확인가능.
- IRI: `rcpp:ShoringCostItem`
- 상위 클래스: `rcpp:CostItem`
- 적용 속성: `rcpp:applicationPart`, `rcpp:installationEnvironment`, `rcpp:maximumVerticalHeight`, `rcpp:minimumVerticalHeight`, `rcpp:shoringType`, `rcpp:shoringWorkType`, `rcpp:verticalHeightBand`, `rcpp:workCondition`

### 3.49. `ShoringType` — 동바리 유형

- 설명: 시스템동바리·강관동바리처럼 동바리 재료 또는 시스템을 구분하는 코드목록.
- IRI: `rcpp:ShoringType`
- 상위 클래스: `rcpp:ControlledSpecificationValue`
- 적용 속성: -

### 3.50. `SourceDocument` — 산정 근거서류

- 설명: 공사기성부분내역서 작성에 필요한 항목을 제공하는 원천 서류.
- IRI: `rcpp:SourceDocument`
- 상위 클래스: `rcpp:ProgressDocument`
- 적용 속성: -

### 3.51. `SourceLocation` — 서류 원천위치

- 설명: 서류 또는 서류내역의 값이 추출된 파일·시트·페이지·행·셀 위치를 선택적으로 기록하는 출처 개체.
- IRI: `rcpp:SourceLocation`
- 상위 클래스: -
- 적용 속성: `rcpp:extractionMethod`, `rcpp:sourceCellRange`, `rcpp:sourceFileName`, `rcpp:sourcePageNumber`, `rcpp:sourceRowNumber`, `rcpp:sourceSheetName`

### 3.52. `SpecificationNormalizationRule` — 규격 정규화규칙

- 설명: 공종별 비용영향 속성의 선택·결합순서·구분자·누락값 처리·규칙버전을 정의하는 정규화 규칙.
- IRI: `rcpp:SpecificationNormalizationRule`
- 상위 클래스: -
- 적용 속성: `rcpp:applicationCondition`, `rcpp:componentDelimiter`, `rcpp:componentOrder`, `rcpp:missingValueTreatment`, `rcpp:ruleVersion`

### 3.53. `SummaryCostItem` — 집계항목

- 설명: 품목별 상세내역의 금액을 공종별 또는 상위 공종으로 합산한 행. 개별 품명·규격·단가를 필수로 요구하지 않음.
- IRI: `rcpp:SummaryCostItem`
- 상위 클래스: `rcpp:DocumentItem`
- 적용 속성: -

### 3.54. `SupportingReferenceDocument` — 지원·교차확인 서류

- 설명: 계약내역서·수량산출서·전회 공사기성부분내역서의 품목·규격·단위·단가·집계를 보조하거나 교차확인하는 서류. 금회수량이나 금액의 직접 근거로 사용하지 않음.
- IRI: `rcpp:SupportingReferenceDocument`
- 상위 클래스: `rcpp:SourceDocument`
- 적용 속성: -
- 주요 관계:
  - `rcpp:expectedDocumentRole` → `rcpp:SupportingReferenceDocumentRole`
  - `rcpp:expectedItemClass` → `rcpp:SupportingReferenceItem`
  - `rcpp:schemaFlowsTo` → `rcpp:DocumentItemMatching`

### 3.55. `SupportingReferenceItem` — 보조자료 항목

- 설명: 공종·품목·규격·수량·단가·집계를 보조하는 지원서류의 내역.
- IRI: `rcpp:SupportingReferenceItem`
- 상위 클래스: `rcpp:DocumentItem`
- 적용 속성: `rcpp:supportAmount`, `rcpp:supportItemCode`, `rcpp:supportItemName`, `rcpp:supportQuantity`, `rcpp:supportSpecification`, `rcpp:supportUnit`, `rcpp:supportUnitPrice`, `rcpp:supportWorkType`

### 3.56. `Unit` — 측정단위

- 설명: 계약수량·기성수량·계약단가에 공통 적용되는 kg·ton·㎥·㎡·개 등의 측정단위 개념.
- IRI: `rcpp:Unit`
- 상위 클래스: -
- 적용 속성: `rcpp:baseUnit`, `rcpp:conversionFactorToBaseUnit`, `rcpp:sourceValueAlias`, `rcpp:unitCode`, `rcpp:unitDimension`, `rcpp:unitSymbol`

### 3.57. `UnitConversionRule` — 단위변환 규칙

- 설명: 원천수량을 동일 차원의 기준단위를 거쳐 계약단가 기준단위의 수량으로 변환하는 규칙.
- IRI: `rcpp:UnitConversionRule`
- 상위 클래스: `rcpp:CalculationRule`
- 적용 속성: -

### 3.58. `UnitPriceAnalysisStatement` — 일위대가내역

- 설명: 계약단가 구성의 근거를 제공함.
- IRI: `rcpp:UnitPriceAnalysisStatement`
- 상위 클래스: `rcpp:SupportingReferenceDocument`
- 적용 속성: -

### 3.59. `WorkCategory` — 공종분류

- 설명: 표준 비용항목과 서류내역을 철근콘크리트공종 및 철근·콘크리트·거푸집·동바리 세부공종으로 분류하는 재사용 개념.
- IRI: `rcpp:WorkCategory`
- 상위 클래스: -
- 적용 속성: `rcpp:parentWorkCategory`, `rcpp:sourceValueAlias`, `rcpp:workCategoryCode`, `rcpp:workCategoryName`

### 3.60. `WorkTypeDetailItem` — 공종별 상세항목

- 설명: 세부 공종의 내역코드·품명·규격·단위·수량·단가·금액을 담는 행.
- IRI: `rcpp:WorkTypeDetailItem`
- 상위 클래스: `rcpp:DetailCostItem`
- 적용 속성: `rcpp:workDetailAmount`, `rcpp:workDetailDirectCost`, `rcpp:workDetailItemCode`, `rcpp:workDetailItemName`, `rcpp:workDetailQuantity`, `rcpp:workDetailSpecification`, `rcpp:workDetailUnit`, `rcpp:workDetailUnitPrice`, `rcpp:workDetailWorkType`
- 주요 관계:
  - `rcpp:expectedAggregationTargetClass` → `rcpp:WorkTypeSummaryItem`
  - `rcpp:expectedCorrespondingItemClass` → `rcpp:ContractStatementItem`
  - `rcpp:expectedCostItemClass` → `rcpp:CostItem`
  - `rcpp:expectedSourceItemClass` → `rcpp:ContractStatementItem`

### 3.61. `WorkTypeDetailStatement` — 공종별내역서

- 설명: 철근·콘크리트·거푸집·동바리의 세부 내역코드·품명·규격·단위·수량·단가·금액을 구성하는 산정 근거서류.
- IRI: `rcpp:WorkTypeDetailStatement`
- 상위 클래스: `rcpp:SourceDocument`
- 적용 속성: -
- 주요 관계:
  - `rcpp:expectedDocumentRole` → `rcpp:DetailedCostDocumentRole`
  - `rcpp:expectedItemClass` → `rcpp:WorkTypeDetailItem`
  - `rcpp:typicalNextDocumentClass` → `rcpp:WorkTypeSummaryStatement`

### 3.62. `WorkTypeSummaryItem` — 공종별 계약집계항목

- 설명: 계약내역 계열의 세부 내역금액을 공종별 계약금액과 필요 시 직접공사비로 집계하는 행. 금회·누계기성금액은 기성 집계내역에서만 계산함.
- IRI: `rcpp:WorkTypeSummaryItem`
- 상위 클래스: `rcpp:SummaryCostItem`
- 적용 속성: `rcpp:summaryContractAmount`, `rcpp:summaryDirectCost`, `rcpp:summaryWorkType`
- 주요 관계:
  - `rcpp:expectedSourceItemClass` → `rcpp:WorkTypeDetailItem`

### 3.63. `WorkTypeSummaryStatement` — 공종별집계표

- 설명: 계약내역 계열의 세부 내역항목을 철근·콘크리트·거푸집·동바리 공종별 계약금액과 직접공사비로 합산하는 원천서류. 금회·누계 기성금액은 포함하지 않음.
- IRI: `rcpp:WorkTypeSummaryStatement`
- 상위 클래스: `rcpp:SourceDocument`
- 적용 속성: -
- 주요 관계:
  - `rcpp:expectedDocumentRole` → `rcpp:CostSummaryDocumentRole`
  - `rcpp:expectedItemClass` → `rcpp:WorkTypeSummaryItem`
  - `rcpp:typicalNextDocumentClass` → `rcpp:CurrentProgressStatement`

## 4. 속성 및 관계 명세

### 4.1. `aggregatedInto` — 집계내역으로 합산

- 설명: 상세내역의 금액이 공종별 집계내역으로 합산되는 관계.
- IRI: `rcpp:aggregatedInto`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:DetailCostItem`
- 치역: `rcpp:SummaryCostItem`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:DetailCostItem`
  - `rdfs:range` → `rcpp:SummaryCostItem`

### 4.2. `aggregatesTo` — 집계 전달

- 설명: 세부 항목의 값을 공종별 또는 전체 합계 항목으로 합산하여 전달하는 관계.
- IRI: `rcpp:aggregatesTo`
- 구분: `항목관계`
- 정의역·적용 클래스: `rdf:Property`
- 치역: `rdf:Property`
- 상위 속성: -
- 적용 서류: -

### 4.3. `amountTolerance` — 금액 허용오차

- 설명: 기록 금액과 교차계산 금액을 비교할 때 허용하는 통화단위 기준 차이.
- IRI: `rcpp:amountTolerance`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:CalculationPolicy`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:CalculationPolicy`

### 4.4. `applicationCondition` — 적용조건

- 설명: 계산규칙 또는 정규화 규칙을 적용할 수 있는 업무 조건.
- IRI: `rcpp:applicationCondition`
- 구분: -
- 정의역·적용 클래스: `rcpp:CalculationRule`, `rcpp:SpecificationNormalizationRule`
- 치역: `rdfs:Literal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rcpp:appliesToClass` → `rcpp:CalculationRule`
  - `rcpp:appliesToClass` → `rcpp:SpecificationNormalizationRule`

### 4.5. `applicationPart` — 적용부위

- 설명: 비용산정 작업이 적용되는 구조부위.
- IRI: `rcpp:applicationPart`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:ConcretePlacementCostItem`, `rcpp:FormworkCostItem`, `rcpp:ShoringCostItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rcpp:appliesToClass` → `rcpp:ConcretePlacementCostItem`
  - `rcpp:appliesToClass` → `rcpp:FormworkCostItem`
  - `rcpp:appliesToClass` → `rcpp:ShoringCostItem`
- 포함 조건: 적용 구조부위에 따라 계약항목이나 계약단가가 구분되는 경우

### 4.6. `appliesPolicy` — 계산정책 적용

- 설명: 계산활동에 적용한 통화·반올림·절사·계산순서 정책.
- IRI: `rcpp:appliesPolicy`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:CalculationActivity`
- 치역: `rcpp:CalculationPolicy`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:CalculationActivity`
  - `rdfs:range` → `rcpp:CalculationPolicy`

### 4.7. `appliesRule` — 계산규칙 적용

- 설명: 실제 계산활동에 사용한 재사용 산식 규칙.
- IRI: `rcpp:appliesRule`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:CalculationActivity`
- 치역: `rcpp:CalculationRule`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:CalculationActivity`
  - `rdfs:range` → `rcpp:CalculationRule`

### 4.8. `appliesToClass` — 적용 클래스

- 설명: 속성이 적용되는 하나 이상의 클래스를 명시함.
- IRI: `rcpp:appliesToClass`
- 구분: -
- 정의역·적용 클래스: -
- 치역: `rdfs:Class`
- 상위 속성: -
- 적용 서류: -

### 4.9. `baseUnit` — 기준단위

- 설명: 동일 차원 단위를 비교·변환할 때 사용하는 기준단위.
- IRI: `rcpp:baseUnit`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:Unit`
- 치역: `rcpp:Unit`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:Unit`
  - `rdfs:range` → `rcpp:Unit`

### 4.10. `belongsToProgressRound` — 기성회차 소속

- 설명: 실제 기성서류가 적용되는 기성회차를 연결함. 계약기준서처럼 여러 회차에 재사용되면 복수 회차에 연결가능.
- IRI: `rcpp:belongsToProgressRound`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:ProgressDocument`
- 치역: `rcpp:ProgressPaymentRound`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ProgressDocument`
  - `rdfs:range` → `rcpp:ProgressPaymentRound`

### 4.11. `belongsToProject` — 프로젝트 소속

- 설명: 실제 기성서류 또는 기성회차를 하나의 프로젝트 문맥에 연결함.
- IRI: `rcpp:belongsToProject`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:ProgressDocument`, `rcpp:ProgressPaymentRound`
- 치역: `rcpp:Project`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rcpp:appliesToClass` → `rcpp:ProgressDocument`
  - `rcpp:appliesToClass` → `rcpp:ProgressPaymentRound`
  - `rdfs:range` → `rcpp:Project`

### 4.12. `belongsToWorkCategory` — 공종분류 소속

- 설명: 서류내역 또는 표준 비용항목을 재사용 가능한 공종분류 자원에 연결함.
- IRI: `rcpp:belongsToWorkCategory`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:CostItem`, `rcpp:DocumentItem`
- 치역: `rcpp:WorkCategory`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rcpp:appliesToClass` → `rcpp:CostItem`
  - `rcpp:appliesToClass` → `rcpp:DocumentItem`
  - `rdfs:range` → `rcpp:WorkCategory`

### 4.13. `calculationInputFor` — 산식 입력

- 설명: 원천 항목이 대상 계산항목의 산식에 입력되는 영향 관계.
- IRI: `rcpp:calculationInputFor`
- 구분: `항목관계`
- 정의역·적용 클래스: `rdf:Property`
- 치역: `rdf:Property`
- 상위 속성: -
- 적용 서류: -

### 4.14. `calculationInputItem` — 계산 입력항목

- 설명: 실제 계산에 입력된 계약·전회·금회수량 서류내역.
- IRI: `rcpp:calculationInputItem`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:CalculationActivity`
- 치역: `rcpp:DocumentItem`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:CalculationActivity`
  - `rdfs:range` → `rcpp:DocumentItem`

### 4.15. `calculationOrder` — 계산순서

- 설명: 항목별 자릿수 처리 후 합계 또는 합계 후 자릿수 처리처럼 금액 오차에 영향을 주는 순서.
- IRI: `rcpp:calculationOrder`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:CalculationPolicy`
- 치역: `rdfs:Literal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:CalculationPolicy`

### 4.16. `calculationOutputItem` — 계산 출력항목

- 설명: 계산결과가 기록된 공사기성부분내역서 등의 서류내역.
- IRI: `rcpp:calculationOutputItem`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:CalculationActivity`
- 치역: `rcpp:DocumentItem`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:CalculationActivity`
  - `rdfs:range` → `rcpp:DocumentItem`

### 4.17. `calculationRound` — 계산 기성회차

- 설명: 계산활동이 실행된 프로젝트 기성회차.
- IRI: `rcpp:calculationRound`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:CalculationActivity`
- 치역: `rcpp:ProgressPaymentRound`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:CalculationActivity`
  - `rdfs:range` → `rcpp:ProgressPaymentRound`

### 4.18. `calculationStatus` — 계산상태

- 설명: 대기·완료·오류 등 계산활동의 실행 상태.
- IRI: `rcpp:calculationStatus`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:CalculationActivity`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:CalculationActivity`

### 4.19. `cementType` — 시멘트 종류

- 설명: 단가항목을 구분하는 시멘트 종류.
- IRI: `rcpp:cementType`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:ReadyMixedConcreteCostItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ReadyMixedConcreteCostItem`
- 포함 조건: 시멘트 종류가 레미콘 계약단가항목을 구분하는 경우

### 4.20. `codeValue` — 표준 코드값

- 설명: 통제 규격값·통화·반올림 방식 개체를 언어와 무관하게 식별하는 기계가독형 코드.
- IRI: `rcpp:codeValue`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:ControlledSpecificationValue`, `rcpp:Currency`, `rcpp:RoundingMode`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rcpp:appliesToClass` → `rcpp:ControlledSpecificationValue`
  - `rcpp:appliesToClass` → `rcpp:Currency`
  - `rcpp:appliesToClass` → `rcpp:RoundingMode`

### 4.21. `complexityLevel` — 복잡도

- 설명: 내역서에서 단가를 구분하는 작업 난이도.
- IRI: `rcpp:complexityLevel`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:FormworkCostItem`
- 치역: `rcpp:ComplexityLevel`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:FormworkCostItem`
  - `rdfs:range` → `rcpp:ComplexityLevel`
- 포함 조건: 간단·보통·복잡 등 난이도에 따라 계약단가가 달라지는 경우

### 4.22. `componentDelimiter` — 규격코드 구분자

- 설명: 정규화된 규격요소 사이에 사용하는 문자.
- IRI: `rcpp:componentDelimiter`
- 구분: -
- 정의역·적용 클래스: `rcpp:SpecificationNormalizationRule`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:SpecificationNormalizationRule`

### 4.23. `componentOrder` — 규격요소 결합순서

- 설명: 정규화 규격코드에 포함하는 비용영향 속성과 결합 순서.
- IRI: `rcpp:componentOrder`
- 구분: -
- 정의역·적용 클래스: `rcpp:SpecificationNormalizationRule`
- 치역: `rdfs:Literal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:SpecificationNormalizationRule`

### 4.24. `concreteType` — 콘크리트 종류

- 설명: 보통·고강도·경량 등 콘크리트 유형.
- IRI: `rcpp:concreteType`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:ReadyMixedConcreteCostItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ReadyMixedConcreteCostItem`
- 포함 조건: 보통·고강도·경량 등 콘크리트 유형이 계약단가를 구분하는 경우

### 4.25. `confidenceScore` — 매칭 신뢰도

- 설명: 0 이상 1 이하로 기록하는 자동 또는 반자동 매칭 후보의 신뢰도.
- IRI: `rcpp:confidenceScore`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:DocumentItemMatching`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:DocumentItemMatching`

### 4.26. `consistencyComparedWith` — 일관성 비교

- 설명: 서류 간 동일해야 하거나 계산 한계를 비교해야 하는 항목 관계.
- IRI: `rcpp:consistencyComparedWith`
- 구분: `항목관계`
- 정의역·적용 클래스: `rdf:Property`
- 치역: `rdf:Property`
- 상위 속성: -
- 적용 서류: -

### 4.27. `containsItem` — 서류 내역 포함

- 설명: 실제 프로젝트 서류 개체와 그 서류에 포함된 행 개체를 연결함.
- IRI: `rcpp:containsItem`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:ProgressDocument`
- 치역: `rcpp:DocumentItem`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ProgressDocument`
  - `rdfs:range` → `rcpp:DocumentItem`

### 4.28. `contractAmount` — 계약금액

- 설명: 계약수량과 계약단가의 곱이며 비율과 잔여금액의 기준 금액. 도급금액·도급액은 원문 필드명으로 보존함.
- IRI: `rcpp:contractAmount`
- 구분: `계산`
- 정의역·적용 클래스: `rcpp:ContractStatementItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasAmountValue`
- 적용 서류: `rcpp:ContractStatement`
- 주요 관계:
  - `rcpp:consistencyComparedWith` → `rcpp:outputContractAmount`
  - `rcpp:fieldOfDocument` → `rcpp:ContractStatement`
  - `rcpp:mapsDirectlyTo` → `rcpp:outputContractAmount`
  - `rcpp:mapsDirectlyTo` → `rcpp:workDetailAmount`
  - `rdfs:domain` → `rcpp:ContractStatementItem`
- 산식: 계약금액 = 계약수량 × 계약단가

### 4.29. `contractItemCode` — 계약 품목코드

- 설명: 계약내역서·수량산출서·전회 공사기성부분내역서와 산정 결과서류의 동일 행을 연결하는 기본 매칭키.
- IRI: `rcpp:contractItemCode`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:ContractStatementItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasItemCode`
- 적용 서류: `rcpp:ContractStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:ContractStatement`
  - `rcpp:mapsDirectlyTo` → `rcpp:outputItemCode`
  - `rcpp:mapsDirectlyTo` → `rcpp:workDetailItemCode`
  - `rdfs:domain` → `rcpp:ContractStatementItem`

### 4.30. `contractItemName` — 공사내역·세부품목

- 설명: 최종 공사내역 열에 전달되는 계약 품목명.
- IRI: `rcpp:contractItemName`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:ContractStatementItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasItemName`
- 적용 서류: `rcpp:ContractStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:ContractStatement`
  - `rcpp:mapsDirectlyTo` → `rcpp:outputWorkDescription`
  - `rcpp:mapsDirectlyTo` → `rcpp:workDetailItemName`
  - `rdfs:domain` → `rcpp:ContractStatementItem`

### 4.31. `contractQuantity` — 계약수량

- 설명: 계약금액과 잔여수량의 기준이 되는 계약 수량.
- IRI: `rcpp:contractQuantity`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:ContractStatementItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasQuantityValue`
- 적용 서류: `rcpp:ContractStatement`
- 주요 관계:
  - `rcpp:calculationInputFor` → `rcpp:contractAmount`
  - `rcpp:calculationInputFor` → `rcpp:progressRemainingQuantity`
  - `rcpp:consistencyComparedWith` → `rcpp:outputCumulativeQuantity`
  - `rcpp:fieldOfDocument` → `rcpp:ContractStatement`
  - `rcpp:mapsDirectlyTo` → `rcpp:outputContractQuantity`
  - `rcpp:mapsDirectlyTo` → `rcpp:workDetailQuantity`
  - `rdfs:domain` → `rcpp:ContractStatementItem`

### 4.32. `contractQuantityBasis` — 계약수량 산출근거

- 설명: 수량산출서에서 전달된 계약수량의 구조물·위치·규격·산식 근거.
- IRI: `rcpp:contractQuantityBasis`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:ContractStatementItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: `rcpp:ContractStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:ContractStatement`
  - `rdfs:domain` → `rcpp:ContractStatementItem`

### 4.33. `contractSpecification` — 규격

- 설명: 계약 품목의 원문 규격이며 품목코드와 함께 매칭 정확도를 높인다.
- IRI: `rcpp:contractSpecification`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:ContractStatementItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasSpecificationText`
- 적용 서류: `rcpp:ContractStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:ContractStatement`
  - `rcpp:mapsDirectlyTo` → `rcpp:outputSpecification`
  - `rcpp:mapsDirectlyTo` → `rcpp:workDetailSpecification`
  - `rdfs:domain` → `rcpp:ContractStatementItem`

### 4.34. `contractUnit` — 단위

- 설명: 계약수량·금회기성수량·출력수량에 공통으로 적용되어야 하는 단위.
- IRI: `rcpp:contractUnit`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:ContractStatementItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasSourceUnitText`
- 적용 서류: `rcpp:ContractStatement`
- 주요 관계:
  - `rcpp:consistencyComparedWith` → `rcpp:outputUnit`
  - `rcpp:consistencyComparedWith` → `rcpp:quantityUnit`
  - `rcpp:fieldOfDocument` → `rcpp:ContractStatement`
  - `rcpp:mapsDirectlyTo` → `rcpp:outputUnit`
  - `rcpp:mapsDirectlyTo` → `rcpp:workDetailUnit`
  - `rdfs:domain` → `rcpp:ContractStatementItem`

### 4.35. `contractUnitPrice` — 계약단가

- 설명: 계약금액과 금회기성금액에 적용되는 계약 단가. 전회누계기성금액은 전회서류 값을 이월하고 이 단가로 계산한 값은 교차검토에만 사용함.
- IRI: `rcpp:contractUnitPrice`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:ContractStatementItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasUnitPriceValue`
- 적용 서류: `rcpp:ContractStatement`
- 주요 관계:
  - `rcpp:calculationInputFor` → `rcpp:contractAmount`
  - `rcpp:fieldOfDocument` → `rcpp:ContractStatement`
  - `rcpp:inputToCalculationClass` → `rcpp:CurrentProgressAmountCalculation`
  - `rcpp:mapsDirectlyTo` → `rcpp:outputContractUnitPrice`
  - `rcpp:mapsDirectlyTo` → `rcpp:workDetailUnitPrice`
  - `rdfs:domain` → `rcpp:ContractStatementItem`

### 4.36. `contractWorkType` — 공종

- 설명: 철근·콘크리트·거푸집·동바리 등 계약 공종.
- IRI: `rcpp:contractWorkType`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:ContractStatementItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasSourceWorkCategoryText`
- 적용 서류: `rcpp:ContractStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:ContractStatement`
  - `rcpp:mapsDirectlyTo` → `rcpp:outputWorkType`
  - `rcpp:mapsDirectlyTo` → `rcpp:workDetailWorkType`
  - `rdfs:domain` → `rcpp:ContractStatementItem`

### 4.37. `conversionFactorToBaseUnit` — 기준단위 변환계수

- 설명: 현재 단위의 수량에 곱하여 기준단위 수량으로 바꾸는 계수. 예: 1 ton × 1000 = 1000 kg.
- IRI: `rcpp:conversionFactorToBaseUnit`
- 구분: `계산`
- 정의역·적용 클래스: `rcpp:Unit`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:Unit`

### 4.38. `correspondsToItem` — 동일 서류내역 대응

- 설명: 서로 다른 기성서류의 내역이 동일한 표준 비용항목을 표현함을 직접 연결함.
- IRI: `rcpp:correspondsToItem`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:DocumentItem`
- 치역: `rcpp:DocumentItem`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:DocumentItem`
  - `rdfs:range` → `rcpp:DocumentItem`

### 4.39. `costItemCode` — 정규화 내역코드

- 설명: 프로젝트별 원문 품목코드와 구분되는 표준 비용항목의 기준 식별자.
- IRI: `rcpp:costItemCode`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:CostItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:CostItem`

### 4.40. `costItemName` — 정규화 품명

- 설명: 표준 공종·정규화 규격·표준 단위와 함께 동일 표준 비용항목을 판별하는 프로젝트 독립 품명.
- IRI: `rcpp:costItemName`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:CostItem`
- 치역: `rdfs:Literal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:CostItem`

### 4.41. `crossCheckFormulaExpression` — 교차검토 산식

- 설명: 원천 서류의 확정값을 대체하지 않고 계산 결과와 비교하는 검토용 산식을 기록함.
- IRI: `rcpp:crossCheckFormulaExpression`
- 구분: -
- 정의역·적용 클래스: -
- 치역: `rdfs:Literal`
- 상위 속성: -
- 적용 서류: -

### 4.42. `currency` — 통화

- 설명: 금액 계산·반올림·허용오차 해석에 적용할 통화 개체를 계산정책에 연결함.
- IRI: `rcpp:currency`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:CalculationPolicy`
- 치역: `rcpp:Currency`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:CalculationPolicy`
  - `rdfs:range` → `rcpp:Currency`

### 4.43. `decimalScale` — 금액 소수점 자릿수

- 설명: 반올림 방식을 적용한 후 금액에 유지할 소수점 이하 자릿수. 0은 통화의 정수 단위까지 처리함을 뜻함.
- IRI: `rcpp:decimalScale`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:CalculationPolicy`
- 치역: `xsd:integer`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:CalculationPolicy`

### 4.44. `derivedFrom` — 내역값 파생 근거

- 설명: 목표 서류내역의 값이 어느 원천 서류내역에서 전달·계산되었는지 나타낸다.
- IRI: `rcpp:derivedFrom`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:DocumentItem`
- 치역: `rcpp:DocumentItem`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:DocumentItem`
  - `rdfs:range` → `rcpp:DocumentItem`

### 4.45. `detailCurrentQuantity` — 상세 금회기성수량

- 설명: 하나의 위치·부재별 상세행에 기록된 금회기성수량.
- IRI: `rcpp:detailCurrentQuantity`
- 구분: `수량`
- 정의역·적용 클래스: `rcpp:ProgressQuantityDetailItem`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rcpp:aggregatesTo` → `rcpp:progressCurrentQuantity`
  - `rdfs:domain` → `rcpp:ProgressQuantityDetailItem`

### 4.46. `detailLocationText` — 상세 위치문구

- 설명: 기성수량 상세행을 구분하는 층·구조물·구간·부재 등의 원문 위치정보.
- IRI: `rcpp:detailLocationText`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:ProgressQuantityDetailItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ProgressQuantityDetailItem`

### 4.47. `diameterCategory` — 지름구간

- 설명: 단가가 적용되는 철근 지름 범위.
- IRI: `rcpp:diameterCategory`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:RebarCostItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:RebarCostItem`
- 포함 조건: 정확한 지름 하나가 아니라 철근 지름 범위로 계약단가가 적용되는 경우

### 4.48. `documentCode` — 문서코드

- 설명: 서류 유형을 구분하는 온톨로지 문서코드.
- IRI: `rcpp:documentCode`
- 구분: -
- 정의역·적용 클래스: -
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -

### 4.49. `documentIdentifier` — 문서 식별자

- 설명: 실제 서류 파일 또는 시트를 구분하는 식별자.
- IRI: `rcpp:documentIdentifier`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:ProgressDocument`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ProgressDocument`

### 4.50. `documentName` — 문서명

- 설명: 실제 서류 또는 시트의 명칭.
- IRI: `rcpp:documentName`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:ProgressDocument`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ProgressDocument`

### 4.51. `documentReferenceDate` — 문서 기준일

- 설명: 계약 또는 기성 회차 적용을 판단하는 기준일.
- IRI: `rcpp:documentReferenceDate`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:ProgressDocument`
- 치역: `xsd:date`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ProgressDocument`

### 4.52. `documentRevision` — 문서 개정번호

- 설명: 적용할 서류 버전을 구분하는 개정번호.
- IRI: `rcpp:documentRevision`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:ProgressDocument`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ProgressDocument`

### 4.53. `exampleValue` — 예시값

- 설명: 속성 정의를 이해하기 위한 대표 값이며 실제 인스턴스 값은 아니다.
- IRI: `rcpp:exampleValue`
- 구분: -
- 정의역·적용 클래스: -
- 치역: `rdfs:Literal`
- 상위 속성: -
- 적용 서류: -

### 4.54. `expectedAggregationTargetClass` — 예상 집계대상 클래스

- 설명: 상세내역 개체가 집계될 결과서류 내부 또는 공종별 집계내역 클래스를 지정함.
- IRI: `rcpp:expectedAggregationTargetClass`
- 구분: `스키마관계`
- 정의역·적용 클래스: -
- 치역: `rdfs:Class`
- 상위 속성: -
- 적용 서류: -

### 4.55. `expectedAmountCalculationClass` — 예상 금액계산 클래스

- 설명: 결과서류 유형에서 사용하는 기성금액 계산 클래스를 지정함.
- IRI: `rcpp:expectedAmountCalculationClass`
- 구분: `스키마관계`
- 정의역·적용 클래스: -
- 치역: `rdfs:Class`
- 상위 속성: -
- 적용 서류: -

### 4.56. `expectedCorrespondingItemClass` — 예상 대응내역 클래스

- 설명: 서로 다른 서류의 어떤 내역 클래스끼리 실제 개체 수준에서 대응해야 하는지 설명함.
- IRI: `rcpp:expectedCorrespondingItemClass`
- 구분: `스키마관계`
- 정의역·적용 클래스: -
- 치역: `rdfs:Class`
- 상위 속성: -
- 적용 서류: -

### 4.57. `expectedCostItemClass` — 예상 표준 비용항목 클래스

- 설명: 서류내역 클래스가 인스턴스 수준에서 표현해야 할 표준 비용항목 클래스를 지정함.
- IRI: `rcpp:expectedCostItemClass`
- 구분: `스키마관계`
- 정의역·적용 클래스: -
- 치역: `rdfs:Class`
- 상위 속성: -
- 적용 서류: -

### 4.58. `expectedDocumentRole` — 대표 서류역할

- 설명: 서류 유형 클래스에 일반적으로 기대되는 역할 개체를 연결하는 스키마 주석관계. 실제 프로젝트 서류는 hasDocumentRole을 사용함.
- IRI: `rcpp:expectedDocumentRole`
- 구분: `스키마관계`
- 정의역·적용 클래스: -
- 치역: `rcpp:DocumentRole`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:range` → `rcpp:DocumentRole`

### 4.59. `expectedIdentificationReferenceClass` — 예상 품목식별 참고 클래스

- 설명: 금회기성수량의 직접 출처가 아니라 품명·규격·단위와 동일 계약내역 식별에 참고하는 서류내역 클래스.
- IRI: `rcpp:expectedIdentificationReferenceClass`
- 구분: `스키마관계`
- 정의역·적용 클래스: -
- 치역: `rdfs:Class`
- 상위 속성: -
- 적용 서류: -

### 4.60. `expectedItemClass` — 예상 서류내역 클래스

- 설명: 서류 유형 클래스가 포함할 수 있는 내역의 클래스를 설명하며 실제 서류와 내역의 관계를 단정하지 않음.
- IRI: `rcpp:expectedItemClass`
- 구분: `스키마관계`
- 정의역·적용 클래스: -
- 치역: `rdfs:Class`
- 상위 속성: -
- 적용 서류: -

### 4.61. `expectedPreviousQuantitySourceClass` — 예상 전회누계 출처 클래스

- 설명: 현재 회차의 전회누계기성수량을 이월하는 전회 기성항목 클래스.
- IRI: `rcpp:expectedPreviousQuantitySourceClass`
- 구분: `스키마관계`
- 정의역·적용 클래스: -
- 치역: `rdfs:Class`
- 상위 속성: -
- 적용 서류: -

### 4.62. `expectedQuantityBasisClass` — 예상 계약수량 근거 클래스

- 설명: 금회기성수량이 아니라 계약수량의 산출근거를 제공하는 수량산출 내역 클래스.
- IRI: `rcpp:expectedQuantityBasisClass`
- 구분: `스키마관계`
- 정의역·적용 클래스: -
- 치역: `rdfs:Class`
- 상위 속성: -
- 적용 서류: -

### 4.63. `expectedRequirementTargetClass` — 항목값 요구 대상 클래스

- 설명: FieldRequirement 개체가 필수·조건부 항목값을 지정하는 대상의 공통 상위 클래스를 설명함.
- IRI: `rcpp:expectedRequirementTargetClass`
- 구분: `스키마관계`
- 정의역·적용 클래스: -
- 치역: `rdfs:Class`
- 상위 속성: -
- 적용 서류: -

### 4.64. `expectedSourceItemClass` — 예상 파생근거 클래스

- 설명: 대상 내역값의 실제 개체가 어느 서류내역 클래스의 개체에서 파생되어야 하는지 설명함.
- IRI: `rcpp:expectedSourceItemClass`
- 구분: `스키마관계`
- 정의역·적용 클래스: -
- 치역: `rdfs:Class`
- 상위 속성: -
- 적용 서류: -

### 4.65. `expectedUnitClass` — 예상 표준 단위 클래스

- 설명: 서류내역과 표준 비용항목의 실제 개체가 usesUnit으로 연결할 표준 단위 클래스.
- IRI: `rcpp:expectedUnitClass`
- 구분: `스키마관계`
- 정의역·적용 클래스: -
- 치역: `rdfs:Class`
- 상위 속성: -
- 적용 서류: -

### 4.66. `expectedUnitPriceSourceClass` — 예상 계약단가 출처 클래스

- 설명: 기성 상세내역이 계약단가를 참조해야 할 계약 내역 클래스를 지정함.
- IRI: `rcpp:expectedUnitPriceSourceClass`
- 구분: `스키마관계`
- 정의역·적용 클래스: -
- 치역: `rdfs:Class`
- 상위 속성: -
- 적용 서류: -

### 4.67. `expectedWorkCategoryClass` — 예상 표준 공종 클래스

- 설명: 서류내역과 표준 비용항목의 실제 개체가 belongsToWorkCategory로 연결할 표준 공종 클래스.
- IRI: `rcpp:expectedWorkCategoryClass`
- 구분: `스키마관계`
- 정의역·적용 클래스: -
- 치역: `rdfs:Class`
- 상위 속성: -
- 적용 서류: -

### 4.68. `extractionMethod` — 값 기록방법

- 설명: 원천서류의 값을 온톨로지 데이터에 기록하거나 변환한 방법을 식별하는 설명.
- IRI: `rcpp:extractionMethod`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:SourceLocation`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:SourceLocation`

### 4.69. `fabricationMethod` — 가공방식

- 설명: 철근을 공장 또는 현장에서 가공하는 방식의 구분.
- IRI: `rcpp:fabricationMethod`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:RebarCostItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:RebarCostItem`
- 포함 조건: 공장가공과 현장가공의 계약단가가 다른 경우

### 4.70. `fieldOfDocument` — 소속 서류

- 설명: 데이터 항목이 정의된 서류 유형.
- IRI: `rcpp:fieldOfDocument`
- 구분: -
- 정의역·적용 클래스: -
- 치역: `rdfs:Class`
- 상위 속성: -
- 적용 서류: -

### 4.71. `fieldOrder` — 내역 순서

- 설명: 서류내역 흐름 시각화에서 사용하는 의미 순서.
- IRI: `rcpp:fieldOrder`
- 구분: -
- 정의역·적용 클래스: -
- 치역: `xsd:integer`
- 상위 속성: -
- 적용 서류: -

### 4.72. `formulaCategory` — 산식 구분

- 설명: 기본·공종별·집계·일관성 산식을 구분함.
- IRI: `rcpp:formulaCategory`
- 구분: -
- 정의역·적용 클래스: -
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -

### 4.73. `formulaExpression` — 산식

- 설명: 클래스 또는 서류내역에 적용되는 계산식을 기록함.
- IRI: `rcpp:formulaExpression`
- 구분: -
- 정의역·적용 클래스: -
- 치역: `rdfs:Literal`
- 상위 속성: -
- 적용 서류: -

### 4.74. `formworkType` — 거푸집 종류

- 설명: 재료 또는 공법에 따른 거푸집 구분.
- IRI: `rcpp:formworkType`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:FormworkCostItem`
- 치역: `rcpp:FormworkType`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:FormworkCostItem`
  - `rdfs:range` → `rcpp:FormworkType`

### 4.75. `formworkWorkType` — 거푸집 작업유형

- 설명: 거푸집 비용에 포함되는 작업 범위.
- IRI: `rcpp:formworkWorkType`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:FormworkCostItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:FormworkCostItem`

### 4.76. `graphLevel` — 그래프 표시수준

- 설명: core·extended·structure·detail 중 시각화 노출 수준.
- IRI: `rcpp:graphLevel`
- 구분: -
- 정의역·적용 클래스: -
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -

### 4.77. `groupsByField` — 그룹 기준

- 설명: 공종명처럼 합산하지 않고 여러 상세행을 같은 집계행으로 묶는 분류 기준 항목 관계.
- IRI: `rcpp:groupsByField`
- 구분: `항목관계`
- 정의역·적용 클래스: `rdf:Property`
- 치역: `rdf:Property`
- 상위 속성: -
- 적용 서류: -

### 4.78. `hasAmountValue` — 공통 금액값

- 설명: 도급·전회·금회·누계·잔여 및 공종별 합계 금액 속성을 포괄하는 공통 상위 속성.
- IRI: `rcpp:hasAmountValue`
- 구분: `금액`
- 정의역·적용 클래스: `rcpp:DocumentItem`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:DocumentItem`

### 4.79. `hasDocumentRole` — 서류역할 보유

- 설명: 실제 프로젝트 서류 개체가 수행하는 하나 이상의 역할을 연결함.
- IRI: `rcpp:hasDocumentRole`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:ProgressDocument`
- 치역: `rcpp:DocumentRole`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ProgressDocument`
  - `rdfs:range` → `rcpp:DocumentRole`

### 4.80. `hasItemCode` — 공통 내역코드

- 설명: 서류 종류와 관계없이 동일 표준 비용항목을 식별하기 위한 공통 코드 속성. 각 서류의 원천 코드 속성은 이 속성의 하위속성으로 둔다.
- IRI: `rcpp:hasItemCode`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:DocumentItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:DocumentItem`

### 4.81. `hasItemName` — 공통 품명

- 설명: 서류별 품명·공사내역 문자열을 공통 의미로 조회하기 위한 상위 속성.
- IRI: `rcpp:hasItemName`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:DocumentItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:DocumentItem`

### 4.82. `hasQuantityValue` — 공통 수량값

- 설명: 계약·전회·금회·누계·잔여 등 서류별 수량 속성을 포괄하는 공통 상위 속성.
- IRI: `rcpp:hasQuantityValue`
- 구분: `수량`
- 정의역·적용 클래스: `rcpp:DocumentItem`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:DocumentItem`

### 4.83. `hasSourceLocation` — 원천위치 연결

- 설명: 서류 또는 서류내역을 실제 파일·시트·페이지·행·셀 위치 개체에 연결함.
- IRI: `rcpp:hasSourceLocation`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:DocumentItem`, `rcpp:ProgressDocument`
- 치역: `rcpp:SourceLocation`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rcpp:appliesToClass` → `rcpp:DocumentItem`
  - `rcpp:appliesToClass` → `rcpp:ProgressDocument`
  - `rdfs:range` → `rcpp:SourceLocation`

### 4.84. `hasSourceUnitText` — 원문 단위문구

- 설명: M2·m²·㎡처럼 프로젝트 서류에 적힌 단위 문자열을 보존하는 공통 상위 속성. 정규화된 표준 단위는 usesUnit으로 연결함.
- IRI: `rcpp:hasSourceUnitText`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:DocumentItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:DocumentItem`

### 4.85. `hasSourceWorkCategoryText` — 원문 공종문구

- 설명: 프로젝트 서류에 적힌 공종 문자열을 손실 없이 보존하는 공통 상위 속성. 정규화된 표준 공종은 belongsToWorkCategory로 연결함.
- IRI: `rcpp:hasSourceWorkCategoryText`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:DocumentItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:DocumentItem`

### 4.86. `hasSpecificationText` — 공통 규격문구

- 설명: 각 기성서류에 기록된 원문 규격문구의 공통 상위 속성. 계약단가 식별용 규격 개념과 원문 문자열을 구분함.
- IRI: `rcpp:hasSpecificationText`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:DocumentItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:DocumentItem`

### 4.87. `hasUnitPriceValue` — 공통 단가값

- 설명: 계약내역과 결과서류 등에 기록된 단가 속성을 포괄하는 공통 상위 속성.
- IRI: `rcpp:hasUnitPriceValue`
- 구분: `단가`
- 정의역·적용 클래스: `rcpp:DocumentItem`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:DocumentItem`

### 4.88. `identificationReferencedFrom` — 품목식별 참고

- 설명: 품명·규격·단위와 동일 계약항목을 확인할 때 참고하지만 대상 수량값의 직접 출처로 사용하지 않는 항목 관계.
- IRI: `rcpp:identificationReferencedFrom`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:DocumentItem`
- 치역: `rcpp:DocumentItem`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:DocumentItem`
  - `rdfs:range` → `rcpp:DocumentItem`

### 4.89. `inclusionCondition` — 포함 조건

- 설명: 규격속성을 분해하여 모델링해야 하는 비용산정상의 조건.
- IRI: `rcpp:inclusionCondition`
- 구분: -
- 정의역·적용 클래스: -
- 치역: `rdfs:Literal`
- 상위 속성: -
- 적용 서류: -

### 4.90. `inputQuantityProperty` — 수량 입력속성

- 설명: 계산 클래스가 입력으로 요구하는 계약수량·전회누계수량·금회기성수량 속성을 지정함.
- IRI: `rcpp:inputQuantityProperty`
- 구분: `스키마관계`
- 정의역·적용 클래스: `rdfs:Class`
- 치역: `rdf:Property`
- 상위 속성: -
- 적용 서류: -

### 4.91. `inputToCalculationClass` — 금액계산 입력 전달

- 설명: 금회기성수량 또는 계약단가 속성에서 금회기성금액 계산 클래스로 이어지는 스키마상 입력 흐름.
- IRI: `rcpp:inputToCalculationClass`
- 구분: `스키마관계`
- 정의역·적용 클래스: `rdf:Property`
- 치역: `rdfs:Class`
- 상위 속성: -
- 적용 서류: -

### 4.92. `inputUnitPriceProperty` — 단가 입력속성

- 설명: 계산 클래스가 입력으로 요구하는 계약단가 속성을 지정함.
- IRI: `rcpp:inputUnitPriceProperty`
- 구분: `스키마관계`
- 정의역·적용 클래스: `rdfs:Class`
- 치역: `rdf:Property`
- 상위 속성: -
- 적용 서류: -

### 4.93. `installationEnvironment` — 설치환경

- 설명: 동바리 설치 장소나 환경의 구분.
- IRI: `rcpp:installationEnvironment`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:ShoringCostItem`
- 치역: `rcpp:InstallationEnvironment`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ShoringCostItem`
  - `rdfs:range` → `rcpp:InstallationEnvironment`
- 포함 조건: 육상·수상 등 설치환경에 따라 계약단가가 달라지는 경우

### 4.94. `isExposedFinish` — 노출 여부

- 설명: 노출콘크리트용 거푸집인지 여부.
- IRI: `rcpp:isExposedFinish`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:FormworkCostItem`
- 치역: `xsd:boolean`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:FormworkCostItem`
- 포함 조건: 노출콘크리트용 거푸집 여부에 따라 계약단가가 달라지는 경우

### 4.95. `isFirstProgressRound` — 최초 기성회차 여부

- 설명: 이전 기성회차와 전회 기성서류 없이 전회누계수량·금액을 0으로 적용하는 최초회차인지 표시함.
- IRI: `rcpp:isFirstProgressRound`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:ProgressPaymentRound`
- 치역: `xsd:boolean`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ProgressPaymentRound`

### 4.96. `mapsDirectlyTo` — 그대로 전달

- 설명: 원천서류의 값을 목표 서류내역으로 직접 전달함.
- IRI: `rcpp:mapsDirectlyTo`
- 구분: `항목관계`
- 정의역·적용 클래스: `rdf:Property`
- 치역: `rdf:Property`
- 상위 속성: -
- 적용 서류: -

### 4.97. `matchedCostItem` — 매칭 표준 비용항목

- 설명: 두 서류내역이 함께 표현한다고 판단한 표준 비용항목.
- IRI: `rcpp:matchedCostItem`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:DocumentItemMatching`
- 치역: `rcpp:CostItem`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:DocumentItemMatching`
  - `rdfs:range` → `rcpp:CostItem`

### 4.98. `matchesWithField` — 매칭 기준

- 설명: 두 서류의 행이 같은 계약항목인지 확인하는 항목 관계.
- IRI: `rcpp:matchesWithField`
- 구분: `항목관계`
- 정의역·적용 클래스: `rdf:Property`
- 치역: `rdf:Property`
- 상위 속성: -
- 적용 서류: -

### 4.99. `matchingEvidence` — 매칭 근거

- 설명: 코드·품명·규격·단위·공종 일치 등 대응 판단에 사용한 근거.
- IRI: `rcpp:matchingEvidence`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:DocumentItemMatching`
- 치역: `rdfs:Literal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:DocumentItemMatching`

### 4.100. `matchingMethod` — 매칭 방법

- 설명: 내역코드 일치·정규화 복합기준 비교·담당자 확인 등 서류내역의 대응관계를 판단한 방법.
- IRI: `rcpp:matchingMethod`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:DocumentItemMatching`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:DocumentItemMatching`

### 4.101. `maximumAggregateSize` — 굵은골재 최대치수(mm)

- 설명: 레미콘 규격을 구성하는 굵은골재의 최대치수.
- IRI: `rcpp:maximumAggregateSize`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:ReadyMixedConcreteCostItem`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ReadyMixedConcreteCostItem`

### 4.102. `maximumDiameter` — 최대지름(mm)

- 설명: 단가가 적용되는 철근 지름구간의 최댓값.
- IRI: `rcpp:maximumDiameter`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:RebarCostItem`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:RebarCostItem`
- 포함 조건: 계약내역이 D13 이하처럼 지름구간의 상한으로 단가를 구분하는 경우

### 4.103. `maximumQuantityThreshold` — 최대물량(㎥)

- 설명: 물량구간의 최댓값.
- IRI: `rcpp:maximumQuantityThreshold`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:ConcretePlacementCostItem`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ConcretePlacementCostItem`
- 포함 조건: 물량구간의 상한을 수치로 비교해야 하는 경우

### 4.104. `maximumVerticalHeight` — 최대수직고(m)

- 설명: 단가가 적용되는 수직고구간의 최댓값.
- IRI: `rcpp:maximumVerticalHeight`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:FormworkCostItem`, `rcpp:ShoringCostItem`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rcpp:appliesToClass` → `rcpp:FormworkCostItem`
  - `rcpp:appliesToClass` → `rcpp:ShoringCostItem`

### 4.105. `minimumDiameter` — 최소지름(mm)

- 설명: 단가가 적용되는 철근 지름구간의 최솟값.
- IRI: `rcpp:minimumDiameter`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:RebarCostItem`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:RebarCostItem`
- 포함 조건: 계약내역이 D16 이상처럼 지름구간의 하한으로 단가를 구분하는 경우

### 4.106. `minimumQuantityThreshold` — 최소물량(㎥)

- 설명: 물량구간의 최솟값.
- IRI: `rcpp:minimumQuantityThreshold`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:ConcretePlacementCostItem`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ConcretePlacementCostItem`
- 포함 조건: 물량구간의 하한을 수치로 비교해야 하는 경우

### 4.107. `minimumVerticalHeight` — 최소수직고(m)

- 설명: 단가가 적용되는 수직고구간의 최솟값.
- IRI: `rcpp:minimumVerticalHeight`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:FormworkCostItem`, `rcpp:ShoringCostItem`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rcpp:appliesToClass` → `rcpp:FormworkCostItem`
  - `rcpp:appliesToClass` → `rcpp:ShoringCostItem`
- 포함 조건: 수직고구간의 하한을 수치로 비교해야 하는 경우

### 4.108. `missingValueTreatment` — 누락값 처리

- 설명: 비용영향 속성값이 없을 때 생략·대체코드·검토대상 중 어떤 방식으로 처리하는지 정의함.
- IRI: `rcpp:missingValueTreatment`
- 구분: -
- 정의역·적용 클래스: `rcpp:SpecificationNormalizationRule`
- 치역: `rdfs:Literal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:SpecificationNormalizationRule`

### 4.109. `namespaceUri` — 네임스페이스 URI

- 설명: RCPP 자원 IRI의 공통 기반으로 사용하는 온톨로지 네임스페이스 주소.
- IRI: `rcpp:namespaceUri`
- 구분: -
- 정의역·적용 클래스: -
- 치역: `xsd:anyURI`
- 상위 속성: -
- 적용 서류: -

### 4.110. `nominalDiameter` — 호칭지름(mm)

- 설명: 철근의 공칭 지름.
- IRI: `rcpp:nominalDiameter`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:RebarCostItem`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:RebarCostItem`
- 포함 조건: 내역항목이 하나의 공칭 지름으로 구분되는 경우 사용하고, 지름구간으로 구분되면 최소·최대지름 또는 지름구간을 사용

### 4.111. `nominalStrength` — 호칭강도(MPa)

- 설명: 레미콘의 계약 규격을 구분하는 호칭강도.
- IRI: `rcpp:nominalStrength`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:ReadyMixedConcreteCostItem`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ReadyMixedConcreteCostItem`

### 4.112. `normalizedSpecificationCode` — 정규화규격코드

- 설명: 비용 관련 규격요소를 표준 형식으로 결합한 항목 비교용 코드.
- IRI: `rcpp:normalizedSpecificationCode`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:CostItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:CostItem`

### 4.113. `outputColumnGroup` — 출력 열 그룹

- 설명: 공사기성부분내역서에서 항목이 배치되는 열을 표시함.
- IRI: `rcpp:outputColumnGroup`
- 구분: -
- 정의역·적용 클래스: -
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -

### 4.114. `outputContractAmount` — 계약금액

- 설명: 계약내역서의 계약금액을 기준값으로 직접 전달하고 계약수량과 계약단가의 곱은 교차검토에만 사용하는 출력값. 도급금액·도급액은 원문 필드명으로 보존함.
- IRI: `rcpp:outputContractAmount`
- 구분: `출력`
- 정의역·적용 클래스: `rcpp:CurrentProgressDetailItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasAmountValue`
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:aggregatesTo` → `rcpp:outputSummaryContractAmount`
  - `rcpp:calculationInputFor` → `rcpp:outputCumulativeRate`
  - `rcpp:calculationInputFor` → `rcpp:outputCurrentRate`
  - `rcpp:calculationInputFor` → `rcpp:outputPreviousRate`
  - `rcpp:calculationInputFor` → `rcpp:outputRemainingAmount`
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressDetailItem`
- 산식: 출력 계약금액 = 계약내역서 계약금액 직접 전달

### 4.115. `outputContractQuantity` — 계약수량

- 설명: 계약수량을 공사기성부분내역서의 도급액 수량 열로 전달한 값.
- IRI: `rcpp:outputContractQuantity`
- 구분: `출력`
- 정의역·적용 클래스: `rcpp:CurrentProgressDetailItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasQuantityValue`
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressDetailItem`

### 4.116. `outputContractUnitPrice` — 계약단가

- 설명: 계약단가를 공사기성부분내역서의 도급액 단가 열로 전달한 값.
- IRI: `rcpp:outputContractUnitPrice`
- 구분: `출력`
- 정의역·적용 클래스: `rcpp:CurrentProgressDetailItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasUnitPriceValue`
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:calculationInputFor` → `rcpp:outputCurrentAmount`
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressDetailItem`

### 4.117. `outputCumulativeAmount` — 누계기성금액

- 설명: 전회누계기성금액과 금회기성금액의 합.
- IRI: `rcpp:outputCumulativeAmount`
- 구분: `계산`
- 정의역·적용 클래스: `rcpp:CurrentProgressDetailItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasAmountValue`
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:aggregatesTo` → `rcpp:outputSummaryCumulativeAmount`
  - `rcpp:calculationInputFor` → `rcpp:outputCumulativeRate`
  - `rcpp:calculationInputFor` → `rcpp:outputRemainingAmount`
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressDetailItem`
- 산식: 누계기성금액 = 전회누계기성금액 + 금회기성금액

### 4.118. `outputCumulativeQuantity` — 누계기성수량

- 설명: 기성수량산출서의 누계기성수량을 기준값으로 직접 전달하고 전회수량과 금회수량의 합은 교차검토에만 사용함.
- IRI: `rcpp:outputCumulativeQuantity`
- 구분: `출력`
- 정의역·적용 클래스: `rcpp:CurrentProgressDetailItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasQuantityValue`
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressDetailItem`
- 산식: 출력 누계기성수량 = 기성수량산출서 누계기성수량 직접 전달

### 4.119. `outputCumulativeRate` — 누계기성비율(%)

- 설명: 누계기성금액의 계약금액 대비 비율.
- IRI: `rcpp:outputCumulativeRate`
- 구분: `계산`
- 정의역·적용 클래스: `rcpp:CurrentProgressDetailItem`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressDetailItem`
- 산식: 누계기성비율(%) = 누계기성금액 ÷ 계약금액 × 100

### 4.120. `outputCurrentAmount` — 금회기성금액

- 설명: 금회기성수량과 계약단가의 곱.
- IRI: `rcpp:outputCurrentAmount`
- 구분: `계산`
- 정의역·적용 클래스: `rcpp:CurrentProgressDetailItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasAmountValue`
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:aggregatesTo` → `rcpp:outputSummaryCurrentAmount`
  - `rcpp:calculationInputFor` → `rcpp:outputCumulativeAmount`
  - `rcpp:calculationInputFor` → `rcpp:outputCurrentRate`
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressDetailItem`
- 산식: 금회기성금액 = 금회기성수량 × 계약단가

### 4.121. `outputCurrentQuantity` — 금회기성수량

- 설명: 기성수량산출서에서 전달되는 현재 기성회차 적용 수량.
- IRI: `rcpp:outputCurrentQuantity`
- 구분: `출력`
- 정의역·적용 클래스: `rcpp:CurrentProgressDetailItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasQuantityValue`
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:calculationInputFor` → `rcpp:outputCurrentAmount`
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressDetailItem`

### 4.122. `outputCurrentRate` — 금회기성비율(%)

- 설명: 금회기성금액의 계약금액 대비 비율.
- IRI: `rcpp:outputCurrentRate`
- 구분: `계산`
- 정의역·적용 클래스: `rcpp:CurrentProgressDetailItem`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressDetailItem`
- 산식: 금회기성비율(%) = 금회기성금액 ÷ 계약금액 × 100

### 4.123. `outputItemCode` — 출력 품목코드

- 설명: 표시 여부와 무관하게 서류 간 동일 행을 추적하는 공사기성부분내역서의 내부 키.
- IRI: `rcpp:outputItemCode`
- 구분: `출력`
- 정의역·적용 클래스: `rcpp:CurrentProgressDetailItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasItemCode`
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressDetailItem`

### 4.124. `outputPreviousAmount` — 전회누계기성금액

- 설명: 전회 누계금액을 전달하고 전회 누계수량과 계약단가로 교차계산하는 값.
- IRI: `rcpp:outputPreviousAmount`
- 구분: `출력`
- 정의역·적용 클래스: `rcpp:CurrentProgressDetailItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasAmountValue`
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:aggregatesTo` → `rcpp:outputSummaryPreviousAmount`
  - `rcpp:calculationInputFor` → `rcpp:outputCumulativeAmount`
  - `rcpp:calculationInputFor` → `rcpp:outputPreviousRate`
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressDetailItem`
- 산식: 전회누계기성금액 = 전회 공사기성부분내역서의 확정 누계금액 이월

### 4.125. `outputPreviousQuantity` — 전회까지의 기성수량

- 설명: 전회 공사기성부분내역서의 누계기성수량을 전달한 값.
- IRI: `rcpp:outputPreviousQuantity`
- 구분: `출력`
- 정의역·적용 클래스: `rcpp:CurrentProgressDetailItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasQuantityValue`
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressDetailItem`

### 4.126. `outputPreviousRate` — 전회누계기성비율(%)

- 설명: 전회서류의 비율이 있으면 직접 전달하고, 없을 때만 전회누계기성금액과 계약금액으로 계산하는 조건부 출력값.
- IRI: `rcpp:outputPreviousRate`
- 구분: `계산`
- 정의역·적용 클래스: `rcpp:CurrentProgressDetailItem`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressDetailItem`
- 산식: 원천 전회기성비율이 없을 때 전회누계기성비율(%) = 전회누계기성금액 ÷ 계약금액 × 100

### 4.127. `outputReinforcedConcreteAmount` — 철근콘크리트공사 금회기성금액

- 설명: 철근·콘크리트·거푸집·동바리의 공종별 금회기성금액 합계.
- IRI: `rcpp:outputReinforcedConcreteAmount`
- 구분: `출력`
- 정의역·적용 클래스: `rcpp:CurrentProgressSummaryItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasAmountValue`
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressSummaryItem`

### 4.128. `outputRemainingAmount` — 잔여금액

- 설명: 계약금액에서 누계기성금액을 뺀 값.
- IRI: `rcpp:outputRemainingAmount`
- 구분: `계산`
- 정의역·적용 클래스: `rcpp:CurrentProgressDetailItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasAmountValue`
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressDetailItem`
- 산식: 잔여금액 = 계약금액 − 누계기성금액

### 4.129. `outputRemainingQuantity` — 잔여수량

- 설명: 기성수량산출서의 잔여수량을 기준값으로 직접 전달하고 계약수량에서 누계기성수량을 뺀 값은 교차검토에만 사용함.
- IRI: `rcpp:outputRemainingQuantity`
- 구분: `출력`
- 정의역·적용 클래스: `rcpp:CurrentProgressDetailItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasQuantityValue`
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressDetailItem`
- 산식: 출력 잔여수량 = 기성수량산출서 잔여수량 직접 전달

### 4.130. `outputRemarks` — 적요

- 설명: 항목의 특기사항 또는 산정 근거를 기록하는 출력 문자열.
- IRI: `rcpp:outputRemarks`
- 구분: `출력`
- 정의역·적용 클래스: `rcpp:CurrentProgressDetailItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressDetailItem`

### 4.131. `outputSpecification` — 규격

- 설명: 계약내역서에서 전달되는 최종 규격.
- IRI: `rcpp:outputSpecification`
- 구분: `출력`
- 정의역·적용 클래스: `rcpp:CurrentProgressDetailItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasSpecificationText`
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressDetailItem`

### 4.132. `outputSummaryContractAmount` — 공종별 계약금액

- 설명: 동일 공종에 속한 기성 상세내역의 계약금액을 합산한 공종별 계약금액 집계값.
- IRI: `rcpp:outputSummaryContractAmount`
- 구분: `출력`
- 정의역·적용 클래스: `rcpp:CurrentProgressSummaryItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasAmountValue`
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressSummaryItem`
- 산식: 공종별 계약금액 = Σ(공종 내 상세항목 계약금액)

### 4.133. `outputSummaryCumulativeAmount` — 공종별 누계기성금액

- 설명: 공종별 전회누계기성금액과 금회기성금액을 합산한 현재 회차까지의 공종별 누계 금액 집계값.
- IRI: `rcpp:outputSummaryCumulativeAmount`
- 구분: `출력`
- 정의역·적용 클래스: `rcpp:CurrentProgressSummaryItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasAmountValue`
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressSummaryItem`
- 산식: 공종별 누계기성금액 = 공종별 전회누계기성금액 + 공종별 금회기성금액

### 4.134. `outputSummaryCurrentAmount` — 공종별 금회기성금액

- 설명: 동일 공종에 속한 기성 상세내역의 금회기성금액을 합산한 공종별 현재 회차 금액 집계값.
- IRI: `rcpp:outputSummaryCurrentAmount`
- 구분: `출력`
- 정의역·적용 클래스: `rcpp:CurrentProgressSummaryItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasAmountValue`
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressSummaryItem`
- 산식: 공종별 금회기성금액 = Σ(공종 내 상세항목 금회기성금액)

### 4.135. `outputSummaryPreviousAmount` — 공종별 전회누계기성금액

- 설명: 동일 공종에 속한 기성 상세내역의 전회누계기성금액을 합산한 공종별 이월 금액 집계값.
- IRI: `rcpp:outputSummaryPreviousAmount`
- 구분: `출력`
- 정의역·적용 클래스: `rcpp:CurrentProgressSummaryItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasAmountValue`
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressSummaryItem`
- 산식: 공종별 전회누계기성금액 = Σ(공종 내 상세항목 전회누계기성금액)

### 4.136. `outputSummaryWorkCategoryText` — 집계행 원문 공종문구

- 설명: 결과서류 내부 집계행에 표시되는 원문 공종명. 표준 공종은 belongsToWorkCategory로 연결함.
- IRI: `rcpp:outputSummaryWorkCategoryText`
- 구분: `출력`
- 정의역·적용 클래스: `rcpp:CurrentProgressSummaryItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasSourceWorkCategoryText`
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressSummaryItem`

### 4.137. `outputUnit` — 단위

- 설명: 계약내역서 단위 및 수량산출결과 단위와 같아야 하는 출력 단위.
- IRI: `rcpp:outputUnit`
- 구분: `출력`
- 정의역·적용 클래스: `rcpp:CurrentProgressDetailItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasSourceUnitText`
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressDetailItem`

### 4.138. `outputWorkDescription` — 공사내역

- 설명: 계약내역서의 공종과 세부품목을 조합하거나 그대로 전달한 최종 공사내역.
- IRI: `rcpp:outputWorkDescription`
- 구분: `출력`
- 정의역·적용 클래스: `rcpp:CurrentProgressDetailItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasItemName`
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rdfs:domain` → `rcpp:CurrentProgressDetailItem`

### 4.139. `outputWorkType` — 공종

- 설명: 계약내역서와 기성수량산출서에서 전달되는 철근·콘크리트·거푸집·동바리 공종.
- IRI: `rcpp:outputWorkType`
- 구분: `출력`
- 정의역·적용 클래스: `rcpp:CurrentProgressDetailItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasSourceWorkCategoryText`
- 적용 서류: `rcpp:CurrentProgressStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressStatement`
  - `rcpp:groupsByField` → `rcpp:outputSummaryWorkCategoryText`
  - `rdfs:domain` → `rcpp:CurrentProgressDetailItem`

### 4.140. `parentWorkCategory` — 상위 공종분류

- 설명: 세부 공종분류 개체를 직접 상위의 포괄 공종분류 개체에 연결하는 계층 관계.
- IRI: `rcpp:parentWorkCategory`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:WorkCategory`
- 치역: `rcpp:WorkCategory`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:WorkCategory`
  - `rdfs:range` → `rcpp:WorkCategory`

### 4.141. `placementCondition` — 시공조건

- 설명: 타설 난이도나 조건의 구분.
- IRI: `rcpp:placementCondition`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:ConcretePlacementCostItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ConcretePlacementCostItem`
- 포함 조건: 타설 난이도나 시공조건에 따라 계약단가가 달라지는 경우

### 4.142. `placementMethod` — 타설방법

- 설명: 콘크리트를 타설하는 방식.
- IRI: `rcpp:placementMethod`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:ConcretePlacementCostItem`
- 치역: `rcpp:PlacementMethod`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ConcretePlacementCostItem`
  - `rdfs:range` → `rcpp:PlacementMethod`
- 포함 조건: 타설방식에 따라 계약단가가 달라지는 경우

### 4.143. `precedesDocument` — 실제 다음 서류

- 설명: 특정 프로젝트에서 실제로 확인된 서류 작성·전달 순서를 연결함.
- IRI: `rcpp:precedesDocument`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:ProgressDocument`
- 치역: `rcpp:ProgressDocument`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ProgressDocument`
  - `rdfs:range` → `rcpp:ProgressDocument`

### 4.144. `previousCumulativeAmount` — 전회누계기성금액

- 설명: 전회까지 누계된 금액이며 누계기성금액의 입력.
- IRI: `rcpp:previousCumulativeAmount`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:PreviousProgressStatementItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasAmountValue`
- 적용 서류: `rcpp:PreviousProgressStatement`
- 주요 관계:
  - `rcpp:consistencyComparedWith` → `rcpp:outputPreviousAmount`
  - `rcpp:fieldOfDocument` → `rcpp:PreviousProgressStatement`
  - `rcpp:mapsDirectlyTo` → `rcpp:outputPreviousAmount`
  - `rdfs:domain` → `rcpp:PreviousProgressStatementItem`

### 4.145. `previousCumulativeQuantity` — 전회누계기성수량

- 설명: 전회까지 인정되어 누계된 수량이며 금회 누계·잔여수량의 입력.
- IRI: `rcpp:previousCumulativeQuantity`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:PreviousProgressStatementItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasQuantityValue`
- 적용 서류: `rcpp:PreviousProgressStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:PreviousProgressStatement`
  - `rcpp:mapsDirectlyTo` → `rcpp:outputPreviousQuantity`
  - `rcpp:mapsDirectlyTo` → `rcpp:progressPreviousCumulativeQuantity`
  - `rdfs:domain` → `rcpp:PreviousProgressStatementItem`

### 4.146. `previousCumulativeRate` — 전회누계기성비율(%)

- 설명: 전회누계기성금액을 계약금액으로 나눈 비율이며 산식 결과와 교차확인함.
- IRI: `rcpp:previousCumulativeRate`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:PreviousProgressStatementItem`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: `rcpp:PreviousProgressStatement`
- 주요 관계:
  - `rcpp:consistencyComparedWith` → `rcpp:outputPreviousRate`
  - `rcpp:fieldOfDocument` → `rcpp:PreviousProgressStatement`
  - `rcpp:mapsDirectlyTo` → `rcpp:outputPreviousRate`
  - `rdfs:domain` → `rcpp:PreviousProgressStatementItem`

### 4.147. `previousItemCode` — 전회 품목코드

- 설명: 계약내역서 품목코드와 연결되는 전회 내역 행 식별자.
- IRI: `rcpp:previousItemCode`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:PreviousProgressStatementItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasItemCode`
- 적용 서류: `rcpp:PreviousProgressStatement`
- 주요 관계:
  - `rcpp:consistencyComparedWith` → `rcpp:outputItemCode`
  - `rcpp:consistencyComparedWith` → `rcpp:progressQuantityItemCode`
  - `rcpp:fieldOfDocument` → `rcpp:PreviousProgressStatement`
  - `rcpp:matchesWithField` → `rcpp:contractItemCode`
  - `rdfs:domain` → `rcpp:PreviousProgressStatementItem`

### 4.148. `previousProgressRound` — 이전 기성회차

- 설명: 전회누계값 이월과 회차 연속성을 확인하기 위한 직전 기성회차 관계.
- IRI: `rcpp:previousProgressRound`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:ProgressPaymentRound`
- 치역: `rcpp:ProgressPaymentRound`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ProgressPaymentRound`
  - `rdfs:range` → `rcpp:ProgressPaymentRound`

### 4.149. `previousQuantityFrom` — 전회누계수량 이월출처

- 설명: 현재 기성수량 항목의 전회누계기성수량을 전회 기성항목의 확정값에 연결함.
- IRI: `rcpp:previousQuantityFrom`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:CurrentProgressQuantityItem`
- 치역: `rcpp:PreviousProgressStatementItem`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:CurrentProgressQuantityItem`
  - `rdfs:range` → `rcpp:PreviousProgressStatementItem`

### 4.150. `previousSpecification` — 전회 규격

- 설명: 계약 규격과 비교하는 전회 내역 규격.
- IRI: `rcpp:previousSpecification`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:PreviousProgressStatementItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasSpecificationText`
- 적용 서류: `rcpp:PreviousProgressStatement`
- 주요 관계:
  - `rcpp:consistencyComparedWith` → `rcpp:outputSpecification`
  - `rcpp:consistencyComparedWith` → `rcpp:progressQuantitySpecification`
  - `rcpp:fieldOfDocument` → `rcpp:PreviousProgressStatement`
  - `rcpp:matchesWithField` → `rcpp:contractSpecification`
  - `rdfs:domain` → `rcpp:PreviousProgressStatementItem`

### 4.151. `previousUnit` — 전회 단위

- 설명: 계약 및 금회 출력 단위와 비교하는 전회 내역 단위.
- IRI: `rcpp:previousUnit`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:PreviousProgressStatementItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasSourceUnitText`
- 적용 서류: `rcpp:PreviousProgressStatement`
- 주요 관계:
  - `rcpp:consistencyComparedWith` → `rcpp:contractUnit`
  - `rcpp:consistencyComparedWith` → `rcpp:outputUnit`
  - `rcpp:consistencyComparedWith` → `rcpp:progressQuantityUnit`
  - `rcpp:fieldOfDocument` → `rcpp:PreviousProgressStatement`
  - `rcpp:matchesWithField` → `rcpp:contractUnit`
  - `rdfs:domain` → `rcpp:PreviousProgressStatementItem`

### 4.152. `previousWorkDescription` — 전회 공사내역

- 설명: 계약 세부품목명과 비교하는 전회 공사내역.
- IRI: `rcpp:previousWorkDescription`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:PreviousProgressStatementItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasItemName`
- 적용 서류: `rcpp:PreviousProgressStatement`
- 주요 관계:
  - `rcpp:consistencyComparedWith` → `rcpp:outputWorkDescription`
  - `rcpp:consistencyComparedWith` → `rcpp:progressQuantityItemName`
  - `rcpp:fieldOfDocument` → `rcpp:PreviousProgressStatement`
  - `rcpp:matchesWithField` → `rcpp:contractItemName`
  - `rdfs:domain` → `rcpp:PreviousProgressStatementItem`

### 4.153. `processStage` — 처리 단계

- 설명: 기성서류 작성 흐름에서 담당하는 단계를 표시함.
- IRI: `rcpp:processStage`
- 구분: -
- 정의역·적용 클래스: -
- 치역: `rdfs:Literal`
- 상위 속성: -
- 적용 서류: -

### 4.154. `processingStage` — 자릿수 처리시점

- 설명: 수량변환·품목금액·공종합계·총합계 중 반올림 또는 절사를 적용하는 단계.
- IRI: `rcpp:processingStage`
- 구분: -
- 정의역·적용 클래스: `rcpp:CalculationRule`
- 치역: `rdfs:Literal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:CalculationRule`

### 4.155. `producesField` — 산출항목 생성

- 설명: 계산 유형이 산식을 적용하여 생성하는 서류 데이터 항목.
- IRI: `rcpp:producesField`
- 구분: `관계`
- 정의역·적용 클래스: `rdfs:Class`
- 치역: `rdf:Property`
- 상위 속성: -
- 적용 서류: -

### 4.156. `progressCumulativeQuantity` — 누계기성수량

- 설명: 전회누계기성수량과 금회기성수량의 합.
- IRI: `rcpp:progressCumulativeQuantity`
- 구분: `계산`
- 정의역·적용 클래스: `rcpp:CurrentProgressQuantityItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasQuantityValue`
- 적용 서류: `rcpp:CurrentProgressQuantitySheet`
- 주요 관계:
  - `rcpp:calculationInputFor` → `rcpp:progressRemainingQuantity`
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressQuantitySheet`
  - `rcpp:mapsDirectlyTo` → `rcpp:outputCumulativeQuantity`
  - `rdfs:domain` → `rcpp:CurrentProgressQuantityItem`
- 산식: 누계기성수량 = 전회누계기성수량 + 금회기성수량

### 4.157. `progressCurrentQuantity` — 금회기성수량

- 설명: 현재 기성회차의 비용산정에 적용하는 확정 수량.
- IRI: `rcpp:progressCurrentQuantity`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:CurrentProgressQuantityItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasQuantityValue`
- 적용 서류: `rcpp:CurrentProgressQuantitySheet`
- 주요 관계:
  - `rcpp:calculationInputFor` → `rcpp:progressCumulativeQuantity`
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressQuantitySheet`
  - `rcpp:inputToCalculationClass` → `rcpp:CurrentProgressAmountCalculation`
  - `rcpp:mapsDirectlyTo` → `rcpp:outputCurrentQuantity`
  - `rdfs:domain` → `rcpp:CurrentProgressQuantityItem`

### 4.158. `progressPreviousCumulativeQuantity` — 전회누계기성수량

- 설명: 전회 공사기성부분내역서에서 이월된 누계수량.
- IRI: `rcpp:progressPreviousCumulativeQuantity`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:CurrentProgressQuantityItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasQuantityValue`
- 적용 서류: `rcpp:CurrentProgressQuantitySheet`
- 주요 관계:
  - `rcpp:calculationInputFor` → `rcpp:progressCumulativeQuantity`
  - `rcpp:consistencyComparedWith` → `rcpp:outputPreviousQuantity`
  - `rcpp:consistencyComparedWith` → `rcpp:previousCumulativeQuantity`
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressQuantitySheet`
  - `rdfs:domain` → `rcpp:CurrentProgressQuantityItem`

### 4.159. `progressQuantityItemCode` — 내역코드

- 설명: 계약항목과 기성수량 행을 연결하는 코드.
- IRI: `rcpp:progressQuantityItemCode`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:CurrentProgressQuantityItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasItemCode`
- 적용 서류: `rcpp:CurrentProgressQuantitySheet`
- 주요 관계:
  - `rcpp:consistencyComparedWith` → `rcpp:outputItemCode`
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressQuantitySheet`
  - `rcpp:matchesWithField` → `rcpp:contractItemCode`
  - `rdfs:domain` → `rcpp:CurrentProgressQuantityItem`

### 4.160. `progressQuantityItemName` — 품명

- 설명: 계약 품명과 연결되는 기성수량 대상명.
- IRI: `rcpp:progressQuantityItemName`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:CurrentProgressQuantityItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasItemName`
- 적용 서류: `rcpp:CurrentProgressQuantitySheet`
- 주요 관계:
  - `rcpp:consistencyComparedWith` → `rcpp:outputWorkDescription`
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressQuantitySheet`
  - `rcpp:matchesWithField` → `rcpp:contractItemName`
  - `rdfs:domain` → `rcpp:CurrentProgressQuantityItem`

### 4.161. `progressQuantitySpecification` — 규격

- 설명: 계약 규격과 연결되는 기성수량 대상 규격.
- IRI: `rcpp:progressQuantitySpecification`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:CurrentProgressQuantityItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasSpecificationText`
- 적용 서류: `rcpp:CurrentProgressQuantitySheet`
- 주요 관계:
  - `rcpp:consistencyComparedWith` → `rcpp:outputSpecification`
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressQuantitySheet`
  - `rcpp:matchesWithField` → `rcpp:contractSpecification`
  - `rdfs:domain` → `rcpp:CurrentProgressQuantityItem`

### 4.162. `progressQuantityUnit` — 단위

- 설명: 금회기성수량과 계약단가 적용에 사용하는 측정단위.
- IRI: `rcpp:progressQuantityUnit`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:CurrentProgressQuantityItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasSourceUnitText`
- 적용 서류: `rcpp:CurrentProgressQuantitySheet`
- 주요 관계:
  - `rcpp:consistencyComparedWith` → `rcpp:contractUnit`
  - `rcpp:consistencyComparedWith` → `rcpp:outputUnit`
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressQuantitySheet`
  - `rcpp:matchesWithField` → `rcpp:contractUnit`
  - `rdfs:domain` → `rcpp:CurrentProgressQuantityItem`

### 4.163. `progressQuantityWorkType` — 공종

- 설명: 동일 기성항목을 연결하고 공종별 산식을 선택하는 분류.
- IRI: `rcpp:progressQuantityWorkType`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:CurrentProgressQuantityItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasSourceWorkCategoryText`
- 적용 서류: `rcpp:CurrentProgressQuantitySheet`
- 주요 관계:
  - `rcpp:consistencyComparedWith` → `rcpp:outputWorkType`
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressQuantitySheet`
  - `rcpp:matchesWithField` → `rcpp:contractWorkType`
  - `rdfs:domain` → `rcpp:CurrentProgressQuantityItem`

### 4.164. `progressRemainingQuantity` — 잔여수량

- 설명: 계약수량에서 누계기성수량을 뺀 미기성 수량.
- IRI: `rcpp:progressRemainingQuantity`
- 구분: `계산`
- 정의역·적용 클래스: `rcpp:CurrentProgressQuantityItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasQuantityValue`
- 적용 서류: `rcpp:CurrentProgressQuantitySheet`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:CurrentProgressQuantitySheet`
  - `rcpp:mapsDirectlyTo` → `rcpp:outputRemainingQuantity`
  - `rdfs:domain` → `rcpp:CurrentProgressQuantityItem`
- 산식: 잔여수량 = 계약수량 − 누계기성수량

### 4.165. `progressRoundNumber` — 기성 회차번호

- 설명: 하나의 프로젝트 안에서 기성회차의 순서를 구분하는 정수 번호.
- IRI: `rcpp:progressRoundNumber`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:ProgressPaymentRound`
- 치역: `xsd:integer`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ProgressPaymentRound`

### 4.166. `progressRoundReferenceDate` — 기성회차 기준일

- 설명: 해당 기성회차의 수량·금액·누계값을 확정하거나 실적을 집계하는 기준 날짜.
- IRI: `rcpp:progressRoundReferenceDate`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:ProgressPaymentRound`
- 치역: `xsd:date`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ProgressPaymentRound`

### 4.167. `projectIdentifier` — 프로젝트 식별자

- 설명: 서로 다른 프로젝트 개체를 구분하는 기관·사업 기준의 고유 식별 문자열.
- IRI: `rcpp:projectIdentifier`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:Project`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:Project`

### 4.168. `projectName` — 프로젝트명

- 설명: 계약·기성서류에서 프로젝트를 표시하는 사업 또는 공사 명칭.
- IRI: `rcpp:projectName`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:Project`
- 치역: `rdfs:Literal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:Project`

### 4.169. `propertyCategory` — 속성 구분

- 설명: 관계·식별·입력·계산·출력 속성을 구분함.
- IRI: `rcpp:propertyCategory`
- 구분: -
- 정의역·적용 클래스: -
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -

### 4.170. `quantityAggregatedInto` — 기성수량항목으로 합산

- 설명: 위치·부재별 상세수량행을 동일 계약항목 단위의 금회기성수량 항목으로 합산함.
- IRI: `rcpp:quantityAggregatedInto`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:ProgressQuantityDetailItem`
- 치역: `rcpp:CurrentProgressQuantityItem`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ProgressQuantityDetailItem`
  - `rdfs:range` → `rcpp:CurrentProgressQuantityItem`

### 4.171. `quantityBand` — 물량구간

- 설명: 일회 또는 항목별 타설량에 적용되는 단가 구간.
- IRI: `rcpp:quantityBand`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:ConcretePlacementCostItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ConcretePlacementCostItem`
- 포함 조건: 일회 또는 항목별 타설량 구간에 따라 계약단가가 달라지는 경우

### 4.172. `quantityBasisFrom` — 계약수량 산출근거

- 설명: 계약 내역의 계약수량을 수량산출 내역의 산출수량·산식 근거에 연결함.
- IRI: `rcpp:quantityBasisFrom`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:ContractStatementItem`
- 치역: `rcpp:QuantityCalculationItem`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ContractStatementItem`
  - `rdfs:range` → `rcpp:QuantityCalculationItem`

### 4.173. `quantityCalculatedQuantity` — 산출수량

- 설명: 공종별 산식 결과를 합산하여 계약수량으로 전달하는 수량산출 결과.
- IRI: `rcpp:quantityCalculatedQuantity`
- 구분: `계산`
- 정의역·적용 클래스: `rcpp:QuantityCalculationItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasQuantityValue`
- 적용 서류: `rcpp:QuantityCalculationSheet`
- 주요 관계:
  - `rcpp:consistencyComparedWith` → `rcpp:contractQuantity`
  - `rcpp:fieldOfDocument` → `rcpp:QuantityCalculationSheet`
  - `rdfs:domain` → `rcpp:QuantityCalculationItem`
- 산식: 산출수량 = 선택된 공종별 수량산식 결과의 합계

### 4.174. `quantityCalculationBasis` — 수량산출근거

- 설명: 계약수량을 구성한 구조물·위치·규격·산식의 근거.
- IRI: `rcpp:quantityCalculationBasis`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:QuantityCalculationItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: `rcpp:QuantityCalculationSheet`
- 주요 관계:
  - `rcpp:consistencyComparedWith` → `rcpp:contractQuantityBasis`
  - `rcpp:fieldOfDocument` → `rcpp:QuantityCalculationSheet`
  - `rdfs:domain` → `rcpp:QuantityCalculationItem`

### 4.175. `quantityCalculationCode` — 수량산출 항목코드

- 설명: 수량산출서 내부의 산출 행 식별자.
- IRI: `rcpp:quantityCalculationCode`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:QuantityCalculationItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: `rcpp:QuantityCalculationSheet`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:QuantityCalculationSheet`
  - `rdfs:domain` → `rcpp:QuantityCalculationItem`

### 4.176. `quantityContractItemCode` — 내역코드

- 설명: 계약내역서 및 후속 서류의 동일 내역항목을 연결하는 수량산출 행 코드.
- IRI: `rcpp:quantityContractItemCode`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:QuantityCalculationItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasItemCode`
- 적용 서류: `rcpp:QuantityCalculationSheet`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:QuantityCalculationSheet`
  - `rcpp:matchesWithField` → `rcpp:contractItemCode`
  - `rdfs:domain` → `rcpp:QuantityCalculationItem`

### 4.177. `quantityFormula` — 수량산식

- 설명: 구조물·위치·규격·치수를 수량으로 변환하는 공종별 계산식.
- IRI: `rcpp:quantityFormula`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:QuantityCalculationItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: `rcpp:QuantityCalculationSheet`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:QuantityCalculationSheet`
  - `rdfs:domain` → `rcpp:QuantityCalculationItem`

### 4.178. `quantityItemName` — 품명

- 설명: 계약 품명으로 전달되는 수량산출 대상 명칭.
- IRI: `rcpp:quantityItemName`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:QuantityCalculationItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasItemName`
- 적용 서류: `rcpp:QuantityCalculationSheet`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:QuantityCalculationSheet`
  - `rcpp:matchesWithField` → `rcpp:contractItemName`
  - `rdfs:domain` → `rcpp:QuantityCalculationItem`

### 4.179. `quantitySpecification` — 규격

- 설명: 계약 규격으로 전달되고 동일 품목 판별에 사용하는 세부 조건.
- IRI: `rcpp:quantitySpecification`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:QuantityCalculationItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasSpecificationText`
- 적용 서류: `rcpp:QuantityCalculationSheet`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:QuantityCalculationSheet`
  - `rcpp:matchesWithField` → `rcpp:contractSpecification`
  - `rdfs:domain` → `rcpp:QuantityCalculationItem`

### 4.180. `quantityTolerance` — 수량 허용오차

- 설명: 단위변환 또는 소수 자릿수 차이로 발생하는 수량 비교 허용범위.
- IRI: `rcpp:quantityTolerance`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:CalculationPolicy`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:CalculationPolicy`

### 4.181. `quantityUnit` — 단위

- 설명: 산출수량과 계약수량에 공통으로 적용되는 측정기준.
- IRI: `rcpp:quantityUnit`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:QuantityCalculationItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasSourceUnitText`
- 적용 서류: `rcpp:QuantityCalculationSheet`
- 주요 관계:
  - `rcpp:consistencyComparedWith` → `rcpp:contractUnit`
  - `rcpp:fieldOfDocument` → `rcpp:QuantityCalculationSheet`
  - `rcpp:matchesWithField` → `rcpp:contractUnit`
  - `rdfs:domain` → `rcpp:QuantityCalculationItem`

### 4.182. `quantityWorkType` — 공종

- 설명: 철근·콘크리트·거푸집·동바리 산식을 선택하고 계약 공종으로 전달하는 분류.
- IRI: `rcpp:quantityWorkType`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:QuantityCalculationItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasSourceWorkCategoryText`
- 적용 서류: `rcpp:QuantityCalculationSheet`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:QuantityCalculationSheet`
  - `rcpp:matchesWithField` → `rcpp:contractWorkType`
  - `rdfs:domain` → `rcpp:QuantityCalculationItem`

### 4.183. `rebarGrade` — 강종

- 설명: 철근의 재료 강도 등급.
- IRI: `rcpp:rebarGrade`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:RebarCostItem`
- 치역: `rcpp:RebarGrade`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:RebarCostItem`
  - `rdfs:range` → `rcpp:RebarGrade`

### 4.184. `rebarType` — 철근형태

- 설명: 철근의 형상 또는 종류.
- IRI: `rcpp:rebarType`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:RebarCostItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:RebarCostItem`
- 포함 조건: 철근의 형상 또는 종류가 계약항목이나 계약단가를 구분하는 경우

### 4.185. `rebarWorkType` — 철근 작업유형

- 설명: 철근에 수행되는 비용산정 작업.
- IRI: `rcpp:rebarWorkType`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:RebarCostItem`
- 치역: `rcpp:RebarWorkType`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:RebarCostItem`
  - `rdfs:range` → `rcpp:RebarWorkType`

### 4.186. `representsCostItem` — 표준 비용항목 연결

- 설명: 실제 서류내역 개체가 어느 표준 비용항목 개체를 표현하는지 연결함.
- IRI: `rcpp:representsCostItem`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:DocumentItem`
- 치역: `rcpp:CostItem`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:DocumentItem`
  - `rdfs:range` → `rcpp:CostItem`

### 4.187. `requiredForClass` — 요구 적용 클래스

- 설명: 해당 속성 요구조건이 적용되는 서류내역 클래스.
- IRI: `rcpp:requiredForClass`
- 구분: -
- 정의역·적용 클래스: `rcpp:FieldRequirement`
- 치역: `rdfs:Class`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:FieldRequirement`

### 4.188. `requiredProperty` — 요구 속성

- 설명: 클래스별 필드 요구조건이 대상으로 삼는 속성.
- IRI: `rcpp:requiredProperty`
- 구분: -
- 정의역·적용 클래스: `rcpp:FieldRequirement`
- 치역: `rdf:Property`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:FieldRequirement`

### 4.189. `requirementLevel` — 요구수준

- 설명: 필수·조건부·권장 등 속성과 적용 클래스 조합의 요구수준.
- IRI: `rcpp:requirementLevel`
- 구분: -
- 정의역·적용 클래스: `rcpp:FieldRequirement`
- 치역: `rdfs:Literal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:FieldRequirement`

### 4.190. `requirementPurpose` — 요구 목적

- 설명: 원천입력·이월입력·계산입력·계산결과·결과서류출력·교차검토 중 필드 요구조건의 데이터 흐름상 역할.
- IRI: `rcpp:requirementPurpose`
- 구분: -
- 정의역·적용 클래스: `rcpp:FieldRequirement`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:FieldRequirement`

### 4.191. `reuseCount` — 전용횟수

- 설명: 동일 거푸집을 반복 사용하는 횟수.
- IRI: `rcpp:reuseCount`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:FormworkCostItem`
- 치역: `xsd:integer`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:FormworkCostItem`
- 포함 조건: 동일 거푸집의 전용횟수에 따라 계약단가가 달라지는 경우

### 4.192. `reviewStatus` — 매칭 검토상태

- 설명: 후보·승인·반려 등 매칭 결과의 사람 검토 상태.
- IRI: `rcpp:reviewStatus`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:DocumentItemMatching`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:DocumentItemMatching`

### 4.193. `reviewedBy` — 매칭 검토자

- 설명: 매칭 결과를 확인하거나 승인한 담당자의 식별자 또는 역할명.
- IRI: `rcpp:reviewedBy`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:DocumentItemMatching`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:DocumentItemMatching`

### 4.194. `roundingMode` — 반올림 방식

- 설명: 계산된 금액의 지정 자릿수 이하를 반올림·절사·올림 처리하는 방식.
- IRI: `rcpp:roundingMode`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:CalculationPolicy`
- 치역: `rcpp:RoundingMode`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:CalculationPolicy`
  - `rdfs:range` → `rcpp:RoundingMode`

### 4.195. `ruleVersion` — 규칙버전

- 설명: 정규화 규격코드 생성방식의 변경을 식별하는 버전.
- IRI: `rcpp:ruleVersion`
- 구분: -
- 정의역·적용 클래스: `rcpp:SpecificationNormalizationRule`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:SpecificationNormalizationRule`

### 4.196. `schemaFlowsTo` — 스키마상 다음 단계

- 설명: 문서·매칭·계산 클래스 사이의 개념적 처리 순서를 설명하는 클래스 수준 관계.
- IRI: `rcpp:schemaFlowsTo`
- 구분: `스키마관계`
- 정의역·적용 클래스: -
- 치역: `rdfs:Class`
- 상위 속성: -
- 적용 서류: -

### 4.197. `shoringType` — 동바리 종류

- 설명: 재료 또는 시스템에 따른 동바리 구분.
- IRI: `rcpp:shoringType`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:ShoringCostItem`
- 치역: `rcpp:ShoringType`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ShoringCostItem`
  - `rdfs:range` → `rcpp:ShoringType`

### 4.198. `shoringWorkType` — 동바리 작업유형

- 설명: 동바리 비용에 포함되는 작업 범위.
- IRI: `rcpp:shoringWorkType`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:ShoringCostItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ShoringCostItem`

### 4.199. `slump` — 슬럼프(mm)

- 설명: 레미콘 계약 규격을 구분하는 슬럼프값.
- IRI: `rcpp:slump`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:ReadyMixedConcreteCostItem`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ReadyMixedConcreteCostItem`

### 4.200. `sourceCellRange` — 원천 셀범위

- 설명: 스프레드시트에서 값이 위치한 셀 또는 셀 범위.
- IRI: `rcpp:sourceCellRange`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:SourceLocation`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:SourceLocation`

### 4.201. `sourceFieldLabel` — 원문 필드명

- 설명: 표준 온톨로지 개념에 대응하는 프로젝트 서류의 원래 열 이름이나 동의 표현.
- IRI: `rcpp:sourceFieldLabel`
- 구분: -
- 정의역·적용 클래스: -
- 치역: `rdfs:Literal`
- 상위 속성: -
- 적용 서류: -

### 4.202. `sourceFileName` — 원천 파일명

- 설명: 값을 추출한 실제 파일의 이름.
- IRI: `rcpp:sourceFileName`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:SourceLocation`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:SourceLocation`

### 4.203. `sourceItem` — 매칭 원천항목

- 설명: 매칭 후보를 생성할 때 비교의 출발점이 된 서류내역.
- IRI: `rcpp:sourceItem`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:DocumentItemMatching`
- 치역: `rcpp:DocumentItem`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:DocumentItemMatching`
  - `rdfs:range` → `rcpp:DocumentItem`

### 4.204. `sourcePageNumber` — 원천 페이지번호

- 설명: 페이지형 문서에서 값이 위치한 페이지 번호.
- IRI: `rcpp:sourcePageNumber`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:SourceLocation`
- 치역: `xsd:integer`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:SourceLocation`

### 4.205. `sourceRowNumber` — 원천 행번호

- 설명: 표 또는 스프레드시트에서 값이 위치한 행 번호.
- IRI: `rcpp:sourceRowNumber`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:SourceLocation`
- 치역: `xsd:integer`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:SourceLocation`

### 4.206. `sourceSheetName` — 원천 시트명

- 설명: 스프레드시트에서 값이 위치한 시트 이름.
- IRI: `rcpp:sourceSheetName`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:SourceLocation`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:SourceLocation`

### 4.207. `sourceValueAlias` — 원문 값 별칭

- 설명: 프로젝트 원문에서 같은 표준 범주값으로 매핑되는 철자·언어·표현 변형.
- IRI: `rcpp:sourceValueAlias`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:ControlledSpecificationValue`, `rcpp:Unit`, `rcpp:WorkCategory`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rcpp:appliesToClass` → `rcpp:ControlledSpecificationValue`
  - `rcpp:appliesToClass` → `rcpp:Unit`
  - `rcpp:appliesToClass` → `rcpp:WorkCategory`

### 4.208. `specificationRequirement` — 규격속성 필요도

- 설명: 비용 관련 규격속성이 우선 포함인지 계약단가 구분 시 조건부 포함인지 표시함.
- IRI: `rcpp:specificationRequirement`
- 구분: -
- 정의역·적용 클래스: -
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -

### 4.209. `spliceMethod` — 이음방식

- 설명: 철근 이음의 종류.
- IRI: `rcpp:spliceMethod`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:RebarCostItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:RebarCostItem`
- 포함 조건: 철근 이음방식에 별도 계약단가가 적용되는 경우

### 4.210. `summaryContractAmount` — 공종별 계약금액

- 설명: 공종별내역서의 계약금액 합계이며 결과 집계금액과 교차검토함.
- IRI: `rcpp:summaryContractAmount`
- 구분: `계산`
- 정의역·적용 클래스: `rcpp:WorkTypeSummaryItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasAmountValue`
- 적용 서류: `rcpp:WorkTypeSummaryStatement`
- 주요 관계:
  - `rcpp:consistencyComparedWith` → `rcpp:outputSummaryContractAmount`
  - `rcpp:fieldOfDocument` → `rcpp:WorkTypeSummaryStatement`
  - `rdfs:domain` → `rcpp:WorkTypeSummaryItem`
- 산식: 공종별 계약금액 = Σ(동일 공종 내역항목별 계약금액)

### 4.211. `summaryDirectCost` — 직접공사비 합계

- 설명: 공종별내역서에 기록된 세부 직접공사비를 동일 공종별로 합산한 값.
- IRI: `rcpp:summaryDirectCost`
- 구분: `계산`
- 정의역·적용 클래스: `rcpp:WorkTypeSummaryItem`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: `rcpp:WorkTypeSummaryStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:WorkTypeSummaryStatement`
  - `rdfs:domain` → `rcpp:WorkTypeSummaryItem`
- 산식: 공종별 직접공사비 합계 = Σ(동일 공종 세부 직접공사비)

### 4.212. `summaryWorkType` — 공종

- 설명: 철근·콘크리트·거푸집·동바리의 집계 단위.
- IRI: `rcpp:summaryWorkType`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:WorkTypeSummaryItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasSourceWorkCategoryText`
- 적용 서류: `rcpp:WorkTypeSummaryStatement`
- 주요 관계:
  - `rcpp:consistencyComparedWith` → `rcpp:outputSummaryWorkCategoryText`
  - `rcpp:fieldOfDocument` → `rcpp:WorkTypeSummaryStatement`
  - `rdfs:domain` → `rcpp:WorkTypeSummaryItem`

### 4.213. `supportAmount` — 지원자료 금액·집계

- 설명: 품목별·공종별·전체 금액을 교차확인하는 지원자료 금액.
- IRI: `rcpp:supportAmount`
- 구분: `계산`
- 정의역·적용 클래스: `rcpp:SupportingReferenceItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasAmountValue`
- 적용 서류: `rcpp:SupportingReferenceDocument`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:SupportingReferenceDocument`
  - `rdfs:domain` → `rcpp:SupportingReferenceItem`

### 4.214. `supportItemCode` — 지원자료 품목코드

- 설명: 지원서류의 행을 계약 품목코드와 연결하는 식별항목.
- IRI: `rcpp:supportItemCode`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:SupportingReferenceItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasItemCode`
- 적용 서류: `rcpp:SupportingReferenceDocument`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:SupportingReferenceDocument`
  - `rcpp:matchesWithField` → `rcpp:contractItemCode`
  - `rdfs:domain` → `rcpp:SupportingReferenceItem`

### 4.215. `supportItemName` — 지원자료 품목명

- 설명: 계약 세부품목과 비교하는 지원자료 품목명.
- IRI: `rcpp:supportItemName`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:SupportingReferenceItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasItemName`
- 적용 서류: `rcpp:SupportingReferenceDocument`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:SupportingReferenceDocument`
  - `rcpp:matchesWithField` → `rcpp:contractItemName`
  - `rdfs:domain` → `rcpp:SupportingReferenceItem`

### 4.216. `supportQuantity` — 지원자료 수량

- 설명: 품목 또는 집계의 교차확인에 사용하는 지원자료 수량.
- IRI: `rcpp:supportQuantity`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:SupportingReferenceItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasQuantityValue`
- 적용 서류: `rcpp:SupportingReferenceDocument`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:SupportingReferenceDocument`
  - `rdfs:domain` → `rcpp:SupportingReferenceItem`

### 4.217. `supportSpecification` — 지원자료 규격

- 설명: 계약 규격과 비교하는 지원자료 규격.
- IRI: `rcpp:supportSpecification`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:SupportingReferenceItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasSpecificationText`
- 적용 서류: `rcpp:SupportingReferenceDocument`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:SupportingReferenceDocument`
  - `rcpp:matchesWithField` → `rcpp:contractSpecification`
  - `rdfs:domain` → `rcpp:SupportingReferenceItem`

### 4.218. `supportUnit` — 지원자료 단위

- 설명: 계약 단위와 비교하는 지원자료 단위.
- IRI: `rcpp:supportUnit`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:SupportingReferenceItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasSourceUnitText`
- 적용 서류: `rcpp:SupportingReferenceDocument`
- 주요 관계:
  - `rcpp:consistencyComparedWith` → `rcpp:contractUnit`
  - `rcpp:fieldOfDocument` → `rcpp:SupportingReferenceDocument`
  - `rcpp:matchesWithField` → `rcpp:contractUnit`
  - `rdfs:domain` → `rcpp:SupportingReferenceItem`

### 4.219. `supportUnitPrice` — 지원자료 단가

- 설명: 계약단가 구성 또는 값을 교차확인하는 지원자료 단가.
- IRI: `rcpp:supportUnitPrice`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:SupportingReferenceItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasUnitPriceValue`
- 적용 서류: `rcpp:SupportingReferenceDocument`
- 주요 관계:
  - `rcpp:consistencyComparedWith` → `rcpp:contractUnitPrice`
  - `rcpp:fieldOfDocument` → `rcpp:SupportingReferenceDocument`
  - `rdfs:domain` → `rcpp:SupportingReferenceItem`

### 4.220. `supportWorkType` — 지원자료 공종

- 설명: 계약내역서 공종과 비교하는 지원자료 공종.
- IRI: `rcpp:supportWorkType`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:SupportingReferenceItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasSourceWorkCategoryText`
- 적용 서류: `rcpp:SupportingReferenceDocument`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:SupportingReferenceDocument`
  - `rcpp:matchesWithField` → `rcpp:contractWorkType`
  - `rdfs:domain` → `rcpp:SupportingReferenceItem`

### 4.221. `targetItem` — 매칭 대상항목

- 설명: 원천항목과 동일 비용항목인지 비교하는 대상 서류내역.
- IRI: `rcpp:targetItem`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:DocumentItemMatching`
- 치역: `rcpp:DocumentItem`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:DocumentItemMatching`
  - `rdfs:range` → `rcpp:DocumentItem`

### 4.222. `typicalNextDocumentClass` — 대표 다음 서류유형

- 설명: 연구 설명을 위한 대표 흐름이며 모든 프로젝트에 고정된 문서 순서를 의미하지 않음.
- IRI: `rcpp:typicalNextDocumentClass`
- 구분: `스키마관계`
- 정의역·적용 클래스: -
- 치역: `rdfs:Class`
- 상위 속성: -
- 적용 서류: -

### 4.223. `unitCode` — 단위 코드

- 설명: 원문 단위 표현을 정규화한 측정단위 개체를 식별하는 코드.
- IRI: `rcpp:unitCode`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:Unit`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:Unit`

### 4.224. `unitCondition` — 단위조건

- 설명: 계산 입력과 출력에서 충족해야 하는 단위 차원·변환 조건.
- IRI: `rcpp:unitCondition`
- 구분: -
- 정의역·적용 클래스: `rcpp:CalculationRule`
- 치역: `rdfs:Literal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:CalculationRule`

### 4.225. `unitDimension` — 단위 차원

- 설명: 길이·면적·체적·질량·개수 등 단위가 측정하는 물리 차원.
- IRI: `rcpp:unitDimension`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:Unit`
- 치역: `rdfs:Literal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:Unit`

### 4.226. `unitSymbol` — 단위 기호

- 설명: 수량과 함께 표시하는 측정단위의 짧은 기호 또는 현장 표기.
- IRI: `rcpp:unitSymbol`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:Unit`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:Unit`

### 4.227. `usesCalculationPolicy` — 금액 계산정책 사용

- 설명: 기성회차에 적용할 통화·반올림·자릿수·계산순서 정책을 연결함.
- IRI: `rcpp:usesCalculationPolicy`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:ProgressPaymentRound`
- 치역: `rcpp:CalculationPolicy`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ProgressPaymentRound`
  - `rdfs:range` → `rcpp:CalculationPolicy`

### 4.228. `usesSpecificationRule` — 규격코드 규칙 사용

- 설명: 표준 비용항목의 정규화 규격코드를 생성할 때 적용한 공종별 규칙.
- IRI: `rcpp:usesSpecificationRule`
- 구분: -
- 정의역·적용 클래스: `rcpp:CostItem`
- 치역: `rcpp:SpecificationNormalizationRule`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:CostItem`
  - `rdfs:range` → `rcpp:SpecificationNormalizationRule`

### 4.229. `usesUnit` — 측정단위 사용

- 설명: 서류내역 또는 표준 비용항목의 수량·단가에 적용되는 측정단위 자원을 연결함.
- IRI: `rcpp:usesUnit`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:CostItem`, `rcpp:DocumentItem`
- 치역: `rcpp:Unit`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rcpp:appliesToClass` → `rcpp:CostItem`
  - `rcpp:appliesToClass` → `rcpp:DocumentItem`
  - `rdfs:range` → `rcpp:Unit`

### 4.230. `usesUnitConversionRule` — 단위변환 규칙 사용

- 설명: 원천수량과 계약단가 기준단위가 다를 때 실제 계산에 적용한 변환규칙.
- IRI: `rcpp:usesUnitConversionRule`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:CalculationActivity`
- 치역: `rcpp:UnitConversionRule`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:CalculationActivity`
  - `rdfs:range` → `rcpp:UnitConversionRule`

### 4.231. `usesUnitPriceFrom` — 계약단가 참조

- 설명: 기성 상세내역이 대응 계약내역의 계약단가를 금액 계산에 사용함을 나타낸다. 기성수량 내역에는 사용하지 않음.
- IRI: `rcpp:usesUnitPriceFrom`
- 구분: `관계`
- 정의역·적용 클래스: `rcpp:DocumentItem`
- 치역: `rcpp:ContractStatementItem`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:DocumentItem`
  - `rdfs:range` → `rcpp:ContractStatementItem`

### 4.232. `usesVibrator` — 진동기 사용 여부

- 설명: 타설 작업에 진동기를 사용하는지 여부.
- IRI: `rcpp:usesVibrator`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:ConcretePlacementCostItem`
- 치역: `xsd:boolean`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ConcretePlacementCostItem`
- 포함 조건: 진동기 사용 여부에 따라 계약단가가 달라지는 경우

### 4.233. `verticalHeightBand` — 수직고구간

- 설명: 계약단가가 적용되는 수직 높이 범위.
- IRI: `rcpp:verticalHeightBand`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:FormworkCostItem`, `rcpp:ShoringCostItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rcpp:appliesToClass` → `rcpp:FormworkCostItem`
  - `rcpp:appliesToClass` → `rcpp:ShoringCostItem`

### 4.234. `visualizationGroup` — 시각화 그룹

- 설명: 서류·처리·산출유형 등 화면 배치 그룹.
- IRI: `rcpp:visualizationGroup`
- 구분: -
- 정의역·적용 클래스: -
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -

### 4.235. `workCategoryCode` — 공종분류 코드

- 설명: 재사용 공종분류 개체를 식별하고 상·하위 공종 체계에서 구분하는 표준 코드.
- IRI: `rcpp:workCategoryCode`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:WorkCategory`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:WorkCategory`

### 4.236. `workCategoryName` — 공종분류명

- 설명: 원문 공종문구와 구분되는 재사용 공종분류 개체의 표준 명칭.
- IRI: `rcpp:workCategoryName`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:WorkCategory`
- 치역: `rdfs:Literal`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:WorkCategory`

### 4.237. `workCondition` — 작업조건

- 설명: 난이도나 시공조건에 따른 구분.
- IRI: `rcpp:workCondition`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:ShoringCostItem`
- 치역: `xsd:string`
- 상위 속성: -
- 적용 서류: -
- 주요 관계:
  - `rdfs:domain` → `rcpp:ShoringCostItem`
- 포함 조건: 난이도나 시공조건에 따라 계약단가가 달라지는 경우

### 4.238. `workDetailAmount` — 내역항목별 금액

- 설명: 수량과 단가를 곱한 세부 내역항목의 계약금액.
- IRI: `rcpp:workDetailAmount`
- 구분: `계산`
- 정의역·적용 클래스: `rcpp:WorkTypeDetailItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasAmountValue`
- 적용 서류: `rcpp:WorkTypeDetailStatement`
- 주요 관계:
  - `rcpp:aggregatesTo` → `rcpp:summaryContractAmount`
  - `rcpp:fieldOfDocument` → `rcpp:WorkTypeDetailStatement`
  - `rdfs:domain` → `rcpp:WorkTypeDetailItem`
- 산식: 내역항목별 금액 = 수량 × 단가

### 4.239. `workDetailDirectCost` — 직접공사비

- 설명: 공종별내역서에 기록된 원천 직접공사비이며 공종별집계표의 직접공사비 합계로 집계되는 값.
- IRI: `rcpp:workDetailDirectCost`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:WorkTypeDetailItem`
- 치역: `xsd:decimal`
- 상위 속성: -
- 적용 서류: `rcpp:WorkTypeDetailStatement`
- 주요 관계:
  - `rcpp:aggregatesTo` → `rcpp:summaryDirectCost`
  - `rcpp:fieldOfDocument` → `rcpp:WorkTypeDetailStatement`
  - `rdfs:domain` → `rcpp:WorkTypeDetailItem`

### 4.240. `workDetailItemCode` — 내역코드

- 설명: 계약항목과 공종별 세부항목을 연결하는 코드.
- IRI: `rcpp:workDetailItemCode`
- 구분: `식별`
- 정의역·적용 클래스: `rcpp:WorkTypeDetailItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasItemCode`
- 적용 서류: `rcpp:WorkTypeDetailStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:WorkTypeDetailStatement`
  - `rcpp:matchesWithField` → `rcpp:contractItemCode`
  - `rdfs:domain` → `rcpp:WorkTypeDetailItem`

### 4.241. `workDetailItemName` — 품명

- 설명: 공종별 세부 내역항목의 명칭.
- IRI: `rcpp:workDetailItemName`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:WorkTypeDetailItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasItemName`
- 적용 서류: `rcpp:WorkTypeDetailStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:WorkTypeDetailStatement`
  - `rcpp:matchesWithField` → `rcpp:contractItemName`
  - `rdfs:domain` → `rcpp:WorkTypeDetailItem`

### 4.242. `workDetailQuantity` — 수량

- 설명: 계약수량을 공종별 세부내역에 배분한 수량.
- IRI: `rcpp:workDetailQuantity`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:WorkTypeDetailItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasQuantityValue`
- 적용 서류: `rcpp:WorkTypeDetailStatement`
- 주요 관계:
  - `rcpp:calculationInputFor` → `rcpp:workDetailAmount`
  - `rcpp:fieldOfDocument` → `rcpp:WorkTypeDetailStatement`
  - `rdfs:domain` → `rcpp:WorkTypeDetailItem`

### 4.243. `workDetailSpecification` — 규격

- 설명: 공종별 세부 내역항목의 규격.
- IRI: `rcpp:workDetailSpecification`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:WorkTypeDetailItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasSpecificationText`
- 적용 서류: `rcpp:WorkTypeDetailStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:WorkTypeDetailStatement`
  - `rcpp:matchesWithField` → `rcpp:contractSpecification`
  - `rdfs:domain` → `rcpp:WorkTypeDetailItem`

### 4.244. `workDetailUnit` — 단위

- 설명: 공종별 수량과 단가에 적용하는 단위.
- IRI: `rcpp:workDetailUnit`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:WorkTypeDetailItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasSourceUnitText`
- 적용 서류: `rcpp:WorkTypeDetailStatement`
- 주요 관계:
  - `rcpp:consistencyComparedWith` → `rcpp:contractUnit`
  - `rcpp:fieldOfDocument` → `rcpp:WorkTypeDetailStatement`
  - `rcpp:matchesWithField` → `rcpp:contractUnit`
  - `rdfs:domain` → `rcpp:WorkTypeDetailItem`

### 4.245. `workDetailUnitPrice` — 단가

- 설명: 계약내역서에서 전달된 세부 내역항목의 단가.
- IRI: `rcpp:workDetailUnitPrice`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:WorkTypeDetailItem`
- 치역: `xsd:decimal`
- 상위 속성: `rcpp:hasUnitPriceValue`
- 적용 서류: `rcpp:WorkTypeDetailStatement`
- 주요 관계:
  - `rcpp:calculationInputFor` → `rcpp:workDetailAmount`
  - `rcpp:fieldOfDocument` → `rcpp:WorkTypeDetailStatement`
  - `rdfs:domain` → `rcpp:WorkTypeDetailItem`

### 4.246. `workDetailWorkType` — 세부 공종

- 설명: 세부 내역을 철근·콘크리트·거푸집·동바리 공종으로 분류하는 항목.
- IRI: `rcpp:workDetailWorkType`
- 구분: `입력`
- 정의역·적용 클래스: `rcpp:WorkTypeDetailItem`
- 치역: `xsd:string`
- 상위 속성: `rcpp:hasSourceWorkCategoryText`
- 적용 서류: `rcpp:WorkTypeDetailStatement`
- 주요 관계:
  - `rcpp:fieldOfDocument` → `rcpp:WorkTypeDetailStatement`
  - `rcpp:groupsByField` → `rcpp:summaryWorkType`
  - `rcpp:matchesWithField` → `rcpp:contractWorkType`
  - `rdfs:domain` → `rcpp:WorkTypeDetailItem`

## 5. 규칙·통제값·기타 명명 자원

### 5.1. `ApprovedCorrespondenceRule` — 승인 매칭관계 원칙

- 설명: DocumentItemMatching은 후보·근거·신뢰도·검토상태를 기록하고, correspondsToItem은 검토상태가 승인된 최종 서류내역 대응관계에만 사용함.
- IRI: `rcpp:ApprovedCorrespondenceRule`
- 유형: `rdfs:Resource`

### 5.2. `AutomationGoal` — 기성서류 작성 자동화 목표

- 설명: 서류를 반복 탐색하는 비표준 업무를 서류내역 매핑 순서로 정리하여 재작업과 오류를 줄이고, 최종적으로 확장 가능한 기성서류 작성 자동화를 구현함.
- IRI: `rcpp:AutomationGoal`
- 유형: `rdfs:Resource`

### 5.3. `BaseUnitConversionRule` — 기준단위 경유 변환규칙

- 설명: 단위변환 규칙 유형을 실제 계산에 적용하기 위해 정의한 규칙 개체 `기준단위 경유 변환규칙`임.
- IRI: `rcpp:BaseUnitConversionRule`
- 유형: `rcpp:UnitConversionRule`
- 정의값:
  - `rcpp:applicationCondition` = 원천단위와 계약단위의 baseUnit이 동일할 때 적용함.
  - `rcpp:unitCondition` = 원천단위와 계약단위가 동일한 물리 차원이어야 함.

### 5.4. `CalculationActivityRequiredFields` — 계산 실행 필수값

- 설명: 계산 실행에 적용되는 필수 요구조건으로, 계산 기성회차, 계산규칙 적용, 계산정책 적용, 계산 입력항목, 계산 출력항목, 계산상태을(를) 요구함.
- IRI: `rcpp:CalculationActivityRequiredFields`
- 유형: `rcpp:FieldRequirement`
- 주요 관계:
  - `rcpp:requiredForClass` → `rcpp:CalculationActivity`
  - `rcpp:requiredProperty` → `rcpp:appliesPolicy`
  - `rcpp:requiredProperty` → `rcpp:appliesRule`
  - `rcpp:requiredProperty` → `rcpp:calculationInputItem`
  - `rcpp:requiredProperty` → `rcpp:calculationOutputItem`
  - `rcpp:requiredProperty` → `rcpp:calculationRound`
  - `rcpp:requiredProperty` → `rcpp:calculationStatus`
- 정의값:
  - `rcpp:requirementLevel` = 필수
  - `rcpp:requirementPurpose` = 계산입력

### 5.5. `CalculationDependencyRule` — 계산 영향 원칙

- 설명: 계산값마다 어떤 원천서류의 어떤 항목이 산식 입력으로 영향을 주는지 calculationInputFor 관계로 명시함.
- IRI: `rcpp:CalculationDependencyRule`
- 유형: `rdfs:Resource`

### 5.6. `ClassInstanceSeparationRule` — 클래스와 개체 구분 원칙

- 설명: expectedCostItemClass·expectedCorrespondingItemClass 같은 속성은 클래스 설계 관계에만 사용함. representsCostItem·correspondsToItem·usesUnitPriceFrom·derivedFrom·aggregatedInto는 실제 프로젝트 개체 사이에만 사용함. CalculationActivity의 appliesRule은 계산규칙 유형 클래스가 아니라 해당 유형의 실제 규칙 개체를 참조함. 공종별 규격값은 별도 규격 노드를 만들지 않고 해당 CostItem 개체의 속성으로 기록함.
- IRI: `rcpp:ClassInstanceSeparationRule`
- 유형: `rdfs:Resource`

### 5.7. `ClassesModule` — 서류·항목·처리규칙 클래스 모듈

- 설명: 서류 역할, 상세 내역과 집계 내역, 프로젝트 독립 표준 비용항목, 공종분류·측정단위·공종별 속성·매칭·금회기성액 계산·결과서류 내부 집계 규칙을 정의함.
- IRI: `rcpp:ClassesModule`
- 유형: `rdfs:Resource`

### 5.8. `CodeListsModule` — 흐름·역할·범위 지침 모듈

- 설명: 서류별 역할, 항목 매칭 원칙, 포함·제외 범위, 클래스·개체 구분 및 RDFS 추론·향후 SHACL 검증 분리 원칙과 재사용 공종·단위 개체를 정의함.
- IRI: `rcpp:CodeListsModule`
- 유형: `rdfs:Resource`

### 5.9. `ComplexComplexity` — 복잡

- 설명: 복잡도 코드목록에서 계약단가 식별과 규격 정규화에 사용하는 통제값 `복잡`임.
- IRI: `rcpp:ComplexComplexity`
- 유형: `rcpp:ComplexityLevel`
- 정의값:
  - `rcpp:codeValue` = COMPLEX
  - `rcpp:sourceValueAlias` = Complex
  - `rcpp:sourceValueAlias` = 복잡
  - `rcpp:sourceValueAlias` = 복잡형

### 5.10. `ConcretePlacementSpecificationRule` — 콘크리트 타설 규격 정규화규칙

- 설명: 콘크리트 타설 규격 정규화규칙 개체다. 비용항목의 규격 식별요소를 정규화하며 구성순서는 타설방법 → 적용부위 → 물량구간 → 계약단가 구분 시 작업조건임.
- IRI: `rcpp:ConcretePlacementSpecificationRule`
- 유형: `rcpp:SpecificationNormalizationRule`
- 주요 관계:
  - `rcpp:appliesToClass` → `rcpp:ConcretePlacementCostItem`
- 정의값:
  - `rcpp:componentDelimiter` = -
  - `rcpp:componentOrder` = 타설방법 → 적용부위 → 물량구간 → 계약단가 구분 시 작업조건
  - `rcpp:missingValueTreatment` = 계약단가를 구분하지 않는 요소는 생략함.
  - `rcpp:ruleVersion` = 1.0

### 5.11. `ConcreteWorkCategory` — 콘크리트공사

- 설명: 서류항목과 표준 비용항목을 콘크리트으로 분류하기 위한 공종분류 개체이며 공종코드는 RC-CONCRETE임.
- IRI: `rcpp:ConcreteWorkCategory`
- 유형: `rcpp:WorkCategory`
- 주요 관계:
  - `rcpp:parentWorkCategory` → `rcpp:ReinforcedConcreteWorkCategory`
- 정의값:
  - `rcpp:sourceValueAlias` = 콘크리트
  - `rcpp:sourceValueAlias` = 콘크리트공
  - `rcpp:sourceValueAlias` = 콘크리트공사
  - `rcpp:workCategoryCode` = RC-CONCRETE
  - `rcpp:workCategoryName` = 콘크리트

### 5.12. `ContractBasisDocumentRole` — 계약기준 역할

- 설명: 품목코드·계약수량·계약단가·계약금액을 제공하는 역할.
- IRI: `rcpp:ContractBasisDocumentRole`
- 유형: `rcpp:DocumentRole`

### 5.13. `ContractStatementItemCodeCondition` — 계약 내역 코드 조건

- 설명: 계약내역 항목에 적용되는 조건부 요구조건으로, 계약 품목코드을(를) 요구함.
- IRI: `rcpp:ContractStatementItemCodeCondition`
- 유형: `rcpp:FieldRequirement`
- 주요 관계:
  - `rcpp:requiredForClass` → `rcpp:ContractStatementItem`
  - `rcpp:requiredProperty` → `rcpp:contractItemCode`
- 정의값:
  - `rcpp:inclusionCondition` = 원천 품목코드가 있으면 보존하고, 없으면 프로젝트 범위에서 안정적인 행 식별자를 생성함.
  - `rcpp:requirementLevel` = 조건부

### 5.14. `ContractStatementItemRequiredFields` — 계약내역 항목 필수값

- 설명: 계약내역 항목에 적용되는 필수 요구조건으로, 공종, 공사내역·세부품목, 규격, 단위, 측정단위 사용, 계약수량, 계약단가, 계약금액을(를) 요구함.
- IRI: `rcpp:ContractStatementItemRequiredFields`
- 유형: `rcpp:FieldRequirement`
- 주요 관계:
  - `rcpp:requiredForClass` → `rcpp:ContractStatementItem`
  - `rcpp:requiredProperty` → `rcpp:contractAmount`
  - `rcpp:requiredProperty` → `rcpp:contractItemName`
  - `rcpp:requiredProperty` → `rcpp:contractQuantity`
  - `rcpp:requiredProperty` → `rcpp:contractSpecification`
  - `rcpp:requiredProperty` → `rcpp:contractUnit`
  - `rcpp:requiredProperty` → `rcpp:contractUnitPrice`
  - `rcpp:requiredProperty` → `rcpp:contractWorkType`
  - `rcpp:requiredProperty` → `rcpp:usesUnit`
- 정의값:
  - `rcpp:requirementLevel` = 필수

### 5.15. `CostItemRequiredFields` — 표준 비용항목 필수값

- 설명: 표준 비용항목에 적용되는 필수 요구조건으로, 정규화 내역코드, 정규화 품명, 정규화규격코드, 공종분류 소속, 측정단위 사용을(를) 요구함.
- IRI: `rcpp:CostItemRequiredFields`
- 유형: `rcpp:FieldRequirement`
- 주요 관계:
  - `rcpp:requiredForClass` → `rcpp:CostItem`
  - `rcpp:requiredProperty` → `rcpp:belongsToWorkCategory`
  - `rcpp:requiredProperty` → `rcpp:costItemCode`
  - `rcpp:requiredProperty` → `rcpp:costItemName`
  - `rcpp:requiredProperty` → `rcpp:normalizedSpecificationCode`
  - `rcpp:requiredProperty` → `rcpp:usesUnit`
- 정의값:
  - `rcpp:requirementLevel` = 필수

### 5.16. `CostSummaryDocumentRole` — 계약비용집계 역할

- 설명: 계약내역 계열의 세부금액과 직접공사비를 공종별로 집계하는 역할. 금회·누계 기성금액 집계는 결과서류 내부 집계항목의 역할임.
- IRI: `rcpp:CostSummaryDocumentRole`
- 유형: `rcpp:DocumentRole`

### 5.17. `CubicMetreUnit` — 세제곱미터

- 설명: 체적 차원의 표준 측정단위다. 단위코드는 M3, 기호는 ㎥, 기준단위는 세제곱미터, 기준단위 변환계수는 1.0임.
- IRI: `rcpp:CubicMetreUnit`
- 유형: `rcpp:Unit`
- 주요 관계:
  - `rcpp:baseUnit` → `rcpp:CubicMetreUnit`
- 정의값:
  - `rcpp:conversionFactorToBaseUnit` = 1.0
  - `rcpp:sourceValueAlias` = M3
  - `rcpp:sourceValueAlias` = m3
  - `rcpp:sourceValueAlias` = m³
  - `rcpp:sourceValueAlias` = ㎥
  - `rcpp:unitCode` = M3
  - `rcpp:unitDimension` = 체적
  - `rcpp:unitSymbol` = ㎥

### 5.18. `CurrentProgressDetailItemCalculatedFields` — 공사기성 상세항목 계산결과값

- 설명: 공사기성 상세항목에 적용되는 필수 요구조건으로, 금회기성금액, 누계기성수량, 누계기성금액, 잔여수량, 잔여금액을(를) 요구함.
- IRI: `rcpp:CurrentProgressDetailItemCalculatedFields`
- 유형: `rcpp:FieldRequirement`
- 주요 관계:
  - `rcpp:requiredForClass` → `rcpp:CurrentProgressDetailItem`
  - `rcpp:requiredProperty` → `rcpp:outputCumulativeAmount`
  - `rcpp:requiredProperty` → `rcpp:outputCumulativeQuantity`
  - `rcpp:requiredProperty` → `rcpp:outputCurrentAmount`
  - `rcpp:requiredProperty` → `rcpp:outputRemainingAmount`
  - `rcpp:requiredProperty` → `rcpp:outputRemainingQuantity`
- 정의값:
  - `rcpp:requirementLevel` = 필수
  - `rcpp:requirementPurpose` = 계산결과

### 5.19. `CurrentProgressDetailItemConditionalFields` — 공사기성 상세항목 조건부값

- 설명: 공사기성 상세항목에 적용되는 조건부 요구조건으로, 출력 품목코드, 전회누계기성비율(%), 금회기성비율(%), 누계기성비율(%)을(를) 요구함.
- IRI: `rcpp:CurrentProgressDetailItemConditionalFields`
- 유형: `rcpp:FieldRequirement`
- 주요 관계:
  - `rcpp:requiredForClass` → `rcpp:CurrentProgressDetailItem`
  - `rcpp:requiredProperty` → `rcpp:outputCumulativeRate`
  - `rcpp:requiredProperty` → `rcpp:outputCurrentRate`
  - `rcpp:requiredProperty` → `rcpp:outputItemCode`
  - `rcpp:requiredProperty` → `rcpp:outputPreviousRate`
- 정의값:
  - `rcpp:inclusionCondition` = 품목코드는 원천 코드가 없으면 생성 식별자로 대체하며, 비율은 결과 양식에서 요구할 때 산출함.
  - `rcpp:requirementLevel` = 조건부

### 5.20. `CurrentProgressDetailItemTransferredFields` — 공사기성 상세항목 전달·출력값

- 설명: 공사기성 상세항목에 적용되는 필수 요구조건으로, 공종, 공사내역, 규격, 단위, 측정단위 사용, 계약수량, 계약단가, 계약금액, 전회까지의 기성수량, 전회누계기성금액, 금회기성수량을(를) 요구함.
- IRI: `rcpp:CurrentProgressDetailItemTransferredFields`
- 유형: `rcpp:FieldRequirement`
- 주요 관계:
  - `rcpp:requiredForClass` → `rcpp:CurrentProgressDetailItem`
  - `rcpp:requiredProperty` → `rcpp:outputContractAmount`
  - `rcpp:requiredProperty` → `rcpp:outputContractQuantity`
  - `rcpp:requiredProperty` → `rcpp:outputContractUnitPrice`
  - `rcpp:requiredProperty` → `rcpp:outputCurrentQuantity`
  - `rcpp:requiredProperty` → `rcpp:outputPreviousAmount`
  - `rcpp:requiredProperty` → `rcpp:outputPreviousQuantity`
  - `rcpp:requiredProperty` → `rcpp:outputSpecification`
  - `rcpp:requiredProperty` → `rcpp:outputUnit`
  - `rcpp:requiredProperty` → `rcpp:outputWorkDescription`
  - `rcpp:requiredProperty` → `rcpp:outputWorkType`
  - `rcpp:requiredProperty` → `rcpp:usesUnit`
- 정의값:
  - `rcpp:requirementLevel` = 필수
  - `rcpp:requirementPurpose` = 결과서류출력

### 5.21. `CurrentProgressQuantityItemCalculatedFields` — 기성수량 항목 계산결과값

- 설명: 기성수량 항목에 적용되는 필수 요구조건으로, 누계기성수량, 잔여수량을(를) 요구함.
- IRI: `rcpp:CurrentProgressQuantityItemCalculatedFields`
- 유형: `rcpp:FieldRequirement`
- 주요 관계:
  - `rcpp:requiredForClass` → `rcpp:CurrentProgressQuantityItem`
  - `rcpp:requiredProperty` → `rcpp:progressCumulativeQuantity`
  - `rcpp:requiredProperty` → `rcpp:progressRemainingQuantity`
- 정의값:
  - `rcpp:requirementLevel` = 필수
  - `rcpp:requirementPurpose` = 계산결과

### 5.22. `CurrentProgressQuantityItemCarryForwardFields` — 기성수량 항목 이월입력값

- 설명: 기성수량 항목에 적용되는 필수 요구조건으로, 전회누계기성수량을(를) 요구함.
- IRI: `rcpp:CurrentProgressQuantityItemCarryForwardFields`
- 유형: `rcpp:FieldRequirement`
- 주요 관계:
  - `rcpp:requiredForClass` → `rcpp:CurrentProgressQuantityItem`
  - `rcpp:requiredProperty` → `rcpp:progressPreviousCumulativeQuantity`
- 정의값:
  - `rcpp:requirementLevel` = 필수
  - `rcpp:requirementPurpose` = 이월입력

### 5.23. `CurrentProgressQuantityItemCodeCondition` — 기성수량 내역 코드 조건

- 설명: 기성수량 항목에 적용되는 조건부 요구조건으로, 내역코드을(를) 요구함.
- IRI: `rcpp:CurrentProgressQuantityItemCodeCondition`
- 유형: `rcpp:FieldRequirement`
- 주요 관계:
  - `rcpp:requiredForClass` → `rcpp:CurrentProgressQuantityItem`
  - `rcpp:requiredProperty` → `rcpp:progressQuantityItemCode`
- 정의값:
  - `rcpp:inclusionCondition` = 원천 코드가 있으면 보존하고, 없으면 대응 계약항목의 식별자를 사용함.
  - `rcpp:requirementLevel` = 조건부

### 5.24. `CurrentProgressQuantityItemSourceFields` — 기성수량 항목 원천입력값

- 설명: 기성수량 항목에 적용되는 필수 요구조건으로, 공종, 품명, 규격, 단위, 측정단위 사용, 금회기성수량을(를) 요구함.
- IRI: `rcpp:CurrentProgressQuantityItemSourceFields`
- 유형: `rcpp:FieldRequirement`
- 주요 관계:
  - `rcpp:requiredForClass` → `rcpp:CurrentProgressQuantityItem`
  - `rcpp:requiredProperty` → `rcpp:progressCurrentQuantity`
  - `rcpp:requiredProperty` → `rcpp:progressQuantityItemName`
  - `rcpp:requiredProperty` → `rcpp:progressQuantitySpecification`
  - `rcpp:requiredProperty` → `rcpp:progressQuantityUnit`
  - `rcpp:requiredProperty` → `rcpp:progressQuantityWorkType`
  - `rcpp:requiredProperty` → `rcpp:usesUnit`
- 정의값:
  - `rcpp:requirementLevel` = 필수
  - `rcpp:requirementPurpose` = 원천입력

### 5.25. `CurrentProgressSummaryItemRequiredFields` — 공사기성 집계항목 필수값

- 설명: 공사기성 집계항목에 적용되는 필수 요구조건으로, 집계행 원문 공종문구, 공종별 계약금액, 공종별 전회누계기성금액, 공종별 금회기성금액, 공종별 누계기성금액을(를) 요구함.
- IRI: `rcpp:CurrentProgressSummaryItemRequiredFields`
- 유형: `rcpp:FieldRequirement`
- 주요 관계:
  - `rcpp:requiredForClass` → `rcpp:CurrentProgressSummaryItem`
  - `rcpp:requiredProperty` → `rcpp:outputSummaryContractAmount`
  - `rcpp:requiredProperty` → `rcpp:outputSummaryCumulativeAmount`
  - `rcpp:requiredProperty` → `rcpp:outputSummaryCurrentAmount`
  - `rcpp:requiredProperty` → `rcpp:outputSummaryPreviousAmount`
  - `rcpp:requiredProperty` → `rcpp:outputSummaryWorkCategoryText`
- 정의값:
  - `rcpp:requirementLevel` = 필수

### 5.26. `DetailedCostDocumentRole` — 세부비용 역할

- 설명: 공종별 품목·규격·수량·단가·금액의 상세행을 구성하는 역할.
- IRI: `rcpp:DetailedCostDocumentRole`
- 유형: `rcpp:DocumentRole`

### 5.27. `DirectTransferRule` — 직접 전달 원칙

- 설명: 최종 결과의 코드·공종·품명·규격·단위·계약수량·계약단가·계약금액은 계약내역서에서, 전회누계수량·금액과 원천에 존재하는 전회비율은 전회 공사기성부분내역서에서, 금회·누계·잔여수량은 기성수량산출서에서 전달함. 계약금액과 누계·잔여수량의 재계산식은 전달값을 대체하지 않는 교차검토식임. 수량산출서의 산식·근거는 quantityBasisFrom으로 연결하고 산출수량만 계약수량과 일관성 비교함.
- IRI: `rcpp:DirectTransferRule`
- 유형: `rdfs:Resource`

### 5.28. `DocumentFlowDefinition` — 서류 흐름 정의

- 설명: 두 입력 흐름, 즉 ‘수량근거 → 계약기준 → 세부비용 → 계약비용집계’와 ‘전회기성기준 + 확정 금회기성수량 → 기성금액 계산’이 공사기성부분내역서에서 합류하는 대표 흐름을 사용함. 프로젝트별 실제 파일 순서는 고정하지 않음.
- IRI: `rcpp:DocumentFlowDefinition`
- 유형: `rdfs:Resource`

### 5.29. `DocumentItemMatchingConditionalFields` — 서류항목 매칭 조건부값

- 설명: 서류내역 매칭에 적용되는 조건부 요구조건으로, 매칭 신뢰도, 매칭 검토자을(를) 요구함.
- IRI: `rcpp:DocumentItemMatchingConditionalFields`
- 유형: `rcpp:FieldRequirement`
- 주요 관계:
  - `rcpp:requiredForClass` → `rcpp:DocumentItemMatching`
  - `rcpp:requiredProperty` → `rcpp:confidenceScore`
  - `rcpp:requiredProperty` → `rcpp:reviewedBy`
- 정의값:
  - `rcpp:requirementLevel` = 조건부
  - `rcpp:requirementPurpose` = 교차검토

### 5.30. `DocumentItemMatchingRequiredFields` — 서류항목 매칭 필수값

- 설명: 서류내역 매칭에 적용되는 필수 요구조건으로, 매칭 원천항목, 매칭 대상항목, 매칭 표준 비용항목, 매칭 방법, 매칭 근거, 매칭 검토상태을(를) 요구함.
- IRI: `rcpp:DocumentItemMatchingRequiredFields`
- 유형: `rcpp:FieldRequirement`
- 주요 관계:
  - `rcpp:requiredForClass` → `rcpp:DocumentItemMatching`
  - `rcpp:requiredProperty` → `rcpp:matchedCostItem`
  - `rcpp:requiredProperty` → `rcpp:matchingEvidence`
  - `rcpp:requiredProperty` → `rcpp:matchingMethod`
  - `rcpp:requiredProperty` → `rcpp:reviewStatus`
  - `rcpp:requiredProperty` → `rcpp:sourceItem`
  - `rcpp:requiredProperty` → `rcpp:targetItem`
- 정의값:
  - `rcpp:requirementLevel` = 필수
  - `rcpp:requirementPurpose` = 교차검토

### 5.31. `EachUnit` — 개수

- 설명: 개수 차원의 표준 측정단위다. 단위코드는 EA, 기호는 개, 기준단위는 개수, 기준단위 변환계수는 1.0임.
- IRI: `rcpp:EachUnit`
- 유형: `rcpp:Unit`
- 주요 관계:
  - `rcpp:baseUnit` → `rcpp:EachUnit`
- 정의값:
  - `rcpp:conversionFactorToBaseUnit` = 1.0
  - `rcpp:sourceValueAlias` = EA
  - `rcpp:sourceValueAlias` = ea
  - `rcpp:sourceValueAlias` = 개
  - `rcpp:unitCode` = EA
  - `rcpp:unitDimension` = 개수
  - `rcpp:unitSymbol` = 개

### 5.32. `EuroFormwork` — 유로폼

- 설명: 거푸집 유형 코드목록에서 계약단가 식별과 규격 정규화에 사용하는 통제값 `유로폼`임.
- IRI: `rcpp:EuroFormwork`
- 유형: `rcpp:FormworkType`
- 정의값:
  - `rcpp:codeValue` = EURO_FORM
  - `rcpp:sourceValueAlias` = 유로 거푸집
  - `rcpp:sourceValueAlias` = 유로폼

### 5.33. `ExcludedWorkScope` — 제외 서류와 판단

- 설명: 검측요청서·검측결과서, 작업일보·시공일보, 콘크리트 타설일보, 철근가공조서·배근 검측자료, 물량측정서, 시공사진, 자재납품서를 제외함. 실제 시공 여부·검측 적합성·품질 적합성을 판정하지 않음.
- IRI: `rcpp:ExcludedWorkScope`
- 유형: `rdfs:Resource`

### 5.34. `FirstProgressRoundRule` — 최초 기성회차 원칙

- 설명: 최초 기성회차는 previousProgressRound와 전회 공사기성부분내역서를 갖지 않으며 전회누계기성수량과 전회누계기성금액을 0으로 적용함. 이후 회차는 isFirstProgressRound를 false로 두고 직전 회차 확정값을 이월함.
- IRI: `rcpp:FirstProgressRoundRule`
- 유형: `rdfs:Resource`

### 5.35. `FormworkSpecificationRule` — 거푸집 규격 정규화규칙

- 설명: 거푸집 규격 정규화규칙 개체다. 비용항목의 규격 식별요소를 정규화하며 구성순서는 거푸집종류 → 복잡도 → 전용횟수 → 수직고구간 → 작업유형임.
- IRI: `rcpp:FormworkSpecificationRule`
- 유형: `rcpp:SpecificationNormalizationRule`
- 주요 관계:
  - `rcpp:appliesToClass` → `rcpp:FormworkCostItem`
- 정의값:
  - `rcpp:componentDelimiter` = -
  - `rcpp:componentOrder` = 거푸집종류 → 복잡도 → 전용횟수 → 수직고구간 → 작업유형
  - `rcpp:missingValueTreatment` = 계약단가를 구분하지 않는 선택 요소는 생략함.
  - `rcpp:ruleVersion` = 1.0

### 5.36. `FormworkWorkCategory` — 거푸집공사

- 설명: 서류항목과 표준 비용항목을 거푸집으로 분류하기 위한 공종분류 개체이며 공종코드는 RC-FORMWORK임.
- IRI: `rcpp:FormworkWorkCategory`
- 유형: `rcpp:WorkCategory`
- 주요 관계:
  - `rcpp:parentWorkCategory` → `rcpp:ReinforcedConcreteWorkCategory`
- 정의값:
  - `rcpp:sourceValueAlias` = 거푸집
  - `rcpp:sourceValueAlias` = 거푸집공
  - `rcpp:sourceValueAlias` = 거푸집공사
  - `rcpp:workCategoryCode` = RC-FORMWORK
  - `rcpp:workCategoryName` = 거푸집

### 5.37. `FutureShaclValidationRule` — 향후 SHACL 검증 분리 원칙

- 설명: 필수값·데이터형·허용값·최솟값·최댓값·서류 간 수량 및 금액 일관성 검증은 온톨로지 의미모델과 분리한 SHACL shapes 계층으로 확장함.
- IRI: `rcpp:FutureShaclValidationRule`
- 유형: `rdfs:Resource`

### 5.38. `IncludedDocumentTypes` — 사용 기성서류

- 설명: 산정 근거서류는 수량산출서·계약내역서·공종별내역서·공종별집계표·기성수량산출서·전회 공사기성부분내역서와 단가·원가 지원서류이고, 산정 결과서류는 공사기성부분내역서임.
- IRI: `rcpp:IncludedDocumentTypes`
- 유형: `rdfs:Resource`

### 5.39. `IncludedWorkScope` — 현재 포함 공종

- 설명: 현재 온톨로지 구축 범위는 철근콘크리트공종 하나이며 세부공종은 철근·콘크리트·거푸집·동바리 네 가지로 한정함. 다른 공종은 현재 클래스·속성 범위에 포함하지 않음.
- IRI: `rcpp:IncludedWorkScope`
- 유형: `rdfs:Resource`

### 5.40. `InterDocumentFieldTransferDefinition` — 서류 간 항목 전달관계 정의

- 설명: 개별 rdf:Property 사이의 그대로 전달·매칭 기준·산식 입력·집계 전달·일관성 비교 관계로 출발 서류내역과 도착 서류내역을 명시함.
- IRI: `rcpp:InterDocumentFieldTransferDefinition`
- 유형: `rdfs:Resource`

### 5.41. `ItemFlowDefinition` — 항목 흐름 정의

- 설명: 공종·품명·규격·단위·내역코드로 동일 항목을 식별하고 계약수량·단가·금액, 기성수량·금액, 공종별 집계의 계산 순서를 정의함.
- IRI: `rcpp:ItemFlowDefinition`
- 유형: `rdfs:Resource`

### 5.42. `ItemIdentityRule` — 동일 품목 판별 원칙

- 설명: 내역코드와 공종을 보조키로 사용하고 품명·정규화된 비용 관련 규격요소·단위를 복합 비교함. 품명 하나나 원문규격 문자열 하나만으로 서류 행과 계약단가를 연결하지 않음.
- IRI: `rcpp:ItemIdentityRule`
- 유형: `rdfs:Resource`

### 5.43. `KRW` — 대한민국 원

- 설명: 금액 계산정책에서 사용하는 대한민국 원 통화 개체이며 통화코드는 KRW임.
- IRI: `rcpp:KRW`
- 유형: `rcpp:Currency`
- 정의값:
  - `rcpp:codeValue` = KRW

### 5.44. `KRWItemWonHalfUpPolicy` — KRW 항목별 원단위 반올림 정책

- 설명: 기성금액 계산에 적용하는 KRW 항목별 원단위 반올림 정책 개체로, 통화·반올림 방식·자릿수·허용오차와 계산순서를 정의함.
- IRI: `rcpp:KRWItemWonHalfUpPolicy`
- 유형: `rcpp:CalculationPolicy`
- 주요 관계:
  - `rcpp:currency` → `rcpp:KRW`
  - `rcpp:roundingMode` → `rcpp:RoundHalfUp`
- 정의값:
  - `rcpp:amountTolerance` = 0.0
  - `rcpp:calculationOrder` = 수량을 계약단위로 변환 → 품목별 금액 계산 → 원 단위 반올림 → 공종별 합계
  - `rcpp:decimalScale` = 0
  - `rcpp:quantityTolerance` = 0.0001

### 5.45. `KilogramUnit` — 킬로그램

- 설명: 질량 차원의 표준 측정단위다. 단위코드는 KG, 기호는 kg, 기준단위는 킬로그램, 기준단위 변환계수는 1.0임.
- IRI: `rcpp:KilogramUnit`
- 유형: `rcpp:Unit`
- 주요 관계:
  - `rcpp:baseUnit` → `rcpp:KilogramUnit`
- 정의값:
  - `rcpp:conversionFactorToBaseUnit` = 1.0
  - `rcpp:sourceValueAlias` = KG
  - `rcpp:sourceValueAlias` = kg
  - `rcpp:sourceValueAlias` = 킬로그램
  - `rcpp:unitCode` = KG
  - `rcpp:unitDimension` = 질량
  - `rcpp:unitSymbol` = kg

### 5.46. `LandInstallationEnvironment` — 육상

- 설명: 설치환경 코드목록에서 계약단가 식별과 규격 정규화에 사용하는 통제값 `육상`임.
- IRI: `rcpp:LandInstallationEnvironment`
- 유형: `rcpp:InstallationEnvironment`
- 정의값:
  - `rcpp:codeValue` = LAND
  - `rcpp:sourceValueAlias` = 육상

### 5.47. `ManualPlacement` — 인력 타설

- 설명: 타설방법 코드목록에서 계약단가 식별과 규격 정규화에 사용하는 통제값 `인력 타설`임.
- IRI: `rcpp:ManualPlacement`
- 유형: `rcpp:PlacementMethod`
- 정의값:
  - `rcpp:codeValue` = MANUAL
  - `rcpp:sourceValueAlias` = 수작업 타설
  - `rcpp:sourceValueAlias` = 인력 타설
  - `rcpp:sourceValueAlias` = 인력타설

### 5.48. `MetreUnit` — 미터

- 설명: 길이 차원의 표준 측정단위다. 단위코드는 M, 기호는 m, 기준단위는 미터, 기준단위 변환계수는 1.0임.
- IRI: `rcpp:MetreUnit`
- 유형: `rcpp:Unit`
- 주요 관계:
  - `rcpp:baseUnit` → `rcpp:MetreUnit`
- 정의값:
  - `rcpp:conversionFactorToBaseUnit` = 1.0
  - `rcpp:sourceValueAlias` = M
  - `rcpp:sourceValueAlias` = m
  - `rcpp:sourceValueAlias` = 미터
  - `rcpp:unitCode` = M
  - `rcpp:unitDimension` = 길이
  - `rcpp:unitSymbol` = m

### 5.49. `NormalComplexity` — 보통

- 설명: 복잡도 코드목록에서 계약단가 식별과 규격 정규화에 사용하는 통제값 `보통`임.
- IRI: `rcpp:NormalComplexity`
- 유형: `rcpp:ComplexityLevel`
- 정의값:
  - `rcpp:codeValue` = NORMAL
  - `rcpp:sourceValueAlias` = Normal
  - `rcpp:sourceValueAlias` = 보통
  - `rcpp:sourceValueAlias` = 일반

### 5.50. `NormalizedCostItemValueRule` — 정규화 비용항목 값 분리 원칙

- 설명: CostItem에는 정규화 코드·품명·공종·규격·단위만 두며 프로젝트별 계약수량·계약단가·계약금액·기성수량·기성금액은 ContractStatementItem·CurrentProgressQuantityItem·CurrentProgressDetailItem 개체에 기록함.
- IRI: `rcpp:NormalizedCostItemValueRule`
- 유형: `rdfs:Resource`

### 5.51. `NormalizedSpecificationMatchingRule` — 정규화 규격 매칭 원칙

- 설명: 공종별 규격요소를 정규화규격코드로 구성한 뒤 품명과 단위에 결합하여 계약항목과 기성항목의 동일 여부 및 적용 계약단가를 판단함.
- IRI: `rcpp:NormalizedSpecificationMatchingRule`
- 유형: `rdfs:Resource`

### 5.52. `ObservedUnitPriceDifferenceRule` — 실제 계약단가 차이 기준

- 설명: 단가 구분 시 포함 속성은 적용 프로젝트의 계약내역에서 해당 값에 따라 항목 또는 계약단가가 실제로 달라질 때만 분해함. 차이가 확인되지 않은 요소는 표준 비용항목에서 제외하되 원문은 해당 서류 내역의 규격 속성에 보존함.
- IRI: `rcpp:ObservedUnitPriceDifferenceRule`
- 유형: `rdfs:Resource`

### 5.53. `OntologySchema` — OntologySchema

- 설명: RCPP는 Reinforced Concrete Progress Payment의 약어임. 기성서류를 핵심 업무개념으로 유지하면서 Project와 ProgressPaymentRound를 실제 데이터의 적용 문맥으로 명시함. 연구 범위는 철근콘크리트공종의 철근·콘크리트·거푸집·동바리 수량 및 기성금액 산정이며 실제 시공·검측·품질 판정은 제외함.
- IRI: `rcpp:OntologySchema`
- 유형: `rdfs:Resource`
- 주요 관계:
  - `rdfs:seeAlso` → `rcpp:ClassesModule`
  - `rdfs:seeAlso` → `rcpp:CodeListsModule`
  - `rdfs:seeAlso` → `rcpp:ProgressPaymentDataFlow`
  - `rdfs:seeAlso` → `rcpp:PropertiesModule`
  - `rdfs:seeAlso` → `rcpp:PrototypeNamespaceNotice`
- 정의값:
  - `dcterms:created` = 2026-07-16
  - `dcterms:description` = 프로젝트와 기성회차별 서류 역할·서류 내역을 표준 비용항목에 연결하고 철근·콘크리트·거푸집·동바리 비용항목에 직접 부여하는 단가 식별 속성, 서류에 기록된 수량산식·산출근거·산출수량, 단위 변환, 계산정책, 계약단가, 확정 금회기성수량과 금회기성금액 계산을 정의하는 RDF/RDFS 온톨로지.
  - `dcterms:hasVersion` = 1.0.0
  - `dcterms:identifier` = RCPP
  - `dcterms:modified` = 2026-07-28
  - `dcterms:title` = Progress Document Field Mapping and Statement Preparation Ontology
  - `dcterms:title` = 기성서류 내역 매핑 및 공사기성부분내역서 작성 온톨로지
  - `rcpp:namespaceUri` = https://example.org/rcpp#

### 5.54. `OriginalSpecificationPreservationRule` — 규격 원문 보존 원칙

- 설명: 원문규격은 contractSpecification·quantitySpecification·workDetailSpecification·progressQuantitySpecification·outputSpecification처럼 출처 서류 내역의 속성에 보존함. 표준 비용항목에는 원문 문자열을 저장하지 않고 비용 관련 요소와 정규화규격코드만 기록함.
- IRI: `rcpp:OriginalSpecificationPreservationRule`
- 유형: `rdfs:Resource`

### 5.55. `PlywoodFormwork` — 합판거푸집

- 설명: 거푸집 유형 코드목록에서 계약단가 식별과 규격 정규화에 사용하는 통제값 `합판거푸집`임.
- IRI: `rcpp:PlywoodFormwork`
- 유형: `rcpp:FormworkType`
- 정의값:
  - `rcpp:codeValue` = PLYWOOD
  - `rcpp:sourceValueAlias` = 합판 거푸집
  - `rcpp:sourceValueAlias` = 합판거푸집

### 5.56. `PreviousAmountCarryForwardRule` — 전회누계금액 확정값 이월 원칙

- 설명: 전회누계기성금액은 전회 공사기성부분내역서의 확정값을 그대로 이월함. 전회누계수량 × 계약단가는 원천값을 대체하지 않고 계산정책의 허용오차 안에서 교차검토하는 데만 사용함.
- IRI: `rcpp:PreviousAmountCarryForwardRule`
- 유형: `rdfs:Resource`

### 5.57. `PreviousCarryForwardRule` — 전회값 이월 원칙

- 설명: 전회 공사기성부분내역서의 누계기성수량·금액·비율을 동일 계약 품목의 전회까지 기성값으로 연결함.
- IRI: `rcpp:PreviousCarryForwardRule`
- 유형: `rdfs:Resource`

### 5.58. `PreviousProgressBasisDocumentRole` — 전회기성기준 역할

- 설명: 전회누계기성수량·금액·비율을 제공하는 역할.
- IRI: `rcpp:PreviousProgressBasisDocumentRole`
- 유형: `rcpp:DocumentRole`

### 5.59. `PreviousProgressStatementItemConditionalFields` — 전회 기성항목 조건부값

- 설명: 전회 기성항목에 적용되는 조건부 요구조건으로, 전회 품목코드, 전회누계기성비율(%)을(를) 요구함.
- IRI: `rcpp:PreviousProgressStatementItemConditionalFields`
- 유형: `rcpp:FieldRequirement`
- 주요 관계:
  - `rcpp:requiredForClass` → `rcpp:PreviousProgressStatementItem`
  - `rcpp:requiredProperty` → `rcpp:previousCumulativeRate`
  - `rcpp:requiredProperty` → `rcpp:previousItemCode`
- 정의값:
  - `rcpp:inclusionCondition` = 품목코드는 원천 코드가 없으면 생성 식별자로 대체하며, 비율은 원천 서류에 있거나 출력 양식이 요구할 때 사용함.
  - `rcpp:requirementLevel` = 조건부

### 5.60. `PreviousProgressStatementItemRequiredFields` — 전회 기성항목 필수값

- 설명: 전회 기성항목에 적용되는 필수 요구조건으로, 전회 공사내역, 전회 규격, 전회 단위, 측정단위 사용, 전회누계기성수량, 전회누계기성금액을(를) 요구함.
- IRI: `rcpp:PreviousProgressStatementItemRequiredFields`
- 유형: `rcpp:FieldRequirement`
- 주요 관계:
  - `rcpp:requiredForClass` → `rcpp:PreviousProgressStatementItem`
  - `rcpp:requiredProperty` → `rcpp:previousCumulativeAmount`
  - `rcpp:requiredProperty` → `rcpp:previousCumulativeQuantity`
  - `rcpp:requiredProperty` → `rcpp:previousSpecification`
  - `rcpp:requiredProperty` → `rcpp:previousUnit`
  - `rcpp:requiredProperty` → `rcpp:previousWorkDescription`
  - `rcpp:requiredProperty` → `rcpp:usesUnit`
- 정의값:
  - `rcpp:requirementLevel` = 필수

### 5.61. `ProgressPaymentDataFlow` — 공사기성부분내역서 작성 데이터 흐름

- 설명: ① 수량산출서의 산출수량·산식·근거를 계약수량의 근거로 연결함. ② 계약내역을 공종별내역서와 계약비용 집계표로 구성함. ③ 전회 기성 확정값과 기성수량산출서의 확정 금회수량으로 누계·잔여수량을 계산함. ④ 계약기준정보·전회값·확정 금회수량으로 상세 기성금액을 계산하고 그 결과를 공종별로 집계하여 공사기성부분내역서를 작성함.
- IRI: `rcpp:ProgressPaymentDataFlow`
- 유형: `rdfs:Resource`

### 5.62. `ProgressQuantityDetailItemConditionalFields` — 기성수량 상세항목 위치정보 조건

- 설명: 기성수량 상세항목에 적용되는 조건부 요구조건으로, 상세 위치문구, 원천위치 연결을(를) 요구함.
- IRI: `rcpp:ProgressQuantityDetailItemConditionalFields`
- 유형: `rcpp:FieldRequirement`
- 주요 관계:
  - `rcpp:requiredForClass` → `rcpp:ProgressQuantityDetailItem`
  - `rcpp:requiredProperty` → `rcpp:detailLocationText`
  - `rcpp:requiredProperty` → `rcpp:hasSourceLocation`
- 정의값:
  - `rcpp:inclusionCondition` = 원천 서류에 위치·구조물·층·부재 구분이 있으면 원문 위치와 표준 위치 연결을 함께 보존함.
  - `rcpp:requirementLevel` = 조건부

### 5.63. `ProgressQuantityDetailItemRequiredFields` — 기성수량 상세항목 필수값

- 설명: 기성수량 상세항목에 적용되는 필수 요구조건으로, 상세 금회기성수량, 기성수량항목으로 합산, 표준 비용항목 연결, 측정단위 사용을(를) 요구함.
- IRI: `rcpp:ProgressQuantityDetailItemRequiredFields`
- 유형: `rcpp:FieldRequirement`
- 주요 관계:
  - `rcpp:requiredForClass` → `rcpp:ProgressQuantityDetailItem`
  - `rcpp:requiredProperty` → `rcpp:detailCurrentQuantity`
  - `rcpp:requiredProperty` → `rcpp:quantityAggregatedInto`
  - `rcpp:requiredProperty` → `rcpp:representsCostItem`
  - `rcpp:requiredProperty` → `rcpp:usesUnit`
- 정의값:
  - `rcpp:requirementLevel` = 필수
  - `rcpp:requirementPurpose` = 상세수량 집계입력

### 5.64. `ProgressQuantityDocumentRole` — 기성수량 역할

- 설명: 전회누계값과 비용산정용으로 확정 입력된 금회기성수량, 그리고 계산된 누계·잔여 기성수량을 제공하는 역할.
- IRI: `rcpp:ProgressQuantityDocumentRole`
- 유형: `rcpp:DocumentRole`

### 5.65. `ProgressStatementDocumentRole` — 기성결과 역할

- 설명: 계약기준과 기성수량을 결합하여 기성금액 결과를 기록하는 역할.
- IRI: `rcpp:ProgressStatementDocumentRole`
- 유형: `rcpp:DocumentRole`

### 5.66. `ProjectDocumentRoleFlexibilityRule` — 프로젝트별 서류역할 적용 원칙

- 설명: 실제 프로젝트 문서 개체는 파일명과 관계없이 hasDocumentRole로 하나 이상의 역할을 가질 수 있음. 계약내역서와 공종별내역서가 같은 파일이거나 별도 기성수량산출서가 없는 경우에도 역할 조합으로 표현함.
- IRI: `rcpp:ProjectDocumentRoleFlexibilityRule`
- 유형: `rdfs:Resource`

### 5.67. `PropertiesModule` — 서류 내역 및 영향 관계 모듈

- 설명: 각 서류의 원천 데이터 항목을 공통 코드·공종·품명·규격·단위·수량·단가·금액 상위속성에 정렬하고, 공종별 최소 규격속성과 서류 흐름·동일 항목 대응·단가 참조·파생·집계·산식입력 관계를 정의함.
- IRI: `rcpp:PropertiesModule`
- 유형: `rdfs:Resource`

### 5.68. `PrototypeNamespaceNotice` — 프로토타입 네임스페이스 고지

- 설명: https://example.org/rcpp#는 연구·프로토타입용 임시 네임스페이스임. 외부 공개·영구 식별·운영 배포 전에 소유 기관이 통제하는 영구 URI로 일괄 교체필요.
- IRI: `rcpp:PrototypeNamespaceNotice`
- 유형: `rdfs:Resource`

### 5.69. `PumpCarPlacement` — 펌프카 타설

- 설명: 타설방법 코드목록에서 계약단가 식별과 규격 정규화에 사용하는 통제값 `펌프카 타설`임.
- IRI: `rcpp:PumpCarPlacement`
- 유형: `rcpp:PlacementMethod`
- 정의값:
  - `rcpp:codeValue` = PUMP_CAR
  - `rcpp:sourceValueAlias` = 펌프카
  - `rcpp:sourceValueAlias` = 펌프카 타설
  - `rcpp:sourceValueAlias` = 펌프타설

### 5.70. `QuantityAndPriceSpecificationSeparationRule` — 수량입력·비용규격 분리 원칙

- 설명: 수량산출서에 기재된 산식·산출근거·산출수량은 서류 내역의 속성값으로 보존함. 도면의 개수·길이·부재치수·설치간격을 이용해 수량을 새로 계산하는 기능은 포함하지 않음. 강종·호칭강도·전용횟수·최대수직고처럼 단가를 식별하는 값은 비용규격에 둔다.
- IRI: `rcpp:QuantityAndPriceSpecificationSeparationRule`
- 유형: `rdfs:Resource`

### 5.71. `QuantityBasisDocumentRole` — 계약수량 근거 역할

- 설명: 품명·규격·단위 식별정보와 계약수량의 산출근거를 제공함. 금회기성수량의 직접 출처 역할은 아니다.
- IRI: `rcpp:QuantityBasisDocumentRole`
- 유형: `rcpp:DocumentRole`

### 5.72. `QuantityCalculationItemCodeCondition` — 수량산출서 식별코드 조건

- 설명: 수량산출 항목에 적용되는 조건부 요구조건으로, 수량산출 항목코드, 내역코드을(를) 요구함.
- IRI: `rcpp:QuantityCalculationItemCodeCondition`
- 유형: `rcpp:FieldRequirement`
- 주요 관계:
  - `rcpp:requiredForClass` → `rcpp:QuantityCalculationItem`
  - `rcpp:requiredProperty` → `rcpp:quantityCalculationCode`
  - `rcpp:requiredProperty` → `rcpp:quantityContractItemCode`
- 정의값:
  - `rcpp:inclusionCondition` = 원천 코드가 있으면 사용하고, 없으면 복합 식별기준으로 계약항목에 매칭한 뒤 안정적인 식별자를 생성함.
  - `rcpp:requirementLevel` = 조건부

### 5.73. `QuantityCalculationItemRequiredFields` — 수량산출 항목 필수값

- 설명: 수량산출 항목에 적용되는 필수 요구조건으로, 공종, 품명, 규격, 단위, 측정단위 사용, 수량산식, 수량산출근거, 산출수량을(를) 요구함.
- IRI: `rcpp:QuantityCalculationItemRequiredFields`
- 유형: `rcpp:FieldRequirement`
- 주요 관계:
  - `rcpp:requiredForClass` → `rcpp:QuantityCalculationItem`
  - `rcpp:requiredProperty` → `rcpp:quantityCalculatedQuantity`
  - `rcpp:requiredProperty` → `rcpp:quantityCalculationBasis`
  - `rcpp:requiredProperty` → `rcpp:quantityFormula`
  - `rcpp:requiredProperty` → `rcpp:quantityItemName`
  - `rcpp:requiredProperty` → `rcpp:quantitySpecification`
  - `rcpp:requiredProperty` → `rcpp:quantityUnit`
  - `rcpp:requiredProperty` → `rcpp:quantityWorkType`
  - `rcpp:requiredProperty` → `rcpp:usesUnit`
- 정의값:
  - `rcpp:requirementLevel` = 필수

### 5.74. `RdfsDomainRangeInferenceRule` — RDFS domain·range 해석 원칙

- 설명: rdfs:domain과 rdfs:range는 입력값을 차단하는 검증 규칙이 아니라 주어와 목적어의 유형을 추론하는 의미 규칙으로 사용함. 여러 클래스에 재사용하는 속성에는 appliesToClass를 사용하여 의도하지 않은 교집합 추론을 피함.
- IRI: `rcpp:RdfsDomainRangeInferenceRule`
- 유형: `rdfs:Resource`

### 5.75. `ReadyMixedConcreteSpecificationRule` — 레미콘 규격 정규화규칙

- 설명: 레미콘 규격 정규화규칙 개체다. 비용항목의 규격 식별요소를 정규화하며 구성순서는 콘크리트종류 → 굵은골재 최대치수 → 호칭강도 → 슬럼프 → 계약단가 구분 시 시멘트종류임.
- IRI: `rcpp:ReadyMixedConcreteSpecificationRule`
- 유형: `rcpp:SpecificationNormalizationRule`
- 주요 관계:
  - `rcpp:appliesToClass` → `rcpp:ReadyMixedConcreteCostItem`
- 정의값:
  - `rcpp:componentDelimiter` = -
  - `rcpp:componentOrder` = 콘크리트종류 → 굵은골재 최대치수 → 호칭강도 → 슬럼프 → 계약단가 구분 시 시멘트종류
  - `rcpp:missingValueTreatment` = 계약 품목의 필수 규격값이 없으면 원문규격을 보존하고 검토대상으로 둔다.
  - `rcpp:ruleVersion` = 1.0

### 5.76. `RebarAssembly` — 철근 조립

- 설명: 철근 작업유형 코드목록에서 계약단가 식별과 규격 정규화에 사용하는 통제값 `철근 조립`임.
- IRI: `rcpp:RebarAssembly`
- 유형: `rcpp:RebarWorkType`
- 정의값:
  - `rcpp:codeValue` = ASSEMBLY
  - `rcpp:sourceValueAlias` = 조립
  - `rcpp:sourceValueAlias` = 철근조립

### 5.77. `RebarDiameterRepresentationRule` — 철근 지름 표현 원칙

- 설명: 계약항목이 D13처럼 정확한 지름을 사용하면 호칭지름을 정의하고, D13 이하·D16 이상·D10~D13처럼 구간으로 단가를 구분하면 최소지름·최대지름 또는 지름구간을 정의함. 철근 규격은 강종, 호칭지름 또는 지름구간, 작업유형을 최소 권장요소로 사용함.
- IRI: `rcpp:RebarDiameterRepresentationRule`
- 유형: `rdfs:Resource`

### 5.78. `RebarFabrication` — 철근 가공

- 설명: 철근 작업유형 코드목록에서 계약단가 식별과 규격 정규화에 사용하는 통제값 `철근 가공`임.
- IRI: `rcpp:RebarFabrication`
- 유형: `rcpp:RebarWorkType`
- 정의값:
  - `rcpp:codeValue` = FABRICATION
  - `rcpp:sourceValueAlias` = 가공
  - `rcpp:sourceValueAlias` = 철근가공

### 5.79. `RebarFabricationAndAssembly` — 가공 및 조립

- 설명: 철근 작업유형 코드목록에서 계약단가 식별과 규격 정규화에 사용하는 통제값 `가공 및 조립`임.
- IRI: `rcpp:RebarFabricationAndAssembly`
- 유형: `rcpp:RebarWorkType`
- 정의값:
  - `rcpp:codeValue` = FABRICATION_ASSEMBLY
  - `rcpp:sourceValueAlias` = 가공 및 조립
  - `rcpp:sourceValueAlias` = 가공조립
  - `rcpp:sourceValueAlias` = 철근 가공·조립

### 5.80. `RebarSpecificationRule` — 철근 규격 정규화규칙

- 설명: 철근 규격 정규화규칙 개체다. 비용항목의 규격 식별요소를 정규화하며 구성순서는 강종 → 호칭지름 또는 지름구간 → 가공·조립구분 → 계약단가 구분 시 이음방식임.
- IRI: `rcpp:RebarSpecificationRule`
- 유형: `rcpp:SpecificationNormalizationRule`
- 주요 관계:
  - `rcpp:appliesToClass` → `rcpp:RebarCostItem`
- 정의값:
  - `rcpp:componentDelimiter` = -
  - `rcpp:componentOrder` = 강종 → 호칭지름 또는 지름구간 → 가공·조립구분 → 계약단가 구분 시 이음방식
  - `rcpp:missingValueTreatment` = 계약단가 구분에 사용하지 않는 선택 요소는 생략하고, 필수 식별요소가 없으면 검토대상으로 둔다.
  - `rcpp:ruleVersion` = 1.0

### 5.81. `RebarWorkCategory` — 철근공사

- 설명: 서류항목과 표준 비용항목을 철근으로 분류하기 위한 공종분류 개체이며 공종코드는 RC-REBAR임.
- IRI: `rcpp:RebarWorkCategory`
- 유형: `rcpp:WorkCategory`
- 주요 관계:
  - `rcpp:parentWorkCategory` → `rcpp:ReinforcedConcreteWorkCategory`
- 정의값:
  - `rcpp:sourceValueAlias` = 철근
  - `rcpp:sourceValueAlias` = 철근공
  - `rcpp:sourceValueAlias` = 철근공사
  - `rcpp:workCategoryCode` = RC-REBAR
  - `rcpp:workCategoryName` = 철근

### 5.82. `ReinforcedConcreteWorkCategory` — 철근콘크리트공종

- 설명: 서류항목과 표준 비용항목을 철근콘크리트공종으로 분류하기 위한 공종분류 개체이며 공종코드는 RC임.
- IRI: `rcpp:ReinforcedConcreteWorkCategory`
- 유형: `rcpp:WorkCategory`
- 정의값:
  - `rcpp:sourceValueAlias` = 철근콘크리트
  - `rcpp:sourceValueAlias` = 철근콘크리트공
  - `rcpp:sourceValueAlias` = 철근콘크리트공사
  - `rcpp:workCategoryCode` = RC
  - `rcpp:workCategoryName` = 철근콘크리트공종

### 5.83. `RoundDown` — 절사

- 설명: 금액 계산정책에서 계산 결과의 처리 방법을 지정하는 절사 방식 개체다.
- IRI: `rcpp:RoundDown`
- 유형: `rcpp:RoundingMode`
- 정의값:
  - `rcpp:codeValue` = DOWN

### 5.84. `RoundHalfUp` — 반올림

- 설명: 금액 계산정책에서 계산 결과의 처리 방법을 지정하는 반올림 방식 개체다.
- IRI: `rcpp:RoundHalfUp`
- 유형: `rcpp:RoundingMode`
- 정의값:
  - `rcpp:codeValue` = HALF_UP

### 5.85. `RoundUp` — 올림

- 설명: 금액 계산정책에서 계산 결과의 처리 방법을 지정하는 올림 방식 개체다.
- IRI: `rcpp:RoundUp`
- 유형: `rcpp:RoundingMode`
- 정의값:
  - `rcpp:codeValue` = UP

### 5.86. `SD400` — SD400

- 설명: 철근 강종 코드목록에서 계약단가 식별과 규격 정규화에 사용하는 통제값 `SD400`임.
- IRI: `rcpp:SD400`
- 유형: `rcpp:RebarGrade`
- 정의값:
  - `rcpp:codeValue` = SD400
  - `rcpp:sourceValueAlias` = SD 400
  - `rcpp:sourceValueAlias` = 에스디400

### 5.87. `SD500` — SD500

- 설명: 철근 강종 코드목록에서 계약단가 식별과 규격 정규화에 사용하는 통제값 `SD500`임.
- IRI: `rcpp:SD500`
- 유형: `rcpp:RebarGrade`
- 정의값:
  - `rcpp:codeValue` = SD500
  - `rcpp:sourceValueAlias` = SD 500
  - `rcpp:sourceValueAlias` = 에스디500

### 5.88. `SD600` — SD600

- 설명: 철근 강종 코드목록에서 계약단가 식별과 규격 정규화에 사용하는 통제값 `SD600`임.
- IRI: `rcpp:SD600`
- 유형: `rcpp:RebarGrade`
- 정의값:
  - `rcpp:codeValue` = SD600
  - `rcpp:sourceValueAlias` = SD 600
  - `rcpp:sourceValueAlias` = 에스디600

### 5.89. `ShoringSpecificationRule` — 동바리 규격 정규화규칙

- 설명: 동바리 규격 정규화규칙 개체다. 비용항목의 규격 식별요소를 정규화하며 구성순서는 동바리종류 → 설치환경 → 수직고구간 → 작업유형임.
- IRI: `rcpp:ShoringSpecificationRule`
- 유형: `rcpp:SpecificationNormalizationRule`
- 주요 관계:
  - `rcpp:appliesToClass` → `rcpp:ShoringCostItem`
- 정의값:
  - `rcpp:componentDelimiter` = -
  - `rcpp:componentOrder` = 동바리종류 → 설치환경 → 수직고구간 → 작업유형
  - `rcpp:missingValueTreatment` = 계약단가를 구분하지 않는 선택 요소는 생략함.
  - `rcpp:ruleVersion` = 1.0

### 5.90. `ShoringWorkCategory` — 동바리공사

- 설명: 서류항목과 표준 비용항목을 동바리으로 분류하기 위한 공종분류 개체이며 공종코드는 RC-SHORING임.
- IRI: `rcpp:ShoringWorkCategory`
- 유형: `rcpp:WorkCategory`
- 주요 관계:
  - `rcpp:parentWorkCategory` → `rcpp:ReinforcedConcreteWorkCategory`
- 정의값:
  - `rcpp:sourceValueAlias` = 동바리
  - `rcpp:sourceValueAlias` = 동바리공
  - `rcpp:sourceValueAlias` = 동바리공사
  - `rcpp:workCategoryCode` = RC-SHORING
  - `rcpp:workCategoryName` = 동바리

### 5.91. `SimpleComplexity` — 단순

- 설명: 복잡도 코드목록에서 계약단가 식별과 규격 정규화에 사용하는 통제값 `단순`임.
- IRI: `rcpp:SimpleComplexity`
- 유형: `rcpp:ComplexityLevel`
- 정의값:
  - `rcpp:codeValue` = SIMPLE
  - `rcpp:sourceValueAlias` = Simple
  - `rcpp:sourceValueAlias` = 간단
  - `rcpp:sourceValueAlias` = 단순

### 5.92. `SourceTextNormalizationRule` — 원문 문자열과 표준 개체 분리 원칙

- 설명: 서류에 적힌 철근공·철근공사·철근 및 M2·m²·㎡ 등의 표현은 원문 공종문구·원문 단위문구로 보존하고, 표준값은 belongsToWorkCategory와 usesUnit으로 WorkCategory·Unit 개체에 연결함.
- IRI: `rcpp:SourceTextNormalizationRule`
- 유형: `rdfs:Resource`

### 5.93. `SpecificationBandRule` — 구간 규격 표현 원칙

- 설명: 철근 지름·콘크리트 타설물량·거푸집 및 동바리 수직고가 범위로 제시되면 원문 구간문구와 함께 최소값·최대값 또는 구간 분류값을 정의하여 단가 매칭에 사용함.
- IRI: `rcpp:SpecificationBandRule`
- 유형: `rdfs:Resource`

### 5.94. `SpecificationInclusionRule` — 비용규격 속성 포함 원칙

- 설명: 내역항목 식별, 계약단가 구분, 금회기성수량 또는 금액 확인 중 하나 이상에 필요한 속성만 공종별 비용규격으로 분해함. 세 조건에 해당하지 않는 정보는 제외하거나 원문규격에만 보존함.
- IRI: `rcpp:SpecificationInclusionRule`
- 유형: `rdfs:Resource`

### 5.95. `SquareMetreUnit` — 제곱미터

- 설명: 면적 차원의 표준 측정단위다. 단위코드는 M2, 기호는 ㎡, 기준단위는 제곱미터, 기준단위 변환계수는 1.0임.
- IRI: `rcpp:SquareMetreUnit`
- 유형: `rcpp:Unit`
- 주요 관계:
  - `rcpp:baseUnit` → `rcpp:SquareMetreUnit`
- 정의값:
  - `rcpp:conversionFactorToBaseUnit` = 1.0
  - `rcpp:sourceValueAlias` = M2
  - `rcpp:sourceValueAlias` = m2
  - `rcpp:sourceValueAlias` = m²
  - `rcpp:sourceValueAlias` = ㎡
  - `rcpp:unitCode` = M2
  - `rcpp:unitDimension` = 면적
  - `rcpp:unitSymbol` = ㎡

### 5.96. `StandardCurrentProgressAmountRule` — 표준 금회기성금액 계산규칙

- 설명: RCPP 온톨로지에서 금회기성금액 산정규칙 유형으로 사용하는 `표준 금회기성금액 계산규칙` 개체다.
- IRI: `rcpp:StandardCurrentProgressAmountRule`
- 유형: `rcpp:CurrentProgressAmountCalculation`

### 5.97. `StandardProgressQuantityRollupRule` — 표준 기성수량 누계·잔여 규칙

- 설명: 기성수량 누계·잔여 산정규칙 유형을 실제 계산에 적용하기 위해 정의한 규칙 개체 `표준 기성수량 누계·잔여 규칙`임.
- IRI: `rcpp:StandardProgressQuantityRollupRule`
- 유형: `rcpp:ProgressQuantityRollupCalculation`

### 5.98. `StandardProgressSummaryRule` — 표준 공종별·전체 기성집계 규칙

- 설명: 공종별·전체 기성 집계규칙 유형을 실제 계산에 적용하기 위해 정의한 규칙 개체 `표준 공종별·전체 기성집계 규칙`임.
- IRI: `rcpp:StandardProgressSummaryRule`
- 유형: `rcpp:ProgressSummaryCalculation`

### 5.99. `SteelPipeShoring` — 강관동바리

- 설명: 동바리 유형 코드목록에서 계약단가 식별과 규격 정규화에 사용하는 통제값 `강관동바리`임.
- IRI: `rcpp:SteelPipeShoring`
- 유형: `rcpp:ShoringType`
- 정의값:
  - `rcpp:codeValue` = STEEL_PIPE_SHORING
  - `rcpp:sourceValueAlias` = 강관 동바리
  - `rcpp:sourceValueAlias` = 강관동바리

### 5.100. `SupportingReferenceDocumentRole` — 지원·교차확인 역할

- 설명: 단가 및 원가구성을 보조하되 금회수량이나 금액의 직접 근거로 사용하지 않는 역할.
- IRI: `rcpp:SupportingReferenceDocumentRole`
- 유형: `rcpp:DocumentRole`

### 5.101. `SystemShoring` — 시스템동바리

- 설명: 동바리 유형 코드목록에서 계약단가 식별과 규격 정규화에 사용하는 통제값 `시스템동바리`임.
- IRI: `rcpp:SystemShoring`
- 유형: `rcpp:ShoringType`
- 정의값:
  - `rcpp:codeValue` = SYSTEM_SHORING
  - `rcpp:sourceValueAlias` = 시스템 동바리
  - `rcpp:sourceValueAlias` = 시스템동바리

### 5.102. `TonneUnit` — 톤

- 설명: 질량 차원의 표준 측정단위다. 단위코드는 TON, 기호는 ton, 기준단위는 킬로그램, 기준단위 변환계수는 1000.0임.
- IRI: `rcpp:TonneUnit`
- 유형: `rcpp:Unit`
- 주요 관계:
  - `rcpp:baseUnit` → `rcpp:KilogramUnit`
- 정의값:
  - `rcpp:conversionFactorToBaseUnit` = 1000.0
  - `rcpp:sourceValueAlias` = TON
  - `rcpp:sourceValueAlias` = t
  - `rcpp:sourceValueAlias` = ton
  - `rcpp:sourceValueAlias` = 톤
  - `rcpp:unitCode` = TON
  - `rcpp:unitDimension` = 질량
  - `rcpp:unitSymbol` = ton

### 5.103. `UnitConsistencyRule` — 단위 일관성 원칙

- 설명: 계약내역서 단위, 수량산출결과 단위와 공사기성부분내역서 단위는 같거나 같은 차원의 기준단위로 변환 가능필요. 비교와 금액 계산 전에 conversionFactorToBaseUnit을 적용함.
- IRI: `rcpp:UnitConsistencyRule`
- 유형: `rdfs:Resource`

### 5.104. `WaterInstallationEnvironment` — 수상

- 설명: 설치환경 코드목록에서 계약단가 식별과 규격 정규화에 사용하는 통제값 `수상`임.
- IRI: `rcpp:WaterInstallationEnvironment`
- 유형: `rcpp:InstallationEnvironment`
- 정의값:
  - `rcpp:codeValue` = WATER
  - `rcpp:sourceValueAlias` = 수상

### 5.105. `WorkTypeDetailItemCodeCondition` — 공종별 상세내역 코드 조건

- 설명: 공종별 상세항목에 적용되는 조건부 요구조건으로, 내역코드을(를) 요구함.
- IRI: `rcpp:WorkTypeDetailItemCodeCondition`
- 유형: `rcpp:FieldRequirement`
- 주요 관계:
  - `rcpp:requiredForClass` → `rcpp:WorkTypeDetailItem`
  - `rcpp:requiredProperty` → `rcpp:workDetailItemCode`
- 정의값:
  - `rcpp:inclusionCondition` = 원천 코드가 있으면 보존하고, 없으면 대응 계약항목의 식별자를 사용함.
  - `rcpp:requirementLevel` = 조건부

### 5.106. `WorkTypeDetailItemRequiredFields` — 공종별 상세항목 필수값

- 설명: 공종별 상세항목에 적용되는 필수 요구조건으로, 세부 공종, 품명, 규격, 단위, 측정단위 사용, 수량, 단가, 내역항목별 금액을(를) 요구함.
- IRI: `rcpp:WorkTypeDetailItemRequiredFields`
- 유형: `rcpp:FieldRequirement`
- 주요 관계:
  - `rcpp:requiredForClass` → `rcpp:WorkTypeDetailItem`
  - `rcpp:requiredProperty` → `rcpp:usesUnit`
  - `rcpp:requiredProperty` → `rcpp:workDetailAmount`
  - `rcpp:requiredProperty` → `rcpp:workDetailItemName`
  - `rcpp:requiredProperty` → `rcpp:workDetailQuantity`
  - `rcpp:requiredProperty` → `rcpp:workDetailSpecification`
  - `rcpp:requiredProperty` → `rcpp:workDetailUnit`
  - `rcpp:requiredProperty` → `rcpp:workDetailUnitPrice`
  - `rcpp:requiredProperty` → `rcpp:workDetailWorkType`
- 정의값:
  - `rcpp:requirementLevel` = 필수

### 5.107. `WorkTypeSummaryItemRequiredFields` — 공종별 계약집계항목 필수값

- 설명: 공종별 계약집계항목에 적용되는 필수 요구조건으로, 공종, 공종별 계약금액을(를) 요구함.
- IRI: `rcpp:WorkTypeSummaryItemRequiredFields`
- 유형: `rcpp:FieldRequirement`
- 주요 관계:
  - `rcpp:requiredForClass` → `rcpp:WorkTypeSummaryItem`
  - `rcpp:requiredProperty` → `rcpp:summaryContractAmount`
  - `rcpp:requiredProperty` → `rcpp:summaryWorkType`
- 정의값:
  - `rcpp:requirementLevel` = 필수

## 6. 내부 관계 트리플 전체 목록

- 수록대상: 주어와 목적어가 모두 RCPP 네임스페이스의 명명 자원인 관계 트리플 전체
- 리터럴 값: 문자열·숫자·날짜를 앞의 개별 용어 명세에 수록

| 번호 | 주어 | 관계 | 목적어 |
| ---: | --- | --- | --- |
| 1 | `rcpp:BaseUnitConversionRule` | `rdf:type` | `rcpp:UnitConversionRule` |
| 2 | `rcpp:CalculationActivityRequiredFields` | `rcpp:requiredForClass` | `rcpp:CalculationActivity` |
| 3 | `rcpp:CalculationActivityRequiredFields` | `rcpp:requiredProperty` | `rcpp:appliesPolicy` |
| 4 | `rcpp:CalculationActivityRequiredFields` | `rcpp:requiredProperty` | `rcpp:appliesRule` |
| 5 | `rcpp:CalculationActivityRequiredFields` | `rcpp:requiredProperty` | `rcpp:calculationInputItem` |
| 6 | `rcpp:CalculationActivityRequiredFields` | `rcpp:requiredProperty` | `rcpp:calculationOutputItem` |
| 7 | `rcpp:CalculationActivityRequiredFields` | `rcpp:requiredProperty` | `rcpp:calculationRound` |
| 8 | `rcpp:CalculationActivityRequiredFields` | `rcpp:requiredProperty` | `rcpp:calculationStatus` |
| 9 | `rcpp:CalculationActivityRequiredFields` | `rdf:type` | `rcpp:FieldRequirement` |
| 10 | `rcpp:ComplexComplexity` | `rdf:type` | `rcpp:ComplexityLevel` |
| 11 | `rcpp:ComplexityLevel` | `rdfs:subClassOf` | `rcpp:ControlledSpecificationValue` |
| 12 | `rcpp:ConcreteCostItem` | `rdfs:subClassOf` | `rcpp:CostItem` |
| 13 | `rcpp:ConcretePlacementCostItem` | `rdfs:subClassOf` | `rcpp:ConcreteCostItem` |
| 14 | `rcpp:ConcretePlacementSpecificationRule` | `rcpp:appliesToClass` | `rcpp:ConcretePlacementCostItem` |
| 15 | `rcpp:ConcretePlacementSpecificationRule` | `rdf:type` | `rcpp:SpecificationNormalizationRule` |
| 16 | `rcpp:ConcreteWorkCategory` | `rcpp:parentWorkCategory` | `rcpp:ReinforcedConcreteWorkCategory` |
| 17 | `rcpp:ConcreteWorkCategory` | `rdf:type` | `rcpp:WorkCategory` |
| 18 | `rcpp:ConsistencyRule` | `rcpp:schemaFlowsTo` | `rcpp:CurrentProgressStatement` |
| 19 | `rcpp:ContractBasisDocumentRole` | `rdf:type` | `rcpp:DocumentRole` |
| 20 | `rcpp:ContractStatement` | `rcpp:expectedDocumentRole` | `rcpp:ContractBasisDocumentRole` |
| 21 | `rcpp:ContractStatement` | `rcpp:expectedItemClass` | `rcpp:ContractStatementItem` |
| 22 | `rcpp:ContractStatement` | `rcpp:schemaFlowsTo` | `rcpp:DocumentItemMatching` |
| 23 | `rcpp:ContractStatement` | `rcpp:typicalNextDocumentClass` | `rcpp:WorkTypeDetailStatement` |
| 24 | `rcpp:ContractStatement` | `rdfs:subClassOf` | `rcpp:SourceDocument` |
| 25 | `rcpp:ContractStatementItem` | `rcpp:expectedCostItemClass` | `rcpp:CostItem` |
| 26 | `rcpp:ContractStatementItem` | `rcpp:expectedSourceItemClass` | `rcpp:QuantityCalculationItem` |
| 27 | `rcpp:ContractStatementItem` | `rdfs:subClassOf` | `rcpp:DetailCostItem` |
| 28 | `rcpp:ContractStatementItemCodeCondition` | `rcpp:requiredForClass` | `rcpp:ContractStatementItem` |
| 29 | `rcpp:ContractStatementItemCodeCondition` | `rcpp:requiredProperty` | `rcpp:contractItemCode` |
| 30 | `rcpp:ContractStatementItemCodeCondition` | `rdf:type` | `rcpp:FieldRequirement` |
| 31 | `rcpp:ContractStatementItemRequiredFields` | `rcpp:requiredForClass` | `rcpp:ContractStatementItem` |
| 32 | `rcpp:ContractStatementItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:contractAmount` |
| 33 | `rcpp:ContractStatementItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:contractItemName` |
| 34 | `rcpp:ContractStatementItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:contractQuantity` |
| 35 | `rcpp:ContractStatementItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:contractSpecification` |
| 36 | `rcpp:ContractStatementItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:contractUnit` |
| 37 | `rcpp:ContractStatementItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:contractUnitPrice` |
| 38 | `rcpp:ContractStatementItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:contractWorkType` |
| 39 | `rcpp:ContractStatementItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:usesUnit` |
| 40 | `rcpp:ContractStatementItemRequiredFields` | `rdf:type` | `rcpp:FieldRequirement` |
| 41 | `rcpp:CostItem` | `rcpp:expectedUnitClass` | `rcpp:Unit` |
| 42 | `rcpp:CostItem` | `rcpp:expectedWorkCategoryClass` | `rcpp:WorkCategory` |
| 43 | `rcpp:CostItem` | `rcpp:schemaFlowsTo` | `rcpp:DocumentItemMatching` |
| 44 | `rcpp:CostItemRequiredFields` | `rcpp:requiredForClass` | `rcpp:CostItem` |
| 45 | `rcpp:CostItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:belongsToWorkCategory` |
| 46 | `rcpp:CostItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:costItemCode` |
| 47 | `rcpp:CostItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:costItemName` |
| 48 | `rcpp:CostItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:normalizedSpecificationCode` |
| 49 | `rcpp:CostItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:usesUnit` |
| 50 | `rcpp:CostItemRequiredFields` | `rdf:type` | `rcpp:FieldRequirement` |
| 51 | `rcpp:CostStatement` | `rdfs:subClassOf` | `rcpp:SupportingReferenceDocument` |
| 52 | `rcpp:CostSummaryDocumentRole` | `rdf:type` | `rcpp:DocumentRole` |
| 53 | `rcpp:CubicMetreUnit` | `rcpp:baseUnit` | `rcpp:CubicMetreUnit` |
| 54 | `rcpp:CubicMetreUnit` | `rdf:type` | `rcpp:Unit` |
| 55 | `rcpp:CurrentProgressAmountCalculation` | `rcpp:inputQuantityProperty` | `rcpp:progressCurrentQuantity` |
| 56 | `rcpp:CurrentProgressAmountCalculation` | `rcpp:inputUnitPriceProperty` | `rcpp:contractUnitPrice` |
| 57 | `rcpp:CurrentProgressAmountCalculation` | `rcpp:producesField` | `rcpp:outputCurrentAmount` |
| 58 | `rcpp:CurrentProgressAmountCalculation` | `rcpp:schemaFlowsTo` | `rcpp:CurrentProgressStatement` |
| 59 | `rcpp:CurrentProgressAmountCalculation` | `rdfs:subClassOf` | `rcpp:ProgressAmountCalculation` |
| 60 | `rcpp:CurrentProgressDetailItem` | `rcpp:expectedAggregationTargetClass` | `rcpp:CurrentProgressSummaryItem` |
| 61 | `rcpp:CurrentProgressDetailItem` | `rcpp:expectedCorrespondingItemClass` | `rcpp:ContractStatementItem` |
| 62 | `rcpp:CurrentProgressDetailItem` | `rcpp:expectedCorrespondingItemClass` | `rcpp:CurrentProgressQuantityItem` |
| 63 | `rcpp:CurrentProgressDetailItem` | `rcpp:expectedCorrespondingItemClass` | `rcpp:PreviousProgressStatementItem` |
| 64 | `rcpp:CurrentProgressDetailItem` | `rcpp:expectedCostItemClass` | `rcpp:CostItem` |
| 65 | `rcpp:CurrentProgressDetailItem` | `rcpp:expectedSourceItemClass` | `rcpp:ContractStatementItem` |
| 66 | `rcpp:CurrentProgressDetailItem` | `rcpp:expectedSourceItemClass` | `rcpp:CurrentProgressQuantityItem` |
| 67 | `rcpp:CurrentProgressDetailItem` | `rcpp:expectedSourceItemClass` | `rcpp:PreviousProgressStatementItem` |
| 68 | `rcpp:CurrentProgressDetailItem` | `rcpp:expectedUnitPriceSourceClass` | `rcpp:ContractStatementItem` |
| 69 | `rcpp:CurrentProgressDetailItem` | `rdfs:subClassOf` | `rcpp:CurrentProgressStatementItem` |
| 70 | `rcpp:CurrentProgressDetailItem` | `rdfs:subClassOf` | `rcpp:DetailCostItem` |
| 71 | `rcpp:CurrentProgressDetailItemCalculatedFields` | `rcpp:requiredForClass` | `rcpp:CurrentProgressDetailItem` |
| 72 | `rcpp:CurrentProgressDetailItemCalculatedFields` | `rcpp:requiredProperty` | `rcpp:outputCumulativeAmount` |
| 73 | `rcpp:CurrentProgressDetailItemCalculatedFields` | `rcpp:requiredProperty` | `rcpp:outputCumulativeQuantity` |
| 74 | `rcpp:CurrentProgressDetailItemCalculatedFields` | `rcpp:requiredProperty` | `rcpp:outputCurrentAmount` |
| 75 | `rcpp:CurrentProgressDetailItemCalculatedFields` | `rcpp:requiredProperty` | `rcpp:outputRemainingAmount` |
| 76 | `rcpp:CurrentProgressDetailItemCalculatedFields` | `rcpp:requiredProperty` | `rcpp:outputRemainingQuantity` |
| 77 | `rcpp:CurrentProgressDetailItemCalculatedFields` | `rdf:type` | `rcpp:FieldRequirement` |
| 78 | `rcpp:CurrentProgressDetailItemConditionalFields` | `rcpp:requiredForClass` | `rcpp:CurrentProgressDetailItem` |
| 79 | `rcpp:CurrentProgressDetailItemConditionalFields` | `rcpp:requiredProperty` | `rcpp:outputCumulativeRate` |
| 80 | `rcpp:CurrentProgressDetailItemConditionalFields` | `rcpp:requiredProperty` | `rcpp:outputCurrentRate` |
| 81 | `rcpp:CurrentProgressDetailItemConditionalFields` | `rcpp:requiredProperty` | `rcpp:outputItemCode` |
| 82 | `rcpp:CurrentProgressDetailItemConditionalFields` | `rcpp:requiredProperty` | `rcpp:outputPreviousRate` |
| 83 | `rcpp:CurrentProgressDetailItemConditionalFields` | `rdf:type` | `rcpp:FieldRequirement` |
| 84 | `rcpp:CurrentProgressDetailItemTransferredFields` | `rcpp:requiredForClass` | `rcpp:CurrentProgressDetailItem` |
| 85 | `rcpp:CurrentProgressDetailItemTransferredFields` | `rcpp:requiredProperty` | `rcpp:outputContractAmount` |
| 86 | `rcpp:CurrentProgressDetailItemTransferredFields` | `rcpp:requiredProperty` | `rcpp:outputContractQuantity` |
| 87 | `rcpp:CurrentProgressDetailItemTransferredFields` | `rcpp:requiredProperty` | `rcpp:outputContractUnitPrice` |
| 88 | `rcpp:CurrentProgressDetailItemTransferredFields` | `rcpp:requiredProperty` | `rcpp:outputCurrentQuantity` |
| 89 | `rcpp:CurrentProgressDetailItemTransferredFields` | `rcpp:requiredProperty` | `rcpp:outputPreviousAmount` |
| 90 | `rcpp:CurrentProgressDetailItemTransferredFields` | `rcpp:requiredProperty` | `rcpp:outputPreviousQuantity` |
| 91 | `rcpp:CurrentProgressDetailItemTransferredFields` | `rcpp:requiredProperty` | `rcpp:outputSpecification` |
| 92 | `rcpp:CurrentProgressDetailItemTransferredFields` | `rcpp:requiredProperty` | `rcpp:outputUnit` |
| 93 | `rcpp:CurrentProgressDetailItemTransferredFields` | `rcpp:requiredProperty` | `rcpp:outputWorkDescription` |
| 94 | `rcpp:CurrentProgressDetailItemTransferredFields` | `rcpp:requiredProperty` | `rcpp:outputWorkType` |
| 95 | `rcpp:CurrentProgressDetailItemTransferredFields` | `rcpp:requiredProperty` | `rcpp:usesUnit` |
| 96 | `rcpp:CurrentProgressDetailItemTransferredFields` | `rdf:type` | `rcpp:FieldRequirement` |
| 97 | `rcpp:CurrentProgressQuantityItem` | `rcpp:expectedCorrespondingItemClass` | `rcpp:ContractStatementItem` |
| 98 | `rcpp:CurrentProgressQuantityItem` | `rcpp:expectedCorrespondingItemClass` | `rcpp:PreviousProgressStatementItem` |
| 99 | `rcpp:CurrentProgressQuantityItem` | `rcpp:expectedCostItemClass` | `rcpp:CostItem` |
| 100 | `rcpp:CurrentProgressQuantityItem` | `rcpp:expectedIdentificationReferenceClass` | `rcpp:ContractStatementItem` |
| 101 | `rcpp:CurrentProgressQuantityItem` | `rcpp:expectedIdentificationReferenceClass` | `rcpp:QuantityCalculationItem` |
| 102 | `rcpp:CurrentProgressQuantityItem` | `rcpp:expectedPreviousQuantitySourceClass` | `rcpp:PreviousProgressStatementItem` |
| 103 | `rcpp:CurrentProgressQuantityItem` | `rcpp:expectedQuantityBasisClass` | `rcpp:QuantityCalculationItem` |
| 104 | `rcpp:CurrentProgressQuantityItem` | `rcpp:expectedSourceItemClass` | `rcpp:PreviousProgressStatementItem` |
| 105 | `rcpp:CurrentProgressQuantityItem` | `rcpp:expectedSourceItemClass` | `rcpp:ProgressQuantityDetailItem` |
| 106 | `rcpp:CurrentProgressQuantityItem` | `rdfs:subClassOf` | `rcpp:DocumentItem` |
| 107 | `rcpp:CurrentProgressQuantityItemCalculatedFields` | `rcpp:requiredForClass` | `rcpp:CurrentProgressQuantityItem` |
| 108 | `rcpp:CurrentProgressQuantityItemCalculatedFields` | `rcpp:requiredProperty` | `rcpp:progressCumulativeQuantity` |
| 109 | `rcpp:CurrentProgressQuantityItemCalculatedFields` | `rcpp:requiredProperty` | `rcpp:progressRemainingQuantity` |
| 110 | `rcpp:CurrentProgressQuantityItemCalculatedFields` | `rdf:type` | `rcpp:FieldRequirement` |
| 111 | `rcpp:CurrentProgressQuantityItemCarryForwardFields` | `rcpp:requiredForClass` | `rcpp:CurrentProgressQuantityItem` |
| 112 | `rcpp:CurrentProgressQuantityItemCarryForwardFields` | `rcpp:requiredProperty` | `rcpp:progressPreviousCumulativeQuantity` |
| 113 | `rcpp:CurrentProgressQuantityItemCarryForwardFields` | `rdf:type` | `rcpp:FieldRequirement` |
| 114 | `rcpp:CurrentProgressQuantityItemCodeCondition` | `rcpp:requiredForClass` | `rcpp:CurrentProgressQuantityItem` |
| 115 | `rcpp:CurrentProgressQuantityItemCodeCondition` | `rcpp:requiredProperty` | `rcpp:progressQuantityItemCode` |
| 116 | `rcpp:CurrentProgressQuantityItemCodeCondition` | `rdf:type` | `rcpp:FieldRequirement` |
| 117 | `rcpp:CurrentProgressQuantityItemSourceFields` | `rcpp:requiredForClass` | `rcpp:CurrentProgressQuantityItem` |
| 118 | `rcpp:CurrentProgressQuantityItemSourceFields` | `rcpp:requiredProperty` | `rcpp:progressCurrentQuantity` |
| 119 | `rcpp:CurrentProgressQuantityItemSourceFields` | `rcpp:requiredProperty` | `rcpp:progressQuantityItemName` |
| 120 | `rcpp:CurrentProgressQuantityItemSourceFields` | `rcpp:requiredProperty` | `rcpp:progressQuantitySpecification` |
| 121 | `rcpp:CurrentProgressQuantityItemSourceFields` | `rcpp:requiredProperty` | `rcpp:progressQuantityUnit` |
| 122 | `rcpp:CurrentProgressQuantityItemSourceFields` | `rcpp:requiredProperty` | `rcpp:progressQuantityWorkType` |
| 123 | `rcpp:CurrentProgressQuantityItemSourceFields` | `rcpp:requiredProperty` | `rcpp:usesUnit` |
| 124 | `rcpp:CurrentProgressQuantityItemSourceFields` | `rdf:type` | `rcpp:FieldRequirement` |
| 125 | `rcpp:CurrentProgressQuantitySheet` | `rcpp:expectedDocumentRole` | `rcpp:ProgressQuantityDocumentRole` |
| 126 | `rcpp:CurrentProgressQuantitySheet` | `rcpp:expectedItemClass` | `rcpp:CurrentProgressQuantityItem` |
| 127 | `rcpp:CurrentProgressQuantitySheet` | `rcpp:expectedItemClass` | `rcpp:ProgressQuantityDetailItem` |
| 128 | `rcpp:CurrentProgressQuantitySheet` | `rcpp:schemaFlowsTo` | `rcpp:DocumentItemMatching` |
| 129 | `rcpp:CurrentProgressQuantitySheet` | `rcpp:schemaFlowsTo` | `rcpp:ProgressQuantityRollupCalculation` |
| 130 | `rcpp:CurrentProgressQuantitySheet` | `rcpp:typicalNextDocumentClass` | `rcpp:CurrentProgressStatement` |
| 131 | `rcpp:CurrentProgressQuantitySheet` | `rdfs:subClassOf` | `rcpp:SourceDocument` |
| 132 | `rcpp:CurrentProgressStatement` | `rcpp:expectedAmountCalculationClass` | `rcpp:CurrentProgressAmountCalculation` |
| 133 | `rcpp:CurrentProgressStatement` | `rcpp:expectedDocumentRole` | `rcpp:ProgressStatementDocumentRole` |
| 134 | `rcpp:CurrentProgressStatement` | `rcpp:expectedItemClass` | `rcpp:CurrentProgressDetailItem` |
| 135 | `rcpp:CurrentProgressStatement` | `rcpp:expectedItemClass` | `rcpp:CurrentProgressSummaryItem` |
| 136 | `rcpp:CurrentProgressStatement` | `rdfs:subClassOf` | `rcpp:OutputDocument` |
| 137 | `rcpp:CurrentProgressStatementItem` | `rdfs:subClassOf` | `rcpp:DocumentItem` |
| 138 | `rcpp:CurrentProgressSummaryItem` | `rcpp:expectedSourceItemClass` | `rcpp:CurrentProgressDetailItem` |
| 139 | `rcpp:CurrentProgressSummaryItem` | `rdfs:subClassOf` | `rcpp:CurrentProgressStatementItem` |
| 140 | `rcpp:CurrentProgressSummaryItem` | `rdfs:subClassOf` | `rcpp:SummaryCostItem` |
| 141 | `rcpp:CurrentProgressSummaryItemRequiredFields` | `rcpp:requiredForClass` | `rcpp:CurrentProgressSummaryItem` |
| 142 | `rcpp:CurrentProgressSummaryItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:outputSummaryContractAmount` |
| 143 | `rcpp:CurrentProgressSummaryItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:outputSummaryCumulativeAmount` |
| 144 | `rcpp:CurrentProgressSummaryItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:outputSummaryCurrentAmount` |
| 145 | `rcpp:CurrentProgressSummaryItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:outputSummaryPreviousAmount` |
| 146 | `rcpp:CurrentProgressSummaryItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:outputSummaryWorkCategoryText` |
| 147 | `rcpp:CurrentProgressSummaryItemRequiredFields` | `rdf:type` | `rcpp:FieldRequirement` |
| 148 | `rcpp:DetailCostItem` | `rcpp:expectedAggregationTargetClass` | `rcpp:SummaryCostItem` |
| 149 | `rcpp:DetailCostItem` | `rdfs:subClassOf` | `rcpp:DocumentItem` |
| 150 | `rcpp:DetailedCostDocumentRole` | `rdf:type` | `rcpp:DocumentRole` |
| 151 | `rcpp:DocumentItem` | `rcpp:expectedUnitClass` | `rcpp:Unit` |
| 152 | `rcpp:DocumentItem` | `rcpp:expectedWorkCategoryClass` | `rcpp:WorkCategory` |
| 153 | `rcpp:DocumentItemMatching` | `rcpp:schemaFlowsTo` | `rcpp:CurrentProgressAmountCalculation` |
| 154 | `rcpp:DocumentItemMatchingConditionalFields` | `rcpp:requiredForClass` | `rcpp:DocumentItemMatching` |
| 155 | `rcpp:DocumentItemMatchingConditionalFields` | `rcpp:requiredProperty` | `rcpp:confidenceScore` |
| 156 | `rcpp:DocumentItemMatchingConditionalFields` | `rcpp:requiredProperty` | `rcpp:reviewedBy` |
| 157 | `rcpp:DocumentItemMatchingConditionalFields` | `rdf:type` | `rcpp:FieldRequirement` |
| 158 | `rcpp:DocumentItemMatchingRequiredFields` | `rcpp:requiredForClass` | `rcpp:DocumentItemMatching` |
| 159 | `rcpp:DocumentItemMatchingRequiredFields` | `rcpp:requiredProperty` | `rcpp:matchedCostItem` |
| 160 | `rcpp:DocumentItemMatchingRequiredFields` | `rcpp:requiredProperty` | `rcpp:matchingEvidence` |
| 161 | `rcpp:DocumentItemMatchingRequiredFields` | `rcpp:requiredProperty` | `rcpp:matchingMethod` |
| 162 | `rcpp:DocumentItemMatchingRequiredFields` | `rcpp:requiredProperty` | `rcpp:reviewStatus` |
| 163 | `rcpp:DocumentItemMatchingRequiredFields` | `rcpp:requiredProperty` | `rcpp:sourceItem` |
| 164 | `rcpp:DocumentItemMatchingRequiredFields` | `rcpp:requiredProperty` | `rcpp:targetItem` |
| 165 | `rcpp:DocumentItemMatchingRequiredFields` | `rdf:type` | `rcpp:FieldRequirement` |
| 166 | `rcpp:EachUnit` | `rcpp:baseUnit` | `rcpp:EachUnit` |
| 167 | `rcpp:EachUnit` | `rdf:type` | `rcpp:Unit` |
| 168 | `rcpp:EuroFormwork` | `rdf:type` | `rcpp:FormworkType` |
| 169 | `rcpp:FieldRequirement` | `rcpp:expectedRequirementTargetClass` | `rcpp:CalculationActivity` |
| 170 | `rcpp:FieldRequirement` | `rcpp:expectedRequirementTargetClass` | `rcpp:DocumentItem` |
| 171 | `rcpp:FieldRequirement` | `rcpp:expectedRequirementTargetClass` | `rcpp:DocumentItemMatching` |
| 172 | `rcpp:FormworkCostItem` | `rdfs:subClassOf` | `rcpp:CostItem` |
| 173 | `rcpp:FormworkSpecificationRule` | `rcpp:appliesToClass` | `rcpp:FormworkCostItem` |
| 174 | `rcpp:FormworkSpecificationRule` | `rdf:type` | `rcpp:SpecificationNormalizationRule` |
| 175 | `rcpp:FormworkType` | `rdfs:subClassOf` | `rcpp:ControlledSpecificationValue` |
| 176 | `rcpp:FormworkWorkCategory` | `rcpp:parentWorkCategory` | `rcpp:ReinforcedConcreteWorkCategory` |
| 177 | `rcpp:FormworkWorkCategory` | `rdf:type` | `rcpp:WorkCategory` |
| 178 | `rcpp:InstallationEnvironment` | `rdfs:subClassOf` | `rcpp:ControlledSpecificationValue` |
| 179 | `rcpp:KRW` | `rdf:type` | `rcpp:Currency` |
| 180 | `rcpp:KRWItemWonHalfUpPolicy` | `rcpp:currency` | `rcpp:KRW` |
| 181 | `rcpp:KRWItemWonHalfUpPolicy` | `rcpp:roundingMode` | `rcpp:RoundHalfUp` |
| 182 | `rcpp:KRWItemWonHalfUpPolicy` | `rdf:type` | `rcpp:CalculationPolicy` |
| 183 | `rcpp:KilogramUnit` | `rcpp:baseUnit` | `rcpp:KilogramUnit` |
| 184 | `rcpp:KilogramUnit` | `rdf:type` | `rcpp:Unit` |
| 185 | `rcpp:LandInstallationEnvironment` | `rdf:type` | `rcpp:InstallationEnvironment` |
| 186 | `rcpp:ManualPlacement` | `rdf:type` | `rcpp:PlacementMethod` |
| 187 | `rcpp:MetreUnit` | `rcpp:baseUnit` | `rcpp:MetreUnit` |
| 188 | `rcpp:MetreUnit` | `rdf:type` | `rcpp:Unit` |
| 189 | `rcpp:NormalComplexity` | `rdf:type` | `rcpp:ComplexityLevel` |
| 190 | `rcpp:OntologySchema` | `rdfs:seeAlso` | `rcpp:ClassesModule` |
| 191 | `rcpp:OntologySchema` | `rdfs:seeAlso` | `rcpp:CodeListsModule` |
| 192 | `rcpp:OntologySchema` | `rdfs:seeAlso` | `rcpp:ProgressPaymentDataFlow` |
| 193 | `rcpp:OntologySchema` | `rdfs:seeAlso` | `rcpp:PropertiesModule` |
| 194 | `rcpp:OntologySchema` | `rdfs:seeAlso` | `rcpp:PrototypeNamespaceNotice` |
| 195 | `rcpp:OutputDocument` | `rdfs:subClassOf` | `rcpp:ProgressDocument` |
| 196 | `rcpp:PlacementMethod` | `rdfs:subClassOf` | `rcpp:ControlledSpecificationValue` |
| 197 | `rcpp:PlywoodFormwork` | `rdf:type` | `rcpp:FormworkType` |
| 198 | `rcpp:PreviousProgressBasisDocumentRole` | `rdf:type` | `rcpp:DocumentRole` |
| 199 | `rcpp:PreviousProgressStatement` | `rcpp:expectedDocumentRole` | `rcpp:PreviousProgressBasisDocumentRole` |
| 200 | `rcpp:PreviousProgressStatement` | `rcpp:expectedItemClass` | `rcpp:PreviousProgressStatementItem` |
| 201 | `rcpp:PreviousProgressStatement` | `rcpp:schemaFlowsTo` | `rcpp:DocumentItemMatching` |
| 202 | `rcpp:PreviousProgressStatement` | `rcpp:typicalNextDocumentClass` | `rcpp:CurrentProgressQuantitySheet` |
| 203 | `rcpp:PreviousProgressStatement` | `rdfs:subClassOf` | `rcpp:SourceDocument` |
| 204 | `rcpp:PreviousProgressStatementItem` | `rcpp:expectedCorrespondingItemClass` | `rcpp:ContractStatementItem` |
| 205 | `rcpp:PreviousProgressStatementItem` | `rcpp:expectedCostItemClass` | `rcpp:CostItem` |
| 206 | `rcpp:PreviousProgressStatementItem` | `rdfs:subClassOf` | `rcpp:DetailCostItem` |
| 207 | `rcpp:PreviousProgressStatementItemConditionalFields` | `rcpp:requiredForClass` | `rcpp:PreviousProgressStatementItem` |
| 208 | `rcpp:PreviousProgressStatementItemConditionalFields` | `rcpp:requiredProperty` | `rcpp:previousCumulativeRate` |
| 209 | `rcpp:PreviousProgressStatementItemConditionalFields` | `rcpp:requiredProperty` | `rcpp:previousItemCode` |
| 210 | `rcpp:PreviousProgressStatementItemConditionalFields` | `rdf:type` | `rcpp:FieldRequirement` |
| 211 | `rcpp:PreviousProgressStatementItemRequiredFields` | `rcpp:requiredForClass` | `rcpp:PreviousProgressStatementItem` |
| 212 | `rcpp:PreviousProgressStatementItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:previousCumulativeAmount` |
| 213 | `rcpp:PreviousProgressStatementItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:previousCumulativeQuantity` |
| 214 | `rcpp:PreviousProgressStatementItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:previousSpecification` |
| 215 | `rcpp:PreviousProgressStatementItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:previousUnit` |
| 216 | `rcpp:PreviousProgressStatementItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:previousWorkDescription` |
| 217 | `rcpp:PreviousProgressStatementItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:usesUnit` |
| 218 | `rcpp:PreviousProgressStatementItemRequiredFields` | `rdf:type` | `rcpp:FieldRequirement` |
| 219 | `rcpp:PriceCalculationStatement` | `rdfs:subClassOf` | `rcpp:SupportingReferenceDocument` |
| 220 | `rcpp:ProgressAmountCalculation` | `rcpp:schemaFlowsTo` | `rcpp:ConsistencyRule` |
| 221 | `rcpp:ProgressAmountCalculation` | `rcpp:schemaFlowsTo` | `rcpp:CurrentProgressStatement` |
| 222 | `rcpp:ProgressAmountCalculation` | `rdfs:subClassOf` | `rcpp:CalculationRule` |
| 223 | `rcpp:ProgressQuantityDetailItem` | `rcpp:expectedAggregationTargetClass` | `rcpp:CurrentProgressQuantityItem` |
| 224 | `rcpp:ProgressQuantityDetailItem` | `rcpp:expectedCorrespondingItemClass` | `rcpp:ContractStatementItem` |
| 225 | `rcpp:ProgressQuantityDetailItem` | `rcpp:expectedCostItemClass` | `rcpp:CostItem` |
| 226 | `rcpp:ProgressQuantityDetailItem` | `rdfs:subClassOf` | `rcpp:DocumentItem` |
| 227 | `rcpp:ProgressQuantityDetailItemConditionalFields` | `rcpp:requiredForClass` | `rcpp:ProgressQuantityDetailItem` |
| 228 | `rcpp:ProgressQuantityDetailItemConditionalFields` | `rcpp:requiredProperty` | `rcpp:detailLocationText` |
| 229 | `rcpp:ProgressQuantityDetailItemConditionalFields` | `rcpp:requiredProperty` | `rcpp:hasSourceLocation` |
| 230 | `rcpp:ProgressQuantityDetailItemConditionalFields` | `rdf:type` | `rcpp:FieldRequirement` |
| 231 | `rcpp:ProgressQuantityDetailItemRequiredFields` | `rcpp:requiredForClass` | `rcpp:ProgressQuantityDetailItem` |
| 232 | `rcpp:ProgressQuantityDetailItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:detailCurrentQuantity` |
| 233 | `rcpp:ProgressQuantityDetailItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:quantityAggregatedInto` |
| 234 | `rcpp:ProgressQuantityDetailItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:representsCostItem` |
| 235 | `rcpp:ProgressQuantityDetailItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:usesUnit` |
| 236 | `rcpp:ProgressQuantityDetailItemRequiredFields` | `rdf:type` | `rcpp:FieldRequirement` |
| 237 | `rcpp:ProgressQuantityDocumentRole` | `rdf:type` | `rcpp:DocumentRole` |
| 238 | `rcpp:ProgressQuantityRollupCalculation` | `rcpp:inputQuantityProperty` | `rcpp:contractQuantity` |
| 239 | `rcpp:ProgressQuantityRollupCalculation` | `rcpp:inputQuantityProperty` | `rcpp:progressCurrentQuantity` |
| 240 | `rcpp:ProgressQuantityRollupCalculation` | `rcpp:inputQuantityProperty` | `rcpp:progressPreviousCumulativeQuantity` |
| 241 | `rcpp:ProgressQuantityRollupCalculation` | `rcpp:producesField` | `rcpp:progressCumulativeQuantity` |
| 242 | `rcpp:ProgressQuantityRollupCalculation` | `rcpp:producesField` | `rcpp:progressRemainingQuantity` |
| 243 | `rcpp:ProgressQuantityRollupCalculation` | `rcpp:schemaFlowsTo` | `rcpp:ConsistencyRule` |
| 244 | `rcpp:ProgressQuantityRollupCalculation` | `rcpp:schemaFlowsTo` | `rcpp:CurrentProgressAmountCalculation` |
| 245 | `rcpp:ProgressQuantityRollupCalculation` | `rcpp:schemaFlowsTo` | `rcpp:CurrentProgressStatement` |
| 246 | `rcpp:ProgressQuantityRollupCalculation` | `rdfs:subClassOf` | `rcpp:CalculationRule` |
| 247 | `rcpp:ProgressStatementDocumentRole` | `rdf:type` | `rcpp:DocumentRole` |
| 248 | `rcpp:ProgressSummaryCalculation` | `rcpp:schemaFlowsTo` | `rcpp:CurrentProgressStatement` |
| 249 | `rcpp:ProgressSummaryCalculation` | `rdfs:subClassOf` | `rcpp:CalculationRule` |
| 250 | `rcpp:PumpCarPlacement` | `rdf:type` | `rcpp:PlacementMethod` |
| 251 | `rcpp:QuantityBasisDocumentRole` | `rdf:type` | `rcpp:DocumentRole` |
| 252 | `rcpp:QuantityCalculationItem` | `rcpp:expectedCostItemClass` | `rcpp:CostItem` |
| 253 | `rcpp:QuantityCalculationItem` | `rdfs:subClassOf` | `rcpp:DocumentItem` |
| 254 | `rcpp:QuantityCalculationItemCodeCondition` | `rcpp:requiredForClass` | `rcpp:QuantityCalculationItem` |
| 255 | `rcpp:QuantityCalculationItemCodeCondition` | `rcpp:requiredProperty` | `rcpp:quantityCalculationCode` |
| 256 | `rcpp:QuantityCalculationItemCodeCondition` | `rcpp:requiredProperty` | `rcpp:quantityContractItemCode` |
| 257 | `rcpp:QuantityCalculationItemCodeCondition` | `rdf:type` | `rcpp:FieldRequirement` |
| 258 | `rcpp:QuantityCalculationItemRequiredFields` | `rcpp:requiredForClass` | `rcpp:QuantityCalculationItem` |
| 259 | `rcpp:QuantityCalculationItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:quantityCalculatedQuantity` |
| 260 | `rcpp:QuantityCalculationItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:quantityCalculationBasis` |
| 261 | `rcpp:QuantityCalculationItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:quantityFormula` |
| 262 | `rcpp:QuantityCalculationItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:quantityItemName` |
| 263 | `rcpp:QuantityCalculationItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:quantitySpecification` |
| 264 | `rcpp:QuantityCalculationItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:quantityUnit` |
| 265 | `rcpp:QuantityCalculationItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:quantityWorkType` |
| 266 | `rcpp:QuantityCalculationItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:usesUnit` |
| 267 | `rcpp:QuantityCalculationItemRequiredFields` | `rdf:type` | `rcpp:FieldRequirement` |
| 268 | `rcpp:QuantityCalculationSheet` | `rcpp:expectedDocumentRole` | `rcpp:QuantityBasisDocumentRole` |
| 269 | `rcpp:QuantityCalculationSheet` | `rcpp:expectedItemClass` | `rcpp:QuantityCalculationItem` |
| 270 | `rcpp:QuantityCalculationSheet` | `rcpp:schemaFlowsTo` | `rcpp:DocumentItemMatching` |
| 271 | `rcpp:QuantityCalculationSheet` | `rcpp:typicalNextDocumentClass` | `rcpp:ContractStatement` |
| 272 | `rcpp:QuantityCalculationSheet` | `rdfs:subClassOf` | `rcpp:SourceDocument` |
| 273 | `rcpp:ReadyMixedConcreteCostItem` | `rdfs:subClassOf` | `rcpp:ConcreteCostItem` |
| 274 | `rcpp:ReadyMixedConcreteSpecificationRule` | `rcpp:appliesToClass` | `rcpp:ReadyMixedConcreteCostItem` |
| 275 | `rcpp:ReadyMixedConcreteSpecificationRule` | `rdf:type` | `rcpp:SpecificationNormalizationRule` |
| 276 | `rcpp:RebarAssembly` | `rdf:type` | `rcpp:RebarWorkType` |
| 277 | `rcpp:RebarCostItem` | `rdfs:subClassOf` | `rcpp:CostItem` |
| 278 | `rcpp:RebarFabrication` | `rdf:type` | `rcpp:RebarWorkType` |
| 279 | `rcpp:RebarFabricationAndAssembly` | `rdf:type` | `rcpp:RebarWorkType` |
| 280 | `rcpp:RebarGrade` | `rdfs:subClassOf` | `rcpp:ControlledSpecificationValue` |
| 281 | `rcpp:RebarSpecificationRule` | `rcpp:appliesToClass` | `rcpp:RebarCostItem` |
| 282 | `rcpp:RebarSpecificationRule` | `rdf:type` | `rcpp:SpecificationNormalizationRule` |
| 283 | `rcpp:RebarWorkCategory` | `rcpp:parentWorkCategory` | `rcpp:ReinforcedConcreteWorkCategory` |
| 284 | `rcpp:RebarWorkCategory` | `rdf:type` | `rcpp:WorkCategory` |
| 285 | `rcpp:RebarWorkType` | `rdfs:subClassOf` | `rcpp:ControlledSpecificationValue` |
| 286 | `rcpp:ReinforcedConcreteWorkCategory` | `rdf:type` | `rcpp:WorkCategory` |
| 287 | `rcpp:RoundDown` | `rdf:type` | `rcpp:RoundingMode` |
| 288 | `rcpp:RoundHalfUp` | `rdf:type` | `rcpp:RoundingMode` |
| 289 | `rcpp:RoundUp` | `rdf:type` | `rcpp:RoundingMode` |
| 290 | `rcpp:SD400` | `rdf:type` | `rcpp:RebarGrade` |
| 291 | `rcpp:SD500` | `rdf:type` | `rcpp:RebarGrade` |
| 292 | `rcpp:SD600` | `rdf:type` | `rcpp:RebarGrade` |
| 293 | `rcpp:ShoringCostItem` | `rdfs:subClassOf` | `rcpp:CostItem` |
| 294 | `rcpp:ShoringSpecificationRule` | `rcpp:appliesToClass` | `rcpp:ShoringCostItem` |
| 295 | `rcpp:ShoringSpecificationRule` | `rdf:type` | `rcpp:SpecificationNormalizationRule` |
| 296 | `rcpp:ShoringType` | `rdfs:subClassOf` | `rcpp:ControlledSpecificationValue` |
| 297 | `rcpp:ShoringWorkCategory` | `rcpp:parentWorkCategory` | `rcpp:ReinforcedConcreteWorkCategory` |
| 298 | `rcpp:ShoringWorkCategory` | `rdf:type` | `rcpp:WorkCategory` |
| 299 | `rcpp:SimpleComplexity` | `rdf:type` | `rcpp:ComplexityLevel` |
| 300 | `rcpp:SourceDocument` | `rdfs:subClassOf` | `rcpp:ProgressDocument` |
| 301 | `rcpp:SquareMetreUnit` | `rcpp:baseUnit` | `rcpp:SquareMetreUnit` |
| 302 | `rcpp:SquareMetreUnit` | `rdf:type` | `rcpp:Unit` |
| 303 | `rcpp:StandardCurrentProgressAmountRule` | `rdf:type` | `rcpp:CurrentProgressAmountCalculation` |
| 304 | `rcpp:StandardProgressQuantityRollupRule` | `rdf:type` | `rcpp:ProgressQuantityRollupCalculation` |
| 305 | `rcpp:StandardProgressSummaryRule` | `rdf:type` | `rcpp:ProgressSummaryCalculation` |
| 306 | `rcpp:SteelPipeShoring` | `rdf:type` | `rcpp:ShoringType` |
| 307 | `rcpp:SummaryCostItem` | `rdfs:subClassOf` | `rcpp:DocumentItem` |
| 308 | `rcpp:SupportingReferenceDocument` | `rcpp:expectedDocumentRole` | `rcpp:SupportingReferenceDocumentRole` |
| 309 | `rcpp:SupportingReferenceDocument` | `rcpp:expectedItemClass` | `rcpp:SupportingReferenceItem` |
| 310 | `rcpp:SupportingReferenceDocument` | `rcpp:schemaFlowsTo` | `rcpp:DocumentItemMatching` |
| 311 | `rcpp:SupportingReferenceDocument` | `rdfs:subClassOf` | `rcpp:SourceDocument` |
| 312 | `rcpp:SupportingReferenceDocumentRole` | `rdf:type` | `rcpp:DocumentRole` |
| 313 | `rcpp:SupportingReferenceItem` | `rdfs:subClassOf` | `rcpp:DocumentItem` |
| 314 | `rcpp:SystemShoring` | `rdf:type` | `rcpp:ShoringType` |
| 315 | `rcpp:TonneUnit` | `rcpp:baseUnit` | `rcpp:KilogramUnit` |
| 316 | `rcpp:TonneUnit` | `rdf:type` | `rcpp:Unit` |
| 317 | `rcpp:UnitConversionRule` | `rdfs:subClassOf` | `rcpp:CalculationRule` |
| 318 | `rcpp:UnitPriceAnalysisStatement` | `rdfs:subClassOf` | `rcpp:SupportingReferenceDocument` |
| 319 | `rcpp:WaterInstallationEnvironment` | `rdf:type` | `rcpp:InstallationEnvironment` |
| 320 | `rcpp:WorkTypeDetailItem` | `rcpp:expectedAggregationTargetClass` | `rcpp:WorkTypeSummaryItem` |
| 321 | `rcpp:WorkTypeDetailItem` | `rcpp:expectedCorrespondingItemClass` | `rcpp:ContractStatementItem` |
| 322 | `rcpp:WorkTypeDetailItem` | `rcpp:expectedCostItemClass` | `rcpp:CostItem` |
| 323 | `rcpp:WorkTypeDetailItem` | `rcpp:expectedSourceItemClass` | `rcpp:ContractStatementItem` |
| 324 | `rcpp:WorkTypeDetailItem` | `rdfs:subClassOf` | `rcpp:DetailCostItem` |
| 325 | `rcpp:WorkTypeDetailItemCodeCondition` | `rcpp:requiredForClass` | `rcpp:WorkTypeDetailItem` |
| 326 | `rcpp:WorkTypeDetailItemCodeCondition` | `rcpp:requiredProperty` | `rcpp:workDetailItemCode` |
| 327 | `rcpp:WorkTypeDetailItemCodeCondition` | `rdf:type` | `rcpp:FieldRequirement` |
| 328 | `rcpp:WorkTypeDetailItemRequiredFields` | `rcpp:requiredForClass` | `rcpp:WorkTypeDetailItem` |
| 329 | `rcpp:WorkTypeDetailItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:usesUnit` |
| 330 | `rcpp:WorkTypeDetailItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:workDetailAmount` |
| 331 | `rcpp:WorkTypeDetailItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:workDetailItemName` |
| 332 | `rcpp:WorkTypeDetailItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:workDetailQuantity` |
| 333 | `rcpp:WorkTypeDetailItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:workDetailSpecification` |
| 334 | `rcpp:WorkTypeDetailItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:workDetailUnit` |
| 335 | `rcpp:WorkTypeDetailItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:workDetailUnitPrice` |
| 336 | `rcpp:WorkTypeDetailItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:workDetailWorkType` |
| 337 | `rcpp:WorkTypeDetailItemRequiredFields` | `rdf:type` | `rcpp:FieldRequirement` |
| 338 | `rcpp:WorkTypeDetailStatement` | `rcpp:expectedDocumentRole` | `rcpp:DetailedCostDocumentRole` |
| 339 | `rcpp:WorkTypeDetailStatement` | `rcpp:expectedItemClass` | `rcpp:WorkTypeDetailItem` |
| 340 | `rcpp:WorkTypeDetailStatement` | `rcpp:typicalNextDocumentClass` | `rcpp:WorkTypeSummaryStatement` |
| 341 | `rcpp:WorkTypeDetailStatement` | `rdfs:subClassOf` | `rcpp:SourceDocument` |
| 342 | `rcpp:WorkTypeSummaryItem` | `rcpp:expectedSourceItemClass` | `rcpp:WorkTypeDetailItem` |
| 343 | `rcpp:WorkTypeSummaryItem` | `rdfs:subClassOf` | `rcpp:SummaryCostItem` |
| 344 | `rcpp:WorkTypeSummaryItemRequiredFields` | `rcpp:requiredForClass` | `rcpp:WorkTypeSummaryItem` |
| 345 | `rcpp:WorkTypeSummaryItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:summaryContractAmount` |
| 346 | `rcpp:WorkTypeSummaryItemRequiredFields` | `rcpp:requiredProperty` | `rcpp:summaryWorkType` |
| 347 | `rcpp:WorkTypeSummaryItemRequiredFields` | `rdf:type` | `rcpp:FieldRequirement` |
| 348 | `rcpp:WorkTypeSummaryStatement` | `rcpp:expectedDocumentRole` | `rcpp:CostSummaryDocumentRole` |
| 349 | `rcpp:WorkTypeSummaryStatement` | `rcpp:expectedItemClass` | `rcpp:WorkTypeSummaryItem` |
| 350 | `rcpp:WorkTypeSummaryStatement` | `rcpp:typicalNextDocumentClass` | `rcpp:CurrentProgressStatement` |
| 351 | `rcpp:WorkTypeSummaryStatement` | `rdfs:subClassOf` | `rcpp:SourceDocument` |
| 352 | `rcpp:aggregatedInto` | `rdfs:domain` | `rcpp:DetailCostItem` |
| 353 | `rcpp:aggregatedInto` | `rdfs:range` | `rcpp:SummaryCostItem` |
| 354 | `rcpp:amountTolerance` | `rdfs:domain` | `rcpp:CalculationPolicy` |
| 355 | `rcpp:applicationCondition` | `rcpp:appliesToClass` | `rcpp:CalculationRule` |
| 356 | `rcpp:applicationCondition` | `rcpp:appliesToClass` | `rcpp:SpecificationNormalizationRule` |
| 357 | `rcpp:applicationPart` | `rcpp:appliesToClass` | `rcpp:ConcretePlacementCostItem` |
| 358 | `rcpp:applicationPart` | `rcpp:appliesToClass` | `rcpp:FormworkCostItem` |
| 359 | `rcpp:applicationPart` | `rcpp:appliesToClass` | `rcpp:ShoringCostItem` |
| 360 | `rcpp:appliesPolicy` | `rdfs:domain` | `rcpp:CalculationActivity` |
| 361 | `rcpp:appliesPolicy` | `rdfs:range` | `rcpp:CalculationPolicy` |
| 362 | `rcpp:appliesRule` | `rdfs:domain` | `rcpp:CalculationActivity` |
| 363 | `rcpp:appliesRule` | `rdfs:range` | `rcpp:CalculationRule` |
| 364 | `rcpp:baseUnit` | `rdfs:domain` | `rcpp:Unit` |
| 365 | `rcpp:baseUnit` | `rdfs:range` | `rcpp:Unit` |
| 366 | `rcpp:belongsToProgressRound` | `rdfs:domain` | `rcpp:ProgressDocument` |
| 367 | `rcpp:belongsToProgressRound` | `rdfs:range` | `rcpp:ProgressPaymentRound` |
| 368 | `rcpp:belongsToProject` | `rcpp:appliesToClass` | `rcpp:ProgressDocument` |
| 369 | `rcpp:belongsToProject` | `rcpp:appliesToClass` | `rcpp:ProgressPaymentRound` |
| 370 | `rcpp:belongsToProject` | `rdfs:range` | `rcpp:Project` |
| 371 | `rcpp:belongsToWorkCategory` | `rcpp:appliesToClass` | `rcpp:CostItem` |
| 372 | `rcpp:belongsToWorkCategory` | `rcpp:appliesToClass` | `rcpp:DocumentItem` |
| 373 | `rcpp:belongsToWorkCategory` | `rdfs:range` | `rcpp:WorkCategory` |
| 374 | `rcpp:calculationInputItem` | `rdfs:domain` | `rcpp:CalculationActivity` |
| 375 | `rcpp:calculationInputItem` | `rdfs:range` | `rcpp:DocumentItem` |
| 376 | `rcpp:calculationOrder` | `rdfs:domain` | `rcpp:CalculationPolicy` |
| 377 | `rcpp:calculationOutputItem` | `rdfs:domain` | `rcpp:CalculationActivity` |
| 378 | `rcpp:calculationOutputItem` | `rdfs:range` | `rcpp:DocumentItem` |
| 379 | `rcpp:calculationRound` | `rdfs:domain` | `rcpp:CalculationActivity` |
| 380 | `rcpp:calculationRound` | `rdfs:range` | `rcpp:ProgressPaymentRound` |
| 381 | `rcpp:calculationStatus` | `rdfs:domain` | `rcpp:CalculationActivity` |
| 382 | `rcpp:cementType` | `rdfs:domain` | `rcpp:ReadyMixedConcreteCostItem` |
| 383 | `rcpp:codeValue` | `rcpp:appliesToClass` | `rcpp:ControlledSpecificationValue` |
| 384 | `rcpp:codeValue` | `rcpp:appliesToClass` | `rcpp:Currency` |
| 385 | `rcpp:codeValue` | `rcpp:appliesToClass` | `rcpp:RoundingMode` |
| 386 | `rcpp:complexityLevel` | `rdfs:domain` | `rcpp:FormworkCostItem` |
| 387 | `rcpp:complexityLevel` | `rdfs:range` | `rcpp:ComplexityLevel` |
| 388 | `rcpp:componentDelimiter` | `rdfs:domain` | `rcpp:SpecificationNormalizationRule` |
| 389 | `rcpp:componentOrder` | `rdfs:domain` | `rcpp:SpecificationNormalizationRule` |
| 390 | `rcpp:concreteType` | `rdfs:domain` | `rcpp:ReadyMixedConcreteCostItem` |
| 391 | `rcpp:confidenceScore` | `rdfs:domain` | `rcpp:DocumentItemMatching` |
| 392 | `rcpp:containsItem` | `rdfs:domain` | `rcpp:ProgressDocument` |
| 393 | `rcpp:containsItem` | `rdfs:range` | `rcpp:DocumentItem` |
| 394 | `rcpp:contractAmount` | `rcpp:consistencyComparedWith` | `rcpp:outputContractAmount` |
| 395 | `rcpp:contractAmount` | `rcpp:fieldOfDocument` | `rcpp:ContractStatement` |
| 396 | `rcpp:contractAmount` | `rcpp:mapsDirectlyTo` | `rcpp:outputContractAmount` |
| 397 | `rcpp:contractAmount` | `rcpp:mapsDirectlyTo` | `rcpp:workDetailAmount` |
| 398 | `rcpp:contractAmount` | `rdfs:domain` | `rcpp:ContractStatementItem` |
| 399 | `rcpp:contractAmount` | `rdfs:subPropertyOf` | `rcpp:hasAmountValue` |
| 400 | `rcpp:contractItemCode` | `rcpp:fieldOfDocument` | `rcpp:ContractStatement` |
| 401 | `rcpp:contractItemCode` | `rcpp:mapsDirectlyTo` | `rcpp:outputItemCode` |
| 402 | `rcpp:contractItemCode` | `rcpp:mapsDirectlyTo` | `rcpp:workDetailItemCode` |
| 403 | `rcpp:contractItemCode` | `rdfs:domain` | `rcpp:ContractStatementItem` |
| 404 | `rcpp:contractItemCode` | `rdfs:subPropertyOf` | `rcpp:hasItemCode` |
| 405 | `rcpp:contractItemName` | `rcpp:fieldOfDocument` | `rcpp:ContractStatement` |
| 406 | `rcpp:contractItemName` | `rcpp:mapsDirectlyTo` | `rcpp:outputWorkDescription` |
| 407 | `rcpp:contractItemName` | `rcpp:mapsDirectlyTo` | `rcpp:workDetailItemName` |
| 408 | `rcpp:contractItemName` | `rdfs:domain` | `rcpp:ContractStatementItem` |
| 409 | `rcpp:contractItemName` | `rdfs:subPropertyOf` | `rcpp:hasItemName` |
| 410 | `rcpp:contractQuantity` | `rcpp:calculationInputFor` | `rcpp:contractAmount` |
| 411 | `rcpp:contractQuantity` | `rcpp:calculationInputFor` | `rcpp:progressRemainingQuantity` |
| 412 | `rcpp:contractQuantity` | `rcpp:consistencyComparedWith` | `rcpp:outputCumulativeQuantity` |
| 413 | `rcpp:contractQuantity` | `rcpp:fieldOfDocument` | `rcpp:ContractStatement` |
| 414 | `rcpp:contractQuantity` | `rcpp:mapsDirectlyTo` | `rcpp:outputContractQuantity` |
| 415 | `rcpp:contractQuantity` | `rcpp:mapsDirectlyTo` | `rcpp:workDetailQuantity` |
| 416 | `rcpp:contractQuantity` | `rdfs:domain` | `rcpp:ContractStatementItem` |
| 417 | `rcpp:contractQuantity` | `rdfs:subPropertyOf` | `rcpp:hasQuantityValue` |
| 418 | `rcpp:contractQuantityBasis` | `rcpp:fieldOfDocument` | `rcpp:ContractStatement` |
| 419 | `rcpp:contractQuantityBasis` | `rdfs:domain` | `rcpp:ContractStatementItem` |
| 420 | `rcpp:contractSpecification` | `rcpp:fieldOfDocument` | `rcpp:ContractStatement` |
| 421 | `rcpp:contractSpecification` | `rcpp:mapsDirectlyTo` | `rcpp:outputSpecification` |
| 422 | `rcpp:contractSpecification` | `rcpp:mapsDirectlyTo` | `rcpp:workDetailSpecification` |
| 423 | `rcpp:contractSpecification` | `rdfs:domain` | `rcpp:ContractStatementItem` |
| 424 | `rcpp:contractSpecification` | `rdfs:subPropertyOf` | `rcpp:hasSpecificationText` |
| 425 | `rcpp:contractUnit` | `rcpp:consistencyComparedWith` | `rcpp:outputUnit` |
| 426 | `rcpp:contractUnit` | `rcpp:consistencyComparedWith` | `rcpp:quantityUnit` |
| 427 | `rcpp:contractUnit` | `rcpp:fieldOfDocument` | `rcpp:ContractStatement` |
| 428 | `rcpp:contractUnit` | `rcpp:mapsDirectlyTo` | `rcpp:outputUnit` |
| 429 | `rcpp:contractUnit` | `rcpp:mapsDirectlyTo` | `rcpp:workDetailUnit` |
| 430 | `rcpp:contractUnit` | `rdfs:domain` | `rcpp:ContractStatementItem` |
| 431 | `rcpp:contractUnit` | `rdfs:subPropertyOf` | `rcpp:hasSourceUnitText` |
| 432 | `rcpp:contractUnitPrice` | `rcpp:calculationInputFor` | `rcpp:contractAmount` |
| 433 | `rcpp:contractUnitPrice` | `rcpp:fieldOfDocument` | `rcpp:ContractStatement` |
| 434 | `rcpp:contractUnitPrice` | `rcpp:inputToCalculationClass` | `rcpp:CurrentProgressAmountCalculation` |
| 435 | `rcpp:contractUnitPrice` | `rcpp:mapsDirectlyTo` | `rcpp:outputContractUnitPrice` |
| 436 | `rcpp:contractUnitPrice` | `rcpp:mapsDirectlyTo` | `rcpp:workDetailUnitPrice` |
| 437 | `rcpp:contractUnitPrice` | `rdfs:domain` | `rcpp:ContractStatementItem` |
| 438 | `rcpp:contractUnitPrice` | `rdfs:subPropertyOf` | `rcpp:hasUnitPriceValue` |
| 439 | `rcpp:contractWorkType` | `rcpp:fieldOfDocument` | `rcpp:ContractStatement` |
| 440 | `rcpp:contractWorkType` | `rcpp:mapsDirectlyTo` | `rcpp:outputWorkType` |
| 441 | `rcpp:contractWorkType` | `rcpp:mapsDirectlyTo` | `rcpp:workDetailWorkType` |
| 442 | `rcpp:contractWorkType` | `rdfs:domain` | `rcpp:ContractStatementItem` |
| 443 | `rcpp:contractWorkType` | `rdfs:subPropertyOf` | `rcpp:hasSourceWorkCategoryText` |
| 444 | `rcpp:conversionFactorToBaseUnit` | `rdfs:domain` | `rcpp:Unit` |
| 445 | `rcpp:correspondsToItem` | `rdfs:domain` | `rcpp:DocumentItem` |
| 446 | `rcpp:correspondsToItem` | `rdfs:range` | `rcpp:DocumentItem` |
| 447 | `rcpp:costItemCode` | `rdfs:domain` | `rcpp:CostItem` |
| 448 | `rcpp:costItemName` | `rdfs:domain` | `rcpp:CostItem` |
| 449 | `rcpp:currency` | `rdfs:domain` | `rcpp:CalculationPolicy` |
| 450 | `rcpp:currency` | `rdfs:range` | `rcpp:Currency` |
| 451 | `rcpp:decimalScale` | `rdfs:domain` | `rcpp:CalculationPolicy` |
| 452 | `rcpp:derivedFrom` | `rdfs:domain` | `rcpp:DocumentItem` |
| 453 | `rcpp:derivedFrom` | `rdfs:range` | `rcpp:DocumentItem` |
| 454 | `rcpp:detailCurrentQuantity` | `rcpp:aggregatesTo` | `rcpp:progressCurrentQuantity` |
| 455 | `rcpp:detailCurrentQuantity` | `rdfs:domain` | `rcpp:ProgressQuantityDetailItem` |
| 456 | `rcpp:detailLocationText` | `rdfs:domain` | `rcpp:ProgressQuantityDetailItem` |
| 457 | `rcpp:diameterCategory` | `rdfs:domain` | `rcpp:RebarCostItem` |
| 458 | `rcpp:documentIdentifier` | `rdfs:domain` | `rcpp:ProgressDocument` |
| 459 | `rcpp:documentName` | `rdfs:domain` | `rcpp:ProgressDocument` |
| 460 | `rcpp:documentReferenceDate` | `rdfs:domain` | `rcpp:ProgressDocument` |
| 461 | `rcpp:documentRevision` | `rdfs:domain` | `rcpp:ProgressDocument` |
| 462 | `rcpp:expectedDocumentRole` | `rdfs:range` | `rcpp:DocumentRole` |
| 463 | `rcpp:extractionMethod` | `rdfs:domain` | `rcpp:SourceLocation` |
| 464 | `rcpp:fabricationMethod` | `rdfs:domain` | `rcpp:RebarCostItem` |
| 465 | `rcpp:formworkType` | `rdfs:domain` | `rcpp:FormworkCostItem` |
| 466 | `rcpp:formworkType` | `rdfs:range` | `rcpp:FormworkType` |
| 467 | `rcpp:formworkWorkType` | `rdfs:domain` | `rcpp:FormworkCostItem` |
| 468 | `rcpp:hasAmountValue` | `rdfs:domain` | `rcpp:DocumentItem` |
| 469 | `rcpp:hasDocumentRole` | `rdfs:domain` | `rcpp:ProgressDocument` |
| 470 | `rcpp:hasDocumentRole` | `rdfs:range` | `rcpp:DocumentRole` |
| 471 | `rcpp:hasItemCode` | `rdfs:domain` | `rcpp:DocumentItem` |
| 472 | `rcpp:hasItemName` | `rdfs:domain` | `rcpp:DocumentItem` |
| 473 | `rcpp:hasQuantityValue` | `rdfs:domain` | `rcpp:DocumentItem` |
| 474 | `rcpp:hasSourceLocation` | `rcpp:appliesToClass` | `rcpp:DocumentItem` |
| 475 | `rcpp:hasSourceLocation` | `rcpp:appliesToClass` | `rcpp:ProgressDocument` |
| 476 | `rcpp:hasSourceLocation` | `rdfs:range` | `rcpp:SourceLocation` |
| 477 | `rcpp:hasSourceUnitText` | `rdfs:domain` | `rcpp:DocumentItem` |
| 478 | `rcpp:hasSourceWorkCategoryText` | `rdfs:domain` | `rcpp:DocumentItem` |
| 479 | `rcpp:hasSpecificationText` | `rdfs:domain` | `rcpp:DocumentItem` |
| 480 | `rcpp:hasUnitPriceValue` | `rdfs:domain` | `rcpp:DocumentItem` |
| 481 | `rcpp:identificationReferencedFrom` | `rdfs:domain` | `rcpp:DocumentItem` |
| 482 | `rcpp:identificationReferencedFrom` | `rdfs:range` | `rcpp:DocumentItem` |
| 483 | `rcpp:installationEnvironment` | `rdfs:domain` | `rcpp:ShoringCostItem` |
| 484 | `rcpp:installationEnvironment` | `rdfs:range` | `rcpp:InstallationEnvironment` |
| 485 | `rcpp:isExposedFinish` | `rdfs:domain` | `rcpp:FormworkCostItem` |
| 486 | `rcpp:isFirstProgressRound` | `rdfs:domain` | `rcpp:ProgressPaymentRound` |
| 487 | `rcpp:matchedCostItem` | `rdfs:domain` | `rcpp:DocumentItemMatching` |
| 488 | `rcpp:matchedCostItem` | `rdfs:range` | `rcpp:CostItem` |
| 489 | `rcpp:matchingEvidence` | `rdfs:domain` | `rcpp:DocumentItemMatching` |
| 490 | `rcpp:matchingMethod` | `rdfs:domain` | `rcpp:DocumentItemMatching` |
| 491 | `rcpp:maximumAggregateSize` | `rdfs:domain` | `rcpp:ReadyMixedConcreteCostItem` |
| 492 | `rcpp:maximumDiameter` | `rdfs:domain` | `rcpp:RebarCostItem` |
| 493 | `rcpp:maximumQuantityThreshold` | `rdfs:domain` | `rcpp:ConcretePlacementCostItem` |
| 494 | `rcpp:maximumVerticalHeight` | `rcpp:appliesToClass` | `rcpp:FormworkCostItem` |
| 495 | `rcpp:maximumVerticalHeight` | `rcpp:appliesToClass` | `rcpp:ShoringCostItem` |
| 496 | `rcpp:minimumDiameter` | `rdfs:domain` | `rcpp:RebarCostItem` |
| 497 | `rcpp:minimumQuantityThreshold` | `rdfs:domain` | `rcpp:ConcretePlacementCostItem` |
| 498 | `rcpp:minimumVerticalHeight` | `rcpp:appliesToClass` | `rcpp:FormworkCostItem` |
| 499 | `rcpp:minimumVerticalHeight` | `rcpp:appliesToClass` | `rcpp:ShoringCostItem` |
| 500 | `rcpp:missingValueTreatment` | `rdfs:domain` | `rcpp:SpecificationNormalizationRule` |
| 501 | `rcpp:nominalDiameter` | `rdfs:domain` | `rcpp:RebarCostItem` |
| 502 | `rcpp:nominalStrength` | `rdfs:domain` | `rcpp:ReadyMixedConcreteCostItem` |
| 503 | `rcpp:normalizedSpecificationCode` | `rdfs:domain` | `rcpp:CostItem` |
| 504 | `rcpp:outputContractAmount` | `rcpp:aggregatesTo` | `rcpp:outputSummaryContractAmount` |
| 505 | `rcpp:outputContractAmount` | `rcpp:calculationInputFor` | `rcpp:outputCumulativeRate` |
| 506 | `rcpp:outputContractAmount` | `rcpp:calculationInputFor` | `rcpp:outputCurrentRate` |
| 507 | `rcpp:outputContractAmount` | `rcpp:calculationInputFor` | `rcpp:outputPreviousRate` |
| 508 | `rcpp:outputContractAmount` | `rcpp:calculationInputFor` | `rcpp:outputRemainingAmount` |
| 509 | `rcpp:outputContractAmount` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 510 | `rcpp:outputContractAmount` | `rdfs:domain` | `rcpp:CurrentProgressDetailItem` |
| 511 | `rcpp:outputContractAmount` | `rdfs:subPropertyOf` | `rcpp:hasAmountValue` |
| 512 | `rcpp:outputContractQuantity` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 513 | `rcpp:outputContractQuantity` | `rdfs:domain` | `rcpp:CurrentProgressDetailItem` |
| 514 | `rcpp:outputContractQuantity` | `rdfs:subPropertyOf` | `rcpp:hasQuantityValue` |
| 515 | `rcpp:outputContractUnitPrice` | `rcpp:calculationInputFor` | `rcpp:outputCurrentAmount` |
| 516 | `rcpp:outputContractUnitPrice` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 517 | `rcpp:outputContractUnitPrice` | `rdfs:domain` | `rcpp:CurrentProgressDetailItem` |
| 518 | `rcpp:outputContractUnitPrice` | `rdfs:subPropertyOf` | `rcpp:hasUnitPriceValue` |
| 519 | `rcpp:outputCumulativeAmount` | `rcpp:aggregatesTo` | `rcpp:outputSummaryCumulativeAmount` |
| 520 | `rcpp:outputCumulativeAmount` | `rcpp:calculationInputFor` | `rcpp:outputCumulativeRate` |
| 521 | `rcpp:outputCumulativeAmount` | `rcpp:calculationInputFor` | `rcpp:outputRemainingAmount` |
| 522 | `rcpp:outputCumulativeAmount` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 523 | `rcpp:outputCumulativeAmount` | `rdfs:domain` | `rcpp:CurrentProgressDetailItem` |
| 524 | `rcpp:outputCumulativeAmount` | `rdfs:subPropertyOf` | `rcpp:hasAmountValue` |
| 525 | `rcpp:outputCumulativeQuantity` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 526 | `rcpp:outputCumulativeQuantity` | `rdfs:domain` | `rcpp:CurrentProgressDetailItem` |
| 527 | `rcpp:outputCumulativeQuantity` | `rdfs:subPropertyOf` | `rcpp:hasQuantityValue` |
| 528 | `rcpp:outputCumulativeRate` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 529 | `rcpp:outputCumulativeRate` | `rdfs:domain` | `rcpp:CurrentProgressDetailItem` |
| 530 | `rcpp:outputCurrentAmount` | `rcpp:aggregatesTo` | `rcpp:outputSummaryCurrentAmount` |
| 531 | `rcpp:outputCurrentAmount` | `rcpp:calculationInputFor` | `rcpp:outputCumulativeAmount` |
| 532 | `rcpp:outputCurrentAmount` | `rcpp:calculationInputFor` | `rcpp:outputCurrentRate` |
| 533 | `rcpp:outputCurrentAmount` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 534 | `rcpp:outputCurrentAmount` | `rdfs:domain` | `rcpp:CurrentProgressDetailItem` |
| 535 | `rcpp:outputCurrentAmount` | `rdfs:subPropertyOf` | `rcpp:hasAmountValue` |
| 536 | `rcpp:outputCurrentQuantity` | `rcpp:calculationInputFor` | `rcpp:outputCurrentAmount` |
| 537 | `rcpp:outputCurrentQuantity` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 538 | `rcpp:outputCurrentQuantity` | `rdfs:domain` | `rcpp:CurrentProgressDetailItem` |
| 539 | `rcpp:outputCurrentQuantity` | `rdfs:subPropertyOf` | `rcpp:hasQuantityValue` |
| 540 | `rcpp:outputCurrentRate` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 541 | `rcpp:outputCurrentRate` | `rdfs:domain` | `rcpp:CurrentProgressDetailItem` |
| 542 | `rcpp:outputItemCode` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 543 | `rcpp:outputItemCode` | `rdfs:domain` | `rcpp:CurrentProgressDetailItem` |
| 544 | `rcpp:outputItemCode` | `rdfs:subPropertyOf` | `rcpp:hasItemCode` |
| 545 | `rcpp:outputPreviousAmount` | `rcpp:aggregatesTo` | `rcpp:outputSummaryPreviousAmount` |
| 546 | `rcpp:outputPreviousAmount` | `rcpp:calculationInputFor` | `rcpp:outputCumulativeAmount` |
| 547 | `rcpp:outputPreviousAmount` | `rcpp:calculationInputFor` | `rcpp:outputPreviousRate` |
| 548 | `rcpp:outputPreviousAmount` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 549 | `rcpp:outputPreviousAmount` | `rdfs:domain` | `rcpp:CurrentProgressDetailItem` |
| 550 | `rcpp:outputPreviousAmount` | `rdfs:subPropertyOf` | `rcpp:hasAmountValue` |
| 551 | `rcpp:outputPreviousQuantity` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 552 | `rcpp:outputPreviousQuantity` | `rdfs:domain` | `rcpp:CurrentProgressDetailItem` |
| 553 | `rcpp:outputPreviousQuantity` | `rdfs:subPropertyOf` | `rcpp:hasQuantityValue` |
| 554 | `rcpp:outputPreviousRate` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 555 | `rcpp:outputPreviousRate` | `rdfs:domain` | `rcpp:CurrentProgressDetailItem` |
| 556 | `rcpp:outputReinforcedConcreteAmount` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 557 | `rcpp:outputReinforcedConcreteAmount` | `rdfs:domain` | `rcpp:CurrentProgressSummaryItem` |
| 558 | `rcpp:outputReinforcedConcreteAmount` | `rdfs:subPropertyOf` | `rcpp:hasAmountValue` |
| 559 | `rcpp:outputRemainingAmount` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 560 | `rcpp:outputRemainingAmount` | `rdfs:domain` | `rcpp:CurrentProgressDetailItem` |
| 561 | `rcpp:outputRemainingAmount` | `rdfs:subPropertyOf` | `rcpp:hasAmountValue` |
| 562 | `rcpp:outputRemainingQuantity` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 563 | `rcpp:outputRemainingQuantity` | `rdfs:domain` | `rcpp:CurrentProgressDetailItem` |
| 564 | `rcpp:outputRemainingQuantity` | `rdfs:subPropertyOf` | `rcpp:hasQuantityValue` |
| 565 | `rcpp:outputRemarks` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 566 | `rcpp:outputRemarks` | `rdfs:domain` | `rcpp:CurrentProgressDetailItem` |
| 567 | `rcpp:outputSpecification` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 568 | `rcpp:outputSpecification` | `rdfs:domain` | `rcpp:CurrentProgressDetailItem` |
| 569 | `rcpp:outputSpecification` | `rdfs:subPropertyOf` | `rcpp:hasSpecificationText` |
| 570 | `rcpp:outputSummaryContractAmount` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 571 | `rcpp:outputSummaryContractAmount` | `rdfs:domain` | `rcpp:CurrentProgressSummaryItem` |
| 572 | `rcpp:outputSummaryContractAmount` | `rdfs:subPropertyOf` | `rcpp:hasAmountValue` |
| 573 | `rcpp:outputSummaryCumulativeAmount` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 574 | `rcpp:outputSummaryCumulativeAmount` | `rdfs:domain` | `rcpp:CurrentProgressSummaryItem` |
| 575 | `rcpp:outputSummaryCumulativeAmount` | `rdfs:subPropertyOf` | `rcpp:hasAmountValue` |
| 576 | `rcpp:outputSummaryCurrentAmount` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 577 | `rcpp:outputSummaryCurrentAmount` | `rdfs:domain` | `rcpp:CurrentProgressSummaryItem` |
| 578 | `rcpp:outputSummaryCurrentAmount` | `rdfs:subPropertyOf` | `rcpp:hasAmountValue` |
| 579 | `rcpp:outputSummaryPreviousAmount` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 580 | `rcpp:outputSummaryPreviousAmount` | `rdfs:domain` | `rcpp:CurrentProgressSummaryItem` |
| 581 | `rcpp:outputSummaryPreviousAmount` | `rdfs:subPropertyOf` | `rcpp:hasAmountValue` |
| 582 | `rcpp:outputSummaryWorkCategoryText` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 583 | `rcpp:outputSummaryWorkCategoryText` | `rdfs:domain` | `rcpp:CurrentProgressSummaryItem` |
| 584 | `rcpp:outputSummaryWorkCategoryText` | `rdfs:subPropertyOf` | `rcpp:hasSourceWorkCategoryText` |
| 585 | `rcpp:outputUnit` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 586 | `rcpp:outputUnit` | `rdfs:domain` | `rcpp:CurrentProgressDetailItem` |
| 587 | `rcpp:outputUnit` | `rdfs:subPropertyOf` | `rcpp:hasSourceUnitText` |
| 588 | `rcpp:outputWorkDescription` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 589 | `rcpp:outputWorkDescription` | `rdfs:domain` | `rcpp:CurrentProgressDetailItem` |
| 590 | `rcpp:outputWorkDescription` | `rdfs:subPropertyOf` | `rcpp:hasItemName` |
| 591 | `rcpp:outputWorkType` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressStatement` |
| 592 | `rcpp:outputWorkType` | `rcpp:groupsByField` | `rcpp:outputSummaryWorkCategoryText` |
| 593 | `rcpp:outputWorkType` | `rdfs:domain` | `rcpp:CurrentProgressDetailItem` |
| 594 | `rcpp:outputWorkType` | `rdfs:subPropertyOf` | `rcpp:hasSourceWorkCategoryText` |
| 595 | `rcpp:parentWorkCategory` | `rdfs:domain` | `rcpp:WorkCategory` |
| 596 | `rcpp:parentWorkCategory` | `rdfs:range` | `rcpp:WorkCategory` |
| 597 | `rcpp:placementCondition` | `rdfs:domain` | `rcpp:ConcretePlacementCostItem` |
| 598 | `rcpp:placementMethod` | `rdfs:domain` | `rcpp:ConcretePlacementCostItem` |
| 599 | `rcpp:placementMethod` | `rdfs:range` | `rcpp:PlacementMethod` |
| 600 | `rcpp:precedesDocument` | `rdfs:domain` | `rcpp:ProgressDocument` |
| 601 | `rcpp:precedesDocument` | `rdfs:range` | `rcpp:ProgressDocument` |
| 602 | `rcpp:previousCumulativeAmount` | `rcpp:consistencyComparedWith` | `rcpp:outputPreviousAmount` |
| 603 | `rcpp:previousCumulativeAmount` | `rcpp:fieldOfDocument` | `rcpp:PreviousProgressStatement` |
| 604 | `rcpp:previousCumulativeAmount` | `rcpp:mapsDirectlyTo` | `rcpp:outputPreviousAmount` |
| 605 | `rcpp:previousCumulativeAmount` | `rdfs:domain` | `rcpp:PreviousProgressStatementItem` |
| 606 | `rcpp:previousCumulativeAmount` | `rdfs:subPropertyOf` | `rcpp:hasAmountValue` |
| 607 | `rcpp:previousCumulativeQuantity` | `rcpp:fieldOfDocument` | `rcpp:PreviousProgressStatement` |
| 608 | `rcpp:previousCumulativeQuantity` | `rcpp:mapsDirectlyTo` | `rcpp:outputPreviousQuantity` |
| 609 | `rcpp:previousCumulativeQuantity` | `rcpp:mapsDirectlyTo` | `rcpp:progressPreviousCumulativeQuantity` |
| 610 | `rcpp:previousCumulativeQuantity` | `rdfs:domain` | `rcpp:PreviousProgressStatementItem` |
| 611 | `rcpp:previousCumulativeQuantity` | `rdfs:subPropertyOf` | `rcpp:hasQuantityValue` |
| 612 | `rcpp:previousCumulativeRate` | `rcpp:consistencyComparedWith` | `rcpp:outputPreviousRate` |
| 613 | `rcpp:previousCumulativeRate` | `rcpp:fieldOfDocument` | `rcpp:PreviousProgressStatement` |
| 614 | `rcpp:previousCumulativeRate` | `rcpp:mapsDirectlyTo` | `rcpp:outputPreviousRate` |
| 615 | `rcpp:previousCumulativeRate` | `rdfs:domain` | `rcpp:PreviousProgressStatementItem` |
| 616 | `rcpp:previousItemCode` | `rcpp:consistencyComparedWith` | `rcpp:outputItemCode` |
| 617 | `rcpp:previousItemCode` | `rcpp:consistencyComparedWith` | `rcpp:progressQuantityItemCode` |
| 618 | `rcpp:previousItemCode` | `rcpp:fieldOfDocument` | `rcpp:PreviousProgressStatement` |
| 619 | `rcpp:previousItemCode` | `rcpp:matchesWithField` | `rcpp:contractItemCode` |
| 620 | `rcpp:previousItemCode` | `rdfs:domain` | `rcpp:PreviousProgressStatementItem` |
| 621 | `rcpp:previousItemCode` | `rdfs:subPropertyOf` | `rcpp:hasItemCode` |
| 622 | `rcpp:previousProgressRound` | `rdfs:domain` | `rcpp:ProgressPaymentRound` |
| 623 | `rcpp:previousProgressRound` | `rdfs:range` | `rcpp:ProgressPaymentRound` |
| 624 | `rcpp:previousQuantityFrom` | `rdfs:domain` | `rcpp:CurrentProgressQuantityItem` |
| 625 | `rcpp:previousQuantityFrom` | `rdfs:range` | `rcpp:PreviousProgressStatementItem` |
| 626 | `rcpp:previousSpecification` | `rcpp:consistencyComparedWith` | `rcpp:outputSpecification` |
| 627 | `rcpp:previousSpecification` | `rcpp:consistencyComparedWith` | `rcpp:progressQuantitySpecification` |
| 628 | `rcpp:previousSpecification` | `rcpp:fieldOfDocument` | `rcpp:PreviousProgressStatement` |
| 629 | `rcpp:previousSpecification` | `rcpp:matchesWithField` | `rcpp:contractSpecification` |
| 630 | `rcpp:previousSpecification` | `rdfs:domain` | `rcpp:PreviousProgressStatementItem` |
| 631 | `rcpp:previousSpecification` | `rdfs:subPropertyOf` | `rcpp:hasSpecificationText` |
| 632 | `rcpp:previousUnit` | `rcpp:consistencyComparedWith` | `rcpp:contractUnit` |
| 633 | `rcpp:previousUnit` | `rcpp:consistencyComparedWith` | `rcpp:outputUnit` |
| 634 | `rcpp:previousUnit` | `rcpp:consistencyComparedWith` | `rcpp:progressQuantityUnit` |
| 635 | `rcpp:previousUnit` | `rcpp:fieldOfDocument` | `rcpp:PreviousProgressStatement` |
| 636 | `rcpp:previousUnit` | `rcpp:matchesWithField` | `rcpp:contractUnit` |
| 637 | `rcpp:previousUnit` | `rdfs:domain` | `rcpp:PreviousProgressStatementItem` |
| 638 | `rcpp:previousUnit` | `rdfs:subPropertyOf` | `rcpp:hasSourceUnitText` |
| 639 | `rcpp:previousWorkDescription` | `rcpp:consistencyComparedWith` | `rcpp:outputWorkDescription` |
| 640 | `rcpp:previousWorkDescription` | `rcpp:consistencyComparedWith` | `rcpp:progressQuantityItemName` |
| 641 | `rcpp:previousWorkDescription` | `rcpp:fieldOfDocument` | `rcpp:PreviousProgressStatement` |
| 642 | `rcpp:previousWorkDescription` | `rcpp:matchesWithField` | `rcpp:contractItemName` |
| 643 | `rcpp:previousWorkDescription` | `rdfs:domain` | `rcpp:PreviousProgressStatementItem` |
| 644 | `rcpp:previousWorkDescription` | `rdfs:subPropertyOf` | `rcpp:hasItemName` |
| 645 | `rcpp:processingStage` | `rdfs:domain` | `rcpp:CalculationRule` |
| 646 | `rcpp:progressCumulativeQuantity` | `rcpp:calculationInputFor` | `rcpp:progressRemainingQuantity` |
| 647 | `rcpp:progressCumulativeQuantity` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressQuantitySheet` |
| 648 | `rcpp:progressCumulativeQuantity` | `rcpp:mapsDirectlyTo` | `rcpp:outputCumulativeQuantity` |
| 649 | `rcpp:progressCumulativeQuantity` | `rdfs:domain` | `rcpp:CurrentProgressQuantityItem` |
| 650 | `rcpp:progressCumulativeQuantity` | `rdfs:subPropertyOf` | `rcpp:hasQuantityValue` |
| 651 | `rcpp:progressCurrentQuantity` | `rcpp:calculationInputFor` | `rcpp:progressCumulativeQuantity` |
| 652 | `rcpp:progressCurrentQuantity` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressQuantitySheet` |
| 653 | `rcpp:progressCurrentQuantity` | `rcpp:inputToCalculationClass` | `rcpp:CurrentProgressAmountCalculation` |
| 654 | `rcpp:progressCurrentQuantity` | `rcpp:mapsDirectlyTo` | `rcpp:outputCurrentQuantity` |
| 655 | `rcpp:progressCurrentQuantity` | `rdfs:domain` | `rcpp:CurrentProgressQuantityItem` |
| 656 | `rcpp:progressCurrentQuantity` | `rdfs:subPropertyOf` | `rcpp:hasQuantityValue` |
| 657 | `rcpp:progressPreviousCumulativeQuantity` | `rcpp:calculationInputFor` | `rcpp:progressCumulativeQuantity` |
| 658 | `rcpp:progressPreviousCumulativeQuantity` | `rcpp:consistencyComparedWith` | `rcpp:outputPreviousQuantity` |
| 659 | `rcpp:progressPreviousCumulativeQuantity` | `rcpp:consistencyComparedWith` | `rcpp:previousCumulativeQuantity` |
| 660 | `rcpp:progressPreviousCumulativeQuantity` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressQuantitySheet` |
| 661 | `rcpp:progressPreviousCumulativeQuantity` | `rdfs:domain` | `rcpp:CurrentProgressQuantityItem` |
| 662 | `rcpp:progressPreviousCumulativeQuantity` | `rdfs:subPropertyOf` | `rcpp:hasQuantityValue` |
| 663 | `rcpp:progressQuantityItemCode` | `rcpp:consistencyComparedWith` | `rcpp:outputItemCode` |
| 664 | `rcpp:progressQuantityItemCode` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressQuantitySheet` |
| 665 | `rcpp:progressQuantityItemCode` | `rcpp:matchesWithField` | `rcpp:contractItemCode` |
| 666 | `rcpp:progressQuantityItemCode` | `rdfs:domain` | `rcpp:CurrentProgressQuantityItem` |
| 667 | `rcpp:progressQuantityItemCode` | `rdfs:subPropertyOf` | `rcpp:hasItemCode` |
| 668 | `rcpp:progressQuantityItemName` | `rcpp:consistencyComparedWith` | `rcpp:outputWorkDescription` |
| 669 | `rcpp:progressQuantityItemName` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressQuantitySheet` |
| 670 | `rcpp:progressQuantityItemName` | `rcpp:matchesWithField` | `rcpp:contractItemName` |
| 671 | `rcpp:progressQuantityItemName` | `rdfs:domain` | `rcpp:CurrentProgressQuantityItem` |
| 672 | `rcpp:progressQuantityItemName` | `rdfs:subPropertyOf` | `rcpp:hasItemName` |
| 673 | `rcpp:progressQuantitySpecification` | `rcpp:consistencyComparedWith` | `rcpp:outputSpecification` |
| 674 | `rcpp:progressQuantitySpecification` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressQuantitySheet` |
| 675 | `rcpp:progressQuantitySpecification` | `rcpp:matchesWithField` | `rcpp:contractSpecification` |
| 676 | `rcpp:progressQuantitySpecification` | `rdfs:domain` | `rcpp:CurrentProgressQuantityItem` |
| 677 | `rcpp:progressQuantitySpecification` | `rdfs:subPropertyOf` | `rcpp:hasSpecificationText` |
| 678 | `rcpp:progressQuantityUnit` | `rcpp:consistencyComparedWith` | `rcpp:contractUnit` |
| 679 | `rcpp:progressQuantityUnit` | `rcpp:consistencyComparedWith` | `rcpp:outputUnit` |
| 680 | `rcpp:progressQuantityUnit` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressQuantitySheet` |
| 681 | `rcpp:progressQuantityUnit` | `rcpp:matchesWithField` | `rcpp:contractUnit` |
| 682 | `rcpp:progressQuantityUnit` | `rdfs:domain` | `rcpp:CurrentProgressQuantityItem` |
| 683 | `rcpp:progressQuantityUnit` | `rdfs:subPropertyOf` | `rcpp:hasSourceUnitText` |
| 684 | `rcpp:progressQuantityWorkType` | `rcpp:consistencyComparedWith` | `rcpp:outputWorkType` |
| 685 | `rcpp:progressQuantityWorkType` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressQuantitySheet` |
| 686 | `rcpp:progressQuantityWorkType` | `rcpp:matchesWithField` | `rcpp:contractWorkType` |
| 687 | `rcpp:progressQuantityWorkType` | `rdfs:domain` | `rcpp:CurrentProgressQuantityItem` |
| 688 | `rcpp:progressQuantityWorkType` | `rdfs:subPropertyOf` | `rcpp:hasSourceWorkCategoryText` |
| 689 | `rcpp:progressRemainingQuantity` | `rcpp:fieldOfDocument` | `rcpp:CurrentProgressQuantitySheet` |
| 690 | `rcpp:progressRemainingQuantity` | `rcpp:mapsDirectlyTo` | `rcpp:outputRemainingQuantity` |
| 691 | `rcpp:progressRemainingQuantity` | `rdfs:domain` | `rcpp:CurrentProgressQuantityItem` |
| 692 | `rcpp:progressRemainingQuantity` | `rdfs:subPropertyOf` | `rcpp:hasQuantityValue` |
| 693 | `rcpp:progressRoundNumber` | `rdfs:domain` | `rcpp:ProgressPaymentRound` |
| 694 | `rcpp:progressRoundReferenceDate` | `rdfs:domain` | `rcpp:ProgressPaymentRound` |
| 695 | `rcpp:projectIdentifier` | `rdfs:domain` | `rcpp:Project` |
| 696 | `rcpp:projectName` | `rdfs:domain` | `rcpp:Project` |
| 697 | `rcpp:quantityAggregatedInto` | `rdfs:domain` | `rcpp:ProgressQuantityDetailItem` |
| 698 | `rcpp:quantityAggregatedInto` | `rdfs:range` | `rcpp:CurrentProgressQuantityItem` |
| 699 | `rcpp:quantityBand` | `rdfs:domain` | `rcpp:ConcretePlacementCostItem` |
| 700 | `rcpp:quantityBasisFrom` | `rdfs:domain` | `rcpp:ContractStatementItem` |
| 701 | `rcpp:quantityBasisFrom` | `rdfs:range` | `rcpp:QuantityCalculationItem` |
| 702 | `rcpp:quantityCalculatedQuantity` | `rcpp:consistencyComparedWith` | `rcpp:contractQuantity` |
| 703 | `rcpp:quantityCalculatedQuantity` | `rcpp:fieldOfDocument` | `rcpp:QuantityCalculationSheet` |
| 704 | `rcpp:quantityCalculatedQuantity` | `rdfs:domain` | `rcpp:QuantityCalculationItem` |
| 705 | `rcpp:quantityCalculatedQuantity` | `rdfs:subPropertyOf` | `rcpp:hasQuantityValue` |
| 706 | `rcpp:quantityCalculationBasis` | `rcpp:consistencyComparedWith` | `rcpp:contractQuantityBasis` |
| 707 | `rcpp:quantityCalculationBasis` | `rcpp:fieldOfDocument` | `rcpp:QuantityCalculationSheet` |
| 708 | `rcpp:quantityCalculationBasis` | `rdfs:domain` | `rcpp:QuantityCalculationItem` |
| 709 | `rcpp:quantityCalculationCode` | `rcpp:fieldOfDocument` | `rcpp:QuantityCalculationSheet` |
| 710 | `rcpp:quantityCalculationCode` | `rdfs:domain` | `rcpp:QuantityCalculationItem` |
| 711 | `rcpp:quantityContractItemCode` | `rcpp:fieldOfDocument` | `rcpp:QuantityCalculationSheet` |
| 712 | `rcpp:quantityContractItemCode` | `rcpp:matchesWithField` | `rcpp:contractItemCode` |
| 713 | `rcpp:quantityContractItemCode` | `rdfs:domain` | `rcpp:QuantityCalculationItem` |
| 714 | `rcpp:quantityContractItemCode` | `rdfs:subPropertyOf` | `rcpp:hasItemCode` |
| 715 | `rcpp:quantityFormula` | `rcpp:fieldOfDocument` | `rcpp:QuantityCalculationSheet` |
| 716 | `rcpp:quantityFormula` | `rdfs:domain` | `rcpp:QuantityCalculationItem` |
| 717 | `rcpp:quantityItemName` | `rcpp:fieldOfDocument` | `rcpp:QuantityCalculationSheet` |
| 718 | `rcpp:quantityItemName` | `rcpp:matchesWithField` | `rcpp:contractItemName` |
| 719 | `rcpp:quantityItemName` | `rdfs:domain` | `rcpp:QuantityCalculationItem` |
| 720 | `rcpp:quantityItemName` | `rdfs:subPropertyOf` | `rcpp:hasItemName` |
| 721 | `rcpp:quantitySpecification` | `rcpp:fieldOfDocument` | `rcpp:QuantityCalculationSheet` |
| 722 | `rcpp:quantitySpecification` | `rcpp:matchesWithField` | `rcpp:contractSpecification` |
| 723 | `rcpp:quantitySpecification` | `rdfs:domain` | `rcpp:QuantityCalculationItem` |
| 724 | `rcpp:quantitySpecification` | `rdfs:subPropertyOf` | `rcpp:hasSpecificationText` |
| 725 | `rcpp:quantityTolerance` | `rdfs:domain` | `rcpp:CalculationPolicy` |
| 726 | `rcpp:quantityUnit` | `rcpp:consistencyComparedWith` | `rcpp:contractUnit` |
| 727 | `rcpp:quantityUnit` | `rcpp:fieldOfDocument` | `rcpp:QuantityCalculationSheet` |
| 728 | `rcpp:quantityUnit` | `rcpp:matchesWithField` | `rcpp:contractUnit` |
| 729 | `rcpp:quantityUnit` | `rdfs:domain` | `rcpp:QuantityCalculationItem` |
| 730 | `rcpp:quantityUnit` | `rdfs:subPropertyOf` | `rcpp:hasSourceUnitText` |
| 731 | `rcpp:quantityWorkType` | `rcpp:fieldOfDocument` | `rcpp:QuantityCalculationSheet` |
| 732 | `rcpp:quantityWorkType` | `rcpp:matchesWithField` | `rcpp:contractWorkType` |
| 733 | `rcpp:quantityWorkType` | `rdfs:domain` | `rcpp:QuantityCalculationItem` |
| 734 | `rcpp:quantityWorkType` | `rdfs:subPropertyOf` | `rcpp:hasSourceWorkCategoryText` |
| 735 | `rcpp:rebarGrade` | `rdfs:domain` | `rcpp:RebarCostItem` |
| 736 | `rcpp:rebarGrade` | `rdfs:range` | `rcpp:RebarGrade` |
| 737 | `rcpp:rebarType` | `rdfs:domain` | `rcpp:RebarCostItem` |
| 738 | `rcpp:rebarWorkType` | `rdfs:domain` | `rcpp:RebarCostItem` |
| 739 | `rcpp:rebarWorkType` | `rdfs:range` | `rcpp:RebarWorkType` |
| 740 | `rcpp:representsCostItem` | `rdfs:domain` | `rcpp:DocumentItem` |
| 741 | `rcpp:representsCostItem` | `rdfs:range` | `rcpp:CostItem` |
| 742 | `rcpp:requiredForClass` | `rdfs:domain` | `rcpp:FieldRequirement` |
| 743 | `rcpp:requiredProperty` | `rdfs:domain` | `rcpp:FieldRequirement` |
| 744 | `rcpp:requirementLevel` | `rdfs:domain` | `rcpp:FieldRequirement` |
| 745 | `rcpp:requirementPurpose` | `rdfs:domain` | `rcpp:FieldRequirement` |
| 746 | `rcpp:reuseCount` | `rdfs:domain` | `rcpp:FormworkCostItem` |
| 747 | `rcpp:reviewStatus` | `rdfs:domain` | `rcpp:DocumentItemMatching` |
| 748 | `rcpp:reviewedBy` | `rdfs:domain` | `rcpp:DocumentItemMatching` |
| 749 | `rcpp:roundingMode` | `rdfs:domain` | `rcpp:CalculationPolicy` |
| 750 | `rcpp:roundingMode` | `rdfs:range` | `rcpp:RoundingMode` |
| 751 | `rcpp:ruleVersion` | `rdfs:domain` | `rcpp:SpecificationNormalizationRule` |
| 752 | `rcpp:shoringType` | `rdfs:domain` | `rcpp:ShoringCostItem` |
| 753 | `rcpp:shoringType` | `rdfs:range` | `rcpp:ShoringType` |
| 754 | `rcpp:shoringWorkType` | `rdfs:domain` | `rcpp:ShoringCostItem` |
| 755 | `rcpp:slump` | `rdfs:domain` | `rcpp:ReadyMixedConcreteCostItem` |
| 756 | `rcpp:sourceCellRange` | `rdfs:domain` | `rcpp:SourceLocation` |
| 757 | `rcpp:sourceFileName` | `rdfs:domain` | `rcpp:SourceLocation` |
| 758 | `rcpp:sourceItem` | `rdfs:domain` | `rcpp:DocumentItemMatching` |
| 759 | `rcpp:sourceItem` | `rdfs:range` | `rcpp:DocumentItem` |
| 760 | `rcpp:sourcePageNumber` | `rdfs:domain` | `rcpp:SourceLocation` |
| 761 | `rcpp:sourceRowNumber` | `rdfs:domain` | `rcpp:SourceLocation` |
| 762 | `rcpp:sourceSheetName` | `rdfs:domain` | `rcpp:SourceLocation` |
| 763 | `rcpp:sourceValueAlias` | `rcpp:appliesToClass` | `rcpp:ControlledSpecificationValue` |
| 764 | `rcpp:sourceValueAlias` | `rcpp:appliesToClass` | `rcpp:Unit` |
| 765 | `rcpp:sourceValueAlias` | `rcpp:appliesToClass` | `rcpp:WorkCategory` |
| 766 | `rcpp:spliceMethod` | `rdfs:domain` | `rcpp:RebarCostItem` |
| 767 | `rcpp:summaryContractAmount` | `rcpp:consistencyComparedWith` | `rcpp:outputSummaryContractAmount` |
| 768 | `rcpp:summaryContractAmount` | `rcpp:fieldOfDocument` | `rcpp:WorkTypeSummaryStatement` |
| 769 | `rcpp:summaryContractAmount` | `rdfs:domain` | `rcpp:WorkTypeSummaryItem` |
| 770 | `rcpp:summaryContractAmount` | `rdfs:subPropertyOf` | `rcpp:hasAmountValue` |
| 771 | `rcpp:summaryDirectCost` | `rcpp:fieldOfDocument` | `rcpp:WorkTypeSummaryStatement` |
| 772 | `rcpp:summaryDirectCost` | `rdfs:domain` | `rcpp:WorkTypeSummaryItem` |
| 773 | `rcpp:summaryWorkType` | `rcpp:consistencyComparedWith` | `rcpp:outputSummaryWorkCategoryText` |
| 774 | `rcpp:summaryWorkType` | `rcpp:fieldOfDocument` | `rcpp:WorkTypeSummaryStatement` |
| 775 | `rcpp:summaryWorkType` | `rdfs:domain` | `rcpp:WorkTypeSummaryItem` |
| 776 | `rcpp:summaryWorkType` | `rdfs:subPropertyOf` | `rcpp:hasSourceWorkCategoryText` |
| 777 | `rcpp:supportAmount` | `rcpp:fieldOfDocument` | `rcpp:SupportingReferenceDocument` |
| 778 | `rcpp:supportAmount` | `rdfs:domain` | `rcpp:SupportingReferenceItem` |
| 779 | `rcpp:supportAmount` | `rdfs:subPropertyOf` | `rcpp:hasAmountValue` |
| 780 | `rcpp:supportItemCode` | `rcpp:fieldOfDocument` | `rcpp:SupportingReferenceDocument` |
| 781 | `rcpp:supportItemCode` | `rcpp:matchesWithField` | `rcpp:contractItemCode` |
| 782 | `rcpp:supportItemCode` | `rdfs:domain` | `rcpp:SupportingReferenceItem` |
| 783 | `rcpp:supportItemCode` | `rdfs:subPropertyOf` | `rcpp:hasItemCode` |
| 784 | `rcpp:supportItemName` | `rcpp:fieldOfDocument` | `rcpp:SupportingReferenceDocument` |
| 785 | `rcpp:supportItemName` | `rcpp:matchesWithField` | `rcpp:contractItemName` |
| 786 | `rcpp:supportItemName` | `rdfs:domain` | `rcpp:SupportingReferenceItem` |
| 787 | `rcpp:supportItemName` | `rdfs:subPropertyOf` | `rcpp:hasItemName` |
| 788 | `rcpp:supportQuantity` | `rcpp:fieldOfDocument` | `rcpp:SupportingReferenceDocument` |
| 789 | `rcpp:supportQuantity` | `rdfs:domain` | `rcpp:SupportingReferenceItem` |
| 790 | `rcpp:supportQuantity` | `rdfs:subPropertyOf` | `rcpp:hasQuantityValue` |
| 791 | `rcpp:supportSpecification` | `rcpp:fieldOfDocument` | `rcpp:SupportingReferenceDocument` |
| 792 | `rcpp:supportSpecification` | `rcpp:matchesWithField` | `rcpp:contractSpecification` |
| 793 | `rcpp:supportSpecification` | `rdfs:domain` | `rcpp:SupportingReferenceItem` |
| 794 | `rcpp:supportSpecification` | `rdfs:subPropertyOf` | `rcpp:hasSpecificationText` |
| 795 | `rcpp:supportUnit` | `rcpp:consistencyComparedWith` | `rcpp:contractUnit` |
| 796 | `rcpp:supportUnit` | `rcpp:fieldOfDocument` | `rcpp:SupportingReferenceDocument` |
| 797 | `rcpp:supportUnit` | `rcpp:matchesWithField` | `rcpp:contractUnit` |
| 798 | `rcpp:supportUnit` | `rdfs:domain` | `rcpp:SupportingReferenceItem` |
| 799 | `rcpp:supportUnit` | `rdfs:subPropertyOf` | `rcpp:hasSourceUnitText` |
| 800 | `rcpp:supportUnitPrice` | `rcpp:consistencyComparedWith` | `rcpp:contractUnitPrice` |
| 801 | `rcpp:supportUnitPrice` | `rcpp:fieldOfDocument` | `rcpp:SupportingReferenceDocument` |
| 802 | `rcpp:supportUnitPrice` | `rdfs:domain` | `rcpp:SupportingReferenceItem` |
| 803 | `rcpp:supportUnitPrice` | `rdfs:subPropertyOf` | `rcpp:hasUnitPriceValue` |
| 804 | `rcpp:supportWorkType` | `rcpp:fieldOfDocument` | `rcpp:SupportingReferenceDocument` |
| 805 | `rcpp:supportWorkType` | `rcpp:matchesWithField` | `rcpp:contractWorkType` |
| 806 | `rcpp:supportWorkType` | `rdfs:domain` | `rcpp:SupportingReferenceItem` |
| 807 | `rcpp:supportWorkType` | `rdfs:subPropertyOf` | `rcpp:hasSourceWorkCategoryText` |
| 808 | `rcpp:targetItem` | `rdfs:domain` | `rcpp:DocumentItemMatching` |
| 809 | `rcpp:targetItem` | `rdfs:range` | `rcpp:DocumentItem` |
| 810 | `rcpp:unitCode` | `rdfs:domain` | `rcpp:Unit` |
| 811 | `rcpp:unitCondition` | `rdfs:domain` | `rcpp:CalculationRule` |
| 812 | `rcpp:unitDimension` | `rdfs:domain` | `rcpp:Unit` |
| 813 | `rcpp:unitSymbol` | `rdfs:domain` | `rcpp:Unit` |
| 814 | `rcpp:usesCalculationPolicy` | `rdfs:domain` | `rcpp:ProgressPaymentRound` |
| 815 | `rcpp:usesCalculationPolicy` | `rdfs:range` | `rcpp:CalculationPolicy` |
| 816 | `rcpp:usesSpecificationRule` | `rdfs:domain` | `rcpp:CostItem` |
| 817 | `rcpp:usesSpecificationRule` | `rdfs:range` | `rcpp:SpecificationNormalizationRule` |
| 818 | `rcpp:usesUnit` | `rcpp:appliesToClass` | `rcpp:CostItem` |
| 819 | `rcpp:usesUnit` | `rcpp:appliesToClass` | `rcpp:DocumentItem` |
| 820 | `rcpp:usesUnit` | `rdfs:range` | `rcpp:Unit` |
| 821 | `rcpp:usesUnitConversionRule` | `rdfs:domain` | `rcpp:CalculationActivity` |
| 822 | `rcpp:usesUnitConversionRule` | `rdfs:range` | `rcpp:UnitConversionRule` |
| 823 | `rcpp:usesUnitPriceFrom` | `rdfs:domain` | `rcpp:DocumentItem` |
| 824 | `rcpp:usesUnitPriceFrom` | `rdfs:range` | `rcpp:ContractStatementItem` |
| 825 | `rcpp:usesVibrator` | `rdfs:domain` | `rcpp:ConcretePlacementCostItem` |
| 826 | `rcpp:verticalHeightBand` | `rcpp:appliesToClass` | `rcpp:FormworkCostItem` |
| 827 | `rcpp:verticalHeightBand` | `rcpp:appliesToClass` | `rcpp:ShoringCostItem` |
| 828 | `rcpp:workCategoryCode` | `rdfs:domain` | `rcpp:WorkCategory` |
| 829 | `rcpp:workCategoryName` | `rdfs:domain` | `rcpp:WorkCategory` |
| 830 | `rcpp:workCondition` | `rdfs:domain` | `rcpp:ShoringCostItem` |
| 831 | `rcpp:workDetailAmount` | `rcpp:aggregatesTo` | `rcpp:summaryContractAmount` |
| 832 | `rcpp:workDetailAmount` | `rcpp:fieldOfDocument` | `rcpp:WorkTypeDetailStatement` |
| 833 | `rcpp:workDetailAmount` | `rdfs:domain` | `rcpp:WorkTypeDetailItem` |
| 834 | `rcpp:workDetailAmount` | `rdfs:subPropertyOf` | `rcpp:hasAmountValue` |
| 835 | `rcpp:workDetailDirectCost` | `rcpp:aggregatesTo` | `rcpp:summaryDirectCost` |
| 836 | `rcpp:workDetailDirectCost` | `rcpp:fieldOfDocument` | `rcpp:WorkTypeDetailStatement` |
| 837 | `rcpp:workDetailDirectCost` | `rdfs:domain` | `rcpp:WorkTypeDetailItem` |
| 838 | `rcpp:workDetailItemCode` | `rcpp:fieldOfDocument` | `rcpp:WorkTypeDetailStatement` |
| 839 | `rcpp:workDetailItemCode` | `rcpp:matchesWithField` | `rcpp:contractItemCode` |
| 840 | `rcpp:workDetailItemCode` | `rdfs:domain` | `rcpp:WorkTypeDetailItem` |
| 841 | `rcpp:workDetailItemCode` | `rdfs:subPropertyOf` | `rcpp:hasItemCode` |
| 842 | `rcpp:workDetailItemName` | `rcpp:fieldOfDocument` | `rcpp:WorkTypeDetailStatement` |
| 843 | `rcpp:workDetailItemName` | `rcpp:matchesWithField` | `rcpp:contractItemName` |
| 844 | `rcpp:workDetailItemName` | `rdfs:domain` | `rcpp:WorkTypeDetailItem` |
| 845 | `rcpp:workDetailItemName` | `rdfs:subPropertyOf` | `rcpp:hasItemName` |
| 846 | `rcpp:workDetailQuantity` | `rcpp:calculationInputFor` | `rcpp:workDetailAmount` |
| 847 | `rcpp:workDetailQuantity` | `rcpp:fieldOfDocument` | `rcpp:WorkTypeDetailStatement` |
| 848 | `rcpp:workDetailQuantity` | `rdfs:domain` | `rcpp:WorkTypeDetailItem` |
| 849 | `rcpp:workDetailQuantity` | `rdfs:subPropertyOf` | `rcpp:hasQuantityValue` |
| 850 | `rcpp:workDetailSpecification` | `rcpp:fieldOfDocument` | `rcpp:WorkTypeDetailStatement` |
| 851 | `rcpp:workDetailSpecification` | `rcpp:matchesWithField` | `rcpp:contractSpecification` |
| 852 | `rcpp:workDetailSpecification` | `rdfs:domain` | `rcpp:WorkTypeDetailItem` |
| 853 | `rcpp:workDetailSpecification` | `rdfs:subPropertyOf` | `rcpp:hasSpecificationText` |
| 854 | `rcpp:workDetailUnit` | `rcpp:consistencyComparedWith` | `rcpp:contractUnit` |
| 855 | `rcpp:workDetailUnit` | `rcpp:fieldOfDocument` | `rcpp:WorkTypeDetailStatement` |
| 856 | `rcpp:workDetailUnit` | `rcpp:matchesWithField` | `rcpp:contractUnit` |
| 857 | `rcpp:workDetailUnit` | `rdfs:domain` | `rcpp:WorkTypeDetailItem` |
| 858 | `rcpp:workDetailUnit` | `rdfs:subPropertyOf` | `rcpp:hasSourceUnitText` |
| 859 | `rcpp:workDetailUnitPrice` | `rcpp:calculationInputFor` | `rcpp:workDetailAmount` |
| 860 | `rcpp:workDetailUnitPrice` | `rcpp:fieldOfDocument` | `rcpp:WorkTypeDetailStatement` |
| 861 | `rcpp:workDetailUnitPrice` | `rdfs:domain` | `rcpp:WorkTypeDetailItem` |
| 862 | `rcpp:workDetailUnitPrice` | `rdfs:subPropertyOf` | `rcpp:hasUnitPriceValue` |
| 863 | `rcpp:workDetailWorkType` | `rcpp:fieldOfDocument` | `rcpp:WorkTypeDetailStatement` |
| 864 | `rcpp:workDetailWorkType` | `rcpp:groupsByField` | `rcpp:summaryWorkType` |
| 865 | `rcpp:workDetailWorkType` | `rcpp:matchesWithField` | `rcpp:contractWorkType` |
| 866 | `rcpp:workDetailWorkType` | `rdfs:domain` | `rcpp:WorkTypeDetailItem` |
| 867 | `rcpp:workDetailWorkType` | `rdfs:subPropertyOf` | `rcpp:hasSourceWorkCategoryText` |

## 7. 원본 모듈

- `schema.ttl`
- `classes.ttl`
- `properties.ttl`
- `code-lists.ttl`

> 자동 생성 파일. 온톨로지 수정 후 `python KO/ontology/generate_specification.py` 실행 필요.
