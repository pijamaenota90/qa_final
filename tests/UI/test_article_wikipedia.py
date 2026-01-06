import pytest
import allure
from pages.main_page import MainPage
from pages.article_page import ArticlePage


@allure.suite("Тестирование статей на Википедии")
class TestUIWikipediaArticle:

    @allure.title("Проверка, что в статье присутствуют указанные заголовки")
    @allure.tag('UI')
    def test_article_table_elements(self, browser_setup):
        main_page = MainPage()
        article_page = ArticlePage()
        with allure.step("Открываем главную страницу"):
            main_page.open_site()
        with allure.step("Ищем статью"):
            main_page.search('Италия')
        with allure.step("Проверяем наличие заголовков"):
            article_page.check_article_headings_exist(['История'])

    @allure.title("Проверка ссылки на редактирование статьи")
    @allure.tag('UI')
    def test_article_edit_link(self, browser_setup):
        main_page = MainPage()
        article_page = ArticlePage()
        with allure.step("Открываем главную страницу"):
            main_page.open_site()
        with allure.step("Ищем статью"):
            main_page.search('Италия')
        with allure.step("Проверяем наличие кнопки редактирования статьи"):
            article_page.check_edit_button_exists()
        with allure.step("Проверяем наличие линка редактирования у кнопки"):
            article_page.verify_edit_link()