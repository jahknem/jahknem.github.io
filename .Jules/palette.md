# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2025-01-22 - Standalone Login Inputs and Accessibility
**Learning:** Using standalone `<input>` and `<button>` elements for simple client-side login or access gates breaks native keyboard submission (pressing the 'Enter' key). Additionally, missing explicit labels require `aria-label`, and dynamically shown error messages require `role="alert"` to be announced by screen readers.
**Action:** Always wrap logical form groups in a `<form onsubmit="event.preventDefault(); [logic]">` tag, ensure buttons are `type="submit"`, add `aria-label` when visible `<label>` tags are missing, and apply `role="alert"` to dynamic error text.
