from playwright.sync_api import sync_playwright

def verify_rdm53_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:4000/WebsocketTerminalRDM.html")

        # Check if the form exists
        form = page.locator("form#LoginContainer")

        if form.count() == 0:
            print("Form not found. Dumping HTML content:")
            print(page.content())
        else:
            print("Form found!")

        browser.close()

if __name__ == "__main__":
    verify_rdm53_login()
