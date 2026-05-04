# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Form Accessibility for Authentication Gates
**Learning:** Simple authentication gates that only use an `<input>` and a `<button type="button">` prevent users from submitting the form using the "Enter" key, which is a major UX frustration. Additionally, error messages without `role="alert"` are missed by screen readers.
**Action:** Always wrap authentication/login inputs in a semantic `<form>` element with an `onsubmit` handler (using `event.preventDefault()`) and a `<button type="submit">`. Ensure form inputs have `aria-label` if a visible `<label>` is missing, and use `role="alert"` for dynamic error messages.
