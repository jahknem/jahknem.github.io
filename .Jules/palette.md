# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Semantic Form Submissions
**Learning:** Simple input-and-button pairs often lack `form` wrappers, preventing native "submit on Enter" functionality and hurting accessibility. Adding `aria-label` to visually unlabelled inputs and `role="alert"` to dynamic error messages significantly improves screen reader UX.
**Action:** Always wrap interactive input/button pairs in a `<form>` using `onsubmit` with `event.preventDefault()`. Use `aria-label` when visual labels are missing, and mark error messages with `role="alert"`.
