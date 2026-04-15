# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2026-04-15 - Accessible Forms and Keyboard Navigation
**Learning:** Standalone input fields with an onclick button are not keyboard-accessible (cannot submit via Enter key). Screen readers also need `aria-label` for inputs without a visible `<label>` and `role="alert"` for dynamic error messages.
**Action:** Always wrap inputs and submit buttons in a semantic `<form>` tag, use `onsubmit="event.preventDefault(); ..."` for client-side handling, use `<button type="submit">`, provide `aria-label`s where necessary, and add `role="alert"` to error elements.
