# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.
## 2024-05-15 - [Add Form Submission for Auth Check]
**Learning:** Adding a basic Javascript `onclick` handler to a button is not sufficient for keyboard accessibility in form submissions. Wrapping input + button inside a semantic `<form>` with an `onsubmit` handler (and `event.preventDefault()`) allows users to submit the form seamlessly using the "Enter" key. Added `aria-label` to the input field and `role="alert"` to the dynamic error message to assist screen readers.
**Action:** Always wrap interactive login/access components inside a `<form>` and handle submission via `onsubmit` rather than relying solely on button clicks.
