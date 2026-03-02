# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Semantic Forms for Access Gates
**Learning:** Using a `<div>` with an `onclick` button for access gates (like in `WebsocketTerminalRDM`) breaks native keyboard submission (pressing Enter) and is less accessible.
**Action:** Always wrap login/access inputs in a semantic `<form>` element, use `onsubmit` to handle logic (with `event.preventDefault()`), and ensure inputs have `aria-label` and error messages use `role="alert"`.
