# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2026-05-01 - Form Element Wrapping for Keyboard Accessibility
**Learning:** In isolated custom HTML layouts (like `_layouts/WebsocketTerminalRDM.html`), inputs are sometimes wrapped in generic `<div>` tags with `onclick` handlers on buttons instead of `<form>` elements. This breaks default keyboard navigation (e.g., submitting via the "Enter" key). Adding `role="alert"` for dynamically shown error messages is also often missed.
**Action:** Always verify that input/button combinations intended for submission are wrapped in semantic `<form>` tags. Use `onsubmit="event.preventDefault(); logic()"` and `<button type="submit">` to ensure smooth keyboard accessibility. Additionally, assign `aria-label` to standalone inputs and `role="alert"` to dynamic error messages for better screen reader support.
