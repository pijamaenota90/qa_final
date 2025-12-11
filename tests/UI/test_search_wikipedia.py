import pytest
import allure
from pages.main_page import MainPage
from pages.article_page import ArticlePage


@allure.suite("Тест UI_Wikipedia")
class TestUIWikipedia:

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

    @allure.title("Проверка поиска несуществующей статьи")
    def test_search_nonexistent(self, browser_setup):
        main_page = MainPage()
        main_page.open_site()
        main_page.search('qazwsxedcpl,098765')
        main_page.check_no_results_message()


