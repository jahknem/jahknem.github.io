# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Form Wrapping for Access Checks
**Learning:** Single input fields used for access checks or logins (like a password gate) often lack `<form>` wrappers in prototype or admin code. This breaks basic keyboard usability, meaning users cannot hit "Enter" to submit the code, which is a significant frustration point.
**Action:** Always wrap loose inputs used for submission in a `<form>` tag, use a `<button type="submit">`, and handle the submission via the `onsubmit` event (with `event.preventDefault()`) instead of a simple button `onclick` to ensure full keyboard support. Also apply `aria-label` to the input if a `<label>` is missing, and `role="alert"` for error messages.
