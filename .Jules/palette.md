# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-22 - Login Form Accessibility Enhancement
**Learning:** Using a structural `<form>` wrapper around simple "Enter code to access" client-side inputs is not just semantic HTML; it unlocks expected implicit submission behaviors (like hitting 'Enter' to submit) without needing extra JS event listeners. Adding `role="alert"` allows JS-injected error states to be naturally announced to screen readers.
**Action:** Always wrap interactive inputs and buttons in a `<form>`, use `onsubmit` handlers for JS-driven auth rather than `onclick` on the button alone, and use `aria-label` for inputs without explicit label tags.
