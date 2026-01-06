import os

from dotenv import load_dotenv

load_dotenv()


class Data:
    SELENOID_USER = os.getenv('SELENOID_USER')
    SELENOID_PASSWORD = os.getenv('SELENOID_PASSWORD')
    SELENOID_HOST = os.getenv('SELENOID_HOST')
    WIKI_USERNAME = os.getenv('WIKI_USERNAME')
    WIKI_PASSWORD = os.getenv('WIKI_PASSWORD')

    @property
    def selenoid_url(self):
        return f"https://{self.SELENOID_USER}:{self.SELENOID_PASSWORD}@{self.SELENOID_HOST}/wd/hub"
