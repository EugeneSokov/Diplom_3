import allure
from base_page import BasePage
from locators_stellarburgers import ResetPasswordLocators


class ResetPasswPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Полечение текста заголовка "Восстановление пароля"')
    def restore_passw_title_get_text(self):
        return self.find_element_wait(ResetPasswordLocators.RESTORE_PASSW_FIELD).text

    @allure.step('Ввод нового пароля в поле "Пароль"')
    def restore_passw_input_field(self, password_new):
        self.find_element_wait(ResetPasswordLocators.PASSWORD_FIELD)
        self.find_element_click(ResetPasswordLocators.PASSWORD_FIELD)
        password_field = self.find_element_wait(ResetPasswordLocators.ACTIVE_PASSW_INPUT)
        return password_field.send_keys(password_new)

    @allure.step('Нажатие на элемент видимости/сокрытия пароля')
    def visible_element_click(self):
        self.find_element_click(ResetPasswordLocators.VISIBILITY_ELEM)

    @allure.step('Проверка того, что после нажатия на элемент видимости, поле становится активным (focused)')
    def restore_active_password_field(self):
        if self.find_element_wait(ResetPasswordLocators.ACTIVE_FIELD_PASSW) is not None:
            return True
