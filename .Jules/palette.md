# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Accessible Forms & Enter-to-Submit
**Learning:** Standalone inputs without a `<form>` wrapper often miss standard submission behaviors, preventing users from pressing "Enter" to submit. Also, dynamically appearing error messages aren't automatically announced by screen readers.
**Action:** When building login or access gates, always wrap them in a semantic `<form>` with an `onsubmit="event.preventDefault(); handler();"` attribute, use `<button type="submit">`, and assign `role="alert"` to dynamic error text to ensure immediate screen reader announcement.
