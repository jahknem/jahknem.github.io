# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Semantic Form Submissions
**Learning:** Wrapping standalone access code inputs in semantic `<form>` tags and changing the button to `type="submit"` allows users to naturally press "Enter" to submit, improving muscle-memory UX. Additionally, `role="alert"` on dynamically shown error messages ensures screen reader users are immediately informed of failures.
**Action:** Always wrap input/button combinations intended for submission in a `<form>`, handle the event with `onsubmit="event.preventDefault(); ...`, and explicitly define `type="submit"` on the button. Ensure dynamic error messages use `role="alert"`.
