# Public Construction Progress Payment Ontology

PCPO is a foundational RDF/RDFS ontology for calculating and validating current
progress-payment amounts for reinforced concrete work in public construction.
It connects effective contract items, current quantity takeoff data, previously
approved cumulative values, current progress lines, and work-level summaries.

The core calculation is:

```text
current progress amount = current progress quantity × effective contract unit price
```

The implementation intentionally uses only **RDF, RDFS, SPARQL, Python, and
RDFLib**. OWL, SHACL, and SWRL are outside the current scope. Data consistency
and calculation checks are implemented as executable SPARQL `SELECT` queries.

> [!IMPORTANT]
> `data/sample-valid.ttl` and `data/sample-invalid.ttl` are synthetic example
> data. They do not represent an actual public project or an official document format.

## Project Structure

```text
.
├── README.md
├── ontology/
│   ├── schema.ttl
│   ├── classes.ttl
│   ├── properties.ttl
│   └── code-lists.ttl
├── data/
│   ├── sample-valid.ttl
│   └── sample-invalid.ttl
├── queries/
│   ├── Q01_contract_items.rq
│   ├── Q02_current_amount.rq
│   ├── Q03_quantity_status.rq
│   ├── Q04_subwork_summary.rq
│   ├── Q05_rc_total.rq
│   ├── Q06_effective_contract_version.rq
│   └── validation/
│       └── V01_...rq through V15_...rq
├── scripts/
│   ├── validate_rdf.py
│   ├── run_queries.py
│   └── generate_validation_report.py
├── visualization/
│   └── ontology_graph.html
├── .gitignore
└── requirements.txt
```

The ontology is split into four modules to keep schema metadata, the class
hierarchy, properties, and controlled resources independently readable. The
Python scripts always load all four modules as one graph.

The namespace `https://example.org/pcpo#` is temporary and must be replaced with
an official persistent URI before production use. It is declared centrally in
`ontology/schema.ttl` and repeated only in Turtle/SPARQL prefix declarations.

## Environment Setup

Run all commands from the repository root directory.

### 1. Create and Activate the Conda Environment

```bash
conda create --name RC_Ontology python=3.13.14 pip -y
conda activate RC_Ontology
```

### 2. Install the Python Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run the Project

### 1. Parse and Validate the RDF Files

```bash
python scripts/validate_rdf.py
```

This command parses every PCPO Turtle file, loads the valid and invalid-overlay
graphs, and confirms that excluded OWL, SHACL, and SWRL terms are not used.

### 2. Run the Six Retrieval Queries

```bash
python scripts/run_queries.py
```

The command prints contract items, current amounts, quantity status, sub-work
totals, the reinforced-concrete total, and the effective contract version.

### 3. Run All SPARQL Validation Rules

```bash
python scripts/generate_validation_report.py
```

The generated report is written locally to `reports/validation-report.md`; the
`reports/` directory is ignored by Git. A successful test run has these conditions:

- all V01–V15 queries return zero rows for `sample-valid.ttl`;
- all V01–V15 queries detect at least one row after `sample-invalid.ttl` is overlaid.

The synthetic validation tolerance is `0.0001` for quantities and `0.5 KRW` for
amounts. An actual project must replace these values with the applicable owner
or site rounding policy.

## Model Summary

The model distinguishes a document row from the real contract item it describes:

```text
ContractDocumentLine ──representsContractItem──> ContractItem
QuantityCalculationLine ──basedOnContractItem──> ContractItem
CurrentProgressLine ──basedOnContractItem──────> ContractItem
CurrentProgressLine ──carriedForwardFrom───────> PreviousProgressLine
```

The main derived values are:

```text
cumulative quantity = previous cumulative quantity + current progress quantity
remaining quantity = effective contract quantity - cumulative quantity
current progress amount = current progress quantity × effective contract unit price
cumulative amount = previous cumulative amount + current progress amount
contract amount = effective contract quantity × effective contract unit price
```

Rebar, concrete, formwork, and shoring are represented as RDFS subclasses of
`ReinforcedConcreteWorkItem`. Quantities with different units are never directly
compared or added.

## PCPO Visualization

The interactive visualization at `visualization/ontology_graph.html` represents
the current PCPO class hierarchy, document lineage, calculation relations, and
the synthetic round-2 progress example. Its graph data is embedded in the HTML,
so ontology changes must also be reflected in this file manually.

To view the visualization:

```bash
python -m http.server 8000
```

Open `http://localhost:8000/visualization/ontology_graph.html`. The page loads
D3.js from a CDN and therefore requires an internet connection.

## Deactivate the Environment

```bash
conda deactivate
```
