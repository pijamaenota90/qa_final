import allure


@allure.suite("Тест UI_Wikipedia")
class TestUIWikipediaSearch:

    @allure.title("Проверка поиска пустой строки")
    def test_search_empty(self, main_page):
        main_page.open_site()
        main_page.search_empty_article()
        main_page.should_see(main_page.search_input)

    @allure.title("Проверка поиска статьи про Москву")
    def test_search_moscow(self, main_page, article_page):
        main_page.open_site()
        main_page.search_moscow_article()
        article_page.check_moscow_title()
        article_page.check_content_exists()

    @allure.title("Проверка поиска несуществующей статьи")
    def test_search_nonexistent(self, main_page):
        main_page.open_site()
        main_page.search_nonexistent()
        main_page.check_no_results_message()
