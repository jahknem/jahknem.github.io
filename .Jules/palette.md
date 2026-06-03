# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-06-03 - Form Submit for Enter Key Support
**Learning:** Raw input fields and buttons with `onclick` prevent users from submitting access codes by pressing "Enter", hindering basic keyboard navigation and expectation.
**Action:** Always wrap single-input access gates in a `<form>` element with `onsubmit="event.preventDefault();"` and change the button to `type="submit"` to provide native form behavior.
