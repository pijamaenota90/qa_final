import pytest
import allure
from api.wikipedia_client import WikipediaAPIClient
from pages.main_page import MainPage


@allure.suite("Тест API_Wikipedia")
class TestAPIWikipedia:

    def test_api_login(self,wiki_credentials):

        client = WikipediaAPIClient()
        username = wiki_credentials["username"]
        password = wiki_credentials["password"]
        login_success = client.login(username, password)

        assert login_success is True, "Должны успешно войти"
        assert client.is_logged_in is True, "Флаг входа должен быть True"
        assert client.username == username, "Имя пользователя должно сохраниться"

    def test_get_user_info(self,wiki_credentials):

        client = WikipediaAPIClient()
        username = wiki_credentials["username"]
        password = wiki_credentials["password"]
        client.login(username, password)

        user_info = client.get_user_info()
        assert "query" in user_info, "Ответ должен содержать 'query'"
        assert "userinfo" in user_info["query"], "Ответ должен содержать 'userinfo'"

        user_data = user_info["query"]["userinfo"]
        assert "name" in user_data
        assert user_data["name"] == username
        print(f" Пользователь: {user_data['name']}")

        client.logout()
     #   assert client.is_logged_in is False, "После выхода флаг должен быть False"
