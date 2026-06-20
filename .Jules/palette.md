# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-06-20 - RDM53 Login Form Enhancements
**Learning:** Legacy UI components built with purely JS-driven interactions (like the `checkAccess` button in RDM53) often lack basic HTML form semantics, making them un-submittable via keyboard (Enter key) and opaque to screen readers.
**Action:** When working on legacy custom UIs, always evaluate if an interaction feels like a form. If it does, wrap it in a `<form>` tag, use `onsubmit` with `event.preventDefault()`, set `type="submit"` on the button, and ensure inputs have implicit or explicit labels (e.g., `aria-label`). For dynamic error messages, leverage `role="alert"`.
