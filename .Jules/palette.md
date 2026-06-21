# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2026-06-21 - Semantic Authentication Form
**Learning:** The initial authentication step for the Websocket Terminal (`checkAccess()`) was implemented without a semantic `<form>` element. This prevents standard behaviors like submitting the form using the "Enter" key and creates friction for users, especially those relying on screen readers.
**Action:** Always wrap interactive form inputs in semantic `<form>` elements and ensure critical accessibility attributes (`aria-label`, `role="alert"`) are present, even for simple, "quick" JavaScript-driven interactions.
