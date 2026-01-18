"""
Awesome Tech Failures - Intelligence Layer
"""
import json
from pathlib import Path

HERE = Path(__file__).parent

def load_entries():
    """Load all failure entries."""
    with open(HERE / 'entries.ndjson', 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f if line.strip()]

def load_patterns():
    """Load all failure patterns."""
    with open(HERE / 'patterns.ndjson', 'r', encoding='utf-8') as f:
        return [json.loads(line) for line in f if line.strip()]

def load_sources():
    """Load the source registry."""
    with open(HERE / 'sources.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def load_graph():
    """Load the connectivity graph."""
    with open(HERE / 'graph.json', 'r', encoding='utf-8') as f:
        return json.load(f)
