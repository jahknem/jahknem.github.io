from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # 1. Verify Homepage (DE)
        print("Navigating to Homepage (DE)...")
        page.goto("http://localhost:4000/")
        page.wait_for_selector(".hero")
        page.wait_for_selector(".pillars-grid")
        page.screenshot(path="verification_home_de.png")
        print("Homepage (DE) screenshot saved.")

        # Check for Hero content
        content = page.content()
        if "Jan Kühnemund" in content and "Site Reliability Engineer" in content:
            print("Homepage (DE) content verified.")
        else:
            print("Homepage (DE) content missing!")

        # Check for Navigation
        if "EN" in content:
            print("Navigation verified.")
        else:
            print("Navigation missing EN link!")

        # 2. Verify Portfolio
        print("Navigating to Portfolio...")
        page.goto("http://localhost:4000/portfolio/")
        page.wait_for_selector(".project-card")
        page.screenshot(path="verification_portfolio.png")
        print("Portfolio screenshot saved.")

        # 3. Verify CV
        print("Navigating to CV...")
        page.goto("http://localhost:4000/cv/")
        page.wait_for_selector("a[href='/assets/cv/jan-kuehnemund-cv.pdf']")
        page.screenshot(path="verification_cv.png")
        print("CV screenshot saved.")

        # 4. Verify Homepage (EN)
        print("Navigating to Homepage (EN)...")
        page.goto("http://localhost:4000/en/")
        page.wait_for_selector(".hero")
        content_en = page.content()
        if "Specializing in Reliability Engineering" in content_en:
            print("Homepage (EN) content verified.")
        else:
            print("Homepage (EN) content missing!")
        page.screenshot(path="verification_home_en.png")
        print("Homepage (EN) screenshot saved.")

        browser.close()

if __name__ == "__main__":
    run()
