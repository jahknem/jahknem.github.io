# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-25 - Form Submission & Accessibility
**Learning:** Adding a semantic `<form>` wrapper to standalone inputs enables "Enter-to-submit" behavior automatically, improving usability. Additionally, setting `role="alert"` on dynamic error message containers ensures they are announced by screen readers when validation fails.
**Action:** Always wrap inputs in a `<form>` and use `<button type="submit">` even if the submission logic is handled purely in JavaScript via `onsubmit` and `event.preventDefault()`. Use `role="alert"` for client-side form validation feedback.
