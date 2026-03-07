# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2025-01-20 - Semantic Form Submission
**Learning:** Using a simple `<div>` for a login container with a generic `<button onclick="...">` breaks native keyboard accessibility because users expect to be able to press "Enter" to submit a form.
**Action:** Always wrap login/access inputs in a semantic `<form>` element, use `onsubmit` to handle the logic (with `event.preventDefault()`), and use `<button type="submit">`. Also, adding an `aria-label` to inputs without a visible `<label>` and `role="alert"` for error messages are crucial a11y improvements.
