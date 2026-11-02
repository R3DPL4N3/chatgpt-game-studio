---
name: game-implement-feature
description: Implement one authorized game feature in small understandable changes. Use after scope is clear, not for speculative rewrites or planning-only requests.
---

1. Confirm the requested outcome and authorization, read applicable instructions, inspect the working tree, and preserve existing work.
2. Read `studio/engines/unity.md` or `studio/engines/unreal.md` for the selected engine if installed. In the toolkit use `docs/engines/`. Verify version-specific APIs against the actual project and official docs.
3. Use existing architecture and assets. Keep runtime logic and editor wiring deliberately separated. Do not silently create duplicate canvases, inputs, prefabs, components, or Blueprints.
4. Make one coherent change. Do not bypass permissions, install unrequested software, invent object references, or overwrite binary editor assets blindly.
5. Add or update focused tests where feasible. Record exact build/test commands and results. If an editor operation cannot be performed, describe the precise manual step and mark dependent validation blocked.
6. Inspect the final diff. Run game-review-test, using an independent reviewer only if supported; otherwise identify self-review.
7. Explain changed files, design reason, test evidence, limitations, and how the user can observe the result. Do not mark the feature verified if required gameplay checks were not run.

Never equate a generated code file, clean compiler output, or a screenshot of the editor with proof that the requested game behavior works.
