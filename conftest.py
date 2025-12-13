from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from utils import attach
import pytest
from data import Data

data = Data()

@pytest.fixture(scope='function')
def browser_setup():
    options = Options()

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        },
        "goog:chromeOptions": {
            "args": [
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu",
                "--headless=new"
            ]
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=data.selenoid_url,
        options=options
    )
    '''
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    browser.config.driver = driver
    #browser.config.base_url = "https://ru.wikipedia.org"
    '''
    try:
        yield browser
    finally:
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