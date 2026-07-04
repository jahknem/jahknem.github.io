# Palette's UX Journal

## 2024-05-23 - Active Navigation State
**Learning:** `minimal-mistakes` theme navigation lacks `aria-current="page"` and active state styling by default. This is a missed opportunity for both accessibility and visual feedback.
**Action:** When working with Jekyll themes, always check if active states are handled. If not, implementing a simple logic comparing `page.url` and `link.url` is a quick win.

## 2026-07-04 - Semantic Forms for Auth Gates
**Learning:** Client-side auth gates often lack semantic form structures, breaking screen readers and preventing Enter-key submission.
**Action:** Wrap client-side auth inputs in a semantic <form>, use type='submit', and handle onsubmit with preventDefault().
