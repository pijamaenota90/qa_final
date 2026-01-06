from selene import query, have, be
from selene.support.shared.jquery_style import s, ss
import allure


class ArticlePage:
    title = '#firstHeading'
    content = '#mw-content-text'
    table = '#toc'
    edit_button = '#ca-edit a'  # или '.mw-ui-icon-edit'
    edit_tab = '#ca-edit'
    edit_section_links = '.mw-editsection a'
    edit_page_heading = '#firstHeading'  # На странице редактирования
    edit_textarea = '#wpTextbox1'

    @allure.step("Проверить, что заголовок статьи содержит '{expected_text}'")
    def check_title(self, expected_text):
        s(self.title).should(have.text(expected_text))
        return self

    @allure.step("Проверить, что контент статьи есть на странице")
    def check_content_exists(self):
        s(self.content).should(be.visible)
        return self

    @allure.step("Проверить, что у статьи есть оглавление")
    def check_article_table_exists(self):
        s(self.table).should(be.visible)
        return self

    def check_article_headings_exist(self, headings: list):
        for heading in headings:
            selector = f'h2#{heading}'
            element = s(selector)
            element.should(be.visible)
            actual_text = element.get(query.text) or element.text
            assert heading in actual_text
            print(f" Найден заголовок: {heading}")
        return self

    @allure.step("Проверить наличие кнопки редактирования")
    def check_edit_button_exists(self):
        s(self.edit_button).should(be.visible)
        allure.attach("Кнопка редактирования найдена", name="Edit button check")
        return self

    @allure.step("Проверить ссылку на редактирование")
    def verify_edit_link(self):
        edit_link = s(self.edit_button)
        href = edit_link.get(query.attribute('href'))
        link_text = edit_link.get(query.text) or edit_link.get(query.attribute('title'))
        assert href, "Ссылка на редактирование не содержит href"
        assert 'action=edit' in href or 'edit' in href.lower(), \
            f"Ссылка не ведет на редактирование: {href}"

        allure.attach(f"Текст ссылки: {link_text}", name="Edit link info")
        allure.attach(f"URL ссылки: {href}", name="Edit link URL")
        return self



