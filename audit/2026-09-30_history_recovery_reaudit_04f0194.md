# History recovery re-audit

Audit date: 2026-09-30  
Audited commit: `04f0194806465e5daa405fc129840e8745be897f`  
Proposal: 0.60  
Type: repository evolution recovery and verification  
Scope: release ancestry, duplicate-change comparison, source preservation, audit-target availability, imported core provenance, and the new history validator.  
Working tree at the beginning of this re-audit: clean. This record is added after validation of the identified commit.  
External execution: GitHub remote-ref inspection and Git tag/object fetch; no external literature, language checker, or model-certification service was used.

## Result

The original tagged proposal ancestry and all six original historical audit targets are recovered. The prepared mainline uses the original proposal commits, followed by the two unique repository changes and recovery controls. No proposal semantic changes were introduced by this repair.

The previous evolution audit remains an accurate record of the checkout and refs available when it reviewed `46faf0f`. Its missing-ref finding is superseded by the recovery evidence below. That original record and all earlier audits remain unchanged.

## Recovery evidence

Initially, both the local checkout and the advertised remote refs had no milestone tags. Direct GitHub commit-API requests for the full `25885a8` and `7810adc` identities reported that no commit was found. The owner subsequently pushed the forgotten tags. `git fetch origin --tags` then recovered the original commit objects and their ancestry, so inferred replacement identities were unnecessary.

Original annotated tags, including their tag-object identities, are preserved unchanged in `2026-09-30_history_recovery.json`. The common ancestor of the original tagged lineage and the superseded published branch is `f76b81e`.

| Original milestone | Exact recovered commit |
|---|---|
| `core-v5.0.0-rc.1` | `8fb76ee7a1527a05e2b6c3a33a90ed6e6c0cb644` |
| `proposal-0.2` | `d861ac0ff872ddad88f65fbf54ee951971dd6dcd` |
| `proposal-0.17` | `8cba27d5a5a861c3351f5bf9efc76d5bcf0df882` |
| `proposal-0.25` | `7655434e7afafef8421beab35cd1bc1e80626e9b` |
| `proposal-0.30` | `39cc29ff41a4656ddb0e66c90e8b6f2f52651bc2` |
| `proposal-0.40` | `935e3dfcfa63d80ba00ffdbecaa12bb662be4261` |
| `proposal-0.50` | `2feda1a4e52ff0029fa25d794c449a781f48872e` |
| `proposal-0.60` | `168568217a39cb4ec5669ce30f2aea56dfaeb2e8` |

The historical audit targets `25885a8`, `ac6f62e`, `27bf87b`, `7810adc`, `624ba4d`, and baseline `2feda1a` all resolve to their original commit identities and belong to the restored ancestry. This is object recovery, not a mapping inferred from commit subjects.

## Identical changes and retained differences

The original tagged release line contains 84 commits. The superseded branch contains 86. After their common ancestor, 35 pairs represent the same changes, and the superseded branch contains two unique changes:

- `350ce30` — project-name correction;
- `66d3186` — rc.2 core update.

All 35 pairs have matching stable patch IDs. Thirty-three pairs have byte-identical complete diff output. The other two differ only in `index` blob-object header lines for `project.toml`, because the unique name correction changes that file's blob identity. Removing only those header lines yields byte-identical diff text for all 35 pairs. Paths, modes, hunk context, changed content, and whitespace remain part of the comparison. Both complete lineages have no repeated full trees, empty changes, or repeated stable patch IDs internally; there was no basis for deleting a distinct evolution step within either line.

The repaired mainline retains the original 35 commits instead of their replayed counterparts. It then replays the two unique changes as `24a8e60` and `f0e0fe4`, preserving their original authors and author dates and recording the new committer identity/date. Their patches match the original changes. This replaces duplicate representations of changes without discarding a meaningful change.

At `f0e0fe4`, before adding recovery controls, `git diff --exit-code recovery/pre-rework-2026-09-30 HEAD` passed: the complete tree was identical to the superseded published tip. The canonical proposal, backlog, data model, and retraction ledger also have identical blobs at the original 0.60 release and the restored head. Recovery controls subsequently change repository metadata, documentation, validation, and audit evidence only.

The annotated `recovery/pre-rework-2026-09-30` tag preserves the previous published head, including the audit target `46faf0f`. Superseded replay objects remain recoverable through that archival ref; they are excluded from the repaired mainline. A complete pre-repair bundle was also created and verified at `/tmp/hive-before-history-recovery-20260930.bundle`. The Git recovery tag is the durable preservation mechanism; the temporary bundle is supplementary.

## Baseline identification

`project.toml` now distinguishes:

- the active rc.2 core and its repository-update source commit;
- the immutable rc.1 foundation archive name, checksum, and root tag;
- the proposal's existing rc.1 language baseline and corresponding available tag.

`core-v5.0.0-rc.2` identifies the replayed update at `f0e0fe4`. Its entire core tree is identical to the core tree at source `66d3186`. No original rc.2 archive checksum is invented. Proposal §§4.1 and 22 remain unchanged, so this repair does not claim completion of BL-22's normative proposal rebase or designated LMC review.

## Verification

Local tools: Git, Python 3.13.5, jsonschema 4.19.2, referencing 0.36.2, and PyYAML 6.0.2. Network execution: `git ls-remote`, two read-only GitHub commit API requests, and `git fetch origin --tags` against the configured GitHub repository. The initially unsuccessful API checks are preserved above; the later tag fetch supplied the missing objects.

| Check | Result |
|---|---|
| `make validate` at the audited commit | PASS, including history checks |
| `make validate-proposal` | PASS |
| `python3 core/scripts/validate_ads_bundle.py` | PASS, actual rc.2 core |
| `git fsck --full` | PASS; no diagnostics |
| `git diff --check`, clean initial tree | PASS |
| Eight original tag targets and annotations | PASS, unchanged; all targets are ancestors |
| Six historical audit targets | PASS, original identities recovered |
| 35 equivalent-change mappings | PASS, exact diff comparison excluding only blob-ID headers |
| Two unique-change replays | PASS, matching source deltas |
| Historical validators on the restored 86-commit lineage before controls | PASS, 45/45 available validators |
| Audit hashes in the historical rescan, including the prior evolution report | PASS, 0 unresolved out of 38 extracted occurrences |
| Historical display-math delimiter parity | PASS, limited source check |
| Historical control-character defects | Preserved: the same 11 early defective states remain; later sources have the correction |

An isolated local clone regression check exercised seven cases against the final history-validator code:

1. valid restored lineage accepted;
2. missing `proposal-0.50` tag rejected;
3. falsely identifying the active core as rc.1 rejected;
4. false equivalent-change mapping rejected;
5. unavailable audit target rejected;
6. later proposal edits accepted by the history checker, demonstrating that the recovery invariant does not freeze future source evolution to 0.60;
7. the restored state accepted again after removing the probes.

All seven checks passed. The repeatable session runner is `/tmp/hive-history-regression.py`; historical scan results are `/tmp/hive-restored-evolution-evidence.json`. The permanent `scripts/validate-history` verifies the durable recovery manifest and current declared baseline offline. It provides repository-history assurance, not semantic model or language certification.

## Finding disposition

| Prior finding | Disposition at the audited state |
|---|---|
| EV-01 — unavailable milestones and audit targets | VERIFIED / CLOSED: owner-supplied original tags and original audit commit objects are available and verifiable; immutable annotations and ancestry are checked. |
| EV-02 — ambiguous core baseline identification | VERIFIED / CLOSED for repository identification/provenance: active core, foundation archive, and proposal baseline are explicit. Normative proposal adoption of rc.2 remains BL-22. |
| EV-07 — validator coverage | PARTIALLY RESOLVED: milestone, provenance, audit identity, and recovery-delta checks are now enforced. Formal signatures, designated evidence, and remaining semantic checks are not automated. |
| EV-03 through EV-06, EV-08, EV-09 | Remain OPEN in their applicable scope. Original proposal/control blobs are preserved; this history repair does not implement those semantic, measurement-evidence, or date corrections. |

The repaired repository has verifiable evolution ancestry and recoverable evidence. Full proposal conformity remains limited by the prior semantic backlog and designated language-review requirements. PDF rendering and release generation were not repeated; the previously recorded unavailable Pandoc/XeLaTeX toolchain remains a limitation.

This audit does not claim remote publication. Publishing the repaired mainline requires a non-fast-forward update of the previously published branch and publication of the new recovery/core tags. Existing original release tags are not to be moved.
