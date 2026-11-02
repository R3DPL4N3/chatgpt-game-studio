# Agent roster

49 native Codex agent definitions. The main session selects a small team; these are not 49 simultaneous processes.

## Art

- **art-director** → lead: creative-director. Owns visual identity — style guides, art bible, asset standards, color palettes, UI visual direction.
- **technical-artist** → lead: art-director. Technical artist bridging art and engineering — shaders, VFX, rendering optimization, art pipeline tools, art-to-engine issues.

## Audio

- **audio-director** → lead: creative-director. Owns sonic identity — music direction, sound palette, audio implementation strategy, mix balance.
- **sound-designer** → lead: audio-director. SFX specifications and spec sheets — audio event documentation, mixing parameters, sound category definitions.

## Design

- **accessibility-specialist** → lead: ux-designer. Accessibility standards and assistive features — remapping, text scaling, colorblind modes, screen reader support.
- **economy-designer** → lead: game-designer. Resource economies — loot tables, sink/faucet analysis, progression curve calibration, economic balance.
- **game-designer** → lead: creative-director. Mechanical and systems design — core loops, progression, combat, economy, player-facing rules. Mechanics-level questions.
- **level-designer** → lead: game-designer. Spatial design for levels and areas — encounter layouts, pacing, difficulty, layout planning, environmental storytelling.
- **live-ops-designer** → lead: producer. Post-launch content — seasonal events, battle passes, content cadence, retention, engagement analytics. Keeps the game fresh.
- **localization-lead** → lead: producer. Internationalization architecture — i18n system design, string extraction workflows, locale testing, locale-specific issues, translation pipeline.
- **systems-designer** → lead: game-designer. Detailed subsystem mechanics — combat formulas, progression curves, crafting recipes, status effect interactions, mathematical modeling of a mechanic.
- **ux-designer** → lead: art-director. User experience flows, interaction design, information architecture — user flow mapping, interaction pattern design, onboarding, accessibility requirements.

## Direction

- **creative-director** → lead: producer. Highest creative authority — vision, tone, aesthetic direction. Use when a decision affects game identity or department leads deadlock.
- **producer** → lead: main coordinator. Production concerns — sprint planning, milestone tracking, risk, scope, cross-department coordination when multiple departments must synchronize.
- **technical-director** → lead: producer. High-level technical decisions — engine architecture, technology choices, performance strategy, technical risk, cross-system conflicts.

## Engine

- **godot-csharp-specialist** → lead: godot-specialist. Godot 4 C# quality — .NET patterns, attribute-based exports, signal delegates, async patterns, type-safe node access.
- **godot-gdextension-specialist** → lead: godot-specialist. Native code integration with Godot — GDExtension API, godot-cpp and godot-rust bindings, custom node types, the native boundary.
- **godot-gdscript-specialist** → lead: godot-specialist. GDScript code quality — static typing enforcement, signal architecture, coroutine patterns, GDScript idioms, typed and performant.
- **godot-shader-specialist** → lead: godot-specialist. Godot rendering customization — shading language, visual shaders, material setup, particle shaders, post-processing.
- **godot-specialist** → lead: technical-director. Authority on Godot-specific patterns and APIs — node/scene architecture, signals, resources; guides GDScript vs C# vs GDExtension.
- **ue-blueprint-specialist** → lead: unreal-specialist. Blueprint architecture and Blueprint/C++ boundary — optimization, maintainable graphs. Prevents Blueprint spaghetti, enforces clean BP patterns.
- **ue-gas-specialist** → lead: unreal-specialist. Gameplay Ability System — abilities, gameplay effects, attribute sets, tags, ability tasks, prediction. Prevents common GAS anti-patterns.
- **ue-replication-specialist** → lead: unreal-specialist. Unreal networking — property replication, RPCs, client prediction, relevancy, net serialization, bandwidth. Server-authoritative architecture.
- **ue-umg-specialist** → lead: unreal-specialist. Unreal UI implementation — UMG widget hierarchy, data binding, CommonUI input routing, widget styling, UI optimization.
- **unity-addressables-specialist** → lead: unity-specialist. Unity asset management — Addressable groups, loading/unloading, content catalogs, remote delivery, asset bundle optimization, fast load times.
- **unity-dots-specialist** → lead: unity-specialist. Unity Data-Oriented Technology Stack — Entity Component System, Jobs, Burst compiler optimization, hybrid renderer, correct ECS patterns.
- **unity-shader-specialist** → lead: unity-specialist. Unity rendering — Shader Graph, custom HLSL, VFX Graph, render pipeline customization (URP/HDRP), post-processing within performance budgets.
- **unity-specialist** → lead: technical-director. Authority on Unity-specific patterns and APIs — guides MonoBehaviour vs DOTS/ECS, Unity subsystems including Addressables and Input System.
- **unity-ui-specialist** → lead: unity-specialist. Unity UI implementation — UI Toolkit (UXML/USS), UGUI Canvas, data binding, runtime UI performance, cross-platform adaptation.
- **unreal-specialist** → lead: technical-director. Authority on Unreal-specific patterns and APIs — guides Blueprint vs C++, UE subsystems (GAS, Enhanced Input, Niagara, etc.).

## Engineering

- **ai-programmer** → lead: lead-programmer. Implements game AI — behavior trees, state machines, pathfinding, perception, decision-making, NPC and enemy behavior, AI debugging.
- **analytics-engineer** → lead: technical-director. Telemetry and analytics — event tracking, player behavior, A/B test frameworks, dashboard specification, data pipelines.
- **devops-engineer** → lead: technical-director. Build pipelines, CI/CD configuration, version control workflow, branching strategy, automated test pipelines, deployment infrastructure.
- **engine-programmer** → lead: lead-programmer. Core engine systems — rendering pipeline, physics, memory, resource loading, scene management, performance-critical framework code.
- **gameplay-programmer** → lead: lead-programmer. Implements designed mechanics as code — player systems, combat, interactive features, gameplay system code.
- **lead-programmer** → lead: technical-director. Lead programmer — code-level architecture, coding standards, code review, API design, refactoring strategy, assigning work to specialist programmers.
- **network-programmer** → lead: lead-programmer. Multiplayer networking — state replication, lag compensation, matchmaking, network protocol, netcode and bandwidth optimization.
- **performance-analyst** → lead: technical-director. Performance analyst — profiling, bottlenecks, memory analysis, frame time investigation, recommends optimizations, tracks metrics over time.
- **prototyper** → lead: lead-programmer. Throwaway builds — concept prototypes after brainstorm to test an idea is fun before GDDs; vertical slices pre-production. Speed over standards.
- **security-engineer** → lead: technical-director. Protects against cheating, exploits, breaches — anti-cheat measures, secure save data and network comms, player privacy compliance.
- **tools-programmer** → lead: lead-programmer. Internal dev tools — editor extensions, content authoring tools, debug utilities, pipeline automation, editor workflow.
- **ui-programmer** → lead: lead-programmer. Implements user interface systems — menus, HUDs, inventory screens, dialogue boxes, UI framework code, screen flow.

## Narrative

- **narrative-director** → lead: creative-director. Story architecture, world-building, character design, dialogue strategy. Narrative structure and direction rather than writing individual lines.
- **world-builder** → lead: narrative-director. World builder for lore — factions, cultures, history, geography, ecology, world rules. Faction design, lore consistency checks.
- **writer** → lead: narrative-director. Writer of player-facing text — dialogue, lore entries, item and ability descriptions, environmental text.

## Production

- **community-manager** → lead: producer. Player-facing communication — patch notes, social posts, community updates, feedback collection, player bug triage, crisis communication.
- **release-manager** → lead: producer. Release pipeline — certification checklists, store submissions and page prep, platform requirements, version numbering, release-day coordination.

## Quality

- **qa-lead** → lead: producer. Test strategy and process — test plan creation, bug severity assessment, regression planning, release quality gates, readiness evaluation.
- **qa-tester** → lead: qa-lead. Writes test cases, bug reports, and checklists — test case generation, regression checklist creation, execution documentation.

