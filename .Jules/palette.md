# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Semantic Forms for Custom Gates
**Learning:** Custom UI gates (like the RDM53 terminal login) often use standalone inputs and buttons with `onclick`, breaking standard form behaviors (like "Enter" to submit) and accessibility expectations (missing `<label>` or `aria-label`).
**Action:** Always wrap login/access inputs in a semantic `<form>` element, use `onsubmit` with `event.preventDefault()`, set `<button type="submit">`, add `aria-label` to inputs lacking visible labels, and use `role="alert"` for dynamic error messages.
