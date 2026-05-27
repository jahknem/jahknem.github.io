# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-27 - Standalone Form Accessibility
**Learning:** Standalone login/access gates without semantic `<form>` wrappers prevent users from hitting 'Enter' to submit, hurting keyboard accessibility. Error messages lacking `role="alert"` are often ignored by screen readers when dynamically displayed.
**Action:** Always wrap login/access inputs in a semantic `<form>` element, use `onsubmit` for logic (with `event.preventDefault()`), use `<button type="submit">`, and use `role="alert"` for dynamic error messages.
