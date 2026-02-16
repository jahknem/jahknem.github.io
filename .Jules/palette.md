# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2026-02-16 - Native Form Behaviors in Custom UIs
**Learning:** Even in custom interfaces like a "Websocket Terminal", users expect standard form behaviors like pressing Enter to submit. Omitting this breaks user flow.
**Action:** Always add keyboard listeners for primary actions in custom input fields if they aren't part of a standard `<form>`.
