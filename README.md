# 공사기성부분내역서 작성을 위한 온톨로지

이 프로젝트는 건설 프로젝트의 기성서류를 구조화하고, 공사기성부분내역서 작성(특히 금회기성금액)에 필요한 데이터 관계를 표현하는 온톨로지 구축을 목적으로 함.

기성서류의 종류와 항목, 서류 간 데이터 전달, 항목 매칭 및 기성금액 계산 흐름을 RDF + RDFS로 정의함.

대상 공종은 철근콘크리트이며, 철근콘크리트의 상세 속성은 철근, 콘크리트, 거푸집 및 동바리로 정의함.


## 현재 진행도

기성서류 작성 흐름과 데이터 정의를 바탕으로 1차 온톨로지를 구축함.
현재 버전에서는 RDF + RDFS로 클래스·속성·관계를 정의하고, SPARQL 질의를 이용하여 주요 계산 및 데이터 연결 구조를 검증하였음.

## 1. Ontology 설명

### 1-1. Prefix

온톨로지의 기본 Prefix는 `rcpp(Reinforced Concrete Progress Payment)`

```turtle
@prefix rcpp: <https://example.org/rcpp#> .
(현재는 임시 IRI)
```


### 1-2. Class


- 프로젝트 및 기성회차: `Project`, `ProgressPaymentRound`
- 기성서류: `ProgressDocument`, `QuantityCalculationSheet`, `ContractStatement`, `PreviousProgressStatement`, `CurrentProgressQuantitySheet`, `CurrentProgressStatement`
- 서류 내역: `DocumentItem`, `QuantityCalculationItem`, `ContractStatementItem`, `PreviousProgressStatementItem`, `ProgressQuantityDetailItem`, `CurrentProgressQuantityItem`, `CurrentProgressDetailItem`, `CurrentProgressSummaryItem`
- 표준 비용항목: `CostItem`, `RebarCostItem`, `ConcreteCostItem`, `ReadyMixedConcreteCostItem`, `ConcretePlacementCostItem`, `FormworkCostItem`, `ShoringCostItem`
- 서류내역 매칭: `DocumentItemMatching`
- 계산규칙 및 계산활동: `CalculationRule`, `UnitConversionRule`, `ProgressQuantityRollupCalculation`, `CurrentProgressAmountCalculation`, `ProgressSummaryCalculation`, `CalculationActivity`

### 1-3. Property


- 계약내역: `contractItemCode`, `contractWorkType`, `contractItemName`, `contractSpecification`, `contractUnit`, `contractQuantity`, `contractUnitPrice`, `contractAmount`
- 수량산출: `quantityFormula`, `quantityCalculationBasis`, `quantityCalculatedQuantity`
- 기성수량: `progressPreviousCumulativeQuantity`, `progressCurrentQuantity`, `progressCumulativeQuantity`, `progressRemainingQuantity`
- 기성금액: `outputPreviousAmount`, `outputCurrentAmount`, `outputCumulativeAmount`, `outputRemainingAmount`
- 단위변환 및 계산정책: `baseUnit`, `conversionFactorToBaseUnit`, `roundingMode`, `decimalScale`, `calculationOrder`
- 공종별 비용속성: `rebarGrade`, `nominalDiameter`, `maximumAggregateSize`, `nominalStrength`, `slump`, `formworkType`, `reuseCount`, `shoringType`

### 1-4. Relation


- `containsItem`: 서류와 서류 내역 연결
- `representsCostItem`: 서류 내역과 표준 비용항목 연결
- `correspondsToItem`: 승인된 동일 서류 내역 연결
- `usesUnitPriceFrom`: 기성 상세내역과 계약단가 원천 연결
- `quantityBasisFrom`: 계약수량과 수량산출 근거 연결
- `previousQuantityFrom`: 전회누계수량의 이월 원천 연결
- `derivedFrom`: 결과 내역과 원천 내역 연결
- `quantityAggregatedInto`: 상세 기성수량을 계약항목 단위 수량으로 집계
- `aggregatedInto`: 상세 금액을 공종별 집계 내역으로 합산
- `groupsByField`: 상세 내역을 공종별로 묶는 기준 연결

### 1-5. 기성서류 데이터 흐름

```mermaid
flowchart LR
    A[수량산출서] --> B[계약내역서]
    B --> E[항목 매칭 및 계산]
    C[전회 공사기성부분내역서] --> E
    D[기성수량산출서] --> E
    E --> F[공사기성부분내역서]
    F --> G[공종별·전체 금액 집계]
```

### 1-6. 항목 흐름도

```mermaid
flowchart LR
    A[계약내역서의 계약단가] --> D[공사기성부분내역서의 계약단가]
    B[기성수량산출서의 금회기성수량] --> E[공사기성부분내역서의 금회기성수량]
    C[전회 공사기성부분내역서의 누계기성금액] --> F[공사기성부분내역서의 전회누계기성금액]
    D --> G[금회기성금액 계산]
    E --> G
    G --> H[공종별 금회기성금액 집계]
    F --> I[누계기성금액 계산]
    G --> I
```


### 1-7. 데이터 정의도

```mermaid
flowchart LR
    subgraph QS[수량산출서]
        QS1[내역코드]
        QS2[공종]
        QS3[품명]
        QS4[규격]
        QS5[단위]
        QS6[수량산출근거]
        QS7[산출수량]
    end

    subgraph CT[계약내역서]
        CT1[계약 품목코드]
        CT2[공종]
        CT3[공사내역·세부품목]
        CT4[규격]
        CT5[단위]
        CT6[계약수량 산출근거]
        CT7[계약수량]
        CT8[계약단가]
        CT9[계약금액]
    end

    subgraph PV[전회 공사기성부분내역서]
        PV1[전회 품목코드]
        PV2[전회 공사내역]
        PV3[전회 규격]
        PV4[전회 단위]
        PV5[전회누계기성수량]
        PV6[전회누계기성금액]
        PV7[전회누계기성비율]
    end

    subgraph PQ[기성수량산출서]
        PQ1[내역코드]
        PQ2[공종]
        PQ3[품명]
        PQ4[규격]
        PQ5[단위]
        PQ6[전회누계기성수량]
        PQ7[금회기성수량]
        PQ8[누계기성수량]
        PQ9[잔여수량]
    end

    subgraph OP[공사기성부분내역서]
        OP1[출력 품목코드]
        OP2[공종]
        OP3[공사내역]
        OP4[규격]
        OP5[단위]
        OP6[계약수량]
        OP7[계약단가]
        OP8[계약금액]
        OP9[전회까지의 기성수량]
        OP10[전회누계기성금액]
        OP11[전회누계기성비율]
        OP12[금회기성수량]
        OP13[금회기성금액]
        OP14[금회기성비율]
        OP15[누계기성수량]
        OP16[누계기성금액]
        OP17[누계기성비율]
        OP18[잔여수량]
        OP19[잔여금액]
    end

    QS1 -. 항목 매칭 .-> CT1
    QS2 -. 항목 매칭 .-> CT2
    QS3 -. 항목 매칭 .-> CT3
    QS4 -. 항목 매칭 .-> CT4
    QS5 -. 단위 대조 .-> CT5
    QS6 -. 근거 대조 .-> CT6
    QS7 -. 수량 대조 .-> CT7

    CT1 --> OP1
    CT2 --> OP2
    CT3 --> OP3
    CT4 --> OP4
    CT5 --> OP5
    CT7 --> OP6
    CT8 --> OP7
    CT9 --> OP8

    PV1 -. 항목 매칭 .-> CT1
    PV2 -. 항목 매칭 .-> CT3
    PV3 -. 항목 매칭 .-> CT4
    PV4 -. 단위 대조 .-> CT5
    PV5 --> PQ6
    PV5 --> OP9
    PV6 --> OP10
    PV7 --> OP11

    PQ1 -. 항목 매칭 .-> CT1
    PQ2 -. 항목 매칭 .-> CT2
    PQ3 -. 항목 매칭 .-> CT3
    PQ4 -. 항목 매칭 .-> CT4
    PQ5 -. 단위 대조 .-> CT5
    PQ7 --> OP12
    PQ8 --> OP15
    PQ9 --> OP18

    PQ6 -->|더하기| PQ8
    PQ7 -->|더하기| PQ8
    CT7 -->|빼기 기준| PQ9
    PQ8 -->|차감| PQ9

    OP7 -->|곱하기| OP13
    OP12 -->|곱하기| OP13
    OP8 -->|비율 기준| OP14
    OP13 -->|나누기| OP14
    OP10 -->|더하기| OP16
    OP13 -->|더하기| OP16
    OP8 -->|비율 기준| OP17
    OP16 -->|나누기| OP17
    OP8 -->|빼기 기준| OP19
    OP16 -->|차감| OP19
```

실선은 원천값의 직접 전달 또는 계산 입력을, 점선은 동일 항목의 매칭·대조를 나타낸다. 계약정보는 계약내역서에서, 전회 확정값은 전회 공사기성부분내역서에서, 금회 수량은 기성수량산출서에서 가져오며 계산된 금액과 비율은 공사기성부분내역서에 기록한다.



## 2. 실행 방법

### 2-1. Conda 환경 생성

```bash
conda create -n RC_Ontology python=3.10.14 -y
```

### 2-2. Conda 환경 활성화

```bash
conda activate RC_Ontology
```

### 2-3. 패키지 설치

```bash
conda install -y pip
pip install -r requirements.txt
```

### 2-4. 시각화 생성

```bash
cd KO
python visualization/generate_visualization_data.py
```

생성된 `KO/visualization/ontology_graph.html` 파일을 브라우저에서 열어 시각화 확인.

## 3. 파일 구성

- `KO/ontology/schema.ttl`: 온톨로지 정보와 네임스페이스
- `KO/ontology/classes.ttl`: 클래스와 클래스 계층
- `KO/ontology/properties.ttl`: 속성과 관계
- `KO/ontology/code-lists.ttl`: 공종·단위·통제값과 규칙 개체
- `KO/ontology/ONTOLOGY_SPECIFICATION.md`: 클래스·속성·규칙·통제값과 내부 관계 트리플 명세서
- `KO/visualization/ontology_graph.html`: 온톨로지 시각화

## 4. 버전

- Ontology version: `v1.0.0`
- Namespace: `https://example.org/rcpp#`
