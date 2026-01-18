# Startup Failures 🚀

Shutdowns, runways exhausted, product-market fit misses, and the postmortems
from founders who lived to tell the tale.

---

## Entry Template

```yaml
---
type: startup
cause: [incentives|no-pmf|architecture]
stage: [early|growth|scale|decline]
impact: [money|trust|morale]
tags: [free-form, tags]
evidence-type: [direct-incident|repeated-pattern]
severity:
  level: [critical|high|medium|low]
  score: [1-10]
  financial: [Description or N/A]
sources:
  - https://...
supporting-entities: [Entity1, Entity2]
---

**What happened:** [1-2 lines describing the incident]

**Impact:** [who/what got hit]

**Root cause:** [best-known explanation]

**Lessons:**
- [Actionable lesson 1]
- [Actionable lesson 2]

**Related failure patterns:**
- [Pattern 1]
- [Pattern 2]
```

---

## PMF Failures

### (2020) Quibi — $1.75B Burn in 6 Months

```yaml
---
type: startup
cause: incentives
stage: growth
impact: money
tags: [no-pmf, timing, distribution, wrong-assumptions, premium-content]
evidence-type: direct-incident
sources:
  - https://www.theinformation.com/articles/quibi-the-rise-and-fall-of-a-1-75-billion-failure
supporting-entities: [Quibi, The Information]
---

**What happened:** Quibi raised $1.75B to build "Netflix for your phone" with premium short-form content. Launched April 2020, shut down October 2020. Burned through nearly $2B in under 7 months.

**Impact:** Company closed; investors wiped; 500+ employees laid off; content library sold for scraps; became definitive case study in PMF failure.

**Root cause:** No product-market fit; fundamentally wrong assumptions about mobile viewing habits; content didn't justify subscription; premium positioning meaningless without habit formation; distribution strategy failed.

**Lessons:**
- Money doesn't buy demand
- "Premium" means nothing without habit
- Timing assumptions must be tested, not assumed
- Content differentiation must be obvious, not explained

**Related failure patterns:**
- Money ≠ Product-Market Fit
```

### (2018) Theranos — $9B Fraud Built on Lies

```yaml
---
type: startup
cause: incentives
stage: growth
impact: [money, trust]
tags: [fraud, fake-technology, regulatory-failure, healthcare, due-diligence-failure]
evidence-type: direct-incident
severity:
  level: critical
  score: 10
  financial: $9B valuation to zero
sources:
  - https://www.sec.gov/news/press-release/2018-41
  - https://www.wsj.com/articles/theranos-has-struggled-with-blood-tests-1444881901
supporting-entities: [Theranos, SEC, WSJ]
---

**What happened:** Theranos claimed to revolutionize blood testing with proprietary technology that didn't work. Raised $9B in valuation before SEC fraud charges revealed the technology was fake.

**Impact:** $9B valuation to zero; founder charged with fraud; investors wiped; patients received inaccurate medical results; trust in healthcare startups damaged.

**Root cause:** Fake-it-until-you-make-it culture taken to criminal extremes; board lacked technical expertise; investors skipped due diligence because of founder charisma; "stealth mode" prevented scrutiny.

**Lessons:**
- Technical due diligence is not optional for deep-tech investments
- Prestigious boards don't replace domain expertise
- "Stealth mode" can hide fraud, not just competitive advantage
- Healthcare technology requires regulatory validation, not just investor validation

**Related failure patterns:**
- Money ≠ Product-Market Fit
```

---

### (2019) WeWork — Governance Failure at $47B Valuation

```yaml
---
type: startup
cause: incentives
stage: scale
impact: [money, trust]
tags: [governance-failure, valuation-bubble, founder-control, ipo-failure, burn-rate]
evidence-type: direct-incident
severity:
  level: critical
  score: 9
  financial: $47B to $9B valuation collapse
sources:
  - https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=wework&type=S-1
  - https://www.wsj.com/articles/this-is-not-the-way-everybody-behaves-how-adam-neumanns-over-the-top-style-built-wework-11568823827
supporting-entities: [WeWork, SoftBank, SEC]
---

**What happened:** WeWork's IPO filing revealed massive losses, governance failures, and self-dealing. Valuation collapsed from $47B to $9B; founder forced out; IPO cancelled.

**Impact:** $38B valuation destruction; 2,400 layoffs; SoftBank wrote off billions; became defining example of late-stage startup governance failure.

**Root cause:** Founder had voting control without accountability; board failed oversight; investors prioritized growth over governance; "tech company" narrative masked real estate economics.

**Lessons:**
- Governance matters more at scale, not less
- Dual-class shares concentrate power but also risk
- Valuation is not validation
- IPO scrutiny exposes what private markets ignore

**Related failure patterns:**
- Money ≠ Product-Market Fit
- The Innovator's Dilemma
```

---

### (2022) FTX — $32B Collapse in 10 Days

```yaml
---
type: startup
cause: incentives
stage: scale
impact: [money, trust, users]
tags: [fraud, no-controls, crypto, customer-funds, regulatory-evasion]
evidence-type: direct-incident
severity:
  level: critical
  score: 10
  financial: $32B to zero
sources:
  - https://restructuring.ra.kroll.com/FTX/
  - https://www.justice.gov/opa/pr/ftx-founder-sam-bankman-fried-sentenced-25-years-imprisonment
supporting-entities: [FTX, DOJ, Kroll]
---

**What happened:** FTX, valued at $32B, collapsed in 10 days when it was revealed that customer funds were misappropriated. Founder convicted of fraud; bankruptcy revealed no financial controls existed.

**Impact:** $32B to zero; 1M+ customers lost funds; contagion across crypto industry; founder sentenced to 25 years; became largest financial fraud in tech history.

**Root cause:** No financial controls; customer funds mixed with trading arm; board was nominal; regulatory arbitrage via offshore structure; "effective altruism" narrative masked fraud.

**Lessons:**
- Offshore structures don't eliminate accountability, they delay it
- Customer fund segregation is not optional
- Audits by small firms of large companies are red flags
- Speed of growth doesn't excuse absence of controls

**Related failure patterns:**
- Money ≠ Product-Market Fit
- Misconfigured Trust Boundaries
```

---

## Burn Rate & Runway

### (2017) Juicero — $120M for a Juice Bag Squeezer

```yaml
---
type: startup
cause: no-pmf
stage: growth
impact: [money, trust]
tags: [over-engineering, no-pmf, hardware, silicon-valley-excess]
evidence-type: direct-incident
severity:
  level: medium
  score: 6
  financial: $120M lost
sources:
  - https://www.bloomberg.com/news/features/2017-04-19/silicon-valley-s-400-juicer-may-be-feeling-the-squeeze
supporting-entities: [Juicero, Bloomberg]
---

**What happened:** Juicero raised $120M to build a $400 WiFi-connected juicer. Bloomberg revealed the proprietary juice bags could be squeezed by hand, rendering the machine pointless.

**Impact:** Company shut down 4 months after Bloomberg exposé; $120M in investor funds lost; became symbol of Silicon Valley excess and suspension of common sense.

**Root cause:** Solution looking for a problem; investors didn't ask "can you just squeeze the bag?"; over-engineering masked lack of product-market fit; premium pricing without premium value.

**Lessons:**
- Ask the dumb questions before funding
- Hardware complexity doesn't equal value
- Venture capital can fund solutions to non-problems
- The Bloomberg Test: if a journalist can break your thesis in one paragraph, rethink

**Related failure patterns:**
- Money ≠ Product-Market Fit
```

---

### (2017) Jawbone — $3B Wearables Pioneer to Liquidation

```yaml
---
type: startup
cause: architecture
stage: decline
impact: [money, users]
tags: [hardware, competition, quality-issues, market-timing, fitness-wearables]
evidence-type: direct-incident
severity:
  level: high
  score: 8
  financial: $3B+ raised, liquidated
sources:
  - https://techcrunch.com/2017/07/06/jawbone-is-going-out-of-business/
  - https://www.theverge.com/2017/7/6/15929510/jawbone-going-out-of-business-fitness-tracking
supporting-entities: [Jawbone, TechCrunch, The Verge]
---

**What happened:** Jawbone, once valued at $3B+ as a wearables pioneer, liquidated in 2017 after failing to compete with Fitbit and Apple Watch while struggling with hardware quality issues.

**Impact:** $3B+ in funding lost; hundreds of employees laid off; customers left with unsupported devices; demonstrated that being first doesn't mean winning.

**Root cause:** Hardware quality issues eroded trust; couldn't compete on price with Fitbit or features with Apple; pivoted too late to health-focused B2B; burned cash on legal battles with Fitbit.

**Lessons:**
- First-mover advantage is temporary in hardware
- Quality issues in wearables destroy trust faster than software bugs
- Litigation is not a business strategy
- When the platform players enter your market, differentiate or die

**Related failure patterns:**
- Ecosystem Neglect
- Overconfidence From Past Success
```

---

## Founder Conflict

## Distribution Failures

## Premature Scaling
