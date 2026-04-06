# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Semantic Form Accessibility
**Learning:** Wrapping custom access gates in semantic forms enables native keyboard submission (Enter to submit). Dynamic error messages without `role="alert"` are missed by screen readers.
**Action:** Always use `<form>` for inputs and `role="alert"` for dynamic error messages to ensure full keyboard and screen reader accessibility.
