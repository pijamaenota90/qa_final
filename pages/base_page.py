from selene import browser, have, be
from selene.support.shared.jquery_style import s
import allure


class BasePage:
    @allure.step("Кликнуть на элемент {locator}")
    def click(self, locator):
        s(locator).click()

    @allure.step("Ввести текст '{text}' в поле {locator}")
    def type(self, locator, text):
        s(locator).type(text)

    @allure.step("Проверить, что элемент виден {locator}")
    def should_see(self, locator):
        s(locator).should(be.visible)

    @allure.step("Проверить, что элемент содержит текст '{text}'")
    def should_see_text(self, locator, text):
        s(locator).should(have.text(text))

    @allure.step("Проскроллить страницу вниз")
    def scroll_to_bottom(self):
        browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

