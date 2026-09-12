# Third-Party CLI Integration Register

This document is AI CLI PRO's internal compliance register. It records the reviewed integration metadata for each supported CLI, including distribution method, license status, authentication model, and whether AI CLI PRO redistributes the software.

> **Note:** Provider terms, distribution methods, and license conditions can change. Each entry records a "Last Reviewed" date. Review entries when publishing a new release.

---

## Integration Register

### Antigravity CLI

| Field | Value |
| --- | --- |
| **CLI command** | `agy` |
| **Provider** | Google |
| **Trademark owner** | Google LLC |
| **Distribution** | Official installer script |
| **Install source** | `https://antigravity.google/cli/install.sh` |
| **AI CLI PRO redistributes** | No |
| **AI CLI PRO modifies** | No |
| **Authentication** | Handled by Antigravity CLI / Google account |
| **API proxy** | No |
| **Update mechanism** | `agy update` |
| **Known restrictions** | Subject to Google Antigravity terms of service |
| **Official docs** | https://antigravity.google |
| **Last reviewed** | 2026-09-12 |

---

### Gemini CLI

| Field | Value |
| --- | --- |
| **CLI command** | `gemini` |
| **Provider** | Google |
| **Trademark owner** | Google LLC |
| **Distribution** | npm |
| **Package** | `@google/gemini-cli` |
| **AI CLI PRO redistributes** | No |
| **AI CLI PRO modifies** | No |
| **Authentication** | Handled by Gemini CLI / Google account |
| **API proxy** | No |
| **Update mechanism** | `npm update -g @google/gemini-cli` |
| **Known restrictions** | Subject to Google Gemini terms of service and usage policies |
| **Official docs** | https://github.com/google-gemini/gemini-cli |
| **Last reviewed** | 2026-09-12 |

---

### Claude Code

| Field | Value |
| --- | --- |
| **CLI command** | `claude` |
| **Provider** | Anthropic |
| **Trademark owner** | Anthropic, PBC |
| **Distribution** | npm |
| **Package** | `@anthropic-ai/claude-code` |
| **AI CLI PRO redistributes** | No |
| **AI CLI PRO modifies** | No |
| **Authentication** | Handled by Claude Code / Anthropic account |
| **API proxy** | No |
| **Update mechanism** | `npm update -g @anthropic-ai/claude-code` |
| **Known restrictions** | Subject to Anthropic terms of service and usage policies |
| **Official docs** | https://docs.anthropic.com/en/docs/claude-code |
| **Last reviewed** | 2026-09-12 |

---

### GitHub Copilot CLI

| Field | Value |
| --- | --- |
| **CLI command** | `copilot` |
| **Provider** | GitHub / Microsoft |
| **Trademark owner** | Microsoft Corporation |
| **Distribution** | npm |
| **Package** | `@github/copilot` |
| **AI CLI PRO redistributes** | No |
| **AI CLI PRO modifies** | No |
| **Authentication** | Handled by GitHub CLI / GitHub account with Copilot subscription |
| **API proxy** | No |
| **Update mechanism** | `npm install -g @github/copilot@latest` |
| **Known restrictions** | Requires active GitHub Copilot subscription; subject to GitHub terms |
| **Official docs** | https://docs.github.com/en/copilot/github-copilot-in-the-cli |
| **Last reviewed** | 2026-09-12 |

---

### Codex

| Field | Value |
| --- | --- |
| **CLI command** | `codex` |
| **Provider** | OpenAI |
| **Trademark owner** | OpenAI OpCo, LLC |
| **Distribution** | npm |
| **Package** | `@openai/codex` |
| **AI CLI PRO redistributes** | No |
| **AI CLI PRO modifies** | No |
| **Authentication** | Handled by Codex CLI / OpenAI account |
| **API proxy** | No |
| **Update mechanism** | `npm update -g @openai/codex` |
| **Known restrictions** | Subject to OpenAI terms of service and usage policies |
| **Official docs** | https://github.com/openai/codex |
| **Last reviewed** | 2026-09-12 |

---

### Ollama

| Field | Value |
| --- | --- |
| **CLI command** | `ollama` |
| **Provider** | Ollama, Inc. |
| **Trademark owner** | Ollama, Inc. |
| **Distribution** | Official installer script |
| **Install source** | `https://ollama.com/install.sh` |
| **AI CLI PRO redistributes** | No |
| **AI CLI PRO modifies** | No |
| **Authentication** | Local — no provider account required for the Ollama binary |
| **API proxy** | No |
| **Update mechanism** | Re-run official installer |
| **Known restrictions** | Ollama binary: MIT license. Individual models have separate licenses (Llama, Mistral, DeepSeek, Qwen, Phi, etc.) |
| **Model licensing note** | Users are responsible for reviewing the license of each model they download via Ollama |
| **Official docs** | https://ollama.com |
| **Last reviewed** | 2026-09-12 |

---

### Hugging Face CLI

| Field | Value |
| --- | --- |
| **CLI command** | `huggingface-cli` |
| **Provider** | Hugging Face |
| **Trademark owner** | Hugging Face, Inc. |
| **Distribution** | pip |
| **Package** | `huggingface_hub[cli]` |
| **AI CLI PRO redistributes** | No |
| **AI CLI PRO modifies** | No |
| **Authentication** | Handled by Hugging Face CLI / Hugging Face account (for gated models) |
| **API proxy** | No |
| **Update mechanism** | `pip install -U huggingface_hub[cli]` |
| **Known restrictions** | Individual models may require acceptance of model-specific licenses; subject to Hugging Face terms |
| **Official docs** | https://huggingface.co/docs/huggingface_hub/guides/cli |
| **Last reviewed** | 2026-09-12 |

---

### Jules CLI

| Field | Value |
| --- | --- |
| **CLI command** | `jules` |
| **Provider** | Google |
| **Trademark owner** | Google LLC |
| **Distribution** | npm |
| **Package** | `@google/jules` |
| **AI CLI PRO redistributes** | No |
| **AI CLI PRO modifies** | No |
| **Authentication** | Handled by Jules CLI / Google account |
| **API proxy** | No |
| **Update mechanism** | `npm update -g @google/jules` |
| **Known restrictions** | Subject to Google terms of service |
| **Official docs** | See provider documentation |
| **Last reviewed** | 2026-09-12 |

---

### Hermes Agent

| Field | Value |
| --- | --- |
| **CLI command** | `hermes` |
| **Provider** | NousResearch |
| **Trademark owner** | NousResearch |
| **Distribution** | Official installer script |
| **Install source** | `https://hermes-agent.nousresearch.com/install.sh` |
| **AI CLI PRO redistributes** | No |
| **AI CLI PRO modifies** | No |
| **Authentication** | Handled by Hermes Agent / NousResearch account |
| **API proxy** | No |
| **Update mechanism** | `hermes update` |
| **Known restrictions** | Subject to NousResearch terms of service |
| **Official docs** | See provider documentation |
| **Last reviewed** | 2026-09-12 |

---

## Review Schedule

This register should be reviewed for each release that adds, removes, or modifies a CLI integration. Update the "Last reviewed" date whenever an entry is verified against current provider documentation.
