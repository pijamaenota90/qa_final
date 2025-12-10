import pytest
import allure
from api.wikipedia_client import WikipediaAPIClient
from pages.main_page import MainPage


@allure.suite("Интеграционные тесты API + UI")
class TestIntegration:

    @allure.title("Вход через API → проверка в UI")
    def test_api_login_then_ui_check(self, wiki_credentials):

        api_client = WikipediaAPIClient()
        username = wiki_credentials["username"]
        password = wiki_credentials["password"]

        with allure.step(f"API: Входим как {username}"):
            api_client.login(username, password)

        with allure.step("UI: Открываем главную страницу"):
            main_page = MainPage()
            main_page.open_site()

        with allure.step("Проверяем стандартное приветствие"):
            main_page.check_welcome_text('Добро пожаловать в Википедию')

        with allure.step("API: Выходим"):
            api_client.logout()