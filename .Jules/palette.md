# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-06-09 - Accessible Form Wrapping
**Learning:** Wrapping login/access UI elements in a semantic `<form>` rather than using standalone inputs with click handlers significantly improves accessibility. It allows screen readers to correctly identify form contexts and enables submit-on-Enter functionality natively, ensuring keyboard-only users can interact intuitively. Adding `role="alert"` for error messages also ensures immediate announcement when login fails.
**Action:** Always wrap interactive access inputs in `<form>` tags, use `<button type="submit">`, and leverage `event.preventDefault()` instead of standalone button clicks.
