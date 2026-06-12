# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.
## 2024-05-23 - Form Submission for Auth
**Learning:** Wrapping a custom JavaScript-based authentication flow in a standard `<form>` element allows users to submit by pressing "Enter", aligning with natural user expectations.
**Action:** When implementing custom client-side auth gates, always use semantic `<form>` tags with an `onsubmit` handler (and `event.preventDefault()`) instead of standalone inputs and button `onClick` handlers.
