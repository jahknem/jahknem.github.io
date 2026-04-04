# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Semantic Forms for Access Gates
**Learning:** Simple access gates often use a standalone `<input>` and `<button>` tied to a JavaScript `onclick` handler. This breaks the expectation of pressing "Enter" to submit and ignores screen reader dynamics for the lack of `<label>` and error states.
**Action:** Always wrap inputs in a `<form onsubmit="event.preventDefault(); logic()">` for native keyboard support, add `aria-label` to label-less inputs, and assign `role="alert"` to dynamic error messages for screen readers.
