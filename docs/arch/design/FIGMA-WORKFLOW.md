Figma workflow for Graduation-502 website

Goal
- Provide a clear workflow and starter assets so the development and design team can quickly create high-fidelity designs and prototypes in Figma that match the site's new professional brand (teal/orange, deep-slate backgrounds).

Deliverables
- Figma file structure guide (pages + frames)
- Design tokens (color, typography, spacing) as JSON for plugin import
- Starter wireframes (SVGs) for Home hero, Services, About, Contact
- Developer handoff checklist and export settings

Project setup (in Figma)
1. Create a new Figma file and name it: "Graduation-502 - Design System"
2. Pages to create:
   - 00 - Cover & Brief
   - 01 - Tokens (colors, type, spacing)
   - 02 - UI Kit (buttons, form inputs, cards)
   - 03 - Wireframes (home, services, about, contact)
   - 04 - High-Fidelity (desktop / tablet / mobile)
   - 05 - Prototypes
   - 06 - Handoff (assets + specs)
3. Create a component library inside "UI Kit" using Figma Components. Use Variants for button states and icons.

Design tokens & structure
- Import the provided `figma-tokens.json` (Design Tokens plugin or Tokens Studio): it includes brand colors, background shades, typography scale and spacing. Keep tokens hierarchical and named logically (eg: color/brand/primary).

Pages and frames
- Wireframe frames: 1440 (desktop), 1024 (tablet), 390 (mobile).
- Home frame breakdown:
  - Header (logo + menu/hamburger)
  - Hero (logo, typewriter heading, subheading, CTA)
  - Services preview (grid of cards)
  - About (photo + text)
  - Footer
- For each page, create a low-fidelity wireframe and then a high-fidelity version using the UI Kit.

Component recommendations
- Buttons: Primary (teal bg + white text), Secondary (outline), Accent (orange). Create variants for hover/active/disabled.
- Cards: subtle glass/card-surface with drop shadow. Make card components responsive with auto-layout.
- Inputs: single-line text, textarea, select, with error states.
- Iconography: use SVG icons and create an Icon component set. Use `currentColor` so color tokens control fills.

Prototyping interactions
- Typewriter effect: prototype with smart animate and text replacement or use a simple microinteraction for initial load.
- Menu: prototype the open/close overlay for mobile using overlay positioning.
- CTA flows: link hero CTA to Services page / Sign-up modal.

Developer handoff
- Use the Inspect panel to copy CSS values. Export icons as SVG and images at 1x and 2x where needed.
- Export settings for images: PNG or JPG for photos, SVG for icons and logos.
- Provide a small README in the Figma file with tokens mapping to CSS variables used in `css/style.css` (example: --brand-primary -> color/brand/primary).

Plugins & resources
- Recommended plugins: "Design Tokens", "Figma Tokens", "Content Reel", "Icons8 / Feather Icons", "Annotate This" (for specs)

Workflow cadence (example)
1. Create tokens and UI kit (1-2 days)
2. Wireframes for all pages (1 day)
3. High-fidelity mockups (2-3 days)
4. Prototyping & basic testing (1 day)
5. Handoff & asset export (0.5 day)

Handoff checklist
- Tokens page completed and synced to Design Tokens plugin
- All components documented with usage notes and variants
- Exported assets in /design/exports and linked in Handoff page
- Developer notes for responsive breakpoints and CSS variable names

Notes
- Keep naming consistent and use auto-layout. Group by function, not by visual placement.
- If you want, I can produce high-fidelity mockups next (desktop and mobile) using the tokens and assets created here.
