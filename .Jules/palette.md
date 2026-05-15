# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Form Accessibility for Access Gates
**Learning:** Client-side access gates (like the RDM53 terminal login) that use custom JavaScript for validation must still be wrapped in standard semantic `<form>` elements with a `type="submit"` button and an `onsubmit` handler (`event.preventDefault()`). Failing to do so breaks keyboard accessibility (e.g., submitting via the "Enter" key) and screen reader support.
**Action:** Always wrap input and validation button groups in semantic `<form>` elements and manage logic via the `onsubmit` event rather than inline button `onClick` handlers. Additionally, ensure error messages utilize `role="alert"` for proper screen reader announcement.
