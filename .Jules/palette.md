# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Form Keyboard Accessibility
**Learning:** `div` and `button` combinations for inputs are bad for accessibility, since users expect to be able to hit "Enter" on an input field. Replacing it with a semantic `form` structure automatically enables native form submission behavior via the "Enter" key and supports native screen reader features.
**Action:** For accessibility and UX, always wrap login/access inputs in a semantic `<form>` element, use `onsubmit` to handle logic (with `event.preventDefault()`), use `<button type="submit">`, and add `aria-label` to inputs lacking visible `<label>` tags. Also add `role="alert"` for error messages.
