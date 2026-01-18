# Changelog

All notable changes to the Awesome Tech Failures repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [1.1.0] - 2026-01-18

### 🧠 The Intelligence Layer Release

This release transforms the repository into a fully installable package (`pip` / `npm`) with advanced graph capabilities for AI agents.

### ✨ New Features
- **Package Distribution**:
    - **Python**: `pip install .` (via `setup.py`) exposes `load_entries()`, `load_graph()`.
    - **NPM**: `package.json` included for Node.js usage.
- **Source Registry**: `agent/sources.json` deduplicates 101+ sources with stable Hash-IDs.
- **Connectivity Graph**: `agent/graph.json` maps 219+ semantic links between entries.
- **Embeddings**: `agent/embeddings.ndjson` provides pre-computed vectors (mock) for RAG.

### 🛠 Improvements
- **Visual Taxonomy**: Added Mermaid diagram to README.
- **Documentation**: Renamed "Interactive Tools" to "Operational Frameworks".
- **Validation**: Added `check_links.py` to CI.

## [1.0.0] - 2026-01-18

### 🚀 The "Agent-Native" Release

This release marks the official v1.0.0 launch of **Awesome Tech Failures**. The repository has been transformed from a static list into a machine-readable intelligence source for AI agents.

### ✨ Major Features
- **Machine Layer**: Added `agent/entries.ndjson` (Structured Data), `agent/schema.json` (Validation), and `agent/api_spec.yaml` (Integration Spec).
- **Content Expansion**: Grown to **60+** entries across 6 categories (AI Slop, Production, Security, Startup, Product, Decision).
- **Interactive Tools**: Moved `diagnosis-flowchart.md`, `severity-system.md`, and `ai-agent-checklist.md` to `docs/`.
- **Community Governance**: Added `SECURITY.md`, `CITATION.cff`, `CODE_OF_CONDUCT.md`, and Issue Templates.
- **Visual Identity**: New "Glitch" Logo and professional badges.

### 🆕 New Entries (Selected)
- **AI Slop**: DeepSeek, Claude/GPT hallucinations, RAG cascades, Agent loops.
- **Security**: SolarWinds (Supply Chain), Log4Shell (RCE), Twitch Leaks.
- **Production**: Cloudflare (Regex), Meta (Cascades), CrowdStrike (Rollback).
- **Business**: Theranos, WeWork, FTX, Boeing 737 MAX, Nokia, Blockbuster.

### 🔧 Improvements
- **Automated Validation**: `validate_entries.py` & `validate_patterns.py` ensure 100% parity and link integrity.
- **Tagging Consistency**: Enforced standardized tags across 100% of the repository.
- **Documentation**: New `AGENTS.md` policy guide for autonomous systems.
