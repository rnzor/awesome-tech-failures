# Changelog

All notable changes to the Awesome Tech Failures repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [Unreleased]

### Added
- New 2025 entries: Multi-Agent Loop Cost Spike, Agentic Database Migration
- New infrastructure entries: GitLab Data Loss (2017), Fastly Global Outage (2021)
- New security entries: SolarWinds Supply Chain (2020), Uber Social Engineering (2022)
- Severity scoring system with standardized levels (Critical/High/Medium/Low)
- Diagnosis flowchart with Mermaid diagrams
- Prevention playbooks: `agent-deployment.md`, `production-outage.md`
- Issue and PR templates for community contributions
- Updated README with 2026 branding and badges

### Changed
- Updated `agent/schema.json` to require severity metadata
- Enhanced `agent/entries.ndjson` with severity scores for all 25 entries (6 AI Slop, 5 Production, 12 Security, 2 Startup)
- Modernized README navigation and structure

---

## [1.0.0] - 2026-01-18

### Added
- Initial repository structure with 5 failure categories
- 25+ documented failure entries across all categories
- AI Agent Pre-Flight Checklist
- Machine-readable agent layer (NDJSON, JSON Schema)
- 10 failure pattern definitions
- Validation workflow for markdown entries
