import allure


@allure.suite("Тест переключения языка на википедии")
class TestUIWikipediaLanguage:

    @allure.title("Проверка переключения на Английскую версию")
    @allure.tag('UI')
    def test_switch_to_english(self, main_page):
        main_page.open_site()
        main_page.check_welcome_text()
        main_page.switch_to_english()
        main_page.check_welcome_english_text()
