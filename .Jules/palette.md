# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2026-05-03 - Form Input & Theme Accessibility
**Learning:** Legacy form layouts often use adjacent text to imply labels visually, but lack programmatic association (`aria-label` or `<label>`) which hinders screen reader usability. Additionally, default theme components (like `minimal-mistakes` toggles) sometimes rely solely on `visually-hidden` text spans instead of top-level `aria-label` or `title` attributes on buttons.
**Action:** Always scan for `<input>` and `<textarea>` elements without associated `<label>` tags and add descriptive `aria-label`s. Ensure icon-only buttons use native `title` or `aria-label` attributes utilizing existing localized strings.
