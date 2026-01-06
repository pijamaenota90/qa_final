import os

from dotenv import load_dotenv

load_dotenv()


class Data:
    SELENOID_USER = os.getenv('SELENOID_USER')
    SELENOID_PASSWORD = os.getenv('SELENOID_PASSWORD')
    SELENOID_HOST = os.getenv('SELENOID_HOST')

    WIKI_API_URL = os.getenv('WIKI_API_URL')

    @property
    def selenoid_url(self):
        return f"https://{self.SELENOID_USER}:{self.SELENOID_PASSWORD}@{self.SELENOID_HOST}/wd/hub"

    @property
    def wiki_api_url(self):
        return f"https://{self.WIKI_API_URL}"
