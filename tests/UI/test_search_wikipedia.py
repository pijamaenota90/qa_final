import pytest
import allure
from pages.main_page import MainPage
from pages.article_page import ArticlePage


@allure.suite("Тест UI_Wikipedia")
class TestUIWikipediaSearch:

    @allure.title("Проверка поиска пустой строки")
    def test_search_empty(self, browser_setup):
        main_page = MainPage()
        with allure.step("Открываем главную страницу"):
            main_page.open_site()
        with allure.step("Ищем и проверяем, что поиск пустой строки работает"):
            main_page.search('')
            main_page.should_see(main_page.search_input)

    @allure.title("Проверка поиска статьи про Москву")
    def test_search_moscow(self, browser_setup):
        main_page = MainPage()
        article_page = ArticlePage()
        with allure.step("Открываем главную страницу"):
            main_page.open_site()
        with allure.step("Ищем статью"):
            main_page.search('Москва')
        with allure.step("Проверяем, что заголовок совпадает с тем, что искали"):
            article_page.check_title('Москва')
        with allure.step("Проверяем, что в статье есть контент"):
            article_page.check_content_exists()

    @allure.title("Проверка поиска несуществующей статьи")
    def test_search_nonexistent(self, browser_setup):
        main_page = MainPage()
        with allure.step("Открываем главную страницу"):
            main_page.open_site()
        with allure.step("Ищем несуществующую статью"):
            main_page.search('qazwsxedcpl,098765')
        with allure.step("Проверяем, что результата нет"):
            main_page.check_no_results_message()


