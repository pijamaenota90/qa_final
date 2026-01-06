import allure

from api.wikipedia_client import WikipediaAPIClient
from models.user import WikiUser
from pages.main_page import MainPage


@allure.suite("Интеграционные тесты API + UI")
class TestIntegration:

    @allure.title("Вход через API и проверка в UI")
    @allure.tag('integration')
    def test_api_login_then_ui_check(self, browser_setup):
        user = WikiUser()
        api_client = WikipediaAPIClient()

        with allure.step(f"API: Входим как {user.username}"):
            api_client.login(user.username, user.password)

        with allure.step("UI: Открываем главную страницу"):
            main_page = MainPage()
            main_page.open_site()

        with allure.step("UI: Проверяем приветствие"):
            main_page.check_welcome_text()
