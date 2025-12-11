import pytest
import allure
from api.wikipedia_client import WikipediaAPIClient

@allure.suite("Тест API_Wikipedia")
class TestAPIWikipedia:

    def test_api_login(self,wiki_credentials):
        client = WikipediaAPIClient()
        username = wiki_credentials["username"]
        password = wiki_credentials["password"]
        login_success = client.login(username, password)

        assert login_success is True
        assert client.is_logged_in is True
        assert client.username == username

    def test_api_get_user_info(self,wiki_credentials):
        client = WikipediaAPIClient()
        username = wiki_credentials["username"]
        password = wiki_credentials["password"]
        client.login(username, password)
        user_info = client.get_user_info()

        assert "query" in user_info
        assert "userinfo" in user_info["query"]
        user_data = user_info["query"]["userinfo"]
        assert "name" in user_data
        assert user_data["name"] == username
        print(f" Пользователь: {user_data['name']}")

    def test_api_logout(self, wiki_credentials):
        client = WikipediaAPIClient()
        username = wiki_credentials["username"]
        password = wiki_credentials["password"]
        client.login(username, password)
        client.logout()

        assert client.is_logged_in is False
        assert client.username is None