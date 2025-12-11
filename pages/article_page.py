from selene import browser, have, be
from selene.support.shared.jquery_style import s, ss
import allure


class ArticlePage:
    title = '#firstHeading'
    content = '#mw-content-text'
    table = '#toc'
    table_section = '#toc span.toctext'


    @allure.step("Проверить, что заголовок статьи содержит '{expected_text}'")
    def check_title(self, expected_text):
        s(self.title).should(have.text(expected_text))

    @allure.step("Проверить, что контент статьи есть на странице")
    def check_content_exists(self):
        s(self.content).should(be.visible)

    @allure.step("Проверить, что у статьи есть оглавление")
    def check_article_table_exists(self):
        s(self.table).should(be.visible)


    def check_table_sections_exist(self, expected_sections: list):
        table_elements = ss(self.table_section)
        actual_texts = [element.text for element in table_elements]
        for expected_section in expected_sections:
            expected_clean = expected_section.strip()
            assert expected_clean in actual_texts



