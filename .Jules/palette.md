# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Semantic Forms for Client-Side Gates
**Learning:** Client-side authentication hurdles often fail to implement a semantic `<form>`, which disables the expected UX of pressing "Enter" to submit. Additionally, error messages lack the `role="alert"` attribute, which means screen readers won't automatically announce authentication failures.
**Action:** When implementing client-side gates or login prompts, always wrap the inputs in a semantic `<form>` with an `onsubmit` handler (and `event.preventDefault()`), use `type="submit"` for the button, and ensure dynamic error messages use `role="alert"`.
