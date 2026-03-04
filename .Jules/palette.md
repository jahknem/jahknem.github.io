# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Semantic Forms for Access Gates
**Learning:** Standalone inputs and buttons lacking a `<form>` container break native keyboard accessibility. Users cannot submit the input by pressing `Enter`.
**Action:** Always wrap login or access inputs in a `<form>` tag, use `onsubmit` to handle the logic with `event.preventDefault()`, and ensure the submit button uses `type="submit"`. Also, provide `aria-label` for inputs lacking visible `<label>` tags and `role="alert"` for dynamically displayed error messages.
