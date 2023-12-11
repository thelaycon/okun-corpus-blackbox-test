import time
import pytest
from pages.homepage import Homepage
from Screenshot import Screenshot


screen_obj = Screenshot.Screenshot()


def test_homepage(browser):

    # Load page
    homepage = Homepage(browser)
    homepage.load()
    assert browser.title == "Okun Corpus | OLRC"

    # Check for logo in header
    assert homepage.header_logo().is_displayed()
    browser.save_screenshot("tests/screenshots/home.png")

    # assert homepage.get_hero_image().is_displayed()
    browser.save_screenshot("screenshots/hero.png")

    # Check if nav items are displayed
    nav_items = homepage.get_nav_items()
    assert nav_items == ["Home", "Wiki", "Mission", "Portal", "Join"]
    browser.save_screenshot("tests/screenshots/navbar.png")
    homepage.nav_toggle_close()

    # Check for logo in footer
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    assert homepage.footer_logo().is_displayed()
    browser.save_screenshot("tests/screenshots/footer.png")

    # Check if hero animation loads
    browser.execute_script("window.scrollTo(0, 0)")
    # homepage.wait_for_header()
    homepage.go_up()
    time.sleep(5)
    browser.save_screenshot("tests/screenshots/header.png")

    # Check if logo redirects to homepage
    homepage.header_logo().click()
    assert browser.current_url == "https://corpus.okunresearch.com.ng/"

    # Take full screenshot
    screen_obj.full_screenshot(
        browser,
        save_path=r"tests/screenshots",
        image_name="fullshot.png")
