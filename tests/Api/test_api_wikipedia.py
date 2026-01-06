import allure
import pytest

from api.wikipedia_client import WikipediaAPIClient
from models.user import WikiUser


@allure.suite("Тесты API")
class TestAPIWikipedia:

    @pytest.fixture
    def wiki_user(self):
        return WikiUser()

    @pytest.fixture
    def api_client(self):
        return WikipediaAPIClient()

    @pytest.fixture
    def logged_in_client(self, api_client, wiki_user):
        api_client.login(wiki_user.username, wiki_user.password)
        return api_client

    @allure.title("Регистрация с помощью API")
    @allure.tag('API')
    def test_api_login(self, wiki_user, api_client):
        response = api_client.login(wiki_user.username, wiki_user.password)

        with allure.step("Проверяем правильность регистрации"):
            assert response.status_code == 200
            result = response.json()
            login_info = result["login"]
            assert login_info.get("result") == "Success"
            username_without_email = wiki_user.username.split('@')[0]
            assert username_without_email == api_client.username

    @allure.title("Получение данных по пользователю по API")
    @allure.tag('API')
    def test_api_get_user_info(self, logged_in_client, wiki_user):
        response = logged_in_client.get_user_info()

        with allure.step("Проверяем правильность имени пользователя"):
            assert response.status_code == 200
            result = response.json()
            user_data = result["query"]["userinfo"]
            username_without_email = wiki_user.username.split('@')[0]
            assert user_data["name"] == username_without_email
            assert isinstance(user_data["id"], int)
            assert "user" in user_data["groups"]

    @allure.title("Выход с помощью API")
    @allure.tag('API')
    def test_api_logout(self, logged_in_client):
        response = logged_in_client.logout()

        with allure.step("Проверяем корректность выхода"):
            assert response.status_code == 200
            assert logged_in_client.username is None
