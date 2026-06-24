# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-06-24 - Semantic Forms for Access Gates
**Learning:** Even simple client-side access gates like the RDM53 terminal login should use semantic `<form>` tags. Without it, users cannot submit their access code by simply pressing "Enter", and the lack of an explicit `aria-label` on inputs without visible labels degrades screen reader experience. Error messages also need `role="alert"` to be immediately announced.
**Action:** When implementing custom client-side auth UI, always wrap inputs in a `<form>`, use `onsubmit` with `event.preventDefault()`, add `aria-label` to placeholder-only inputs, and add `role="alert"` to dynamic error containers.
