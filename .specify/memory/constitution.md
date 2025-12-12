<!-- SYNC IMPACT REPORT
Version change: N/A → 1.0.0
Modified principles: N/A (new constitution)
Added sections: Mission, Core Principles (5), Forbidden section, Governance
Removed sections: N/A
Templates requiring updates:
  - .specify/templates/plan-template.md ✅ updated
  - .specify/templates/spec-template.md ✅ updated
  - .specify/templates/tasks-template.md ✅ updated
  - .specify/templates/commands/*.md ⚠ pending
  - README.md ⚠ pending
Follow-up TODOs: None
-->

# Policy Pulse Constitution

## Mission
Prevent compliance drift and knowledge loss during vendor onboarding by delivering real-time, contextual policy guidance inside teams' existing chat tools—without replacing legacy systems.

## Core Principles

### Micro-first
Solve one handoff gap (procurement ↔ legal ↔ ops) in <500 lines of logic.

### Zero-config Onboarding
Connect via API to existing knowledge bases (SharePoint, Confluence, Google Drive) in <10 minutes.

### Privacy by Design
All data stays in-client; no external LLM calls with raw company docs.

### Windows-native Support
First-class support for Windows 10/11 (Electron or .NET MAUI for desktop control panel).

### Profit Before Scale
Each feature must justify $1,000/year pricing.

### Forbidden Actions
- Building full workflow automation
- Custom UIs for core logic (use Slack/Teams/Email as frontend)
- Storing customer data on our servers

## Additional Constraints

Policy Pulse shall maintain strict adherence to privacy requirements by ensuring all document processing occurs locally. The system must integrate seamlessly with existing enterprise infrastructure without requiring changes to current data storage practices.

## Development Workflow

All features must be developed with the micro-first principle in mind, focusing on solving specific handoff gaps between procurement, legal, and operations teams. Each feature must undergo privacy review to ensure no customer data leaves the client environment.

## Governance

This constitution supersedes all other development practices for the Policy Pulse project. All team members must verify compliance with these principles during code reviews and feature development. Any deviation from these principles must be documented and approved by the project leadership.

**Version**: 1.0.0 | **Ratified**: 2025-12-12 | **Last Amended**: 2025-12-12
