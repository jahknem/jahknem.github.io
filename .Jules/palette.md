# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2026-06-08 - Form wrapping for keyboard accessibility
**Learning:** Standalone inputs and buttons often miss the ability to use the 'Enter' key for submission, a common keyboard navigation expectation. Wrapping these in a `<form>` with an `onsubmit` handler instantly fixes this.
**Action:** Always wrap logical input-button pairs in a `<form>` element, even if not submitting data to a backend, to ensure native keyboard accessibility.
