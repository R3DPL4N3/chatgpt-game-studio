# Unreal playbook

Inspect the `.uproject`, engine association/version, modules, input system, GameMode/Pawn/Controller setup, and current Blueprints before changing anything. Record real build targets and paths in `studio/PROJECT.md`.

- Put reusable runtime logic in focused C++ classes when that matches the project. Thin Blueprint children, editor-tuned properties, components, meshes, materials, and AnimBlueprints remain useful; “C++ first” does not mean deleting all Blueprints.
- Do not overwrite binary `.uasset` or `.umap` files blindly. Use supported editor operations, and describe exact manual steps if editor access is unavailable.
- Preserve Blueprint parents, inherited defaults, references, input contexts, and possession behavior when migrating a feature. Migrate one feature, then test before removing its old path.
- Check UHT/reflection changes, module dependencies, build configuration, and editor restart/full-build needs. Do not treat IntelliSense warnings or Live Coding output alone as the final build result.
- For networked movement, inspect authority, ownership, RPC context, prediction and corrections. Do not run two competing movement systems on the same owned character.
- The server must validate client requests according to the game's rules. Navigation projection alone is not a complete anti-cheat or authority design.

Acceptance: appropriate C++ build, relevant automation tests, Blueprint compile/reference inspection, PIE behavior, and affected server/owner/observer roles. Standalone, listen-server, dedicated-server, and packaged tests are distinct; report exactly which ran.

Official starting points:
- https://dev.epicgames.com/documentation/en-us/unreal-engine/testing-and-optimizing-your-content
- https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-networked-movement-in-the-character-movement-component-for-unreal-engine

Use documentation matching the actual engine version. This playbook does not supply a universal build command or a working game implementation.
