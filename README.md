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

Core releases use the source archive notation, for example `core-v5.0.0-rc.1`. Version strings are not added to filenames inside `core/` merely because the imported archive has that version.

## Core foundation

The AI DevMode standards release identified in `project.toml` is committed under `core/` as the initial Git commit and tagged `core-v5.0.0-rc.1`. The release-versioned archive wrapper is not stored in the repository, and its version is not added to filenames inside `core/`.

## Build

The build is local and CI-neutral. It does not depend on GitHub Actions or another hosted CI provider.

```sh
make validate
make pdf
make release
```

`make pdf` produces the PDF under `build/`. `make release` creates a self-contained ZIP under `dist/` containing the Markdown source, referenced images, generated PDF, repository metadata, license, and available supplementary data. Generated output is ignored by Git.

A reproducible container build environment is described by `Containerfile`.

## Source and release policy

- Markdown is the canonical proposal source.
- Images referenced by Markdown belong under `assets/images/`.
- Supplementary release data belongs under `data/supplementary/`.
- Generated PDF and release archives belong only under ignored build/output directories.
- Auditing is a separate process and is intentionally outside this repository structure.

## License

This repository is licensed under the Eclipse Public License 2.0. See [`LICENSE`](LICENSE).
