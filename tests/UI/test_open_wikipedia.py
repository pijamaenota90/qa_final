import allure

from pages.main_page import MainPage


@allure.suite("Тест открытия Википедии")
class TestUIWikipediaOpen:

    @allure.title("Проверка открытия сайта с приветствием")
    def test_open_and_check_welcome(self, browser_setup):
        main_page = MainPage()
        with allure.step("Открываем главную страницу"):
            main_page.open_site()
        with allure.step("Проверяем приветствие на Русском"):
            main_page.check_welcome_text()
