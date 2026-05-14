# GitHub Labels Reference

This document outlines all labels used in the AI-CLI-HUB Public Issue Tracker for organizing and categorizing issues.

## 📑 Label Categories

### 1. Issue Type Labels

Describe the **type of issue**:

| Label | Color | Description | Usage |
|-------|-------|-------------|-------|
| `bug` | 🔴 Red | Something is broken or not working as expected | Issues reporting broken functionality |
| `feature-request` | 💜 Purple | Request for a new feature or functionality | Suggestions for new features |
| `enhancement` | 💚 Green | Improvement to existing features or performance | Improvements to current functionality |
| `documentation` | 📘 Blue | Documentation improvements or clarifications | Issues about docs, guides, or examples |
| `question` | 💛 Yellow | General questions about the extension | How-to questions or clarifications |

---

### 2. Priority Labels

Indicate the **urgency and importance**:

| Label | Color | Description | Resolution Target |
|-------|-------|-------------|-------------------|
| `high-priority` | 🔴 Red | Urgent issue affecting many users or critical functionality | 1-2 weeks |
| `medium-priority` | 🟠 Orange | Important but not blocking | 2-4 weeks |
| `low-priority` | 🟡 Yellow | Can be addressed in future releases | When available |

---

### 3. Status Labels

Indicate the **current status** of an issue:

| Label | Color | Description | Next Action |
|-------|-------|-------------|-------------|
| `in-progress` | 🔵 Blue | Currently being worked on | Await updates |
| `awaiting-user-feedback` | 🟣 Purple | Need more information from the reporter | User should respond |
| `awaiting-triage` | ⚪ Gray | Waiting to be reviewed and categorized | Maintainer review |
| `won't-fix` | ⚫ Black | Decided not to implement | Discussion closed |
| `duplicate` | 🩶 Gray | Duplicate of another issue | Refer to original |
| `stale` | 🩶 Gray | No activity for extended period | May be closed |

---

### 4. Feature/Component Labels

Identify the **area of the extension** affected:

| Label | Color | Description | Examples |
|-------|-------|-------------|----------|
| `ai-providers` | 💎 Purple | Related to AI providers (Gemini, Claude, Copilot, etc.) | Provider integration issues |
| `ui-ux` | 💙 Light Blue | User interface or experience related | UI bugs, design requests |
| `performance` | 🟢 Green | Performance, speed, or optimization issues | Slow loading, memory usage |
| `security` | 🔐 Red | Security-related issues | Security vulnerabilities |
| `keyboard-shortcuts` | ⌨️ Orange | Keyboard shortcuts and hotkeys | Shortcut issues/requests |
| `settings-config` | ⚙️ Gray | Settings, preferences, or configuration | Config issues |
| `api` | 📡 Blue | API integration or external service issues | API errors, integration problems |
| `install-update` | 📦 Yellow | Installation or update related issues | Installation problems |

---

### 5. Contributor Labels

Designate **contribution opportunities**:

| Label | Color | Description | Who should work on it |
|-------|-------|-------------|----------------------|
| `good-first-issue` | 💚 Green | Great starting point for new contributors | Newcomers to the project |
| `help-wanted` | 🆘 Red | Community contributions welcome | Anyone from the community |
| `needs-investigation` | 🔍 Blue | Requires investigation or debugging | Experienced contributors |

---

### 6. Special Labels

For **special situations** and categorization:

| Label | Color | Description | When to use |
|-------|-------|-------------|-------------|
| `regression` | 🔴 Red | Issue that worked before but broke in a newer version | When a feature regresses |
| `breaking-change` | ⚠️ Orange | Issue related to breaking changes | API/behavior changes |
| `needs-maintainer-attention` | 👀 Blue | Requires decision from maintainer | Complex decisions needed |
| `windows-specific` | 🪟 Blue | Issue specific to Windows OS | Windows-only problems |
| `macos-specific` | 🍎 Gray | Issue specific to macOS | macOS-only problems |
| `linux-specific` | 🐧 Black | Issue specific to Linux | Linux-only problems |

---

## 🎨 Label Color Scheme

```
🔴 High Priority/Critical:     #d73a49 (Red)
🟠 Medium Priority:             #fb8500 (Orange)
💜 Feature Requests:            #5e4e6f (Purple)
💚 Enhancement/Good First:      #28a745 (Green)
💙 UI/Design/Performance:       #0366d6 (Blue)
💛 Low Priority/Questions:      #ffd33d (Yellow)
⚫ Won't Fix/Duplicate:         #2b3035 (Black)
⚪ Awaiting Triage:             #ededed (Light Gray)
```

---

## 📊 Typical Label Combinations

### Bug Report
```
bug + [high/medium/low-priority] + [optional: ai-providers/ui-ux/etc]
Example: bug, high-priority, ai-providers
```

### Feature Request
```
feature-request + [optional: nice-to-have label]
Example: feature-request, enhancement
```

### Enhancement
```
enhancement + [component label]
Example: enhancement, ui-ux
```

### Good Starting Point
```
good-first-issue + [optional: component]
Example: good-first-issue, documentation
```

---

## 🔄 Label Workflow

### When an issue is created:
1. Add `awaiting-triage` (auto-applied)
2. Maintainer reviews and applies appropriate type label

### As work progresses:
1. Remove `awaiting-triage`
2. Add priority and status labels
3. Add component-specific labels

### When resolved:
1. Keep type and component labels for reference
2. Remove status labels
3. Remove priority labels
4. Mark as closed

---

## ❓ FAQ About Labels

**Q: Why so many labels?**
A: Labels help organize, filter, and prioritize issues. Users can find issues relevant to them, and maintainers can track work effectively.

**Q: Can I suggest new labels?**
A: Yes! Open an issue and explain why a new label would be helpful.

**Q: Do I apply labels myself?**
A: No. When you create an issue, the system applies default labels. Maintainers will adjust them based on triage.

**Q: What labels should I use?**
A: Just pick the appropriate issue template. The maintainers will handle labeling during triage.

---

## 🎯 How to Use Labels Effectively

### As a Reporter:
- Choose the right template (bug vs feature request)
- Provide clear information so labels are accurate
- Check similar labeled issues

### As a Maintainer:
- Apply labels consistently
- Use for filtering and reporting
- Update as status changes

### As a Community Member:
- Use labels to find issues to work on
- Filter by `good-first-issue` to contribute
- Support issues with reactions (don't comment "+1")

---

**Labels last updated: 2026-05-14**
