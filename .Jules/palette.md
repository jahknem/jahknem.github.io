# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Form Semantics in Custom Layouts
**Learning:** Standalone custom layouts (like terminals) often use `div`s and `onclick` handlers for inputs, breaking native keyboard submission (Enter key).
**Action:** Always wrap input-button pairs in a `<form>` tag with `onsubmit` to enable native browser behaviors like "Enter to submit" and accessibility support.
