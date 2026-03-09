# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2026-03-09 - Semantic Forms for Auth Inputs
**Learning:** When creating simple authentication gates or login forms, avoid using standalone inputs and `<button type="button">`. Wrapping inputs in a semantic `<form>` with `onsubmit` logic not only groups them logically for screen readers but critically enables native keyboard submission (pressing "Enter" to submit).
**Action:** Always wrap login/access inputs in a semantic `<form>` element, use `onsubmit` to handle logic (with `event.preventDefault()`), use `<button type="submit">`, add `aria-label` to inputs lacking visible `<label>` tags, and use `role="alert"` for dynamic error messages.
