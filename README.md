<h1 align="center">✨ AI CLI PRO</h1>

<p align="center">
  <b>An Independent AI & Developer CLI Command Center for VS Code.</b><br>
  <i>Discover, launch, provision, and manage supported AI and developer CLIs directly from your editor.</i>
</p>

<p align="center">
  <a href="https://marketplace.visualstudio.com/items?itemName=likhith-adithya.ai-cli-pro">
    <img src="https://img.shields.io/badge/Version-0.0.87-6A11CB?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="Version">
  </a>
  <img src="https://img.shields.io/badge/Status-Tested-2ECC71?style=for-the-badge&logo=checkmarx&logoColor=white" alt="Status">
  <img src="https://img.shields.io/badge/Focus-CLI_Management-FF9F43?style=for-the-badge" alt="Focus">
  <img src="https://img.shields.io/badge/Platform-macOS_|_Win_|_Linux-2575FC?style=for-the-badge" alt="Platforms">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/likhith-adithya/AI-CLI-PRO-Public/main/icon.png" width="256" alt="AI CLI PRO Logo">
</p>



<p align="center">
  <img src="https://raw.githubusercontent.com/likhith-adithya/AI-CLI-PRO-Public/main/assets/FILE1.gif" width="100%" alt="AI CLI PRO Demo">
</p>



---

## ⚡️ Core Capabilities

| 🧩 **Unified Interface** | 🚀 **Guided Setup** | 🛡️ **Local Execution** |
| :--- | :--- | :--- |
| One sidebar for supported AI and developer CLIs, from cloud-based assistants such as Gemini CLI and Claude Code to local tools such as Ollama. | Missing a supported CLI? Select **Provision** to start a guided installation using the configured package manager for that tool. | Run compatible open-weight models locally through supported local runtimes such as Ollama, keeping inference on your machine when the selected model and configuration support local execution. |

---

## 🚀 Getting Started

### 📦 Installation
Getting AI CLI PRO running in your editor takes less than a minute.

**Method 1: VS Code Marketplace (Recommended)**
1. Open VS Code.
2. Go to the Extensions view (`Cmd+Shift+X` or `Ctrl+Shift+X`).
3. Search for **AI CLI PRO**.
4. Click **Install**.

**Method 2: Quick Command**
1. Press `Cmd+P` (macOS) or `Ctrl+P` (Windows/Linux) to open the Quick Open panel.
2. Paste the following command and hit Enter:
   ```bash
   ext install likhith-adithya.ai-cli-pro
   ```

---

## 🎮 How to Use

### 1️⃣ **Discovery**
Open the **AI CLI PRO Sidebar** (terminal icon 📟). Your configured CLI integrations are listed with their current installation status.

### 2️⃣ **Provisioning**

Missing a supported CLI? Select **Provision** to start a guided installation using the configured package manager or installation method associated with that tool.

> AI CLI PRO does not bundle or modify third-party AI services. Installation commands are executed visibly through the user's local VS Code terminal. The user remains responsible for the third-party tool's license, account, subscription, and terms of service.

### 3️⃣ **Execution**

Select **Launch ▶️** to start the selected CLI in a VS Code terminal.

> AI CLI PRO launches the CLI available on the user's system. Authentication, credentials, subscriptions, API access, and communication with the underlying provider remain under the control of that third-party CLI.

---

## 🤖 Supported CLI Integrations

AI CLI PRO provides a unified interface for supported third-party AI and developer CLIs. Product names and services remain owned and operated by their respective providers.

### ☁️ **Cloud CLIs**
*   **Antigravity CLI** • CLI support for the Google Antigravity ecosystem.
*   **Gemini CLI** • Access Google's Gemini capabilities through the official Gemini CLI.
*   **Claude Code** • Anthropic's coding-focused CLI.
*   **GitHub Copilot CLI** • GitHub's command-line interface for Copilot.
*   **Codex** • OpenAI's coding-focused CLI.

### 🦙 **Local Runtime Support (via Ollama)**
*   **DeepSeek, Llama, Mistral, Phi, Qwen** • Run compatible open-weight models locally through Ollama. Model availability and licensing depend on the individual model — see [Model Licensing](#-model-licensing) below.

> **Note:** "Supported" means AI CLI PRO provides one or more documented integration workflows for the tool, such as launch, provisioning, update, or removal. Support does not imply affiliation, endorsement, certification, authorization, or ownership by the third-party provider. See [Legal & Third-Party Notice](#️-legal--third-party-notice) below.

---

## ✨ Features

*   **🚀 Fast Sidebar**: Loads with VS Code, keeping your workflow fluid.
*   **🛠️ CLI Lifecycle Management**: Detect supported tools and provide installation, update, launch, and removal workflows.
*   **🛰️ Unified Control Plane**: Manage **AWS, Docker, and Kubernetes** side-by-side with your AI CLI integrations.
*   **🧹 Controlled Cleanup**: Removal operations target only the CLI binary managed by AI CLI PRO. User-created configuration, authentication data, models, and project files are not automatically deleted.

---

## ⌨️ Power User Shortcuts

| Action | macOS | Windows/Linux |
| :--- | :--- | :--- |
| **Quick Launch** | `Cmd + Opt + A` | `Ctrl + Alt + A` |
| **Focus Dashboard** | `Cmd + Shift + P` → `Focus` | `Ctrl + Shift + P` → `Focus` |

---

## 🔐 Authentication & Credentials

AI CLI PRO does not require users to provide third-party API keys, OAuth tokens, passwords, or authentication secrets to AI CLI PRO.

Supported third-party CLIs handle their own authentication and communication with their respective providers. AI CLI PRO does not intentionally extract, proxy, reuse, or transmit third-party CLI authentication credentials.

You remain responsible for maintaining valid accounts, licenses, subscriptions, and authorization for the third-party tools you use.

---

## 📦 Third-Party Software

AI CLI PRO may detect, launch, install, update, or manage third-party command-line software.

Unless explicitly stated otherwise, AI CLI PRO does not distribute the underlying third-party service itself. Third-party software remains subject to its own license and terms. Installation and update commands may download software from official vendor or package-manager distribution channels.

AI CLI PRO does not bypass, circumvent, disable, or interfere with third-party authentication, authorization, subscriptions, usage limits, access controls, safety controls, or licensing requirements.

---

## 🧠 Model Licensing

AI CLI PRO may provide integrations with local model runtimes and model registries.

Individual models may have separate licenses, usage restrictions, attribution requirements, acceptable-use policies, or commercial-use conditions. Users are responsible for reviewing and complying with the license applicable to each model they download or use.

---

## 📊 Third-Party Provider Responsibilities

| Integration | AI CLI PRO provides | Provider controls |
| --- | --- | --- |
| Gemini CLI | Launch and installation workflow | Authentication, Google services, usage policies |
| Claude Code | Launch and installation workflow | Anthropic authentication, service access, licensing |
| GitHub Copilot CLI | Launch and installation workflow | GitHub account, Copilot entitlement, service policies |
| Codex | Launch and installation workflow | OpenAI authentication and service access |
| Ollama | Local CLI management | Local model execution and model-specific licenses |
| Hugging Face CLI | CLI management | Hugging Face account/services and applicable model licenses |

Third-party integrations may change as provider software, licenses, or service policies change.

---

## 🤝 Community & Support

<p align="left">
  <a href="https://github.com/likhith-adithya/AI-CLI-PRO-Public/issues/new?title=Feature+Request">
    <img src="https://img.shields.io/badge/Suggest-Feature-6A11CB?style=for-the-badge&logo=github" alt="Feature Request">
  </a>
  <a href="https://github.com/likhith-adithya/AI-CLI-PRO-Public/issues/new?title=Bug+Report">
    <img src="https://img.shields.io/badge/Report-Bug-eb4034?style=for-the-badge&logo=github" alt="Bug Report">
  </a>
  <a href="https://github.com/likhith-adithya/AI-CLI-PRO-Public#%EF%B8%8F-support--sponsorship">
    <img src="https://img.shields.io/badge/Support-Project-FF9F43?style=for-the-badge&logo=github-sponsors" alt="Support">
  </a>
</p>

<p align="left">
  <a href="https://marketplace.visualstudio.com/items?itemName=likhith-adithya.ai-cli-pro&ssr=false#review-details">
    <img src="https://img.shields.io/badge/Leave_a_Review-Support_the_Project-2ECC71?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="Leave a Review">
  </a>
</p>

---

## ⚖️ Legal & Third-Party Notice

**AI CLI PRO is an independent third-party developer tool. It is not affiliated with, endorsed by, sponsored by, or officially associated with Google, Anthropic, GitHub, OpenAI, Meta, Mistral AI, DeepSeek, Ollama, Hugging Face, or other third-party providers referenced by the project, unless expressly stated otherwise.**

Third-party product names and trademarks belong to their respective owners. References to third-party products are made for identification, compatibility, and integration purposes only.

AI CLI PRO provides integration and lifecycle management capabilities for supported command-line tools. Third-party CLIs, models, APIs, accounts, subscriptions, and services remain subject to their respective licenses and terms.

[Privacy Policy](https://github.com/likhith-adithya/AI-CLI-PRO-Public/blob/main/docs/legal/PRIVACY.md) • [Terms](https://github.com/likhith-adithya/AI-CLI-PRO-Public/blob/main/docs/legal/TERMS.md) • [License](https://github.com/likhith-adithya/AI-CLI-PRO-Public/blob/main/LICENSE) • [Third-Party Notices](https://github.com/likhith-adithya/AI-CLI-PRO-Public/blob/main/THIRD-PARTY-NOTICES.md) • [Security](https://github.com/likhith-adithya/AI-CLI-PRO-Public/blob/main/SECURITY.md)

---
<p align="center">
  <b>Built for developers who live in the terminal but work in the IDE.</b> 💻
</p>
