# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Accessible Authentication Forms
**Learning:** Pure JS-driven authentication hurdles (like `checkAccess()` in standalone HTML layouts) often forget basic HTML semantics. Without `<form>`, users cannot submit by pressing "Enter", hindering keyboard accessibility and standard browser behavior. Additionally, dynamically displayed errors lack `role="alert"`, remaining invisible to screen readers.
**Action:** Always wrap JS-driven login inputs in a `<form onsubmit="...">` with a `<button type="submit">`, add `aria-label` to inputs without `<label>`, and use `role="alert"` on dynamic error containers.
