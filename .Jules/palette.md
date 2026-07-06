# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2025-02-09 - Semantic Forms for Auth Hurdles
**Learning:** Custom authorization hurdles or JS-gated login inputs often use disconnected input fields and standalone buttons with `onclick` handlers, removing the browser's implicit submission behavior (like submitting via 'Enter') which degrades usability and accessibility.
**Action:** Always wrap login/access inputs in a semantic `<form>` element, use `onsubmit` for logic (with `event.preventDefault()`), use a `<button type="submit">`, and add `aria-label` to fields lacking visible `<label>` tags.
