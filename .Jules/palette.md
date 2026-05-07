# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Login Form Accessibility
**Learning:** The simple UI login gate used a standard `<input>` and `<button>` without wrapping them in a semantic `<form>`. This broke "Enter to submit" functionality and lacked an `aria-label` and `role="alert"` for accessibility.
**Action:** Always wrap form-like inputs in an actual `<form>` tag, use `event.preventDefault()` to stop page reloads, and add `role="alert"` for dynamically displayed error messages.
