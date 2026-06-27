# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.
## 2026-06-27 - Form wrapping for isolated JS authentication gates
**Learning:** JS-only authentication gates often omit semantic `<form>` wrappers, preventing users from submitting with the 'Enter' key and removing context for screen readers.
**Action:** Always wrap JS login inputs and submit buttons in a semantic `<form>` tag, attach an `onsubmit` handler calling the auth function with `event.preventDefault()`, and use a `type="submit"` button.
