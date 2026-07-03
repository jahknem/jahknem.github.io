# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-07-03 - Semantic Forms for Access Gates
**Learning:** Standalone inputs used for access gates (without `<form>` wrappers) break expected user behaviors like "Enter to submit" and reduce screen reader context.
**Action:** Always wrap login/access inputs in a semantic `<form>` element, use `onsubmit` with `event.preventDefault()`, use `<button type="submit">`, add `aria-label` to inputs lacking visible `<label>` tags, and use `role="alert"` for dynamic error messages.
