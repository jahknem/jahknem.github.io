# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2026-06-10 - Accessible Client-side Login Forms
**Learning:** Raw input fields and buttons with `onclick` handlers for client-side gates (like the RDM53 terminal login) break screen reader expectations, miss out on native validation, and fail to announce dynamic errors.
**Action:** Always wrap login/access inputs in a semantic `<form>` element, use `onsubmit` to handle logic (with `event.preventDefault()`), use `<button type="submit">`, add `aria-label` to inputs lacking visible `<label>` tags, and use `role="alert"` for dynamic error messages.
