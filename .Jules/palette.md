# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-07-02 - Form Semantics for Access Gates
**Learning:** Simple access gates built with raw inputs and JavaScript buttons lack natural keyboard support (like hitting Enter to submit) and semantic meaning for screen readers.
**Action:** Always wrap login/access inputs in a semantic `<form>` element, use `onsubmit` (with `event.preventDefault()`) for logic handling, use `<button type="submit">`, add `aria-label` to inputs lacking visual labels, and use `role="alert"` for dynamic error messages.
