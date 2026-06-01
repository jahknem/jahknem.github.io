# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Semantic Forms for Client-Side Gates
**Learning:** Simple `<div>` based client-side authentication hurdles often lack keyboard support (e.g., submitting on Enter) and proper screen reader announcements for errors.
**Action:** Always wrap login or access inputs in a semantic `<form>` element, use `<button type="submit">`, add `aria-label` to inputs lacking visible `<label>` tags, and use `role="alert"` for dynamic error messages. Use `onsubmit` with `event.preventDefault()` to handle the logic.
