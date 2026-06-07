# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-11-20 - Semantic Forms for Auth Gates
**Learning:** Auth gates implemented as `div` wrappers without proper form semantics lack support for "Enter" key submission and fail to provide necessary screen reader context.
**Action:** When creating login or access gates, always wrap the inputs in a semantic `<form>` element, use `<button type="submit">`, add `aria-label` to inputs without visible labels, and use `role="alert"` for error messages to ensure keyboard and screen reader accessibility.
