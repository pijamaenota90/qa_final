import allure

from api.wikipedia_client import WikipediaAPIClient


@allure.suite("Тесты API")
class TestAPIWikipedia:

    @allure.title("Регистрация с помощью API")
    @allure.tag('API')
    def test_api_login(self, wiki_credentials):
        client = WikipediaAPIClient()
        username = wiki_credentials["username"]
        password = wiki_credentials["password"]
        with allure.step("Регистрируемся по API"):
            login_success = client.login(username, password)
        with allure.step("Проверяем правильность регистрации"):
            assert login_success is True
            assert client.is_logged_in is True
            assert client.username == username

    @allure.title("Получение данных по пользователю по API")
    @allure.tag('API')
    def test_api_get_user_info(self, wiki_credentials):
        client = WikipediaAPIClient()
        username = wiki_credentials["username"]
        password = wiki_credentials["password"]
        with allure.step("Регистрируемся по API"):
            client.login(username, password)
        with allure.step("Получаем информацию по пользователю"):
            user_info = client.get_user_info()

        with allure.step("Проверяем правильность имени пользователя"):
            assert "query" in user_info
            assert "userinfo" in user_info["query"]
            user_data = user_info["query"]["userinfo"]
            assert "name" in user_data
            base_username = username.split('@')[0]
            assert user_data["name"] == base_username
            print(f" Пользователь: {user_data['name']}")

    @allure.title("Выход с помощью API")
    @allure.tag('API')
    def test_api_logout(self, wiki_credentials):
        client = WikipediaAPIClient()
        username = wiki_credentials["username"]
        password = wiki_credentials["password"]
        with allure.step("Регистрируемся по API"):
            client.login(username, password)
        with allure.step("Выход по API"):
            client.logout()

        with allure.step("Проверяем корректность выхода"):
            assert client.is_logged_in is False
            assert client.username is None
