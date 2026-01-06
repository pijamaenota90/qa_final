import allure
from selene import browser, have, be
from selene.support.shared.jquery_style import s


class MainPage:
    search_input = '#searchInput'
    search_button = '#searchButton'
    page_content = 'body'
    english_link = 'a[lang="en"]'
    no_results_message = 'p.mw-search-nonefound'
    search_suggestions = '.suggestions-results'
    login_link = '#pt-login'

    @allure.step("Открыть сайт Wikipedia")
    def open_site(self):
        browser.open('https://ru.wikipedia.org')
        return self

    @allure.step("Поиск приветственной фразы")
    def check_welcome_text(self):
        s(self.page_content).should(have.text('Добро пожаловать в Википедию'))
        return self

    @allure.step("Поиск приветственной фразы на Английском")
    def check_welcome_english_text(self):
        s(self.page_content).should(have.text('Welcome to Wikipedia'))
        return self

    @allure.step("Поиск статьи про Москву")
    def search_moscow_article(self):
        s(self.search_input).type('Москва')
        s(self.search_button).click()
        return self

    @allure.step("Поиск статьи про Италию")
    def search_italy_article(self):
        s(self.search_input).type('Италия')
        s(self.search_button).click()
        return self

    @allure.step("Поиск пустой статьи")
    def search_empty_article(self):
        s(self.search_input).type('Москва')
        s(self.search_button).click()
        return self

    @allure.step("Поиск несуществующей статьи")
    def search_nonexistent(self):
        s(self.search_input).type('qazwsxedcpl,098765')
        s(self.search_button).click()
        return self

    @allure.step("Переключить на Английскую версию сайта")
    def switch_to_english(self):
        browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        s(self.english_link).click()
        return self

    @allure.step("Проверить, что пользователь не авторизован")
    def check_user_not_logged_in(self):
        s(self.login_link).should(be.visible)
        s(self.login_link).should(have.text('Войти'))
        return self

    @allure.step("Проверить сообщение 'Соответствий запросу не найдено'")
    def check_no_results_message(self):
        s(self.no_results_message).should(be.visible)
        s(self.no_results_message).should(have.text('Соответствий запросу не найдено'))
        return self

    @allure.step("Проверить, что элемент виден")
    def should_see(self, locator):
        s(locator).should(be.visible)
        return self
