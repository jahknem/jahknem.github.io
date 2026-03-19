# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Form Semantics for Custom Access Gates
**Learning:** Custom access control structures built with standard `div` elements miss out on native browser form functionalities. By using a `<form>` tag, we gain native keyboard accessibility (specifically "Enter" key submission) out of the box without manual event listeners. Additionally, error messages mapped with `role="alert"` drastically improve the experience for screen reader users by automatically announcing dynamic text changes when login fails.
**Action:** Whenever building or encountering custom authentication flows or "access gates" that require input, wrap them in semantic `<form>` tags, use `type="submit"` buttons, set proper `onsubmit` handlers (using `event.preventDefault()` for JS-driven logic), and employ ARIA live regions like `role="alert"` for inline validation feedback.
