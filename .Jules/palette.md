# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.
## 2024-05-19 - Improved login form accessibility with semantic HTML
**Learning:** Using `div` and `button type="button"` without a `form` tag on login pages prevents users from pressing "Enter" to submit, causing friction for keyboard navigation. Replacing it with a semantic `<form>` and `onsubmit` requires correctly preventing default actions if using custom JS submission handlers. Additionally, inputs without visual labels must use `aria-label`, and error messages should use `role="alert"` so screen readers immediately voice the failure.
**Action:** Always wrap inputs and action buttons in a semantic `<form>` element, use `event.preventDefault()` in JS handlers when overriding submission, explicitly define `<button type="submit">`, and ensure invisible labels and dynamic error states have appropriate ARIA attributes.
