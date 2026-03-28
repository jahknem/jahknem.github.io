# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-06-25 - Semantic HTML for Custom Auth Gates
**Learning:** Custom authentication gates (like the RDM53 terminal login) often use `<div>` and `<button onclick="...">` which breaks native keyboard accessibility (pressing 'Enter' to submit).
**Action:** Always wrap login/access inputs in a semantic `<form>` element, use `onsubmit` to handle logic (with `event.preventDefault()`), use `<button type="submit">`, and add `role="alert"` for dynamic error messages to ensure screen reader compatibility.
