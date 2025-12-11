import allure
from pages.main_page import MainPage

@allure.suite("Тест UI_Wikipedia")
class TestUIWikipedia:

    @allure.title("Проверка, что пользователь не авторизован")
    def test_user_not_logged_in(self, browser_setup):
        main_page = MainPage()
        main_page.open_site()
        main_page.check_user_not_logged_in('Войти')