# Product & Strategy Failures 🧪

Good engineering, wrong product. Solid execution, wrong market.
When the product was built but nobody wanted it.

---

## Entry Template

```yaml
---
type: product
cause: [timing|ecosystem|ux-mismatch|platform-risk]
stage: [early|growth|scale|decline]
impact: [money|trust|users]
tags: [free-form, tags]
---

**What happened:** [1-2 lines]

**Impact:** [who/what got hit]

**Root cause:** [best-known explanation]

**Lessons:**
- [Actionable lesson 1]
- [Actionable lesson 2]

**Source:** [URL]
```

---

## Premature Launches

### (2014) Google Glass — Technology Ahead of Society

```yaml
---
type: product
cause: timing
stage: growth
impact: trust
tags: [premature, privacy, fashion, user-acceptance, enterprise-pivot]
---

**What happened:** Google launched Glass as a consumer product in 2014 for $1,500. Pulled from market in 2015. Eventually pivoted to enterprise, then discontinued entirely in 2023.

**Impact:** $1,500 device with no practical use case; privacy backlash ("Glassholes"); never achieved mainstream adoption; reputation damage for Google hardware.

**Root cause:** Technology was 5-10 years ahead of social acceptance; no killer app justified the form factor; privacy concerns made people uncomfortable; $1,500 price point with no clear value; marketing couldn't manufacture "cool."

**Lessons:**
- Technology readiness ≠ market readiness
- Social acceptance is as important as technical readiness
- Privacy concerns are product risks, not edge cases
- "Cool" can't be bought through influencer marketing

**Source:** https://www.investopedia.com/articles/investing/052115/how-why-google-glass-failed.asp

**Related failure patterns:**
- Timing Blindness (technology ahead of society)

```

### (2012) Google Wave — Technically Impressive, User Failure

```yaml
---
type: product
cause: incentives
stage: growth
impact: users
tags: [ux-mismatch, wrong-market, documentation-heavy, collaboration-complexity]
---

**What happened:** Google Wave launched as a "revolutionary" collaboration tool combining email, chat, and documents. Despite technical innovation, users couldn't understand its value proposition.

**Impact:** Product discontinued; user adoption never materialized; valuable technology absorbed into other products; significant engineering investment lost.

**Root cause:** UX complexity too high; unclear value proposition; users needed tutorials just to understand the product; "cool tech" doesn't create demand; marketing confused novelty with value.

**Lessons:**
- Cool tech doesn't create demand
- If users need tutorials, you're already in trouble
- Value proposition must be obvious within seconds
- Technical excellence ≠ product success

**Source:** https://googleblog.blogspot.com/2012/08/update-on-google-wave.html

**Related failure patterns:**
- Ecosystem Neglect

```

### (2017) Windows Phone — Ecosystem Neglect

```yaml
---
type: product
cause: incentives
stage: scale
impact: users
tags: [ecosystem-failure, platform-risk, developer-trust, late-entry, app-gap]
---

**What happened:** Windows Phone launched with a strong, innovative OS but failed to attract app developers. By 2017, the platform was abandoned, leaving users without support or apps.

**Impact:** Platform abandoned; billions in investment lost; user trust destroyed; developers who invested in the platform left stranded; mobile market permanently lost to iOS/Android.

**Root cause:** Late market entry; developer ecosystem neglected; app gap persisted too long; developer trust is non-renewable; competing platforms had insurmountable network effects.

**Lessons:**
- Platforms live or die by ecosystems
- Developer trust is non-renewable — once burned, they won't return
- Late entry requires 10x better, not 10% better
- App ecosystem gap is a death spiral, not a temporary problem

**Source:** https://www.theverge.com/2017/10/8/16437700/microsoft-windows-phone-dead

**Related failure patterns:**
- Ecosystem Neglect

```

---

## Ecosystem Dependencies

## UX Mismatches

## Platform Risk

## Timing Failures
