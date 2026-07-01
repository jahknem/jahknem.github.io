# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-07-01 - Semantic Form Gates
**Learning:** Custom client-side authentication or access gates often miss semantic form structures, meaning they lack keyboard "Enter" submission by default and require manual `role="alert"` configuration for accessibility.
**Action:** Always wrap password/access inputs and submit buttons in a `<form>` element, handle the logic via `onsubmit` preventing default action, and apply `role="alert"` for any dynamically revealed error messages.
