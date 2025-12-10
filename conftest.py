from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from utils import attach
import pytest
import os
from dotenv import load_dotenv
from api.wikipedia_client import WikipediaAPIClient

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
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    try:
        yield browser
    finally:
        attach.add_screenshot(browser)
        attach.add_logs(browser)
        attach.add_html(browser)
        attach.add_video(browser)
        browser.quit()

load_dotenv()

@pytest.fixture
def api_client():
    client = WikipediaAPIClient()
    yield client
    # Автоматически выходим после теста
    if client.is_logged_in:
        client.logout()

@pytest.fixture
def wiki_credentials():
    return {
        "username": os.getenv("WIKI_USERNAME"),
        "password": os.getenv("WIKI_PASSWORD")
    }