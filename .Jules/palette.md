# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2026-05-05 - Native Semantic Forms for Client-Side Access Gates
**Learning:** Client-side UI login/access hurdles using simple `<div>` tags and `onclick` buttons break expected standard UX flows (like pressing "Enter" to submit) and lack proper a11y support.
**Action:** Always wrap login/access inputs in semantic `<form>` elements with `onsubmit="event.preventDefault(); logic();"` and `<button type="submit">`. Include `aria-label` for inputs without visible `<label>` tags and use `role="alert"` for dynamically shown error messages to ensure screen readers announce them properly.
