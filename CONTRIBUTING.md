# Contributing

This repo is high-signal. Please keep it that way.

## What We Accept

- Public postmortems, incident reports, breach writeups
- Founder shutdown essays and retrospective posts
- Credible analyses of product failures
- Talks/articles with real lessons (not hot takes)
- Verified AI/automation failures with documentation

## What We Reject

- Speculation without sources
- "AI said..." summaries without the original source
- Clickbait, drama, blamey content
- Duplicate entries (check before adding)
- Vendor FUD without lessons

## Required for Each Entry

1. **Link to a primary source** (preferred) or reputable secondary source
2. **1–2 line "what happened"** summary
3. **At least 2 actionable lessons** — what could have prevented this?
4. **All required tags** (type, cause, stage, impact)
5. **2–5 free tags** for pattern matching

## Entry Format

```yaml
---
type: [ai-slop|outage|security|startup|product|decision]
cause: [ai|automation|architecture|human-error|incentives]
stage: [early|growth|scale|decline]
impact: [data-loss|money|trust|users|morale]
tags: [free-form, tags, here]
---

**What happened:** [1-2 lines]

**Impact:** [who/what got hit, with numbers if possible]

**Root cause:** [best-known explanation]

**Lessons:**
- [Actionable lesson 1]
- [Actionable lesson 2]

**Source:** [URL]
```

## AI Content Rules

- AI can help summarize, but **humans own the final text**
- Label uncertain claims as uncertain
- Don't invent root causes or timelines
- Verify all URLs point to real sources

## Submission Process

1. Fork this repo
2. Add your entry to the appropriate category file
3. Run the validation script: `python validate.py`
4. Submit a PR with:
   - Entry description
   - Source verification
   - Why this adds signal, not noise

## Validation Checks

The CI workflow checks:
- [ ] Valid YAML frontmatter
- [ ] Required tags present
- [ ] Source URL is valid
- [ ] At least 2 lessons listed
- [ ] No markdown formatting errors

---

**Quality over quantity.** We'd rather have 10 well-documented failures than 100 links with no lessons.
