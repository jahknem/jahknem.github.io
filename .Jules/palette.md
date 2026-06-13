# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Login Form Accessibility and Keyboard Support
**Learning:** Standalone inputs without a surrounding `<form>` prevent natural keyboard interactions, like pressing "Enter" to submit. Additionally, dynamically appearing error messages often lack `role="alert"`, causing screen readers to miss them.
**Action:** Always wrap interactive inputs (like login fields) in a semantic `<form>` with a `<button type="submit">` and handle submission via `onsubmit` with `event.preventDefault()`. Use `role="alert"` for dynamically displayed error messages to ensure they are announced to screen readers.
