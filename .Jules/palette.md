# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Form Accessibility and Roles
**Learning:** Using semantic `<form>` wrappers around inputs not only improves structure but also enables native keyboard submissions (pressing Enter). Additionally, error messages that dynamically appear need `role="alert"` so screen readers proactively read them out. The `onsubmit` handler is the best place to attach validation logic for forms, paired with `event.preventDefault()`.
**Action:** When implementing login screens or access barriers, always ensure inputs are inside a semantic `<form>` tag and provide visual error messages with `role="alert"`.
