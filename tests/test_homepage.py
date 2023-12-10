import pytest
from pages.homepage import Homepage


def test_homepage_nav(browser):
    homepage = Homepage(browser)
    homepage.load()
    nav_items = homepage.get_nav_items()
    browser.save_screenshot("home.png")
    assert nav_items == ["Home", "Wiki", "Mission", "Portal", "Join"]

    # Check for logo in header

    # Check for logo in footer

    # Check if logo redirects to homepage


@pytest.mark.skip()
def test_homepage_animation(browser):
    pass
    # Check if animation loads


@pytest.mark.skip()
def test_navigation_bar(browser):
    pass
    # Check if navigation items are visible


@pytest.mark.skip()
def test_features(browser):
    pass
    # Check if mission is visible

    # Check if objectives are visible

    # Check if contributors are visible


@pytest.mark.skip()
def test_join_form(browser):
    pass
    # Check if form works


@pytest.mark.skip()
def test_footer_contact(browser):
    pass
    # Check if footer contains contact
