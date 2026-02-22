# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2026-02-22 - Accessible Form Submission
**Learning:** Custom interactive components often use `onclick` handlers on buttons, neglecting standard form submission behavior (Enter key). This frustrates keyboard users.
**Action:** Always wrap input fields and submit buttons in a `<form>` tag with an `onsubmit` handler to support native browser behavior and improve accessibility.
