
import time
import pytest
from playwright.sync_api import Page, expect


def test_demoblaze(page: Page):
    page.goto("https://www.demoblaze.com/index.html")

    page.locator('a[id=signin2]').click()
    page.locator('input[id=sign-username]').fill('ekramul.ben@gmail.com')
    page.locator('input[id=sign-password]').fill('1qazZAQ!')
    page.locator('button[type=button]').filter(has_text="Sign up").click()
    time.sleep(10)

    # # Expect a title "to contain" a substring.
    # expect(page).to_have_title(re.compile("Playwright"))
    #
    # # create a locator
    # get_started = page.get_by_role("link", name="Get started")
    #
    # # Expect an attribute "to be strictly equal" to the value.
    # expect(get_started).to_have_attribute("href", "/docs/intro")
    #
    # # Click the get started link.
    # get_started.click()
    #
    # # Expects the URL to contain intro.
    # expect(page).to_have_url(re.compile(".*intro"))
