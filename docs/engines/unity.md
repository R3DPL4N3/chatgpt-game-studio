# Unity playbook

Read the actual project before choosing APIs or packages. Record Unity version, render pipeline, input system, networking stack, test packages, and platform in `studio/PROJECT.md`.

- Runtime behavior generally belongs in small existing C# components. Keep designer values and object references editable where the project already uses the Inspector.
- Prefer existing scenes, prefabs, UI, input actions, and serialized references. Do not replace editor-authored UI with an unrelated code-created hierarchy without approval.
- Preserve `.meta` files and GUID relationships. Do not regenerate or mass-edit serialized assets merely to wire a reference.
- Check scene/prefab overrides, disabled objects, missing components, event subscriptions, and cleanup when entering/leaving play mode.
- Use the project's installed Unity Test Framework and existing EditMode/PlayMode tests where appropriate. Verify command syntax for that exact version; do not invent batch commands.
- For multiplayer, identify authoritative state, owner input, prediction/interpolation, and server-side validation in the chosen stack. Do not assume networking behavior from another library.

Acceptance: compile, applicable tests, editor wiring inspection, actual play-mode behavior, and relevant player build/network roles. Document unrun stages separately.

Official starting point: https://docs.unity3d.com/Manual/index.html . Use the version selector matching the project, then its testing and package documentation.
