# DK Code Factory

Independent MIT skills for Claude Code and Codex. Choose each plugin separately.

| Plugin | Claude Code | Codex | Optional tools |
|---|---|---|---|
| [dk-workflows](https://github.com/dk-code-factory/dk-workflows) | Native, 14 skills | Native, 14 skills | Selected reviewers only |
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

Python 3.11+ supports lifecycle helpers; Git and authenticated gh are needed for GitHub workflows. Authenticate each host through its normal login. DK works with no reviewers for unrelated workflows and uses bundled drafting by default. Select reviewer or replacement drafting bindings through dk-config. Reviewer implementations and external tools remain optional.

Both catalogs reference the implementation repositories' released `main` branches. Each plugin starts at 1.0.0, versions independently, and publishes `vX.Y.Z` GitHub releases. Each plugin ships its own standard-library updater with notify (default), auto, and off policies. Native host updating is separate; see each implementation README. This repository has no runtime, dependency installation, submodules, or generated plugin copies.
