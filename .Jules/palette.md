# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Semantic Boundaries in JS-Driven Access Gates
**Learning:** Access gates or authentication prompts built as generic `<div>` containers with custom JavaScript event handlers (like `onclick="checkAccess()"`) break native keyboard behaviors. Users expecting to submit by pressing "Enter" within the password field are unable to do so, degrading accessibility. Additionally, missing `<label>` tags and `role="alert"` for error messages make the experience poor for screen readers.
**Action:** Always wrap interactive access logic in semantic `<form>` tags. Handle the logic using `onsubmit="event.preventDefault(); functionCall()"` instead of binding to button clicks. Provide `aria-label`s for inputs if a visible `<label>` is not present, and ensure dynamic error messages use `role="alert"`.