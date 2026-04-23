# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Interactive Element Wrappers
**Learning:** Legacy login components often use plain `<div>` containers instead of `<form>` elements, breaking native 'Enter' key submission and limiting accessibility.
**Action:** When working on authentication or data-entry components, actively convert generic wrapper `<div>`s to `<form>` tags with explicit `onsubmit` handlers (using `event.preventDefault()`) and proper `<button type="submit">` configuration. This is a zero-risk pattern that immediately unlocks keyboard navigation.
