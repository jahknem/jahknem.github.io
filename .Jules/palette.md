# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2026-06-14 - Semantic Forms for Auth Inputs
**Learning:** Standalone inputs with standard buttons block 'Enter' key submission and lack semantic meaning for screen readers.
**Action:** Always wrap authentication/login inputs in a semantic `<form>`, use `<button type="submit">`, add `aria-label` if there is no visible `<label>`, and use `role="alert"` for dynamic error messages.
