from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from utils import attach
import pytest
from data import Data
import os

data = Data()

@pytest.fixture(scope='function')
def browser_setup():

    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 60
    browser.config._save_screenshot_on_failure = False
    browser.config._save_page_source_on_failure = False
    options = Options()

    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--disable-web-security')
    options.add_argument('--allow-insecure-localhost')
    options.add_argument('--disable-blink-features=AutomationControlled')

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True

        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN_SELENOID')
    password = os.getenv('PASSWORD_SELENOID')
    host = os.getenv('HOST_SELENOID')
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{host}/wd/hub",
        options=options
    )
    driver.set_page_load_timeout(60)
    browser.config.driver = driver

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    browser.quit()

@pytest.fixture
def wiki_credentials():
    return {
        "username": data.WIKI_USERNAME,
        "password": data.WIKI_PASSWORD
    }