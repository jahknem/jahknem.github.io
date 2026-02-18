# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Standalone Layout Accessibility
**Learning:** Standalone Jekyll layouts (like `WebsocketTerminalRDM.html`) often bypass the main theme's CSS and utilities. This leads to missing accessibility primitives like `.sr-only`.
**Action:** When working on custom layouts, verify if they include necessary utility classes or if they need to be manually added to the specific stylesheet.
