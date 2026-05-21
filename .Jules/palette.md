# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Login Form Accessibility
**Learning:** The RDM53 login interface relied on a raw input and a standard button with an `onclick` handler, breaking the expected behavior of pressing "Enter" to submit. Additionally, error messages were not dynamically announced to screen readers.
**Action:** Always wrap inputs in a semantic `<form>` element, map the enter action via `onsubmit` paired with `event.preventDefault()`, assign `type="submit"` to buttons, ensure inputs without visible labels have an `aria-label`, and use `role="alert"` for dynamically displayed error messages.
