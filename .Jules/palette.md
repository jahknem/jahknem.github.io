# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-10-24 - Forms for Access Gates
**Learning:** Custom login gates wrapped in `<div>` instead of `<form>` break natural keyboard navigation (like pressing Enter to submit) and lack proper semantics for screen readers. Dynamic error messages also need `role="alert"` to be announced.
**Action:** Always wrap login/access inputs in a semantic `<form>`, use `onsubmit="event.preventDefault(); [logic]"`, `<button type="submit">`, add `aria-label` to inputs without visible `<label>`, and use `role="alert"` for dynamic errors.
