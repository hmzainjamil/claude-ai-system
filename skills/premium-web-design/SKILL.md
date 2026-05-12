# Premium Web Design — AI-Powered Workflow Skill

## Trigger Phrases (auto-activates on any of these)
- "premium website", "build a site", "design a website", "web design workflow"
- "stitch mockup", "google stitch", "nano banana", "21st.dev", "ux skill pack"
- "design blueprint", "mockup to code", "pixel perfect site"
- "ugc website", "build landing page premium", "premium ui", "pro website"

---

## OVERVIEW

Four-tool stack that takes a client brief → pixel-perfect site in one session:

| Tool | Role | Cost |
|---|---|---|
| **Google Stitch MCP** | Prompt → high-fidelity mockup | Free |
| **Nano Banana/2** | Refine with shadows, textures, realism | Free/cheap |
| **GitHub UX/UI Skill Pack** | Embed spacing + hierarchy rules into Claude | Free |
| **21st.dev Asset Library** | Pre-built 3D widgets + reactive components | Free/paid |

---

## WORKFLOW — 5 STEPS

### STEP 1 — BRIEF INTAKE
Collect from client:
- Brand colors (hex codes or URL to pull from)
- Typography preferences (or "choose for me")
- 3 screen sizes needed (mobile / tablet / desktop)
- Key sections: hero, features, pricing, CTA, footer
- Tone: minimal / bold / corporate / playful

### STEP 2 — MOCKUP GENERATION (Google Stitch MCP)
```
Prompt Stitch:
"Create a high-fidelity website mockup for [PRODUCT].
Layout: 12-column grid, 12px baseline.
Colors: [HEX1], [HEX2], [HEX3].
Font: [FONT FAMILY], H1=24pt, H2=18pt, body=14pt/1.5x.
Sections: Header, Hero, Features (3 cards), Pricing, CTA, Footer.
Corner radius: 8px. Style: [minimal/bold/corporate].
Export as layered PNG at 2x resolution."
```

Layer naming convention:
- `Header` · `Hero` · `Features` · `Pricing` · `CTA` · `Footer`
- Export both PNG (visual reference) + SVG (CSS precision)

### STEP 3 — REFINE IN NANO BANANA/2
- Add realistic drop shadows (8px blur, 20% opacity)
- Apply texture overlays where needed
- Final polish: depth, contrast, micro-details
- Export final at 2× resolution for sharper AI interpretation

### STEP 4 — CLAUDE BUILD PROMPT (with UX Skill Pack)
```
Prompt Claude:
"Use the attached mockup as the design blueprint.
Apply Pro UX spacing rules: 12px grid, 1.5x line height,
8px border radius. Build in React/Next.js using Tailwind.
Import these 21st.dev components: [COMPONENT URLS].
Match hierarchy exactly: H1/H2/body as shown.
Color palette: [HEX1 primary], [HEX2 accent], [HEX3 bg].
Output: production-ready component files."
```

UX Skill Pack rules auto-applied:
- 12px baseline grid for all margins/padding
- Color palette max 3–4 shades
- Line height = 1.5× font size
- H1/H2/body hierarchy locked
- Consistent corner radius throughout

### STEP 5 — 21ST.DEV COMPONENT DROP-IN
Go to **21st.dev** → search for needed components:
- 3D hero elements · animated counters · testimonial carousels
- Pricing tables · CTA blocks · nav menus · footer layouts

Copy HTML/CSS snippets → replace placeholder blocks in Claude output.

Run visual diff:
```bash
# Side-by-side compare: AI output vs original mockup
# Check: spacing ✓ typography ✓ colors ✓ alignment ✓ components ✓
```

---

## QUALITY CHECKLIST (run before delivery)

- [ ] Color palette ≤ 4 shades, all hex-defined
- [ ] Typography: H1 24pt · H2 18pt · body 14pt · line-height 1.5×
- [ ] 12px baseline grid applied throughout
- [ ] All 3 screen sizes (mobile/tablet/desktop) render correctly
- [ ] 21st.dev components replaced all placeholders
- [ ] Visual diff vs mockup: zero alignment drift
- [ ] Corner radius consistent (8px default)
- [ ] Layer names match section names

---

## COMMON PITFALLS + FIXES

| Pitfall | Fix |
|---|---|
| "Make it look modern" (vague) | Attach mockup with hex codes + font specs |
| Generic placeholders | Pre-select 21st.dev assets before prompting |
| Alignment drift | Run visual diff before delivery |
| Spacing errors | Load UX skill pack rules in every Claude prompt |
| Missing responsive breakpoints | Specify all 3 sizes in Stitch prompt |

---

## RATE POSITIONING

With this stack:
- Generic AI site: $200–500
- **Premium AI site (this workflow): $1,500–4,000**
- Differentiator: mockup-first approach + 21st.dev components + UX rules
- Client sees: professional polish, not "AI draft"

---

## QUICK COMMANDS

```bash
# Check 21st.dev for components
open https://21st.dev

# Clone UX/UI skill pack (if not already present)
git clone --depth=1 https://github.com/nicholasgasior/ux-patterns ~/.claude/skills/ux-ui-pack/

# Stitch MCP — add to .mcp.json if not wired
# "stitch": { "command": "npx", "args": ["@google/stitch-mcp"] }
```

---

## AUTO-AGENTS ACTIVATED WITH THIS SKILL

- **UX Architect** — CSS systems, component hierarchy, design tokens
- **Frontend Developer** — React/Next.js/Tailwind implementation
- **UI Designer** — visual system, spacing, typography enforcement
- **Brand Guardian** — color palette + brand consistency checks
