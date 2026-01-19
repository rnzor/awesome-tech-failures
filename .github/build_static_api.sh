#!/bin/bash
# Build static API from source files for GitHub Pages deployment

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DOCS_DIR="$REPO_ROOT/docs"
API_DIR="$DOCS_DIR/api"
AGENT_DIR="$REPO_ROOT/agent"

echo "🏗️  Building static API..."

# Create api directory
mkdir -p "$API_DIR"

# 1. Convert NDJSON files to JSON arrays (using Python instead of jq)
echo "📦 Converting NDJSON to JSON..."

python3 -c "
import json
from pathlib import Path

# Convert entries.ndjson → failures.json
entries_file = Path('$AGENT_DIR/entries.ndjson')
output_file = Path('$API_DIR/failures.json')
entries = []
with open(entries_file, 'r') as f:
    for line in f:
        if line.strip():
            entries.append(json.loads(line))
with open(output_file, 'w') as f:
    json.dump(entries, f, indent=2)
print(f'Converted {len(entries)} entries to failures.json')

# Convert patterns.ndjson → patterns.json
patterns_file = Path('$AGENT_DIR/patterns.ndjson')
output_file = Path('$API_DIR/patterns.json')
patterns = []
with open(patterns_file, 'r') as f:
    for line in f:
        if line.strip():
            patterns.append(json.loads(line))
with open(output_file, 'w') as f:
    json.dump(patterns, f, indent=2)
print(f'Converted {len(patterns)} patterns to patterns.json')

# Convert playbooks.ndjson → playbooks.json
playbooks_file = Path('$AGENT_DIR/playbooks.ndjson')
output_file = Path('$API_DIR/playbooks.json')
playbooks = []
with open(playbooks_file, 'r') as f:
    for line in f:
        if line.strip():
            playbooks.append(json.loads(line))
with open(output_file, 'w') as f:
    json.dump(playbooks, f, indent=2)
print(f'Converted {len(playbooks)} playbooks to playbooks.json')
"

# 2. Copy existing JSON files
echo "📋 Copying metadata files..."
cp "$AGENT_DIR/tags.json" "$API_DIR/tags.json"
cp "$AGENT_DIR/graph.json" "$API_DIR/graph.json"

# 3. Prepare embeddings for client-side search
echo "🧠 Preparing embeddings for client-side search..."

# Copy embeddings as-is (already in JSON format)
cp "$AGENT_DIR/embeddings.ndjson" "$API_DIR/embeddings.json"

# 4. Create hybrid lookup for common terms
echo "🔍 Creating hybrid term lookup..."
python3 "$REPO_ROOT/.github/create_hybrid_lookup.py"

# 5. Create API index
echo "📝 Creating API index..."
python3 "$REPO_ROOT/.github/create_api_index.py"

# 6. Copy OpenAPI spec to docs
echo "📄 Copying OpenAPI spec..."
cp "$AGENT_DIR/api_spec.yaml" "$DOCS_DIR/openapi.yaml"

# 7. Create Swagger UI HTML
echo "🌐 Creating Swagger UI..."
cat > "$DOCS_DIR/swagger-ui.html" << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Awesome Tech Failures API</title>
    <link rel="stylesheet" type="text/css" href="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css">
    <style>
        body { margin: 0; padding: 20px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
        #swagger-ui { max-width: 1460px; margin: 0 auto; }
        .topbar { display: none !important; }
    </style>
</head>
<body>
    <div id="swagger-ui"></div>
    <script src="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
    <script>
        window.onload = function() {
            window.ui = SwaggerUIBundle({
                url: './openapi.yaml',
                dom_id: '#swagger-ui',
                deepLinking: true,
                presets: [
                    SwaggerUIBundle.presets.apis,
                    SwaggerUIBundle.SwaggerUIStandalonePreset
                ],
                layout: "BaseLayout",
                defaultModelsExpandDepth: 1,
                defaultModelExpandDepth: 1
            });
        };
    </script>
</body>
</html>
EOF

echo "✅ Static API build complete!"
echo "📂 API files located at: $API_DIR"
echo "🌐 OpenAPI spec at: $DOCS_DIR/openapi.yaml"
echo "📚 Swagger UI at: $DOCS_DIR/swagger-ui.html"
