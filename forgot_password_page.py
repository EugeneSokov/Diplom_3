from base_page import BasePage
from locators_stellarburgers import ForgotPasswordLocators


class PasswordRestorePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def restore_password_get_text(self):
        return self.find_element_wait(ForgotPasswordLocators.RESTORE_BUTTON).text

    def enter_email(self, email):
        self.find_element_click(ForgotPasswordLocators.EMAIL_FIELD)
        email_field = self.find_element_wait(ForgotPasswordLocators.EMAIL_FIELD)
        email_field.send_keys(email)

    def restore_button_click(self):
        self.find_element_click(ForgotPasswordLocators.RESTORE_BUTTON)
