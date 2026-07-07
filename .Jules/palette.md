# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2025-02-17 - Client-side Login Form UX
**Learning:** Custom JavaScript-based login hurdles (like in `_layouts/WebsocketTerminalRDM.html`) often implement inputs and buttons without an enclosing `<form>` element. This prevents the browser from handling default form behaviors, such as submitting when pressing the "Enter" key, and reduces screen reader context.
**Action:** Always wrap client-side login inputs in a semantic `<form>` element, use `onsubmit="event.preventDefault(); logic()"` for handling, and ensure inputs have `aria-label`s if visual labels are missing. Use `role="alert"` for dynamic error messages.
