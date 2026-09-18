# PIIP example

Forkable consumer of the public PIIP specification. Intended as a GitHub template. This repository holds a closed example ontology and uses the `piip` tools. It does **not** vendor the public spec and does **not** contain tooling sources.

Public ontologies are resolved by URI (`LinkedOntologies` → `https://w3id.org/piip/…`). Own YAML lives under `example_spec/` with URIs under `https://example.org/…`.

## Quick start

```text
python -m venv .venv
.venv\Scripts\activate
pip install piip
python run.py
```

Until PyPI, `pip install -e .` uses the git tag pin, or install a sibling clone:

```text
pip install git+https://github.com/A-S-Consult-GmbH/PIIP_tooling.git@v0.1.3
python -m piip validate --config piip_config.yaml
python -m piip docs --config piip_config.yaml
python -m piip generate --config piip_config.yaml
```

Relative paths in `piip_config.yaml` are resolved against that file's directory. Public YAML is fetched via the packaged w3id catalog unless `catalog` in that file overrides it.

## Fork as own project

1. Fork or copy this repository.
2. Replace `example_spec/` with own ontologies (own http(s) URI, not `w3id.org/piip/`).
3. Keep `LinkedOntologies` pointing at public w3id URIs. Do not edit public YAML.
4. Adjust `entry` in `piip_config.yaml` if the folder name changes.

## Layout

```text
piip_config.yaml          # entries, outputs
example_spec/             # closed Domain + System + InstanceSet
gen/                      # derived (gitignored)
run.py
```

License of orchestrator files: Apache 2.0. Public PIIP YAML remains CC BY-ND 4.0 at [A-S-Consult-GmbH/PIIP](https://github.com/A-S-Consult-GmbH/PIIP).
