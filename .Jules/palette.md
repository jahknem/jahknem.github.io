# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Semantic Forms for Client-Side Auth
**Learning:** Client-side authentication gates often use `div` elements and click handlers instead of semantic `form` elements. This breaks native keyboard accessibility, such as pressing "Enter" to submit.
**Action:** Always wrap login/access inputs in a semantic `<form>` element, use `onsubmit` to handle logic (with `event.preventDefault()`), and use `<button type="submit">` to preserve default browser behaviors and keyboard access.
