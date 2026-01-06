import allure
import pytest

from api.wikipedia_client import WikipediaAPIClient
from models.user import WikiUser


@allure.suite("Интеграционные тесты API + UI")
class TestIntegration:

    @pytest.fixture
    def wiki_user(self):
        return WikiUser()

    @pytest.fixture
    def api_client(self):
        return WikipediaAPIClient()

    @allure.title("Вход через API и проверка в UI")
    @allure.tag('integration')
    def test_api_login_then_ui_check(self, wiki_user, api_client, main_page):
        with allure.step(f"API: Входим как {wiki_user.username}"):
            api_client.login(wiki_user.username, wiki_user.password)
            main_page.open_site()
            main_page.check_welcome_text()
