import allure
import requests

from models.data import Data


class WikipediaAPIClient:

    def __init__(self):
        self.data = Data()
        self.api_url = self.data.wiki_api_url
        self.session = requests.Session()
        self.session.verify = False
        self.session.headers.update({
            "User-Agent": "MyTestBot/1.0"
        })
        self.is_logged_in = False
        self.username = None

    @allure.step("Войти на сайт через API")
    def login(self, username: str, password: str) -> requests.Response:
        token_response = self.session.get(
            self.api_url,
            params={
                "action": "query",
                "meta": "tokens",
                "type": "login",
                "format": "json"
            }
        )

        token_data = token_response.json()
        login_token = token_data["query"]["tokens"]["logintoken"]

        login_data = {
            "action": "login",
            "lgname": username,
            "lgpassword": password,
            "lgtoken": login_token,
            "format": "json"
        }

        response = self.session.post(self.api_url, data=login_data)
        result = response.json()
        login_info = result.get("login", {})

        if login_info.get("result") == "Success":
            self.username = login_info.get("lgusername")

        return response

    @allure.step("Получить информацию о пользователе")
    def get_user_info(self) -> requests.Response:
        response = self.session.get(
            self.api_url,
            params={
                "action": "query",
                "meta": "userinfo",
                "uiprop": "groups|editcount",
                "format": "json"
            }
        )

        return response

    @allure.step("Выйти из системы")
    def logout(self) -> requests.Response:
        token_response = self.session.get(
            self.api_url,
            params={
                "action": "query",
                "meta": "tokens",
                "type": "csrf",
                "format": "json"
            }
        )

        token_data = token_response.json()
        csrf_token = token_data["query"]["tokens"]["csrftoken"]

        response = self.session.post(
            self.api_url,
            data={
                "action": "logout",
                "token": csrf_token,
                "format": "json"
            }
        )

        self.username = None

        return response
