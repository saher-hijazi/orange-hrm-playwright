import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="PIM").click()
    page.get_by_role("button", name=" Add").click()
    page.get_by_role("textbox", name="First Name").click()
    page.get_by_role("textbox", name="First Name").fill("Saher")
    page.get_by_role("textbox", name="First Name").press("Tab")
    page.get_by_role("textbox", name="Middle Name").fill("0594017407")
    page.get_by_role("textbox", name="Middle Name").press("Tab")
    page.get_by_role("textbox", name="Last Name").fill("Hijazi")
    page.get_by_role("textbox", name="Last Name").click()
    page.get_by_role("button", name="Save").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)