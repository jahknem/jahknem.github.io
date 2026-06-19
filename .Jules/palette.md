# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2025-02-12 - Client-Side Access Gates
**Learning:** Simple client-side authorization gates (like `LoginContainer`) often lack semantic form structures because they don't submit to a backend. This breaks keyboard accessibility (like pressing Enter to submit) and screen reader expectations for form inputs and error messages.
**Action:** Always wrap client-side login inputs in a `<form>`, use `onsubmit="event.preventDefault(); logic();"`, add `<button type="submit">`, and ensure dynamic error messages use `role="alert"`.
