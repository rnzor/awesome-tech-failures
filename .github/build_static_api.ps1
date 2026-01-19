# Build static API for GitHub Pages
$ErrorActionPreference = "Continue"

$REPO_ROOT = $PSScriptRoot.Parent.FullName
$DOCS_DIR = Join-Path $REPO_ROOT "docs"
$API_DIR = Join-Path $DOCS_DIR "api\v1"
$AGENT_DIR = Join-Path $REPO_ROOT "agent"

Write-Host "Building static API..."

# Create api directory
New-Item -ItemType Directory -Force -Path $API_DIR | Out-Null

# 1. Convert NDJSON files to JSON arrays
Write-Host "Converting NDJSON to JSON..."
& python ".github\convert_ndjson.py"

# 2. Copy existing JSON files
Write-Host "Copying metadata files..."
Copy-Item -Path "$AGENT_DIR\tags.json" -Destination "$API_DIR\tags.json" -Force
Copy-Item -Path "$AGENT_DIR\graph.json" -Destination "$API_DIR\graph.json" -Force

# 3. Prepare embeddings for client-side search
Write-Host "Preparing embeddings for client-side search..."
Copy-Item -Path "$AGENT_DIR\embeddings.ndjson" -Destination "$API_DIR\embeddings.json" -Force

# 4. Create hybrid lookup for common terms
Write-Host "Creating hybrid term lookup..."
& python ".github\create_hybrid_lookup.py"

# 5. Create API index
Write-Host "Creating API index..."
& python ".github\create_api_index.py"

# 6. Copy OpenAPI spec to docs
Write-Host "Copying OpenAPI spec..."
Copy-Item -Path "$AGENT_DIR\api_spec.yaml" -Destination "$DOCS_DIR\openapi.yaml" -Force

# 7. Create Swagger UI HTML
Write-Host "Creating Swagger UI..."
$swaggerUI = @"
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
"@

Set-Content -Path "$DOCS_DIR\swagger-ui.html" -Value $swaggerUI

Write-Host "Static API build complete!"
Write-Host "API files located at: $API_DIR"
Write-Host "OpenAPI spec at: $DOCS_DIR\openapi.yaml"
Write-Host "Swagger UI at: $DOCS_DIR\swagger-ui.html"
