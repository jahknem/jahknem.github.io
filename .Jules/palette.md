# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2026-07-08 - Semantic Forms for Access Gates
**Learning:** Client-side access gates (like the RDM terminal) using basic inputs and `onclick` buttons prevent standard form behaviors like Enter-key submission and lack accessibility roles, leading to a frustrating user experience for keyboard users.
**Action:** Always wrap single-input access or login fields in a semantic `<form>` element with an `onsubmit` handler (using `event.preventDefault()`) and a `type="submit"` button, and apply `role="alert"` for error messages.
