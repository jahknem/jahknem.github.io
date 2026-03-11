# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2025-01-20 - RDM53 Login Form Accessibility
**Learning:** The custom RDM53 Webinterface (`_layouts/WebsocketTerminalRDM.html`) implemented its login flow using a `<div>` container instead of a `<form>`. This breaks the expected UX of pressing "Enter" to submit and lacks semantic meaning for screen readers. Furthermore, the inputs lacked `aria-label`s.
**Action:** Always wrap login/access inputs in a semantic `<form>` element, use `onsubmit` to handle logic (with `event.preventDefault()`), and use `<button type="submit">`. Add `aria-label` to inputs lacking visible `<label>` tags, and use `role="alert"` for dynamic error messages.