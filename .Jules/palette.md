# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-06-11 - Accessible Login Forms
**Learning:** Standalone inputs without `<form>` wrappers break native keyboard submission (Enter key), hurting both accessibility and standard UX. Dynamically appearing error messages are also ignored by screen readers without `role="alert"`.
**Action:** Always wrap login/access inputs in semantic `<form>` tags using `onsubmit="event.preventDefault(); ..."` and add `role="alert"` to dynamically toggled error messages for proper screen reader announcements.
