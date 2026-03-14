# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Login Form Accessibility
**Learning:** Standalone inputs with `onclick` buttons prevent native keyboard submission (Enter key) and lack proper semantics for screen readers, especially without visible labels or dynamic error states.
**Action:** Always wrap login/access inputs in a semantic `<form>` element, use `onsubmit` with `event.preventDefault()`, and include a `<button type="submit">`. Ensure inputs have `aria-label` if no `<label>` is present, and use `role="alert"` for dynamic error messages.
