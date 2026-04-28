# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Login Form Accessibility
**Learning:** Wrapping login inputs in a semantic `<form>` element enables native keyboard "Enter" submissions without needing custom JavaScript event listeners on inputs. Furthermore, adding `role="alert"` to dynamic error messages improves screen reader experiences by announcing errors as they appear.
**Action:** Always wrap interrelated inputs and submission buttons in a `<form>` element, and use ARIA attributes like `role="alert"` for dynamically displayed error elements and `aria-label` for inputs without explicit `<label>` elements.
