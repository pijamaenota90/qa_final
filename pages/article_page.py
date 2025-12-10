from .base_page import BasePage
import allure


class ArticlePage(BasePage):
    title = '#firstHeading'
    content = '#mw-content-text'

    @allure.step("Проверить, что заголовок статьи содержит '{expected_text}'")
    def check_title(self, expected_text):
        self.should_see_text(self.title, expected_text)

    @allure.step("Проверить, что контент статьи есть на странице")
    def check_content_exists(self):
        self.should_see(self.content)