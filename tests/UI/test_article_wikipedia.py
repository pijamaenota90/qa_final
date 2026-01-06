import allure


@allure.suite("Тестирование статей на Википедии")
class TestUIWikipediaArticle:

    @allure.title("Проверка, что в статье присутствуют указанные заголовки")
    @allure.tag('UI')
    def test_article_table_elements(self, main_page, article_page):
        main_page.open_site()
        main_page.search_italy_article()
        article_page.check_article_headings_exist(['История'])

    @allure.title("Проверка ссылки на редактирование статьи")
    @allure.tag('UI')
    def test_article_edit_link(self, main_page, article_page):
        main_page.open_site()
        main_page.search_italy_article()
        article_page.check_edit_button_exists()
        article_page.verify_edit_link()
