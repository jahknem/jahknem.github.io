# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.
## 2024-11-20 - RDM53 Login Form Form Semantics
**Learning:** Adding a semantic `<form>` wrapper to login input groups (even simple custom-auth implementations) unlocks expected native browser behaviors, critically the ability to submit the form via the "Enter" key, drastically improving keyboard accessibility. Using `role="alert"` for error messages ensures screen readers pick up the dynamic text immediately.
**Action:** Always verify custom login or code gates have proper `<form>` wrappers with `onsubmit`, and verify dynamically displayed errors have `role="alert"`.
