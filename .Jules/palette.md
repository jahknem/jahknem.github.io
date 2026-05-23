# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Interactive Login Components
**Learning:** Even simple JavaScript-gated access components should be wrapped in semantic `<form>` tags. Without a form and `type="submit"` button, users cannot submit the form using the Enter key. Adding `role="alert"` is also crucial for dynamically appearing error messages to ensure screen reader users are notified immediately.
**Action:** Always wrap interactive inputs and buttons in semantic `<form>` elements and ensure dynamic error messages use `role="alert"`, even if the form isn't performing a traditional POST request and is purely client-side logic.
