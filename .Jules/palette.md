# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Form wrappers for auth gates
**Learning:** Adding a standalone client-side authentication UI (like RDM53 terminal login) often misses semantic form elements. Wrapping inputs in a `<form>` and handling `onsubmit` allows standard browser behavior like pressing "Enter" to submit, significantly improving usability and accessibility.
**Action:** When implementing or reviewing login/access UI elements, always ensure they are wrapped in semantic `<form>` tags, use `onsubmit` with `event.preventDefault()` to handle logic, have a submit button, and provide `aria-label`s for inputs lacking explicit `<label>` tags. Also, use `role="alert"` for dynamically displayed error messages.
