# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.
## 2024-05-23 - Login Form Accessibility
**Learning:** Wrapping a login form in a semantic `<form>` element natively supports 'Enter' to submit via keyboard, enhancing usability. Furthermore, adding `aria-label` to inputs missing explicit labels, and using `role="alert"` for dynamically appearing error messages makes authentication flows accessible for screen readers.
**Action:** Always prefer native semantic elements for interactive forms and complement them with appropriate ARIA roles where implicit visual cues (like an error text) exist.
