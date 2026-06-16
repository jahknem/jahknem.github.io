# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Login Hurdles & Semantic HTML
**Learning:** Client-side "hurdles" or password gates are often built quickly with loose inputs and buttons (`type="button"`). This breaks the expected UX of submitting via the "Enter" key and removes semantic context for screen readers.
**Action:** Always wrap login or access-code inputs in a semantic `<form>` element, handle the submission with `onsubmit="function(event)"`, use `event.preventDefault()`, and ensure inputs have `aria-label`s and errors have `role="alert"`.
