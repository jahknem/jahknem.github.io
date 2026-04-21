# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Login Form Accessibility and Native Submission
**Learning:** Wrapping custom JavaScript-driven login interfaces in semantic `<form>` tags with `onsubmit="event.preventDefault()"` immediately unlocks native "Enter" key submission, significantly improving keyboard user experience. Additionally, using `role="alert"` on dynamic error message containers ensures screen readers announce authentication failures proactively.
**Action:** Always check custom authentication modals or inputs to ensure they are wrapped in a form, have an `aria-label` when labels are omitted visually, and use `role="alert"` for inline validation feedback.
