# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Native Form Submission
**Learning:** Hardcoded login components utilizing isolated input and button tags fail to support native form submissions via the Enter key. A `<form>` wrapper natively addresses this without custom keydown listeners. Adding screen reader context, like `role="alert"` for error messages, is also frequently missed in such custom auth implementations.
**Action:** Always wrap input fields intended for submission (like login codes or search queries) within a `<form>` element to ensure keyboard accessibility and proper semantics.
