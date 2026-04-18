# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Form Submissions and ARIA Alerts
**Learning:** Wrapping login or input fields in a semantic `<form>` element provides native Enter-key submission, vastly improving keyboard accessibility without additional Javascript event listeners. Also, using `role="alert"` on dynamically displayed error message elements ensures screen readers immediately announce errors to users when they occur.
**Action:** Always verify that input structures act as proper forms for optimal UX, add `aria-label` when visible `<label>`s are missing, and use `role="alert"` for client-side validation errors.
