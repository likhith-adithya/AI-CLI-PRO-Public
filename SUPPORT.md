# Support

## Supported Platforms

| Platform | Status |
| --- | --- |
| macOS (12 Monterey and later) | ✅ Supported |
| Windows 10 / 11 (PowerShell 5.1+) | ✅ Supported |
| Linux (Debian/Ubuntu, RHEL/Fedora) | ✅ Supported |

## Supported VS Code Versions

AI CLI PRO requires **VS Code 1.80.0 or later**.

## Supported CLI Versions

AI CLI PRO launches and manages CLI tools that are already installed and available on the user's `$PATH`. Version compatibility depends on the respective provider's current release.

| CLI | Minimum tested version | Distribution |
| --- | --- | --- |
| Antigravity CLI (`agy`) | Latest stable | Official installer |
| Gemini CLI (`gemini`) | Latest stable | npm: `@google/gemini-cli` |
| Claude Code (`claude`) | Latest stable | npm: `@anthropic-ai/claude-code` |
| GitHub Copilot CLI | Latest stable | npm: `@github/copilot` |
| Codex (`codex`) | Latest stable | npm: `@openai/codex` |
| Ollama | 0.20+ | Official installer |
| Hugging Face CLI | Latest stable | pip: `huggingface_hub[cli]` |

## Installation Requirements

*   **Node.js / npm** — required for npm-distributed CLIs (Gemini, Claude, Copilot, Codex)
*   **Python / pip** — required for pip-distributed CLIs (Hugging Face CLI)
*   **curl** — required for installer-script-based CLIs (Antigravity, Ollama, Hermes)
*   **Homebrew (macOS)** — recommended for macOS package management
*   **PowerShell 5.1+ (Windows)** — required for Windows installer scripts

## Provider-Specific Requirements

Each third-party CLI may require:

*   A valid account with the provider
*   An active subscription or license
*   API access or OAuth authentication
*   Acceptance of the provider's terms of service

AI CLI PRO does not provide or manage these requirements. Refer to each provider's documentation.

## Known Limitations

*   AI CLI PRO launches CLIs in VS Code terminal sessions. Behavior depends on the user's shell configuration and PATH.
*   Uninstall workflows remove the CLI binary only; user data, model files, and configuration directories are not automatically deleted.
*   Provisioning via `curl | bash` scripts requires internet access and may need elevated privileges on some systems.
*   Local model availability depends on Ollama's current model library. Model licenses vary.

## Getting Help

*   **Bug Reports:** [https://github.com/likhith-adithya/AI-CLI-PRO-Public/issues/new?title=Bug+Report](https://github.com/likhith-adithya/AI-CLI-PRO-Public/issues/new?title=Bug+Report)
*   **Feature Requests:** [https://github.com/likhith-adithya/AI-CLI-PRO-Public/issues/new?title=Feature+Request](https://github.com/likhith-adithya/AI-CLI-PRO-Public/issues/new?title=Feature+Request)
*   **Security Issues:** See [SECURITY.md](./SECURITY.md)
*   **General Discussion:** [https://github.com/likhith-adithya/AI-CLI-PRO-Public/issues](https://github.com/likhith-adithya/AI-CLI-PRO-Public/issues)

## Security Reporting

Please report security vulnerabilities privately. See [SECURITY.md](./SECURITY.md) for instructions.
