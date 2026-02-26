# Verify Frontend Changes

from playwright.sync_api import sync_playwright

def verify_frontend():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Test navigation to portfolio page and scroll to top
        try:
            page.goto("http://localhost:4000/portfolio/")

            # Check for scroll-to-top button visibility after scrolling down
            page.evaluate("window.scrollTo(0, 1000)")
            page.wait_for_timeout(1000) # Wait for potential animation

            # Verify scroll-to-top button exists and is visible
            button = page.locator("#back-to-top")
            if button.is_visible():
                print("SUCCESS: Back to top button is visible after scrolling.")
            else:
                print("FAILURE: Back to top button is NOT visible after scrolling.")

            page.screenshot(path="portfolio_page_scrolled.png", full_page=True)

        except Exception as e:
            print(f"Error during verification: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    verify_frontend()
