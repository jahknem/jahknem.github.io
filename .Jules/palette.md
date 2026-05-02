# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-10-24 - Form Semantics for Authentication
**Learning:** Hardcoded authentication modals without `<form>` elements prevent native "Enter" key submission, which is frustrating for users and worse for accessibility. Error messages also need a `role="alert"` so screen readers immediately read out the failure.
**Action:** Always wrap input and submit buttons in a semantic `<form onsubmit="event.preventDefault(); logic()">` structure. Add `role="alert"` to dynamic error message containers.
