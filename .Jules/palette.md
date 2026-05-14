# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Client-side Auth Forms
**Learning:** Client-side authentication barriers constructed with simple inputs and buttons (often done to prevent immediate UI rendering) break default form behavior. When users hit "Enter" to submit, nothing happens because they aren't wrapped in `<form>` elements.
**Action:** When implementing any authentication or input gate (even client-side only ones), always wrap the inputs in a `<form>`, use `type="submit"` on the primary button, and handle the logic via the `onsubmit` event (with `event.preventDefault()`). Always add `aria-label` to inputs without `<label>` elements and `role="alert"` for dynamically shown error messages.
