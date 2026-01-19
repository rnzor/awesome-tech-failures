# Frontend Integration Guide

This guide explains how to integrate with the Awesome Tech Failures API.

---

## Base URLs

| Environment | Base URL | Description |
|-------------|-----------|-------------|
| Production | `https://rnzor.github.io/awesome-tech-failures/api/v1` | GitHub Pages static API v1 |
| Development | `http://localhost:3000/api/v1` | Local development path |

---

## API Endpoints

### GET /failures
List all failure entries with optional filtering.

**Request:**
```typescript
interface GetFailuresParams {
  category?: 'ai-slop' | 'outage' | 'security' | 'startup' | 'product' | 'decision';
  tags?: string[];
  limit?: number;
  offset?: number;
}

const failures = await fetch('https://rnzor.github.io/awesome-tech-failures/api/v1/failures.json')
  .then(r => r.json());
```

**Response:**
```typescript
interface FailuresResponse {
  total: number;
  data: Failure[];
}
```

---

### GET /failures/{id}
Get specific failure entry.

**Request:**
```typescript
const failure = await fetch('https://rnzor.github.io/awesome-tech-failures/api/v1/failures.json')
  .then(r => r.json())
  .then(data => data.find(f => f.id === 'aws-s3-us-east-1-2017'));
```

---

### clientSearchSimilarity()
**IMPORTANT:** This is a client-side function, not a network endpoint.

**Request:**
```typescript
interface SimilaritySearchRequest {
  query: string;
  top_k?: number;
  filters?: {
    category?: string;
    severity?: string;
    tags?: string[];
  };
  use_hybrid_only?: boolean;
  embedding_api_key?: string;
}
```

**Implementation Steps:**

1. Load embeddings once on app mount:
```typescript
let embeddingsCache: Embedding[] | null = null;

async function loadEmbeddings() {
  if (!embeddingsCache) {
    const response = await fetch('https://rnzor.github.io/awesome-tech-failures/api/v1/embeddings.json');
    const data = await response.json();
    embeddingsCache = data;
  }
  return embeddingsCache;
}
```

2. Load hybrid lookup for pre-embedded terms:
```typescript
let hybridLookupCache: Record<string, number[]> | null = null;

async function loadHybridLookup() {
  if (!hybridLookupCache) {
    const response = await fetch('https://rnzor.github.io/awesome-tech-failures/api/v1/hybrid_lookup.json');
    const data = await response.json();
    hybridLookupCache = data.terms;
  }
  return hybridLookupCache;
}
```

3. Cosine similarity function:
```typescript
function cosineSimilarity(vec1: number[], vec2: number[]): number {
  let dot = 0, norm1 = 0, norm2 = 0;
  for (let i = 0; i < vec1.length; i++) {
    dot += vec1[i] * vec2[i];
    norm1 += vec1[i] * vec1[i];
    norm2 += vec2[i] * vec2[i];
  }
  return dot / (Math.sqrt(norm1) * Math.sqrt(norm2));
}
```

4. Get query embedding (hybrid approach):
```typescript
async function getQueryEmbedding(query: string, options: { apiKey?: string, useHybridOnly?: boolean } = {}): Promise<number[]> {
  const { apiKey, useHybridOnly = true } = options;
  const hybridLookup = await loadHybridLookup();
  
  if (hybridLookup[query]) {
    console.log('Using pre-embedded term');
    return hybridLookup[query].vector;
  }
  
  if (apiKey && !useHybridOnly) {
    console.log('Using embedding API for custom query');
    const response = await fetch('https://api.openai.com/v1/embeddings', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`
      },
      body: JSON.stringify({
        model: 'text-embedding-3-small',
        input: query
      })
    });
    
    if (!response.ok) throw new Error('Embedding API failed');
    const data = await response.json();
    return data.data[0].embedding;
  }
  
  throw new Error('NO_EMBEDDING_AVAILABLE: Term not in hybrid lookup and no API key provided.');
}
```

5. Similarity search function:
```typescript
async function searchSimilarity(
  query: string,
  topK: number = 5,
  filters?: SearchFilters,
  useHybridOnly: boolean = true,
  apiKey?: string
): Promise<SimilarityResult[]> {
  const embeddings = await loadEmbeddings();
  const queryVector = await getQueryEmbedding(query, { apiKey, useHybridOnly });
  
  const results = embeddings
    .filter(emb => applyFilters(emb, filters))
    .map(emb => ({
      ...emb,
      similarity_score: cosineSimilarity(queryVector, emb.vector)
    }))
    .sort((a, b) => b.similarity_score - a.similarity_score)
    .slice(0, topK);
  
  return results;
}
```

---

## Vite Configuration

### Development Proxy

Create `vite.config.ts` to proxy API requests:

```typescript
import { defineConfig } from 'vite';

export default defineConfig({
  server: {
    proxy: {
      '/api': {
        target: 'https://rnzor.github.io/awesome-tech-failures',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '/api')
      }
    }
  }
});
```

### Local Build with API Files

```bash
# In package.json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build && npm run build:api && cp -r public/api dist/api"
  }
}
```

---

## Performance Considerations

1. Embeddings Loading:
   - File size: ~256KB
   - Load time: < 100ms on modern browsers
   - Cache in localStorage for faster subsequent loads

2. Similarity Calculation:
   - Complexity: `O(N * d)` where N is entry count and d is dimensions.
   - Time: Expected < 10ms for current dataset.
   - Scales linearly with entry count.

3. Hybrid Mode:
   - Pre-embedded terms: Instant (no network)
   - Custom queries: Requires API call (100-500ms)

4. Optimizations:
   - Implement Web Workers for similarity calculation
   - Use IndexedDB for embeddings caching
   - Lazy load embeddings on first search only

---

## CORS Configuration

No CORS issues expected when using GitHub Pages.

---

## 🔒 Security & Privacy

1. **API Keys**:
   - **CRITICAL**: Never store OpenAI/external API keys in `localStorage` or `cookies`.
   - Use per-session memory input only.
   - For public deployments, forced `useHybridOnly: true` is recommended.

2. **Data Privacy**:
   - All similarity calculations happen locally.
   - No failure data is sent to external servers unless a custom embedding is requested.

---

## TypeScript Types

Generate types from OpenAPI spec:

```bash
npm install -D openapi-typescript
npx openapi-typescript https://rnzor.github.io/awesome-tech-failures/openapi.yaml -o src/types/api.ts
```

---

## Next Steps

1. Set up Vite proxy for development
2. Load embeddings on app mount
3. Implement cosine similarity function
4. Add hybrid lookup for common terms
5. Create search UI component
6. Test with various queries
7. Deploy to production

---

## Support

For issues or questions:
- Check [API Documentation](https://rnzor.github.io/awesome-tech-failures/swagger-ui.html)
- Open an issue at: https://github.com/rnzor/awesome-tech-failures/issues
