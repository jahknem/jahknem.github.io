# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2025-02-12 - Form Accessibility & Usability
**Learning:** Custom layouts often miss basic HTML structure like `<html lang="en">` and form semantics. Wrapping inputs in a `<form>` enables native Enter key submission, a huge usability win.
**Action:** Always check standalone layouts for missing `lang` attributes and form wrappers around inputs.
