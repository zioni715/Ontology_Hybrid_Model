# Ontology Hybrid Model

An RDF/RDFS ontology and knowledge graph visualization model for the integrated
estimation of progress payments and construction progress in reinforced concrete works.

## Project Structure

```text
ontology/
├── ontology.ttl                  # RDF/RDFS ontology schema
└── sample_data.ttl               # Sample instance data
validation/
└── progress_payment_shapes.ttl   # SHACL validation rules
visualization/
└── ontology_graph.html           # D3.js-based ontology visualization
requirements.txt                  # Python package dependencies
```

## Environment Setup

Run the following commands from the repository root directory.

### 1. Create and Activate the Conda Environment

```bash
conda create --name RC_Ontology python=3.13.14 pip -y
conda activate RC_Ontology
```

### 2. Install the Python Dependencies

```bash
conda install -y pip
pip install --upgrade pip
pip install -r requirements.txt
```

## Validate the Ontology

Validate the sample data against the ontology schema and SHACL rules:

```bash
python -m pyshacl \
  -i rdfs \
  -s validation/progress_payment_shapes.ttl \
  -e ontology/ontology.ttl \
  ontology/sample_data.ttl
```

Successful validation produces `Conforms: True` in the output.

## Run the Visualization

Start a local web server from the repository root directory:

```bash
python -m http.server 8000
```

Open the following URL in a web browser:

```text
http://localhost:8000/visualization/ontology_graph.html
```

The visualization loads D3.js from a CDN, so an internet connection is required
when loading it. Press `Ctrl+C` in the terminal to stop the local server.

## Deactivate the Environment

```bash
conda deactivate
```
