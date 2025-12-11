import allure
from pages.main_page import MainPage



@allure.suite("Тест UI_Wikipedia")
class TestUIWikipedia:

    @allure.title("Проверка переключения на Английскую версию")
    def test_switch_to_english(self, browser_setup):
        main_page = MainPage()
        main_page.open_site()
        main_page.check_welcome_text('Добро пожаловать в Википедию')
        main_page.switch_to_english()
        main_page.check_welcome_text('Welcome to Wikipedia')