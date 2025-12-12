---
id: 1
title: "Policy Pulse Founding Constitution"
stage: constitution
date_iso: "2025-12-12"
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: user
command: "/sp.constitution"
labels: ["constitution", "governance", "policy"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - ".specify/memory/constitution.md"
  - "history/prompts/constitution/1-policy-pulse-founding.constitution.prompt.md"
tests_yaml: []
---

# Prompt Text

```
text
# Policy Pulse: Founding Constitution

## Mission
Prevent compliance drift and knowledge loss during vendor onboarding by delivering real-time, contextual policy guidance inside teams' existing chat tools—without replacing legacy systems.

## Core Principles
1. **Micro-first**: Solve one handoff gap (procurement ↔ legal ↔ ops) in <500 lines of logic.
2. **Zero-config onboarding**: Connect via API to existing knowledge bases (SharePoint, Confluence, Google Drive) in <10 minutes.
3. **Privacy by design**: All data stays in-client; no external LLM calls with raw company docs.
4. **Windows-native**: First-class support for Windows 10/11 (Electron or .NET MAUI for desktop control panel).
5. **Profit before scale**: Each feature must justify $1,000/year pricing.

## Forbidden
- Building full workflow automation
- Custom UIs for core logic (use Slack/Teams/Email as frontend)
- Storing customer data on our servers
```

# Response Text

Created the founding constitution for Policy Pulse project by filling the template with the provided mission, core principles, and forbidden actions. The constitution establishes governance for the project with version 1.0.0, ratified on 2025-12-12. The constitution defines five core principles (Micro-first, Zero-config Onboarding, Privacy by Design, Windows-native Support, Profit Before Scale) plus a Forbidden Actions section. Additional sections include Mission, Additional Constraints, Development Workflow, and Governance.

# Outcome

The Policy Pulse constitution has been successfully created at `.specify/memory/constitution.md` with version 1.0.0. The file includes all the specified principles and governance structure. The constitution emphasizes privacy, micro-first development, and Windows-native support as key project constraints.

# Evaluation

The constitution aligns with all user requirements:
- [X] Mission statement included
- [X] Five core principles implemented
- [X] Forbidden actions section added
- [X] Proper governance structure established
- [X] Version 1.0.0 assigned with correct dates
- [X] Template properly filled with no remaining placeholder tokens