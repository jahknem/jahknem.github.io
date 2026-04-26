# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Login Form Accessibility & Keyboard Support
**Learning:** Hardcoded access gates using simple inputs and buttons (like the `checkAccess` RDM53 gate) often miss critical native form behaviors. Because the input and button weren't wrapped in a semantic `<form>`, users couldn't hit "Enter" to submit, degrading keyboard accessibility and basic UX expectations. In addition, standalone password inputs without explicit `<label>` tags need an `aria-label`, and dynamic error messages must have `role="alert"` for screen readers to notice them when their display state changes from `none` to `block`.
**Action:** Always wrap login/access inputs in a semantic `<form>` element, use `onsubmit` to handle logic (with `event.preventDefault()`), use `<button type="submit">`, add `aria-label` to inputs lacking visible `<label>` tags, and use `role="alert"` for dynamic error messages.
