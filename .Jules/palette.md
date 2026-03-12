# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2024-05-23 - Missing RDM53TerminalScripts.js during Playwright testing
**Learning:** A critical javascript file referenced in the `WebsocketTerminalRDM.html` file is missing. This will block normal playwright testing of that file by throwing an error and hanging the page execution.
**Action:** When building playwright tests, route calls to `RDM53TerminalScripts.js` must be bypassed: `page.route("**/RDM53TerminalScripts.js", lambda route: route.fulfill(status=200, body=""))`
