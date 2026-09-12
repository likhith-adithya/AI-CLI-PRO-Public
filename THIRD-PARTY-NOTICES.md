# Third-Party Notices

AI CLI PRO ("the Extension") is an independent VS Code extension. It includes or depends upon third-party open-source software components. The licenses and copyright notices for these components remain applicable to their respective components and are not replaced by the Apache-2.0 license covering AI CLI PRO itself.

---

## 1. VS Code Extension API

The Extension is built using the VS Code Extension API, provided by Microsoft Corporation under the terms of the Visual Studio Code License and associated agreements.

---

## 2. @vscode/extension-telemetry (if included)

**Package:** `@vscode/extension-telemetry`  
**Publisher:** Microsoft  
**License:** MIT

The applicable license and copyright notices are retained with the corresponding package. For the complete license text, see the `LICENSE` file distributed with `@vscode/extension-telemetry` in your local `node_modules` directory or the [package repository](https://github.com/microsoft/vscode-extension-telemetry).

---

## 3. Node.js Dependencies

AI CLI PRO depends on several npm packages. Complete license information for all dependencies can be reviewed by running:

```bash
npx license-checker --summary
```

in the project directory, or by reviewing the `package-lock.json` and the `LICENSE` files distributed within each package in `node_modules/`.

---

## 4. Third-Party CLI Integrations (Not Distributed)

AI CLI PRO supports the following third-party CLI tools. These tools are **not bundled or redistributed** by AI CLI PRO unless expressly stated.

Important: AI CLI PRO may initiate or automate installation using official package managers or vendor-provided installers, but it does not bundle, redistribute, or repackage third-party CLIs unless explicitly authorized and documented. In other words, AI CLI PRO can invoke an official installer on the user's system, but it does not act as a redistributor of the third-party software.

They are installed by the user through official distribution channels.

| CLI | Provider | Distribution | License |
| --- | --- | --- | --- |
| Antigravity CLI (`agy`) | Google | Official installer | See provider terms |
| Gemini CLI (`gemini`) | Google | npm: `@google/gemini-cli` | See provider terms |
| Claude Code (`claude`) | Anthropic | npm: `@anthropic-ai/claude-code` | See provider terms |
| GitHub Copilot CLI | GitHub / Microsoft | npm: `@github/copilot` | See provider terms |
| Codex (`codex`) | OpenAI | npm: `@openai/codex` | See provider terms |
| Ollama | Ollama, Inc. | Official installer | MIT (Ollama binary); model licenses vary |
| Hugging Face CLI | Hugging Face | pip: `huggingface_hub[cli]` | Apache-2.0 |
| Jules CLI | Google | npm: `@google/jules` | See provider terms |
| Hermes Agent | NousResearch | Official installer | See provider terms |

**Note:** Individual models run through local runtimes such as Ollama may carry separate licenses (e.g., Llama, Mistral, DeepSeek, Phi, Qwen). Users are responsible for reviewing and complying with the applicable model license before use.

---

## 5. Trademarks

Product names, logos, and trademarks referenced in this project belong to their respective owners. References are made for identification, compatibility, and integration purposes only and do not imply affiliation, endorsement, or sponsorship.

---

*For questions regarding third-party licensing, please open an issue at:*  
[https://github.com/likhith-adithya/AI-CLI-PRO-Public/issues](https://github.com/likhith-adithya/AI-CLI-PRO-Public/issues)
