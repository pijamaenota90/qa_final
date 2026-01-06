import allure
from pages.main_page import MainPage



@allure.suite("Тест переключения языка на википедии")
class TestUIWikipediaLanguage:

    @allure.title("Проверка переключения на Английскую версию")
    @allure.tag('UI')
    def test_switch_to_english(self, browser_setup):
        main_page = MainPage()
        with allure.step("Открываем главную страницу"):
            main_page.open_site()
        with allure.step("Проверяем приветствие на Русском"):
            main_page.check_welcome_text()
        with allure.step("Меняем язык"):
            main_page.switch_to_english()
        with allure.step("Проверяем приветствие на Английском"):
            main_page.check_welcome_english_text()