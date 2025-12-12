import allure
from pages.main_page import MainPage

@allure.suite("Тест UI_Wikipedia")
class TestUIWikipediaUser:

    @allure.title("Проверка, что пользователь не авторизован")
    def test_user_not_logged_in(self, browser_setup):
        main_page = MainPage()
        with allure.step("Открываем главную страницу"):
            main_page.open_site()
        with allure.step("Проверяем, что пользователь не залогинен"):
            main_page.check_user_not_logged_in('Войти')