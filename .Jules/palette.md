# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2026-03-27 - Semantic Forms for Login Accessibility
**Learning:** Wrapping login inputs in a semantic `<form>` tag, using a `type="submit"` button, and preventing default behavior with `onsubmit` ensures keyboard navigation (like hitting Enter) natively submits the form. Also, error messages should use `role="alert"` for screen reader accessibility, and unlabelled inputs must have an `aria-label`.
**Action:** When implementing standalone login or input containers, always wrap them in a semantic `<form>` and use proper ARIA labels and roles.
