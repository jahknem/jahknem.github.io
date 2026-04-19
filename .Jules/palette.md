# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Form Elements for Login Inputs
**Learning:** Using a simple `<div>` for a login container with an `onclick` handler on a `<button>` prevents users from using the native "Enter" key to submit the form. Also, dynamically shown error messages may not be announced by screen readers without a `role="alert"`.
**Action:** Always wrap standalone login inputs in semantic `<form>` elements and use `onsubmit` (with `event.preventDefault()`) for native keyboard submission support. Add `aria-label` to inputs missing a visual label, and use `role="alert"` for validation error text.
