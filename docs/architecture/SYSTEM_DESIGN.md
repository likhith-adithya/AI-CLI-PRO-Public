# AI CLI PRO: System Architecture Design

## 🏗️ 1. High-Level Architecture
AI CLI PRO is built on a **Stateless Service-Oriented Architecture (SOA)** designed specifically for the VS Code Extension environment. 

The core philosophy is: **No Third-Party Agent Execution in the Background.** AI CLI PRO itself performs lightweight background state checks and extension-level maintenance where enabled, but third-party AI agents are not silently executed as background processes. The extension acts as a lightweight, cross-platform launcher that delegates execution to the host OS terminal.

### 🔄 Data Flow Overview
1.  **Sidebar UI**: Requests the list of available CLI integrations.
2.  **Environment Detection Service**: Scans the user's `$PATH` (async/non-blocking) and updates the in-memory cache.
3.  **Config Manager**: Merges built-in registry defaults with user-defined settings.
4.  **Terminal Manager**: Resolves OS-specific commands and creates/manages VS Code terminal sessions.

---

## 🧩 2. Core Service Layers

### A. Data & Persistence (`src/models/`, `src/services/configManager.ts`)
*   **Static Registry (`registry.ts`)**: Hardcoded, internally reviewed installation definitions based on documented installation methods for supported tools. This is AI CLI PRO's integration metadata; the vendor's official documentation remains authoritative.
*   **Config Manager**: Manages user-specific overrides. It reads from VS Code's `settings.json` (`aiCliPro.agents`) and merges it with the Static Registry, ensuring user custom tools don't break built-in logic.

### B. Environment Detection Service (`src/services/environmentService.ts`)
*   **Asynchronous Detection**: Uses `child_process.exec` (Unix: `command -v`, Windows: `Get-Command`) to scan the user's `$PATH`.
*   **Optimistic Caching**: To prevent UI stuttering, detection results are cached in-memory (`states: Map`). The cache is only invalidated when a user explicitly initiates an install/uninstall action, ensuring fast sidebar rendering.

### C. The Execution Engine (`src/services/terminalManager.ts`)
*   **Cross-Platform Resolution**: Translates a generic installation intent into OS-specific execution. 
    *   *Example*: Resolves Unix `if [ "$(uname)" = "Darwin" ]; then ...` inline logic before sending strings to the terminal.
*   **Terminal Lifecycle**: Manages dedicated VS Code terminal instances per CLI integration. 
*   **Design Choice (Memory over Disk)**: Removing a CLI integration preserves the terminal session active in memory. This prevents loss of work if a user removes a CLI while a session is still active.

---

## 💻 3. UI and Presentation

### A. Sidebar Providers (`src/providers/agentTreeDataProvider.ts`)
The sidebar is powered by VS Code's `TreeDataProvider`. It maps the merged state (Registry + Environment Cache) into interactive UI items.
*   **Context Values**: Nodes are tagged with contexts (`installed`, `missing`, `suggested`) which dictates which inline actions (Play button vs Download cloud) appear next to them.

### B. Rich Renderers (`src/utils/markdownUtils.ts`, `src/ui/templates.ts`)
The "What's New" panel uses a custom regex-based parser to inject release notes (`docs/news/`) into a stylized Webview HTML template. This ensures a consistent visual experience regardless of the user's VS Code theme.

---

## 🛡️ 4. Security & Safety Principles

1.  **User-Visible Execution:** Supported CLI commands are executed through VS Code terminal sessions so that command execution is visible to the user. A VS Code terminal is a standard user terminal session, not a security sandbox.
2.  **No Credential Proxying:** The extension does not intentionally collect, extract, proxy, or transmit third-party authentication credentials. Authentication is delegated to the respective third-party CLI or provider.
3.  **Controlled Cleanup:** Removal operations target only the CLI binary that AI CLI PRO manages. User-created configuration files, authentication data, model data, cached downloads, project files, and unrelated system resources are not automatically deleted.
4.  **Explicit Execution:** Scripts are passed to the terminal visibly. The user can see exactly what is being executed (e.g., Homebrew, Pip, or NPM commands).
