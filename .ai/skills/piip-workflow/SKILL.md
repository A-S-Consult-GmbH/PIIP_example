---
name: piip-workflow
description: Set up a PIIP consumer project and run its validate, docs, and generate pipeline (piip_config.yaml, spec YAML, InstanceSet, gen/). Use when asked to init, scaffold, or fork a PIIP project, or to validate, check, document, or regenerate PIIP ontology YAML.
license: Apache-2.0
user_invocable: true
---

# PIIP consumer workflow

references:
Syntax: https://github.com/A-S-Consult-GmbH/PIIP/blob/main/doc/syntax.md
Validation: https://github.com/A-S-Consult-GmbH/PIIP/blob/main/doc/validation.md

## 1. Init (once per project)

```text
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # POSIX
pip install piip
python -m piip config show
```

Until PyPI: `pip install git+https://github.com/A-S-Consult-GmbH/PIIP_tooling.git@v0.1.3`.
Editable sibling clone: `pip install -e ../PIIP_tooling` (path relative to the consumer project).
The installed version must satisfy `requires.piip` in `piip_config.yaml`.

Config fields (`piip_config.yaml`, relative paths resolve against the config file directory):

- `entry`: spec folders (example: `example_spec/`)
- `outputs.docs`: doc output (example: `gen/doc`)
- `outputs.codegen`: optional adapter targets (`adapter: cpp-std`, `out: gen/code/cpp-std`)
- `catalog`: optional URI locator overrides, omit for the packaged w3id default

Empty project: `python -m piip config init`, then edit the fields above.

URI rules:

- Own ontologies use own http(s) URIs (example: `https://example.org/...`).
- The `https://w3id.org/piip/` prefix is reserved for public ontologies. Closed ontologies must not use it.
- Public ontologies are referenced via `LinkedOntologies` w3id URIs and resolved by the catalog. Never edit or vendor public YAML.

Fork checklist: replace the example spec folder with own ontologies, adjust `entry` if the folder name changes, keep `LinkedOntologies` at w3id URIs, then run validate and docs.

## 2. Validate

```text
python -m piip validate --config piip_config.yaml
python -m piip validate --config piip_config.yaml --level 1   # syntax only
python -m piip validate --config piip_config.yaml --level 2   # grammar only
python -m piip validate --config piip_config.yaml --level 3   # semantics only
```

Fix from cheap to expensive. Later levels are meaningless on broken syntax.

- L1: YAML syntax, duplicate keys, line length, required UTF-8 BOM prefix.
- L2: structural grammar, unknown keys are typos. Components allow only `Doc` and `Members`.
- L3: cross-file semantics over the transitive `LinkedOntologies` graph: naming (`*Component`, `*Archetype`), unique names, URI/version match, prefix rules, reference resolution including `Optional<>`, `Set<>`, `List<>`, `Link<>`, `Data<>`.

InstanceSet documents share L1/L2 and add L3 checks (UUID identity, member resolution, required members, typed values).

Success ends with `ALL CHECKS PASSED`. Quote exact error lines when reporting. Fix the YAML to satisfy the contract, never suggest renaming checks.

## 3. Docs and generate

```text
python -m piip validate --config piip_config.yaml
python -m piip docs --config piip_config.yaml
python -m piip generate --config piip_config.yaml
```

Always validate first. Docs from a broken model are misleading. Full pipeline in one step: `python run.py` (validate, docs, generate, fail fast).

Output contract (`outputs.docs`, example `gen/doc`):

- `_generated_ontologies.md`: lookup table of all ontologies
- `ontologies/_<Name>.md`: one file per ontology (entry plus linked)

Generated files carry an auto-generated note and are derived data: never hand-edit, change the YAML and rerun. Consumer projects keep `gen/` gitignored; in the public spec repo `doc/` is regenerated and committed together with the YAML change.

Regenerate after every change under `entry` paths and after `LinkedOntologies` changes.

Report the result (config summary, `ALL CHECKS PASSED`, generated file list), then stop.
