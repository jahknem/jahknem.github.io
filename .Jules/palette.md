# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Login Form Accessibility
**Learning:** Wrapping login inputs and buttons in a semantic `<form>` element enables native "Enter" key submission, significantly improving keyboard accessibility and UX. Adding `aria-label` to input fields without explicit `<label>` tags and using `role="alert"` for dynamic error messages ensures screen readers can correctly interpret the interface.
**Action:** When working with login components or input fields, always ensure they are wrapped in a `<form>` to leverage native browser behavior, and always provide accessible names and roles for dynamic content.
