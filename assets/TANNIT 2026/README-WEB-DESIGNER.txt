TANNIT Agency — Design System
For: Web Designer
Version 2.0 · April 2026
Contact: hello@tannitagency.es · tannitagency.es
======================================================

This folder is the single source of truth for the TANNIT visual identity.
Do not recreate, modify or substitute any asset without approval.


QUICK START
──────────────────────────────────────────────
1. Read the Brand Guidelines first (see below)
2. Use SVG assets wherever possible — they are the primary format
3. PNG is the fallback for contexts where SVG is not supported
4. Any decision not covered by the guidelines → ask before implementing


BRAND GUIDELINES
──────────────────────────────────────────────
File: TANNIT_Brand_Guidelines_EN_v2.html
Open in Chrome or Edge (not Firefox).

Covers: brand strategy · logo system · colour palette · typography ·
        iconography · illustration · layout & grid · digital applications ·
        brand voice · asset package · digital marketing sub-brand (ch. 12)

Chapters relevant to web:
  Ch. 04  Colour Palette       — hex values, usage rules, never-do list
  Ch. 05  Typography           — typefaces, scale, hierarchy
  Ch. 06  Iconography          — icon style, sizing, colour variants
  Ch. 07  Illustration         — usage context, which variant where
  Ch. 08  Layout & Grid        — 12-col grid, spacing, white space
  Ch. 09  Digital Applications — buttons, forms, cards, email, navigation
  Ch. 12  Digital Marketing    — extended palette, gradients, pill shapes


COLOURS (quick reference)
──────────────────────────────────────────────
Core brand — paste directly into CSS:

  --purple:      #8a6e9a;   /* Primary accent */
  --purple-dk:   #4a3260;   /* Dark purple, headings on light bg */
  --purple-md:   #a98ebb;
  --purple-lt:   #c9b5d8;
  --purple-pl:   #f2ecf7;   /* Purple tint, backgrounds */
  --teal:        #6aa8a4;   /* Secondary accent */
  --teal-md:     #8ec5c2;
  --teal-lt:     #b4d5d3;
  --teal-pl:     #e8f4f3;
  --warm:        #f8f0e3;   /* Warm white, main background */
  --cream:       #f2e8d4;
  --ink:         #1a1218;   /* Body text */
  --ink-70:      #4a3c52;
  --ink-40:      #9a8aa5;   /* Muted text */
  --ink-15:      #e6e0ec;   /* Borders, dividers */

Digital Marketing sub-brand (ch. 12 only):
  Electric Violet  #7B2FD4
  Magenta          #CC3FCC
  Neon Teal        #50D4CC
  Deep Night       #080820


TYPOGRAPHY
──────────────────────────────────────────────
Headings:   Montserrat (Google Fonts) — weights 600, 700, 800
Body:       Helvetica Neue / Helvetica / Arial (system stack)

Google Fonts import:
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&display=swap" rel="stylesheet">

Scale (see ch. 05 for full hierarchy):
  H1  40–48pt / 800 weight / letter-spacing -0.03em
  H2  24pt    / 700 weight
  H3  13pt    / 600 weight / uppercase / letter-spacing 0.12em
  Body  9.5–10pt / 1.7 line-height


LOGOS/SVG/   — which variant to use
──────────────────────────────────────────────
Dark backgrounds  →  Primary logo - White - Blue.svg
                     Horizontal - Monochrome.- White.svg
                     Isotype - white - blue.svg

Light backgrounds →  Primary logo - Black - Blue.svg
                     Horizontal - Blue - Black.svg
                     Isotype - Black - Blue.svg

Favicon / small   →  Isotype - white - blue.svg  (crop to square)
                     Isotype- square- white - blue.svg  (pre-squared)

Always use SVG. Minimum logo width: 24mm / 90px. Clear space: 1× isotype height on all sides.


ICONS/SVG/   — usage
──────────────────────────────────────────────
Two colour variants per icon: Blue and Purple.
Use Blue icons on light/neutral backgrounds.
Use Purple icons on warm/cream backgrounds or as the primary accent.
Never recolour icons manually — use the supplied variants.
Source Figma file: Icons/Icon set- Tannit- Figma components.fig


ILLUSTRATIONS/SVG/   — usage
──────────────────────────────────────────────
Two variants: Colour (vivid) and Pastel (soft).
Use Colour variant for primary/hero placements.
Use Pastel variant for supporting or secondary contexts.

  Computer     →  Ilustration - Computer.svg / Ilustration- computer- pastel.svg
  Medica       →  Medica - Color.svg / Medica Color Pastel.svg
  Collaboration→  cooperacion.png (PNG only, single colour — SVG pending)


BACKGROUNDS/   — gradient assets
──────────────────────────────────────────────
Ready-to-use SVG backgrounds. All are 1000×1000 unless noted.

Core brand:
  Gradient-01-Digital.svg          DM palette · full spectrum
  Gradient-02-Purple.svg           Purple range (light → dark)
  Gradient-03-Teal.svg             Teal range (light → dark)
  Gradient-04-Violet-Cream.svg     Purple → Warm cream (hero sections)
  Gradient-05-Teal-Black.svg       Neon Teal → Black (DM dark sections)

Atmospheric (hero/cover use):
  Gradient-06-Digital-Orbs.svg     Dark bg + soft teal & violet glows
  Gradient-07-Glass-Blue.svg       Deep blue with warm diagonal light
  Gradient-08-Holographic.svg      Iridescent light (white base)
  Gradient-09-Blue-Cyan-Wave.svg   Electric blue + cyan wave

DM pill system:
  DM-Background-Dark.svg           1200×800 · dark bg with pills (full page)
  DM-Background-Light.svg          1200×800 · light bg with pills
  DM-Gradient-Pills-Sheet.svg      Reference sheet (gradient system + pill library)
  DM-Pill-Horizontal.svg / DM-Pill-Vertical.svg   Single pill assets
  DM-Pills-Composition.svg         Multi-pill decorative composition


VISUAL REFERENCES/
──────────────────────────────────────────────
Internal PDFs for design context — not for the website.
  Pitchdeck2026.pdf         Brand pitch deck (tone & layout reference)
  Briefing web.pdf          Web project brief
  Onepage - Agencia.pdf     Agency one-pager (content & hierarchy reference)
  One page- pharma.pdf      Pharma vertical one-pager


RULES — ALWAYS / NEVER
──────────────────────────────────────────────
ALWAYS
  · Use SVG for logos and icons
  · Use print-color-adjust: exact for any PDF or print export
  · Maintain logo clear space (1× isotype height on all sides)
  · Use Warm White (#F8F0E3) as the default page background
  · Use --ink (#1a1218) for body text

NEVER
  · Stretch, rotate or recolour logos
  · Use pure white (#ffffff) as the only background
  · Apply gradients to body text or labels under 10pt
  · Mix the Digital Marketing gradient palette with core brand in one composition
  · Use more than 2 typeface weights in a single UI component
