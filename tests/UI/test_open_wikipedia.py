import pytest
import allure
from pages.main_page import MainPage

@allure.suite("Тест UI_Wikipedia")
class TestUIWikipedia:

    @allure.title("Проверка открытия сайта с приветствием")
    def test_open_and_check_welcome(self, browser_setup):
        main_page = MainPage()
        main_page.open_site()
        main_page.check_welcome_text('Добро пожаловать в Википедию')