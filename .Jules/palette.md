# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Form Semantics for Access Gates
**Learning:** Using purely `<div>` based access controls (like in RDM53's login prompt) breaks Enter-key submission and reduces screen reader context compared to a semantic form.
**Action:** Always wrap login/access inputs in a semantic `<form>` element, use `onsubmit` with `event.preventDefault()`, a `type="submit"` button, `aria-label` for inputs, and `role="alert"` for dynamic error messages to ensure both accessibility and standard keyboard interactions.
