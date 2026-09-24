# ADS 5.0.0-rc.1 Known Issues

Date: 2026-09-13

| ID | Severity | Known issue | Release effect |
|---|---|---|---|
| A4T-03 | Major | `dispatch_state="request"` can still carry `resolved_target_version`. | Blocks stable promotion until the communication-state contract is resolved or explicitly accepted. |
| A4T-04 | Major | The package validator still accepts duplicate YAML frontmatter keys because the YAML loader keeps one value. | Blocks stable promotion until duplicate-key handling is deterministic. |
| A4T-05 | Important | The common communication envelope defines requests but not a common result/response envelope or correlation identifier. | Known interface limitation. |
| A4T-06 | Important | Validator Python dependencies are not declared for a clean Python environment. | Reproducibility limitation. |
| A4T-07 | Important | `--skill-package` does not automate all installer, changelog-serving, and operations-guide content gates. | Command scope remains limited. |
| LMC-EVIDENCE | Release prerequisite | Project-designated ASD-STE100 Issue 9 checker/review evidence is not available in this runtime. | Stable promotion is blocked. |
| G13-RUNTIME | Release prerequisite | Clean Codex and Claude Code runtime execution tests have not run in this environment. | Stable promotion is blocked. |

The ADS 4 rc.1 critical findings A4T-01 and A4T-02 remain fixed in this candidate.
