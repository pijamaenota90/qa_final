import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class WikipediaAPIClient:

    def __init__(self):
        self.api_url = "https://ru.wikipedia.org/w/api.php"
        self.session = requests.Session()
        self.session.verify = False
        self.session.headers.update({
            "User-Agent": "MyTestBot/1.0"
        })
        self.is_logged_in = False
        self.username = None

    def login(self, username: str, password: str) -> bool:

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

        # 3. Проверяем результат
        if result.get("login", {}).get("result") == "Success":
            self.is_logged_in = True
            self.username = username
            print(f" Успешный вход как {username}")
            return True
        else:
            error = result.get("login", {}).get("result", "Unknown error")
            print(f" Ошибка входа: {error}")
            return False

    def logout(self) -> bool:

        if not self.is_logged_in:
            return True
        response = self.session.get(
            self.api_url,
            params={"action": "logout", "format": "json"}
        )
        if response.json().get("logout", {}).get("result") == "Success":
            self.is_logged_in = False
            self.username = None
            print(" Успешный выход")
            return True
        return False

    def get_user_info(self) -> dict:
        """Получить информацию о текущем пользователе"""
        if not self.is_logged_in:
            return {"error": "Not logged in"}

        response = self.session.get(
            self.api_url,
            params={
                "action": "query",
                "meta": "userinfo",
                "uiprop": "groups|editcount",
                "format": "json"
            }
        )
        return response.json()