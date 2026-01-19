# Product & Strategy Failures 🧪

Good engineering, wrong product. Solid execution, wrong market.
When the product was built but nobody wanted it.

---

## Entry Template

> **Header Format:** `### (YYYY) Title` or `### (YYYY-YYYY) Title` (use END year for ranges).
> For ongoing issues, use `### (Ongoing) Title` and add `year: YYYY` to frontmatter.

```yaml
---
type: product
cause: [timing|ecosystem|ux-mismatch|platform-risk]
stage: [early|growth|scale|decline]
impact: [money|trust|users]
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

## Premature Launches

### (2014) Google Glass — Technology Ahead of Society

```yaml
---
type: product
cause: timing
stage: growth
impact: trust
tags: [premature, privacy, fashion, user-acceptance, enterprise-pivot]
evidence-type: direct-incident
sources:
  - https://www.investopedia.com/articles/investing/052115/how-why-google-glass-failed.asp
supporting-entities: [Google]
---

**What happened:** Google launched Glass as a consumer product in 2014 for $1,500. Pulled from market in 2015. Eventually pivoted to enterprise, then discontinued entirely in 2023.

**Impact:** $1,500 device with no practical use case; privacy backlash ("Glassholes"); never achieved mainstream adoption; reputation damage for Google hardware.

**Root cause:** Technology was 5-10 years ahead of social acceptance; no killer app justified the form factor; privacy concerns made people uncomfortable; $1,500 price point with no clear value; marketing couldn't manufacture "cool."

**Lessons:**
- Technology readiness ≠ market readiness
- Social acceptance is as important as technical readiness
- Privacy concerns are product risks, not edge cases
- "Cool" can't be bought through influencer marketing

**Related failure patterns:**
- Overconfidence From Past Success

```

### (2012) Google Wave — Technically Impressive, User Failure

```yaml
---
type: product
cause: incentives
stage: growth
impact: users
tags: [ux-mismatch, wrong-market, documentation-heavy, collaboration-complexity]
evidence-type: direct-incident
sources:
  - https://googleblog.blogspot.com/2012/08/update-on-google-wave.html
supporting-entities: [Google]
---

**What happened:** Google Wave launched as a "revolutionary" collaboration tool combining email, chat, and documents. Despite technical innovation, users couldn't understand its value proposition.

**Impact:** Product discontinued; user adoption never materialized; valuable technology absorbed into other products; significant engineering investment lost.

**Root cause:** UX complexity too high; unclear value proposition; users needed tutorials just to understand the product; "cool tech" doesn't create demand; marketing confused novelty with value.

**Lessons:**
- Cool tech doesn't create demand
- If users need tutorials, you're already in trouble
- Value proposition must be obvious within seconds
- Technical excellence ≠ product success

**Related failure patterns:**
- Ecosystem Neglect

```yaml
severity: medium
recurrence: single
prevention: Test value proposition on naive users without documentation; simplicity before features
```

```

### (2017) Windows Phone — Ecosystem Neglect

```yaml
---
type: product
cause: incentives
stage: scale
impact: users
tags: [ecosystem-failure, platform-risk, developer-trust, late-entry, app-gap]
evidence-type: direct-incident
sources:
  - https://www.theverge.com/2017/10/8/16437700/microsoft-windows-phone-dead
supporting-entities: [Microsoft]
---

**What happened:** Windows Phone launched with a strong, innovative OS but failed to attract app developers. By 2017, the platform was abandoned, leaving users without support or apps.

**Impact:** Platform abandoned; billions in investment lost; user trust destroyed; developers who invested in the platform left stranded; mobile market permanently lost to iOS/Android.

**Root cause:** Late market entry; developer ecosystem neglected; app gap persisted too long; developer trust is non-renewable; competing platforms had insurmountable network effects.

**Lessons:**
- Platforms live or die by ecosystems
- Developer trust is non-renewable — once burned, they won't return
- Late entry requires 10x better, not 10% better
- App ecosystem gap is a death spiral, not a temporary problem

**Related failure patterns:**
- Ecosystem Neglect

```yaml
severity: critical
recurrence: single
prevention: Launch ecosystems before products; developer trust is non-renewable
```

```

---

### (2019) Google+ — The Social Network Nobody Wanted

```yaml
---
type: product
cause: incentives
stage: scale
impact: [users, trust]
tags: [social-network, forced-integration, privacy-breach, network-effects, late-entry]
evidence-type: direct-incident
severity:
  level: high
  score: 7
  financial: Billions in investment
sources:
  - https://blog.google/technology/safety-security/project-strobe/
  - https://www.theverge.com/2019/4/2/18290637/google-plus-shutdown-consumer-version-today
supporting-entities: [Google, The Verge]
---

**What happened:** Google launched Google+ in 2011 to compete with Facebook, forcing integration across Google products. After years of low engagement, a privacy breach became the final trigger for shutdown in 2019.

**Impact:** Billions in investment lost; forced integrations damaged other Google products; privacy breach affected 500K users; reinforced that Google struggles with social.

**Root cause:** Launched to compete, not to serve users; forced adoption created resentment; network effects favor incumbents; bolting social onto utility products doesn't create social behavior.

**Lessons:**
- Forced adoption creates usage, not engagement
- Network effects mean second place often means zero
- Social products require social DNA, not just social features
- Internal metrics (signups) can mask external reality (nobody cares)

**Related failure patterns:**
- Ecosystem Neglect
- Overconfidence From Past Success
```

---

### (2014) Amazon Fire Phone — When Amazon Tried to Be Apple

```yaml
---
type: product
cause: incentives
stage: growth
impact: [money, trust]
tags: [hardware, wrong-market, amazon-ecosystem, premium-pricing, gimmick-features]
evidence-type: direct-incident
severity:
  level: high
  score: 7
  financial: $170M write-off
sources:
  - https://www.fastcompany.com/3039887/fire-phone-was-a-misfire-but-amazon-isnt-done-reinventing-the-smartphone
  - https://www.theverge.com/2014/12/16/7404231/amazon-fire-phone-83-million-loss
supporting-entities: [Amazon, Fast Company, The Verge]
---

**What happened:** Amazon launched the Fire Phone at $199 with gimmick features (Dynamic Perspective 3D) that nobody asked for. Within months, price dropped to $0.99; Amazon wrote off $170M in unsold inventory.

**Impact:** $170M write-off; hardware division restructured; reinforced that Amazon's strength is services, not premium devices.

**Root cause:** Built to drive Amazon shopping, not to be a great phone; gimmick features over core functionality; premium price without premium value; ignored what made Kindle successful (low price, single purpose).

**Lessons:**
- Gimmick features don't overcome fundamental value propositions
- Amazon's ecosystem strength is low prices and convenience, not premium hardware
- Copying Apple's playbook requires Apple's brand
- Phones are commodities; differentiation must be 10x, not 10%

**Related failure patterns:**
- Money ≠ Product-Market Fit
- Overconfidence From Past Success
```

---

### (2013) Facebook Home — Replacing Android, Alienating Users

```yaml
---
type: product
cause: timing
stage: growth
impact: [users, trust]
tags: [mobile, ux-mismatch, user-rejection, forced-social, platform-overreach]
evidence-type: direct-incident
severity:
  level: medium
  score: 5
  financial: Reputation damage
sources:
  - https://www.theverge.com/2013/5/13/4325050/htc-first-facebook-home-phone-report-card
  - https://techcrunch.com/2013/06/14/facebook-home-1-million/
supporting-entities: [Facebook, HTC, TechCrunch]
---

**What happened:** Facebook launched "Home" — an Android launcher that replaced your home screen with Facebook content. The dedicated HTC First phone flopped; app removed from Play Store after abysmal ratings.

**Impact:** HTC First price dropped from $99 to $0.99 in weeks; app ratings below 2 stars; demonstrated Facebook's inability to own the device layer.

**Root cause:** Users didn't want Facebook to own their phone experience; replaced useful home screen with content stream; privacy concerns in always-on Facebook mode; assumed users wanted more Facebook, not productivity.

**Lessons:**
- Owning the home screen requires earning trust, not forcing presence
- Social content as default interface is exhausting, not engaging
- Diminishing returns on Facebook surface area
- Users will reject products that prioritize platform over user

**Related failure patterns:**
- Ecosystem Neglect
```

---

## Ecosystem Dependencies

### (2001-2020) Segway — The Future That Wasn't

```yaml
---
type: product
cause: timing
stage: growth
impact: [money, trust]
tags: [overhype, wrong-market, regulation, infrastructure-dependency, premium-pricing]
evidence-type: direct-incident
severity:
  level: medium
  score: 6
  financial: $100M+ investment
sources:
  - https://www.wired.com/story/rise-and-fall-of-the-segway/
  - https://www.bbc.com/news/technology-53181792
supporting-entities: [Segway, Wired, BBC]
---

**What happened:** Segway launched in 2001 with hype claiming it would "change cities." It became a mall cop vehicle and tourist rental. Production ended in 2020 after selling ~140,000 units total.

**Impact:** Never achieved mainstream adoption; became cultural punchline; investors lost $100M+; proved that hype cannot manufacture demand.

**Root cause:** Solved a problem (walking) that wasn't painful enough; premium pricing ($5,000) for marginal utility; required infrastructure (sidewalks, regulations) that didn't exist; hype created unrealistic expectations.

**Lessons:**
- Revolutionary tech requires revolutionary problems
- Infrastructure dependencies can kill products
- Hype creates expectations that poison adoption
- Niche success (security, tourism) can mask mass-market failure

**Related failure patterns:**
- Money ≠ Product-Market Fit
- Overconfidence From Past Success
```

---

## UX Mismatches

## Platform Risk

## Timing Failures
