# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2026-06-28 - Login Form Accessibility
**Learning:** Adding a semantic `<form>` wrapper to login inputs naturally enables "Enter-to-submit" functionality, improving usability for keyboard users. Input elements without explicit `<label>` tags must have an `aria-label` attribute for screen readers. Using `role="alert"` on error messages ensures they are announced dynamically when they appear.
**Action:** When reviewing login forms or custom UI gates, always ensure a semantic `<form>` structure is used, input fields have accessible names, and error messages use `role="alert"`.
