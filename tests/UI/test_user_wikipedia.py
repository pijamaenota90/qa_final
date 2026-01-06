import allure


@allure.suite("Тест UI_Wikipedia")
class TestUIWikipediaUser:

    @allure.title("Проверка, что пользователь не авторизован")
    def test_user_not_logged_in(self, main_page):
        main_page.open_site()
        main_page.check_user_not_logged_in()
