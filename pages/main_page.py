from selene import browser
from .base_page import BasePage
import allure


class MainPage(BasePage):
    search_input = '#searchInput'
    search_button = '#searchButton'
    page_content = 'body'
    english_link = 'a[lang="en"]'


    @allure.step("Открыть сайт Wikipedia")
    def open_site(self):
        browser.open('https://ru.wikipedia.org')

    @allure.step("Поиск приветственной фразы")
    def check_welcome_text(self, text):
        self.should_see_text(self.page_content, text)

    @allure.step("Поиск текста '{text}'")
    def search(self, text):
        self.type(self.search_input, text)
        self.click(self.search_button)

    @allure.step("Переключение на Английскую версию сайта")
    def switch_to_english(self):
        self.scroll_to_bottom()
        self.click(self.english_link)

    @allure.step("Проверить что пользователь не авторизован")
    def check_user_not_logged_in(self, text):
        self.should_see_text(self.page_content, text)
