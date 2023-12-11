"""
A module for loading the homepage objects
"""

import selenium.webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import HomepageLocators


class Homepage:

    HOMEPAGE = HomepageLocators()

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.HOMEPAGE.URL)

    def nav_toggle(self):
        self.browser.find_element(*self.HOMEPAGE.NAV_TOGGLE).click()

    def nav_toggle_close(self):
        self.browser.find_element(*self.HOMEPAGE.NAV_TOGGLE_CLOSE).click()

    def get_nav_items(self):
        self.nav_toggle()
        nav_bar_items = self.browser.find_elements(
            *self.HOMEPAGE.NAV_BAR_ITEMS)
        items = [item.text for item in nav_bar_items]
        return items

    def header_logo(self):
        logo = self.browser.find_element(*self.HOMEPAGE.HEADER_LOGO)
        return logo

    def footer_logo(self):
        logo = self.browser.find_element(*self.HOMEPAGE.FOOTER_LOGO)
        return logo

    def get_hero_image(self):
        wait = WebDriverWait(self.browser, 30)
        hero = wait.until(
            EC.visibility_of_element_located(
                self.HOMEPAGE.HERO_IMAGE))
        return hero

    def wait_for_header(self):
        wait = WebDriverWait(self.browser, 30)
        wait.until(EC.visibility_of_element_located(self.HOMEPAGE.HERO_IMAGE))

    def go_up(self):
        self.browser.find_element(*self.HOMEPAGE.TO_TOP).click()
