# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2026-04-30 - Custom Access Gate Form Semantics
**Learning:** For single-page or client-side authentication screens (like the RDM53 terminal login), wrapping the elements in a semantic `<form>` with `onsubmit="event.preventDefault(); checkAccess()"` greatly improves accessibility. It natively supports keyboard interaction (like pressing "Enter" inside the input to submit) without needing to add custom event listeners for keyboard events. Including `role="alert"` for the error messages ensures screen readers immediately announce authentication failures.
**Action:** When implementing simple client-side access gates, always use `<form>` elements and avoid relying solely on `<button type="button" onclick="...">`.
