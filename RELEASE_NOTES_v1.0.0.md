# v1.0.0: Initial Stable Release 🚀

We are proud to announce the first stable release of **Awesome Tech Failures**, the most complete, curated library of public technology postmortems. 

This release transforms the repository from a static list into a **machine-readable intelligence source** for AI agents and engineering teams.

## 🧩 Core Failure Categories
This release creates a structured taxonomy of over 46+ failure analysis entries across six critical domains:

- **AI Slop & Automation**: Documenting the new wave of failures from RAG cascades, infinite agent loops, and hallucination-induced outages.
- **Production Outages**: Classic and modern infrastructure failures (S3, DNS, BGP) to learn from.
- **Security Incidents**: Supply chain attacks, misconfigurations, and social engineering breaches.
- **Startup Failures**: Business model collapses, premature scaling, and "finding a problem for a solution."
- **Product Failures**: Features that flopped and market misreads.
- **Decision & Process**: The human element—groupthink, metric gaming, and leadership failures.

## 🤖 The Machine Layer (Agent-Native)
Version 1.0.0 introduces dedicated support for autonomous agents to ingest and learn from this dataset:
- **`agent/entries.ndjson`**: All failures available as newline-delimited JSON for efficient streaming and RAG indexing.
- **OpenAPI 3.0 Spec**: A full [API Specification](agent/api_spec.yaml) defining how agents should query this data.
- **Strict Schema**: Validated against `agent/schema.json` to ensure 100% data integrity.

## 🤝 Contributing
This is a living history of failure. We welcome contributions from the community!
Please read our [CONTRIBUTING.md](CONTRIBUTING.md) to submit new entries or improvements.

---
*Failure is data. Studying it is a competitive advantage.*
