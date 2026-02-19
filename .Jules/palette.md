# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2026-02-19 - Login Form Accessibility
**Learning:** Legacy terminal layouts often rely on simple div/input structures without form semantics, making them inaccessible to screen readers and keyboard users (no "Enter" to submit).
**Action:** When encountering standalone auth widgets, always wrap them in a `<form>` element with an `onsubmit` handler and ensure all inputs have associated labels (using `aria-label` or `.sr-only` if visual design constraints apply).
