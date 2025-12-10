import pytest
import allure
from pages.main_page import MainPage
from pages.article_page import ArticlePage


@allure.suite("Тест UI_Wikipedia")
class TestUIWikipedia:

    @allure.title("Проверка открытия сайта с приветствием")
    def test_open_and_check_welcome(self, browser_setup):
        main_page = MainPage()

        main_page.open_site()
        main_page.check_welcome_text('Добро пожаловать в Википедию')

    @allure.title("Проверка поиска пустой строки")
    def test_search_empty(self, browser_setup):
        main_page = MainPage()

        main_page.open_site()
        main_page.search('')

        main_page.should_see(main_page.search_input)


    @allure.title("Проверка поиска статьи про Москву")
    def test_search_moscow(self, browser_setup):
        main_page = MainPage()
        article_page = ArticlePage()

        main_page.open_site()
        main_page.search('Москва')

        article_page.check_title('Москва')
        article_page.check_content_exists()

    @allure.title("Проверка переключения на Английскую версию")
    def test_switch_to_english(self, browser_setup):
        main_page = MainPage()

        main_page.open_site()
        main_page.check_welcome_text('Добро пожаловать в Википедию')
        main_page.switch_to_english()
        main_page.check_welcome_text('Welcome to Wikipedia')

    @allure.title("Проверка, что пользователь не авторизован")
    def test_user_not_logged_in(self, browser_setup):
        main_page = MainPage()
        main_page.open_site()
        main_page.check_user_not_logged_in('Войти')
