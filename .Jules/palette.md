# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Semantic Forms and Native Submission
**Learning:** Adding inputs inside a non-semantic container (like a `<div>`) instead of a proper `<form>` prevents users from using native submission methods (e.g., hitting the 'Enter' key).
**Action:** Always wrap inputs and action buttons in a semantic `<form>` and use `onsubmit` with `event.preventDefault()` to run validation or async logic while supporting standard accessibility/usability expectations like `button[type="submit"]`. Use `role="alert"` for dynamically displayed error messages within the form.
