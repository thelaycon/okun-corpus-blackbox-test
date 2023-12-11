"""
Configuration file for Selenium testing
"""

import selenium.webdriver
import pytest
import json


@pytest.fixture
def config(scope="session") -> dict:

    # Load in configuration from config.json
    with open("config.json") as config_file:
        config = json.load(config_file)

    assert config["browser"] in ["Chrome", "Edge"]
    assert isinstance(config["implicitly_wait"], int)
    assert isinstance(config["headless"], bool)
    assert config["implicitly_wait"] > 0

    return config


@pytest.fixture
def browser(config):

    # Creating browser instance based on configuration
    if config["headless"] == True:
        if config["browser"] == "Chrome":
            options = selenium.webdriver.ChromeOptions()
            options.add_argument("headless")
            BROWSER = selenium.webdriver.Chrome(options=options)
        elif config["browser"] == "Edge":
            options = selenium.webdriver.EdgeOptions()
            options.add_argument("headless")
            BROWSER = selenium.webdriver.Edge(options=options)
        else:
            raise Exception("Set browser to either Chrome or Edge")
    else:
        if config["browser"] == "Chrome":
            BROWSER = selenium.webdriver.Chrome()
        elif config["browser"] == "Edge":
            BROWSER = selenium.webdriver.Edge()
        else:
            raise Exception("Set browser to either Chrome or Edge")

    # BROWSER.implicitly_wait(config["implicitly_wait"])

    yield BROWSER

    BROWSER.quit()
