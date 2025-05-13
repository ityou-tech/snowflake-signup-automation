"""
Snowflake Signup Automation Script

This script automates the process of signing up for a Snowflake account using Playwright.

EDUCATIONAL PURPOSE ONLY: This script is provided for educational purposes only.
Misuse is against Snowflake's Terms of Service.
"""

import asyncio
import os
import json
from playwright.async_api import Playwright, async_playwright
from config import DEFAULT_CONFIG, print_disclaimer


def load_config():
    """Load configuration from file or environment variables"""
    config_file = os.environ.get("SNOWFLAKE_CONFIG_FILE", "snowflake_config.json")

    # First check if config file exists
    if os.path.exists(config_file):
        try:
            with open(config_file, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading config file: {e}")

    # If no file, get from environment or prompt user
    config = DEFAULT_CONFIG.copy()

    for key in config.keys():
        env_var = f"SNOWFLAKE_{key.upper()}"
        if os.environ.get(env_var):
            config[key] = os.environ.get(env_var)

    # If config still has empty values, prompt user
    missing_values = [
        k for k, v in config.items() if not v and k not in ["cloud_provider", "edition"]
    ]
    if missing_values:
        print("\nPlease provide the following information:")
        for key in missing_values:
            config[key] = input(f"{key.replace('_', ' ').title()}: ")

    return config


async def run(playwright: Playwright, config=None) -> None:
    """Run the Snowflake signup automation"""
    if config is None:
        config = load_config()

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
    await page.get_by_test_id("firstName-input").fill(config["first_name"])
    await page.get_by_test_id("lastName-input").fill(config["last_name"])
    await page.get_by_test_id("email-input").fill(config["email"])
    await page.get_by_role("button", name="Continue").click()
    await page.get_by_test_id("companyName-input").fill(config["company"])
    await page.get_by_test_id("jobTitle-input").fill(config["job_title"])
    await page.get_by_test_id("edition-input").click()

    # Handle edition selection based on the specific UI text structure
    if config["edition"] == "Business Critical":
        await page.get_by_text("Business CriticalEnterprise").click()
    elif config["edition"] == "Enterprise":
        await page.get_by_text("Enterprise").click()
    elif config["edition"] == "Standard":
        await page.get_by_text("Standard").click()
    else:
        # Default to Business Critical if unrecognized
        print(
            f"Warning: Unrecognized edition '{config['edition']}', defaulting to Business Critical"
        )
        await page.get_by_text("Business CriticalEnterprise").click()
    await page.get_by_role("button", name=config["cloud_provider"]).click()
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
    """Main entry point for the script"""
    try:
        # Show disclaimer and get confirmation
        if not print_disclaimer():
            return

        config = load_config()
        async with async_playwright() as playwright:
            await run(playwright, config)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user. Exiting.")
        return


if __name__ == "__main__":
    asyncio.run(main())
