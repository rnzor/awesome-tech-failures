# Sources & Evidence Index 📚

This document maps repo entries to **public sources**.
Some failures are documented as single incidents; others are **repeated patterns**
observed across multiple credible sources.

We explicitly distinguish between the two.

---

## Evidence Types

- **direct-incident**  
  A specific event with a clear timeline and public write-up.

- **repeated-pattern**  
  Multiple independent write-ups describing the same failure mode.
   Common in AI, automation, and decision failures where companies avoid postmortems.

---

## AI Slop & Automation Failures

### AI Agents with Destructive Tool Access

**Evidence type:** repeated-pattern

**Sources:**
- LangChain blog & docs: agent safety and tool misuse
- Engineering blogs warning against giving LLMs write access
- Conference talks (SREcon, KubeCon) on unsafe automation

**Notes:**
This pattern appears repeatedly in internal retrospectives shared publicly,
even when companies avoid naming incidents.

---

### Runaway AI Agents / Token Cost Explosions

**Evidence type:** direct-incident

**Sources:**
- LangChain GitHub issues documenting infinite agent loops
- Hacker News posts: "My LLM agent burned $X overnight"
- Cloud cost postmortems referencing uncontrolled automation

---

### AI-Generated SEO Content Causing Ranking Drops

**Evidence type:** direct-incident

**Sources:**
- Google Search Central blog (Helpful Content updates)
- Ahrefs & SEMrush case studies
- SEO agency postmortems showing before/after traffic loss

---

### LLM-Written Code Breaking Production

**Evidence type:** repeated-pattern

**Sources:**
- GitHub Copilot discussions & blog posts
- Engineering blogs: "Why we stopped merging AI-generated code blindly"
- Indie Hacker retrospectives on AI-heavy codebases

---

### Prompt Injection & Tool Abuse

**Evidence type:** direct-incident

**Sources:**
- OWASP Top 10 for LLM Applications
- Microsoft security blogs on prompt injection
- Academic papers on LLM tool exploitation

---

### AI Summaries Replacing Understanding (Decision Failures)

**Evidence type:** repeated-pattern

**Sources:**
- Research on automation bias
- Management blogs on dashboard-driven decisions
- Internal retrospectives shared publicly

---

### "Vibe Coding" → Unmaintainable Systems

**Evidence type:** repeated-pattern

**Sources:**
- Indie Hacker shutdown posts
- Engineering blogs on failed rewrites
- GitHub discussions about AI-generated architectures

---

### Over-Automated Customer Support Destroying Trust

**Evidence type:** direct-incident

**Sources:**
- Air Canada chatbot incident (2024)
- SaaS company reversals ("we brought humans back" posts)
- CX industry analyses

---

## Production & Security Incidents

### GitHub Database Outage (2018)

**Evidence type:** direct-incident
**Source:** GitHub Engineering Blog

---

### AWS us-east-1 S3 Outage (2017)

**Evidence type:** direct-incident
**Source:** AWS Postmortem

---

### Capital One Data Breach (2019)

**Evidence type:** direct-incident
**Sources:** DOJ filings, public disclosures

---

## Notes on Evidence

- Absence of a single "perfect" postmortem does **not** mean a failure is fictional.
- AI and automation failures are often **underreported**, not nonexistent.
- Repeated patterns are labeled as such to maintain honesty and trust.

If you believe an entry lacks sufficient evidence, open an issue or PR with sources.
