# v1.2.0: The Connectivity API 🌐

This release unlocks **serverless, client-side semantic search** and interactive API documentation, running entirely on GitHub Pages.

## ⚡ Static API
The repository now auto-generates a static API from the raw data files.
- **Base URL**: `https://rnzor.github.io/awesome-tech-failures/api`
- **Endpoints**:
    - `/failures.json`: Complete dataset with 62+ failures.
    - `/patterns.json`: All 10+ failure patterns.
    - `/hybrid_lookup.json`: Pre-computed embeddings for instant search.

## 🧠 Client-Side Search
We've introduced a **Hybrid Search** mechanism that allows frontend applications to perform semantic queries without a backend server.
- **Zero Latency**: Uses pre-computed vectors for common terms.
- **Privacy First**: No data leaves the client's browser.
- **Implementation**: See [Frontend Integration Guide](docs/FRONTEND_INTEGRATION.md).

## 📚 Interactive Documentation
Fully interactive **OpenAPI 3.1** documentation is now available directly in the repo.
- **Swagger UI**: [View Docs](https://rnzor.github.io/awesome-tech-failures/swagger-ui.html)
- **Spec**: `docs/openapi.yaml`

---
*Query the history of failure, directly from your browser.*
