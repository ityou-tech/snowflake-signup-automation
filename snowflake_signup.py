import asyncio
from playwright.async_api import Playwright, async_playwright


async def run(playwright: Playwright) -> None:
    # 🚀 Phase 1: Headful mode to solve CAPTCHA manually
    print("🌐 Launching browser in VISIBLE mode for CAPTCHA...")
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()

    await page.goto("https://signup.snowflake.com/#")
    await page.get_by_role("button", name="Reject All").click()
    await page.get_by_test_id("signupReason-input").click()
    await page.get_by_role("option", name="Personal learning and").locator(
        "div"
    ).first.click()
    await page.get_by_role("checkbox", name="opt-out-agreement").check()
    await page.get_by_test_id("firstName-input").fill("Enri")
    await page.get_by_test_id("lastName-input").fill("Peters")
    await page.get_by_test_id("email-input").fill("enri@ityou.tech")
    await page.get_by_role("button", name="Continue").click()
    await page.get_by_test_id("companyName-input").fill("ITYOU.tech")
    await page.get_by_test_id("jobTitle-input").fill("IT Engineer")
    await page.get_by_test_id("edition-input").click()
    await page.get_by_text("Business CriticalEnterprise").click()
    await page.get_by_role("button", name="Amazon Web Services").click()
    await page.get_by_role("checkbox", name="terms-agreement").check()
    await page.get_by_role("button", name="Get started").click()

    print("⚠️ Waiting for you to solve the CAPTCHA manually...")

    # ✅ Automatically wait until the CAPTCHA is solved (Skip link becomes visible)
    await page.wait_for_selector('a:has-text("Skip")', timeout=0)

    print("✅ CAPTCHA solved. Continuing automation...")

    await page.get_by_role("link", name="Skip").click()
    await page.get_by_role("link", name="Skip").click()

    # 📌 Check if 'Check your inbox!' message appears, dynamically without fixed timeout
    print("⏳ Waiting for 'Check your inbox!' message...")
    while True:
        inbox_message = await page.query_selector('text="Check your inbox!"')
        if inbox_message:
            print("📧 'Check your inbox!' message detected. Closing browser.")
            break
        await asyncio.sleep(1)  # Check every second

    await context.close()
    await browser.close()

    # 🚀 Phase 2: Continue in HEADLESS mode if needed
    print("🤖 Launching browser in HEADLESS mode to finish automation (if required)...")
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context()
    page = await context.new_page()

    # You can continue automation here if needed, or just close:
    await context.close()
    await browser.close()

    print("✅ Automation completed successfully.")


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
