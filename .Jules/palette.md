# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Semantic Form Wrappers for Accessibility
**Learning:** Custom login or access hurdles (like the client-side gate for RDM53) often implement input logic solely via JavaScript `onclick` events on buttons. This breaks native "Enter" key submission and removes crucial semantic context for screen readers.
**Action:** Always wrap interactive inputs and their corresponding action buttons in a semantic `<form>` element, utilize `onsubmit` with `event.preventDefault()`, and assign appropriate `aria-label`s to inputs without explicit `<label>` elements. Also, error messages should carry `role="alert"` for proper screen reader announcements.
