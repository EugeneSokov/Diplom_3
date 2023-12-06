import allure
from base_page import BasePage
from locators_stellarburgers import ForgotPasswordLocators


class PasswordRestorePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Полечение текста кнопки "Восстановить"')
    def restore_password_get_text(self):
        return self.find_element_wait(ForgotPasswordLocators.RESTORE_BUTTON).text

    @allure.step('Ввод email-адреса в поле Email')
    def enter_email(self, email):
        self.find_element_click(ForgotPasswordLocators.EMAIL_FIELD)
        email_field = self.find_element_wait(ForgotPasswordLocators.EMAIL_FIELD)
        email_field.send_keys(email)

    @allure.step('Нажатие на кнопку "Востановить"')
    def restore_button_click(self):
        self.find_element_click(ForgotPasswordLocators.RESTORE_BUTTON)
