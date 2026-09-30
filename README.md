# AI Aided Hive Engineering

This repository contains the **AI DevMode standards core** and the source of the **AI Aided Hive Engineering Proposal**. The core is the root of the Git history; proposal evolution is reconstructed above it as reviewable commits.

The canonical proposal source is [`proposal/AI_Aided_Hive_Engineering.md`](proposal/AI_Aided_Hive_Engineering.md). Generated PDF documents are release artifacts and are not committed to Git.

## Versioning

Proposal milestones use tags of the form `proposal-X.Y`. The reconstructed milestone tags are:

- `proposal-0.2`
- `proposal-0.17`
- `proposal-0.25`
- `proposal-0.30`
- `proposal-0.40`
- `proposal-0.50`
- `proposal-0.60`

Fetch milestone tags with `git fetch origin --tags`. The original annotated proposal tags are retained unchanged. In particular, `proposal-0.50` and `proposal-0.60` identify the original release lineage referenced by the historical audit records.

Core releases use tags such as `core-v5.0.0-rc.1` and `core-v5.0.0-rc.2`. Version strings are not added to filenames inside `core/` merely because the imported archive has that version.

## Core foundation

The initial rc.1 import is the root commit, tagged `core-v5.0.0-rc.1`. Its original archive metadata remains in `project.toml` under `core.foundation`. The release-versioned archive wrapper is not stored in the repository.

The current core is rc.2, retained as a repository update after the original proposal release lineage. Its source commit and current tag are recorded separately from the rc.1 archive provenance; no rc.2 archive checksum is asserted. The proposal's declared language baseline remains rc.1 and is explicitly recorded under `proposal.language_baseline`. Integrating rc.2 into the proposal's normative language profile remains BL-22.

## Evolution integrity

The mainline retains the original tagged proposal history and the two unique repository changes recovered from the superseded branch. Equivalent replayed proposal commits are represented once on the mainline. `recovery/pre-rework-2026-09-30` preserves the superseded published head for rollback and the audit that reviewed it.

The [recovery evidence](audit/2026-09-30_history_recovery.json) records exact retained and superseded commit identities, equivalent changes, unique replays, and milestone targets. It is supporting evidence; Git commits and tags remain the evolution source.

`make validate-history` verifies milestone ancestry, audit-target availability, core provenance, and the recovery mapping. It requires a Git checkout with its tags. Full `make validate` includes this check; `make validate-proposal` validates portable source/build inputs without Git-history requirements.

Future changes extend the accepted mainline with new commits. Released tags and committed audit records remain immutable. A history repair preserves its source refs and records the mapping before publication.

## Build

The build is local and CI-neutral. It does not depend on GitHub Actions or another hosted CI provider.

```sh
make validate
make pdf
make release
```

`make pdf` produces the PDF under `build/`. `make release` creates a self-contained ZIP under `dist/` containing the canonical proposal Markdown, current proposal backlog and development-control records, referenced images, generated PDF, repository metadata, license, and available supplementary data. Audit records remain outside the release archive. Generated output is ignored by Git.

A reproducible container build environment is described by `Containerfile`.

## Source and release policy

- Markdown is the canonical proposal source.
- Images referenced by Markdown belong under `assets/images/`.
- Supplementary release data belongs under `data/supplementary/`.
- Generated PDF and release archives belong only under ignored build/output directories.
- Proposal development-control records (`BACKLOG.md`, `DATA_MODEL.md`, and `RETRACTIONS.md`) live under `proposal/` and are included in proposal releases as non-canonical companion records.
- Human-readable audit records belong under `audit/`; they are tied to specific committed states and are not canonical proposal semantics or proposal release artifacts.

## License

This repository is licensed under the Eclipse Public License 2.0. See [`LICENSE`](LICENSE).
