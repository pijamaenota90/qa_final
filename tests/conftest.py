import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from data import Data
from utils import attach

data = Data()


@pytest.fixture(scope='function')
def browser_setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 60
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--disable-web-security')
    options.add_argument('--allow-insecure-localhost')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--window-size=1920,1080')

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        },
        "goog:chromeOptions": {
            "args": [
                "--ignore-certificate-errors",
                "--ignore-ssl-errors",
                "--disable-web-security",
                "--allow-insecure-localhost",
                "--disable-blink-features=AutomationControlled",
                "--window-size=1920,1080",
                "--no-sandbox",
                "--disable-dev-shm-usage"
            ]
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=data.selenoid_url,
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


@pytest.fixture(scope='function')
def local_driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(60)
    yield driver
    driver.quit()


@pytest.fixture
def wiki_credentials():
    return {
        "username": data.WIKI_USERNAME,
        "password": data.WIKI_PASSWORD
    }
