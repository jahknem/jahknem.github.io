# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2026-06-29 - Semantic Forms for Access Gates
**Learning:** Security or access gate inputs (like the RDM53 terminal login) that rely purely on `onclick` handlers on `<button>` elements prevent users from natively submitting by pressing the `Enter` key.
**Action:** Always wrap these access inputs in a `<form>` tag. Move the click logic to the form's `onsubmit` handler (ensuring to call `event.preventDefault()` if executing JS logic), and change the button to `type="submit"` to restore native accessibility and keyboard interactions.
