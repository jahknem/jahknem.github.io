# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2026-05-28 - Login Accessibility
**Learning:** Wrapping login inputs in semantic forms supports 'Enter' key submission out of the box and provides better screen reader announcements when combined with `aria-label` and `role="alert"` for error messages.
**Action:** Always wrap login inputs in semantic `<form>` tags and add appropriate ARIA attributes.
