# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2025-01-28 - Wrapping Login Elements in a semantic Form for Accessibility
**Learning:** Adding a basic wrapper like `onsubmit="event.preventDefault()"` with a semantic `<form>` helps to catch native submit events (e.g., hitting the Enter key) which significantly improves UX for keyboard users over relying solely on a generic "click" event handler on a `<button type="button">`. Additionally, inputs without visual labels need `aria-label` attributes to be properly announced by screen readers, and error messages that appear dynamically should have a `role="alert"` so they're reliably announced when their state changes.
**Action:** Always check if login sections and interactive inputs are properly wrapped in semantic forms, and check that dynamic error messages use `role="alert"`.
