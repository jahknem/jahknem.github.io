# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Semantic Forms for Access Gates
**Learning:** Custom authentication gates (client-side) often use simple `input` and `button` elements, breaking native behavior like "Enter to submit" and confusing screen readers.
**Action:** Always wrap input fields in a `<form>` element with a submit button, even for client-side logic (using `onsubmit="event.preventDefault()"`).
