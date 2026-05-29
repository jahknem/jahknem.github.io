# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-29 - Login Form Accessibility
**Learning:** Custom login gates implemented as static `<div>` containers with click handlers miss crucial native form behaviors (like "Enter" to submit) and accessibility features.
**Action:** Always wrap input and submit button combinations in semantic `<form>` elements with `onsubmit` handlers, and ensure inputs without visible text labels have `aria-label` attributes. Add `role="alert"` for error messages.
