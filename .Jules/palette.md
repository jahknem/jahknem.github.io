# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Keyboard Accessible Forms
**Learning:** Standalone password or access code inputs often lack proper `<form>` wrappers, forcing users to click submit buttons instead of naturally hitting 'Enter'.
**Action:** Always wrap standalone inputs and their submit buttons in a semantic `<form>` element, use `onsubmit="event.preventDefault(); [yourLogic]()"`, and ensure the button is `type="submit"`. Also, provide an `aria-label` for inputs lacking visible labels.
