# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2026-02-27 - Semantic Forms for Standalone Apps
**Learning:** Using `<div>` containers for login interfaces breaks standard keyboard behavior (Enter to submit) and accessibility.
**Action:** Always wrap input fields and action buttons in a `<form>` element, even for client-side only apps. Use `onsubmit='event.preventDefault()'` to handle logic without reloading.
