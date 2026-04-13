# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Native Form Submission for Login Components
**Learning:** Standalone, client-side 'login' gates (like those guarding hidden terminals) often use a `<div>` with an `onclick` button, forcing users to click rather than hit 'Enter'. Converting the wrapper to a `<form>` and using `onsubmit` with `event.preventDefault()` enables standard keyboard accessibility for free.
**Action:** Always wrap input and submit button pairs in semantic `<form>` tags, even if the submission logic is purely client-side JavaScript.
