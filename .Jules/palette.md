# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Form Submission UX
**Learning:** Standalone inputs with `onclick` buttons break the expected "Enter to submit" behavior. This is a common pattern in older or "hacky" interfaces (like this terminal emulator).
**Action:** Always wrap input+button groups in a `<form>` tag with `onsubmit` handling, even for client-side only logic. It's a zero-cost accessibility and usability win.
