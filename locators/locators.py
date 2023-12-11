from selenium.webdriver.common.by import By


class HomepageLocators:
    URL = "https://corpus.okunresearch.com.ng"
    NAV_TOGGLE = (By.CSS_SELECTOR, "i.bi.mobile-nav-toggle.bi-list")
    NAV_TOGGLE_CLOSE = (By.CSS_SELECTOR, "i.bi.mobile-nav-toggle.bi-x")
    NAV_BAR_ITEMS = (By.CSS_SELECTOR, "a.nav-link.scrollto")
    HEADER_LOGO = (By.XPATH, "//*[@id='header']/div/a/img")
    FOOTER_LOGO = (By.XPATH, "//*[@id='footer']/div[1]/div/div/div[1]/a/img")
    HERO_IMAGE = (By.XPATH, "/html/body/section/div/div/div[2]/img")
    TO_TOP = (By.XPATH, "/html/body/a/i")
