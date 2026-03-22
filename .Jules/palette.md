# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Semantic Form Submissions
**Learning:** Authentication hurdles in standalone HTML files (like the RDM53 terminal) often use bare `<input>` and `<button>` elements, breaking native "Enter" key submission and lacking ARIA context.
**Action:** Always wrap login/access inputs in a semantic `<form>` element. Use `onsubmit="event.preventDefault(); handler();"` to intercept submission, and include `aria-label` for inputs lacking visible `<label>` tags. Ensure dynamic error messages use `role="alert"`.
