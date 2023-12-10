"""
A module for loading the homepage objects
"""

import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Homepage:

    # The url to load
    URL = "https://corpus.okunresearch.com.ng"
    NAV_BAR_ITEMS = (By.CSS_SELECTOR, "a.nav-link.scrollto")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def get_nav_items(self):
        self.browser.find_element(
            By.CSS_SELECTOR,
            "i.bi.mobile-nav-toggle.bi-list").click()
        nav_bar_items = self.browser.find_elements(*self.NAV_BAR_ITEMS)
        items = [item.text for item in nav_bar_items]
        return items
