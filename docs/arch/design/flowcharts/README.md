Figma flowcharts import README

Files added:
- design/flowcharts/user-journey.svg
- design/flowcharts/frontend-architecture.svg
- design/flowcharts/backend-architecture.svg

How to import into Figma
1. Open Figma -> File -> Place Image (or drag & drop) and select the SVG files in `design/flowcharts/`.
2. Each SVG will be imported as a vector group. Ungroup if you need to edit shapes/text.
3. Create a new page in your Figma file named "Flowcharts" and place the imported SVGs there.
4. To convert any legend/text to Figma text layers (editable), ungroup the SVG and replace or edit the text nodes.

What each flowchart shows
- user-journey.svg: primary conversion path (Home → Services → Sign-up → Dashboard) plus feedback loop.
- frontend-architecture.svg: UI components, data flow to client-side state, and integration hints (SVG icons, tokens, responsive behavior).
- backend-architecture.svg: API gateway, services (Auth, Content, Analytics), databases and third-party integrations.

How to use in design reviews
- Use the "Flowcharts" page to annotate responsibilities: assign components to design (UI Kit) vs engineering (API contract).
- Link frames in Figma Prototype mode to show end-to-end flows: for example, click hero CTA → open Services frame; click Sign-up → show modal.

Developer handoff tips
- Export these flowcharts as PNG for documentation or leave as SVG for high-quality prints.
- Add links to relevant code files in the Figma file (e.g., link to `home-1.html`, `css/style.css`) in the Handoff page.

If you want, I can now:
- Convert these SVGs into editable Figma components (split shapes & text into frames and components)
- Produce a printable PDF flow diagram for stakeholder review
- Add swimlanes (User / Frontend / Backend) to each flowchart for clearer responsibilities

Which of these follow-ups do you want next?