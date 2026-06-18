# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2026-06-18 - Semantic Login Forms
**Learning:** The login UI in custom standalone layouts (like `WebsocketTerminalRDM.html`) was implemented without a semantic `<form>`, making it less accessible for screen readers and keyboard navigation (e.g. Enter to submit). Furthermore, error messages displayed dynamically lack ARIA roles.
**Action:** Always wrap login or access inputs in a `<form>` element, use `onsubmit` with `event.preventDefault()`, and add `role="alert"` to dynamically displayed error messages to ensure proper screen reader announcements.