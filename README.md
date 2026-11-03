# DK Code Factory

Independent MIT skills for Claude Code and Codex. Choose each plugin separately.

| Plugin | Claude Code | Codex | Optional tools |
|---|---|---|---|
| [dk-workflows](https://github.com/dk-code-factory/dk-workflows) | Native, 3 skills | Native, 3 skills | Selected reviewers only |
| [dk-pr-skills](https://github.com/dk-code-factory/dk-pr-skills) | Native, 13 skills | Native, 13 skills | Git and authenticated gh for remote PR work |
| [dk-architecture](https://github.com/dk-code-factory/dk-architecture) | Native, 3 skills | Native, 3 skills | Git |
| [code-review-ad](https://github.com/dk-code-factory/code-review-ad) | Native AD | Native AD | Node.js inventory helper |
| [code-review-matpocock](https://github.com/dk-code-factory/code-review-matpocock) | Bundled MIT adaptation | Native review | None |
| [code-review-qodo](https://github.com/dk-code-factory/code-review-qodo) | Portable Qodo workflow | Portable Qodo workflow | Qodo CLI and account |

## Install through the organization catalog

Claude Code:

```text
/plugin marketplace add dk-code-factory/skills
/plugin install code-review-ad@dk-code-factory
```

Codex:

```sh
codex plugin marketplace add dk-code-factory/skills
codex plugin add code-review-ad@dk-code-factory
```

Replace `code-review-ad` with any plugin above. Adding this catalog does not install all plugins. Each implementation also offers a standalone marketplace with the same name as its repository. For example, independent AD installation:

```text
Claude:
/plugin marketplace add dk-code-factory/code-review-ad
/plugin install code-review-ad@code-review-ad

Codex:
codex plugin marketplace add dk-code-factory/code-review-ad
codex plugin add code-review-ad@code-review-ad
```

Python 3.11+ supports the deterministic helpers; Git and authenticated gh are needed for remote PR work. Authenticate each host through its normal login. dk-workflows coordinates selected installed skills and has no default reviewer. dk-pr-skills owns drafting, Decisions, feedback, publication, cleanup and CI. dk-architecture is independently usable and is never automatically invoked or required by workflow v2. Select workflow skills/reviewers through dk-config and domain settings through their owner.

Both catalogs reference the implementation repositories' released `main` branches. Each plugin versions independently and publishes `vX.Y.Z` GitHub releases. Follow each implementation README for native host installation and updates. The v2 workflow and extracted domain packages have no custom updater lifecycle. This repository has no runtime, dependency installation, submodules, or generated plugin copies.
