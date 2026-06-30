# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-06-30 - [Semantic Forms for Standalone Inputs]
**Learning:** Standalone inputs without a `<form>` tag break standard keyboard interaction (like pressing Enter to submit) and accessibility expectations, which is a common pattern in custom components like the RDM53 login gate.
**Action:** Always wrap interactive inputs and submission buttons in a semantic `<form>` element, use `type="submit"`, and handle the logic with `onsubmit` and `event.preventDefault()`.
