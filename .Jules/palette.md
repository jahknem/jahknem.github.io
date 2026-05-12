# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.
## 2026-05-12 - Login Form UX
**Learning:** Standalone inputs without a form wrapper break the natural "press Enter to submit" expectation, degrading UX.
**Action:** Always wrap login/access inputs in a semantic `<form>` with an `onsubmit` handler to support default keyboard behaviors, and ensure proper ARIA attributes like `aria-label` for unlabeled inputs and `role="alert"` for dynamic error messages.
