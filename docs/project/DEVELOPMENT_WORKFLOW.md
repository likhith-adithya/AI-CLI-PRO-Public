# 🔄 AI CLI PRO: Standard Development Workflow

This document defines the end-to-end lifecycle for implementing features, fixing bugs, and releasing new versions. Adherence to this workflow is mandatory to maintain the **Technical Integrity** of the project.

---

## 🚀 Phase 1: Research & Grounding
Before writing a single line of code, you must ground your implementation in official documentation.

1.  **Requirement Analysis**: Review `SPEC.md` and `GEMINI.md` to ensure the task aligns with project goals.
2.  **Official Documentation (Grounding)**: If adding or updating a CLI tool, verify the latest installation/uninstallation commands from the official repository (e.g., GitHub, official docs).
3.  **Cross-Platform Verification**: Check that the commands work for **macOS (Intel & M1)**, **Linux (Debian/Ubuntu)**, and **Windows (PowerShell)**.

---

## 🛠️ Phase 2: Implementation (Stateless & OS-Agnostic)
Implement your changes following the modular service-oriented architecture.

1.  **Update Registry/Model**: If adding a tool, update `src/models/registry.ts` and `src/models/agent.ts`.
2.  **Stateless Service Logic**: Ensure all new logic lives in the appropriate service (e.g., `EnvironmentService` for detection, `TerminalManager` for execution).
3.  **UI Integration**: Add the necessary commands to `src/commands/` and register them in `package.json`.
4.  **No "Hidden" Logic**: Never use reflection or prototype manipulation. Use explicit types and interfaces.

---

## 🧪 Phase 3: Multi-OS Functional Validation
**STATIC CHECKS ARE INSUFFICIENT.** Every behavioral change must be verified on live systems.

1.  **Compile & Lint**:
    ```bash
    npm run compile
    npm run lint
    ```
2.  **Functional Testing**:
    - **Provisioning**: Trigger "Install" and verify the CLI is correctly added to the system.
    - **Launching**: Verify the "Launch" button opens a terminal and starts the tool correctly.
    - **Uninstallation**: Verify "Uninstall" removes binaries and cleans up environment paths.
3.  **Regression Testing**: Run the private test suite: `./local-tests/run.sh`.

---

## 📦 Phase 4: Release & Documentation
A feature is not "Done" until it is documented and ready for the user.

1.  **Version Bump**: Update `version` in `package.json`.
2.  **Release Notes**: Create a new release file in `docs/news/v<version>.md`. 
    - *Note*: This is critical for the "What's New" panel to appear.
3.  **Sync Badge**: Run `npm run sync-version` to update the README.
4.  **Final Verification**: Perform a final `npm run compile` and `npm run lint`.

---

## 🛑 Ripple Effect Checklist
Before submitting a PR, verify you haven't broken these links:
- [ ] **Type Safety**: Did I change `agent.ts`? If so, did I update all services?
- [ ] **Sidebar Sync**: Does the `EnvironmentService` correctly trigger a refresh after my action?
- [ ] **OS Compatibility**: Did I test my new command on Windows PowerShell and macOS/Linux Bash?
- [ ] **Telemetry**: Did I add a telemetry event in `agentCommands.ts` for the new action?

---

## 🤝 Contribution Guidelines
*   **Atomic Commits**: Keep commits focused on a single logical change.
*   **JSDoc Documentation**: All public methods MUST have JSDoc comments explaining parameters and the "Why" behind the logic.
*   **Zero Tolerance for Hacks**: No `@ts-ignore`, no `any`, and no disabling lint rules without a Senior Architect's review.
