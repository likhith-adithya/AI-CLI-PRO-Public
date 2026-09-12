# Security Policy

## Supported Versions

The following versions of AI CLI PRO are currently supported with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 0.0.x   | :white_check_mark: |
| < 0.0.1 | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability within this project, please report it using the following method:

1. **GitHub Issues:** Open a new issue in this repository and apply the `security` label. 
2. **Details:** Provide a detailed description of the vulnerability, steps to reproduce, and any potential impact.

We aim to acknowledge all reports within 48 hours and provide a fix or mitigation plan as soon as possible.

## Our Security Principles

- **Local First:** AI CLI PRO is designed to run your CLI agents locally. We do not store or transmit your API keys, credentials, or terminal session data to any external servers.
- **Safe Execution:** Commands are executed through your local terminal environment. We recommend reviewing the `installCommand` and `command` of any custom agent you add to the registry.
- **Transparency:** The extension source code is open-source and available for audit at any time.
