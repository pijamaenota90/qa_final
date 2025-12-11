import pytest
import allure
from pages.main_page import MainPage
from pages.article_page import ArticlePage


@allure.suite("Тест UI_Wikipedia")
class TestUIWikipedia:

    @allure.title("Проверка, что открыта статья со структурой")
    def test_article_structure(self, browser_setup):
        main_page = MainPage()
        article_page = ArticlePage()
        main_page.open_site()
        main_page.search('Наука')
        article_page.check_article_table_exists()

    @allure.title("Проверка, что в статье присутствуют указанные заголовки")
    def test_article_table_elements(self, browser_setup):
        main_page = MainPage()
        article_page = ArticlePage()
        main_page.open_site()
        main_page.search('Наука')
        article_page.check_table_sections_exist(['История', 'Учёные'])