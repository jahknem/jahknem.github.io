# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.
## 2024-05-23 - Form Wrapping for Accessibility
**Learning:** In legacy components (like `_layouts/WebsocketTerminalRDM.html`), login interfaces often lack `<form>` wrappers and use simple button `onclick` events, preventing native keyboard submission (hitting "Enter").
**Action:** When auditing authentication forms, wrap them in semantic `<form>` tags, change the submission button to `type="submit"`, and add `onsubmit="event.preventDefault(); logic();"` to dramatically improve keyboard accessibility while maintaining existing logic.
