# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2025-02-12 - Wrap Login Inputs
**Learning:** Wrapping login inputs in a semantic `<form>` component adds necessary keyboard accessibility features, like the "Enter" key trigger.
**Action:** When adding accessibility features to input fields, ensure that related elements are grouped in a `<form>` block and the submission input type is set to `submit`.
