# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-10-24 - Semantic Forms for Access Gates
**Learning:** Using a generic `<div>` with `type="button"` for login gates prevents standard keyboard interaction (submitting with the Enter key). Screen readers also lack context for form fields without `aria-label` or `<label>` tags, and error messages aren't announced dynamically.
**Action:** Always wrap access/login inputs in a semantic `<form>` element. Use `onsubmit="event.preventDefault(); logic()"` to support native enter-to-submit behavior, change the button to `type="submit"`, add `aria-label` to inputs, and use `role="alert"` for error messages.
