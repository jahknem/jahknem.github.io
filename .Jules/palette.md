# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Semantic Forms for Access Gates
**Learning:** Custom access gates built with `<div>` and `<button type="button">` block native keyboard submission (Enter key) and lack proper semantics. Using a `<form>` element with `onsubmit` and a `<button type="submit">` fixes this and significantly improves keyboard accessibility for vanilla HTML components.
**Action:** Always wrap input and submit combinations in a `<form>` tag to enable default browser keyboard handling, even for purely client-side logic. Add `role="alert"` for error messages.
