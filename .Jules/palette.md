# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-02-23 - Login Form Accessibility
**Learning:** The login gate UI for RDM53 missed basic form a11y: lacking `<form>` wrapping for Enter-to-submit, missing `aria-label` for placeholder-only input, and missing `role="alert"` for the dynamic error message.
**Action:** Always verify that custom login gates (even client-side ones) use semantic form elements (`<form onsubmit>`, `<button type="submit">`) and provide aria roles for dynamic error content.
