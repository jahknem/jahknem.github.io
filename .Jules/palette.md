# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2025-04-09 - Semantic Login Forms
**Learning:** Legacy interfaces often use a generic `<div>` container coupled with an `onclick` handler on a generic button for simple auth flows. This breaks keyboard accessibility because the standard "Enter to Submit" form behavior is missing.
**Action:** When auditing or implementing simple login logic, always wrap inputs inside a semantic `<form>` tag and use `onsubmit="event.preventDefault(); ..."` coupled with a `<button type="submit">` element.
