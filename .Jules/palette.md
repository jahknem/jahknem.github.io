# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2026-06-06 - Semantic Login Form for Terminal Access
**Learning:** Raw input and button combinations for login flows lack native "submit on Enter" functionality and semantic meaning for screen readers. This breaks expectations for standard keyboard navigation (like hitting Enter to log in).
**Action:** Always wrap interactive login inputs in a semantic `<form>`, even if it only triggers client-side JavaScript. Handle logic with `onsubmit="event.preventDefault(); logic();"` and `<button type="submit">`. Also, ensure inputs have an `aria-label` when visible `<label>`s are missing, and use `role="alert"` for dynamic error messages.
