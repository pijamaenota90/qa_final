import allure


@allure.suite("Тест открытия Википедии")
class TestUIWikipediaOpen:

    @allure.title("Проверка открытия сайта с приветствием")
    def test_open_and_check_welcome(self, main_page):
        main_page.open_site()
        main_page.check_welcome_text()
