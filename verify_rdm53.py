from playwright.sync_api import sync_playwright

def verify_rdm53_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the RDM53 terminal page (using the correct permalink)
        page.goto("http://localhost:4000/rdm53/")

        # Verify the form element exists
        form = page.locator("form#LoginContainer")
        assert form.count() == 1, "Login container form not found"

        # Verify the input has the correct aria-label
        input_field = page.get_by_role("textbox", name="Access Code")
        assert input_field.count() == 1, "Input with aria-label 'Access Code' not found"

        # Verify the button is type submit
        button = page.locator("button[type='submit']")
        assert button.count() == 1, "Submit button not found"

        # Verify the error message has role="alert"
        error_msg = page.locator("#loginError[role='alert']")
        assert error_msg.count() == 1, "Error message with role='alert' not found"

        # Take a screenshot
        page.screenshot(path="verification_rdm53.png")
        print("Verification successful! Screenshot saved as verification_rdm53.png")

        browser.close()

if __name__ == "__main__":
    verify_rdm53_login()
