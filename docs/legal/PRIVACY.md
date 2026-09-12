# Privacy Policy for AI CLI PRO

**Effective Date:** May 15, 2026  
**Version:** 1.2

AI CLI PRO ("we," "our," or "the Extension") is committed to transparency about how the extension functions and what data, if any, it handles. This policy describes our data practices and your rights.

---

### 1. Architecture: Local-First Design

The Extension is built on a **local-first** architecture. AI CLI PRO operates as a launcher and lifecycle manager for third-party command-line tools running in the user's own terminal. It does not operate a backend server that processes your prompts or agent outputs.

---

### 2. What AI CLI PRO Does Not Intentionally Collect

*   **No Third-Party Credentials:** AI CLI PRO does not request, store, or transmit your API keys, OAuth tokens, or passwords. All authentication remains managed by the respective third-party CLI tools in their local configuration directories.
*   **No Prompts or Code:** AI CLI PRO does not intercept, read, or transmit the prompts, code, or responses exchanged between you and a third-party CLI.
*   **No Sale of Data:** We do not sell user data to third parties.

---

### 3. Telemetry

AI CLI PRO may collect limited technical telemetry to understand extension usage, reliability, and compatibility characteristics. Telemetry behavior follows VS Code's global telemetry settings — if you have disabled telemetry in VS Code, AI CLI PRO respects that setting.

Depending on your VS Code telemetry configuration, telemetry may include technical information such as:

*   AI CLI PRO version
*   VS Code version
*   Operating system and architecture
*   Basic hardware characteristics
*   Installation or availability state of supported CLI integrations (e.g., "Gemini CLI detected: true/false")
*   Anonymous feature usage events (e.g., "provision workflow initiated")
*   Technical error information

**Telemetry does not include:**

*   API keys, OAuth tokens, or passwords
*   Prompt content or AI-generated responses
*   Source code or workspace file contents
*   Authentication credentials belonging to third-party CLI providers

You can control telemetry via VS Code's `telemetry.telemetryLevel` setting. Setting it to `off` disables telemetry collection for AI CLI PRO.

---

### 4. Third-Party Services & CLI Tools

AI CLI PRO serves as a launcher and lifecycle manager for independent third-party tools (e.g., Gemini CLI, Claude Code, GitHub Copilot CLI, Ollama).

*   **Direct Interaction:** When you use a third-party CLI, your data (including prompts and code) is transmitted directly between the CLI on your machine and the third-party provider. This data is governed by the third party's privacy policy, not by this document.
*   **No Interception:** AI CLI PRO does not proxy, monitor, or intercept the communication between the third-party CLI and its provider.
*   **Package Managers:** Operations like "Provision" or "Update" connect directly to official registries (e.g., npm, PyPI, Homebrew). These connections are standard and direct.

---

### 5. Local Data Storage

To provide its functionality, the Extension stores minimal configuration data (e.g., your preferred CLI visibility settings) locally on your device using the VS Code Global State API.

*   **Control:** You can view, modify, or delete this data at any time by clearing your VS Code global storage or uninstalling the extension.

---

### 6. Legal Requests for Information

AI CLI PRO does not intentionally collect user content or authentication credentials. Because we do not centrally store personal data or credentials, we have very limited data to provide in response to legal requests. Any telemetry data we do retain is governed by applicable law and our retention policies.

---

### 7. Children's Privacy

The Extension is a developer tool and is not directed at children under the age of 16. We do not knowingly collect information from children.

---

### 8. Geographic Information

Telemetry infrastructure may derive coarse geographic information (such as country or region) from network metadata as part of standard telemetry processing. We do not intentionally store raw IP addresses as part of AI CLI PRO's telemetry pipeline.

---

### 9. Changes to This Policy

We reserve the right to update this Privacy Policy to reflect changes in the Extension's functionality, telemetry implementation, or legal requirements. Updates will be noted in the extension's version history and the repository.

---

### 10. Contact Us

For privacy-related inquiries, please open a public issue on our tracker:  
[https://github.com/likhith-adithya/AI-CLI-PRO-Public/issues](https://github.com/likhith-adithya/AI-CLI-PRO-Public/issues)
