# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-24 - Custom Layout Isolation
**Learning:** Custom layouts (like `WebsocketTerminalRDM.html`) often completely bypass the theme's base layout, leading to missing root attributes like `<html lang>` and standard meta tags.
**Action:** When auditing custom layouts, always verify the presence of the `<html>` tag and its attributes, as they won't inherit from the default theme.
