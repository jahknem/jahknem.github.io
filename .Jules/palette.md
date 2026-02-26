# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Scroll-to-Top Accessibility
**Learning:** Adding a "Back to Top" button is great for long pages, but it must be keyboard accessible and not interfere with content. Using `aria-hidden="true"` on the icon and `aria-label` on the button/anchor is crucial.
**Action:** Always ensure floating action buttons have sufficient contrast, focus states, and are reachable via keyboard tabbing.
