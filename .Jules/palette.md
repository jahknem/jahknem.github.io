# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Login Form Accessibility
**Learning:** For client-side access gates relying on JS, simply using input fields and an `onclick` button leads to poor accessibility and missing functionality (e.g. hitting Enter won't submit the code). Wrapping the inputs in a semantic `<form>` and using `onsubmit` allows the browser to handle `<Enter>` naturally and improves screen reader experience.
**Action:** Always wrap login/access inputs in a semantic `<form>` element, use `onsubmit` with `event.preventDefault()`, use `<button type="submit">`, and add `role="alert"` for error messages.
