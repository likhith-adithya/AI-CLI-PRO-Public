# Contributing to AI-CLI-HUB

Thank you for your interest in improving AI-CLI-HUB! This guide will help you submit issues and feature requests effectively.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [How to Report a Bug](#how-to-report-a-bug)
4. [How to Request a Feature](#how-to-request-a-feature)
5. [Issue Quality Guidelines](#issue-quality-guidelines)
6. [Labeling & Workflow](#labeling--workflow)
7. [FAQ](#faq)

---

## Code of Conduct

### Our Commitment

We are committed to providing a welcoming and inclusive environment for all contributors. We expect everyone to:

- **Be respectful** - Treat all members with courtesy and respect
- **Be constructive** - Provide helpful feedback and suggestions
- **Be inclusive** - Welcome people of all backgrounds and experiences
- **Be honest** - Be truthful in your communications
- **Be patient** - Understand that responses may take time

### Unacceptable Behavior

The following behaviors will not be tolerated:

- Harassment, discrimination, or abusive language
- Trolling, spam, or off-topic posts
- Sharing sensitive information (API keys, passwords, personal data)
- Promotional content or self-promotion
- Any form of violence or threats

**Violations may result in being banned from the repository.**

---

## Getting Started

### Prerequisites

Before submitting an issue, make sure you:

1. **Have the latest version** of the extension installed
2. **Have checked existing issues** to avoid duplicates
3. **Can reproduce the issue** (for bugs)
4. **Have clear steps** to describe the problem or feature

### Repository Setup

This is a **public issue tracker only**. The source code is maintained in a private repository.

---

## How to Report a Bug

### Step 1: Search for Existing Issues

Before reporting, [search the issues](../../issues?q=is%3Aissue) to see if someone has already reported it.

### Step 2: Create a New Issue

1. Go to [Issues](../../issues)
2. Click **"New Issue"**
3. Select **"Bug Report"** template

### Step 3: Fill in the Template

**Required Information:**

- **Bug Title**: Clear, concise description (e.g., "Extension crashes when opening settings")
- **Description**: What happened? What did you expect?
- **Steps to Reproduce**: Exact steps to reproduce the issue
- **Expected Behavior**: What should happen
- **Actual Behavior**: What actually happens
- **Environment**:
  - Operating System (Windows, macOS, Linux)
  - VS Code Version
  - Extension Version
  - Any relevant extensions installed

**Optional but Helpful:**

- **Screenshots/Videos**: Visual demonstration of the issue
- **Error Logs**: Copy relevant error messages from the VS Code Output/Debug Console
- **Additional Context**: Any other information that might help

### Step 4: Submit and Follow Up

- Click **"Submit new issue"**
- Be prepared to answer follow-up questions
- Provide additional information if requested
- Monitor your issue for updates

### Example Bug Report

```
Title: Extension fails to load Gemini provider on Windows 10

Description:
The extension crashes when I try to select Gemini as my AI provider.

Steps to Reproduce:
1. Open VS Code
2. Open the AI-CLI-HUB command palette
3. Select "Choose AI Provider"
4. Click on "Gemini"
5. Extension crashes

Expected Behavior:
The Gemini provider should initialize and be ready to use.

Actual Behavior:
Extension crashes with error message in the console.

Environment:
- OS: Windows 10 (Build 19045)
- VS Code: 1.87.2
- Extension Version: 1.2.0

Error Log:
[Error message from console]

Additional Context:
I have Claude provider working fine. Only Gemini causes this issue.
```

---

## How to Request a Feature

### Step 1: Check for Duplicates

[Search for existing feature requests](../../issues?q=is%3Aissue+label%3A%22feature-request%22) to see if someone has already suggested it.

### Step 2: Create a New Issue

1. Go to [Issues](../../issues)
2. Click **"New Issue"**
3. Select **"Feature Request"** template

### Step 3: Fill in the Template

**Required Information:**

- **Feature Title**: Clear, concise description of what you want
- **Problem Statement**: What problem does this solve?
- **Proposed Solution**: How should this feature work?
- **Use Case**: Why do you need this? Who would benefit?

**Optional but Helpful:**

- **Alternative Solutions**: Other ways to solve the same problem
- **Mockups/Examples**: Screenshots, diagrams, or code examples
- **Similar Features**: Links to how other tools implement this
- **Additional Context**: Any other relevant information

### Step 4: Engage with the Community

- Respond to comments and questions
- Help refine the feature description
- Show support for ideas you like (use reactions: 👍 ❤️ etc.)

### Example Feature Request

```
Title: Add keyboard shortcut to quick-switch between AI providers

Problem:
Currently, switching between AI providers requires opening the command palette
and navigating through menus. This is time-consuming when I frequently switch
between Gemini and Claude.

Proposed Solution:
Add a customizable keyboard shortcut (e.g., Ctrl+Alt+A) that opens a quick picker
to switch between enabled AI providers.

Use Case:
As a developer, I use different AI providers for different tasks:
- Claude for code generation
- Gemini for research and general questions

Being able to switch quickly without menu navigation would increase productivity.

Alternative Solutions:
- Add a status bar button to switch providers
- Add provider-specific commands

Mockup:
[ASCII diagram or screenshot showing the quick picker]
```

---

## Issue Quality Guidelines

### What Makes a Good Issue?

✅ **Good Issues Have:**

- Clear, descriptive title
- Detailed description of the problem or feature
- Steps to reproduce (for bugs)
- Expected vs. actual behavior
- Environment information
- Screenshots/logs when applicable
- Proper formatting and grammar
- Links to related issues (if applicable)

❌ **Avoid:**

- Vague titles (e.g., "It doesn't work", "Question")
- Missing environment details
- Blaming tone or frustration
- Multiple unrelated issues in one report
- Sensitive information (API keys, passwords)
- Low-quality screenshots (unreadable, tiny text)
- Wall of text without formatting

### Title Format

Use clear, action-focused titles:

✓ "Extension crashes when opening settings"
✓ "Add keyboard shortcut for AI provider switching"
✓ "Claude provider not responding to requests"

✗ "It broken"
✗ "Help!"
✗ "Question about the extension"

---

## Labeling & Workflow

### Labels We Use

The maintainers will apply these labels to your issue:

| Label | Meaning |
|-------|----------|
| `bug` | Confirmed bug |
| `feature-request` | New feature suggestion |
| `enhancement` | Improvement to existing feature |
| `documentation` | Docs need updating |
| `high-priority` | Urgent |
| `medium-priority` | Important |
| `low-priority` | Can wait |
| `in-progress` | Being worked on |
| `awaiting-user-feedback` | More info needed from you |
| `won't-fix` | Decided not to implement |
| `duplicate` | Already reported |
| `good-first-issue` | Suitable for new contributors |
| `help-wanted` | Looking for community help |

### Issue Workflow

```
┌─────────────┐
│ New Issue   │
└──────┬──────┘
       │
       ├─→ [Triaged] Apply labels, assignee
       │
       ├─→ [In Progress] Work begins
       │
       ├─→ [Awaiting Feedback] Need more info?
       │   └─→ [Reopened] User provides info
       │
       └─→ [Closed]
           ├─ Fixed (merged to release)
           ├─ Won't Fix (rejected)
           └─ Duplicate (linked to original)
```

---

## Response Timeline

- **Acknowledgment**: 2-3 business days
- **High Priority**: Resolution within 1-2 weeks
- **Medium Priority**: Resolution within 2-4 weeks
- **Low Priority**: Future release
- **Feature Requests**: Community discussion, then prioritization

---

## FAQ

### Q: Can I contribute code directly?
A: The source code is in a private repository. However, we're open to community contributions and feature discussions. Please open a feature request or reach out to the maintainers.

### Q: How long does it take to get a response?
A: We aim to acknowledge all issues within 2-3 business days. Complex issues may take longer to investigate.

### Q: What if my issue is marked as "won't-fix"?
A: This means it doesn't align with the project's goals or isn't feasible for technical/business reasons. You're welcome to discuss it, but the decision is final.

### Q: Can I reopen a closed issue?
A: Yes! If you have new information or the issue reoccurs, please comment on the closed issue to reopen it. Include your new findings.

### Q: How can I show support for a feature request?
A: Use GitHub's reaction emojis (👍 ❤️ 🎉) on the issue. Don't post "+1" comments as they clutter the discussion.

### Q: Should I contact maintainers directly?
A: For public bug reports and feature requests, use this repository. For private concerns or security issues, you can reach out privately.

### Q: What if my issue contains sensitive information?
A: Immediately contact a maintainer to have the issue made private. Never post API keys, passwords, or personal data publicly.

---

## Need More Help?

- Read our [README.md](README.md) for overview
- Check [existing issues](../../issues) for similar problems
- View [issue labels](LABELS.md) for categorization
- Look for previous discussions in comments

**Thank you for contributing to AI-CLI-HUB! 🚀**
