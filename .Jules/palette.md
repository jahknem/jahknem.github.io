# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.
## 2024-05-25 - Form Submission Accessibility
**Learning:** Standalone inputs and buttons lacking a `<form>` wrapper prevent expected keyboard behaviors (like pressing "Enter" to submit), degrading UX for keyboard and screen reader users.
**Action:** Always wrap inputs meant for submission inside a semantic `<form>` tag, even for purely client-side logic, and utilize `onsubmit` with `event.preventDefault()`.
