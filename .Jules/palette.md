# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## $(date +%Y-%m-%d) - Wrap login inputs in form and add accessibility tags
**Learning:** Found an isolated login prompt using an `onclick` handler on a plain `<button>` instead of a `<form>` submission. This prevented users from using the Enter key to login. Additionally, missing `aria-label` and `role="alert"` caused issues for screen readers.
**Action:** Always wrap inputs in a semantic `<form>` element, capture submission via `onsubmit` using `event.preventDefault()`, and annotate inputs missing explicit labels with `aria-label`, and dynamic error messages with `role="alert"`.
