import allure
from selenium.webdriver.common.by import By
from base_page import BasePage


class ResetPasswordLocators:

    RESTORE_PASSW_FIELD = (By.XPATH, "//h2[contains(text(),'Восстановление пароля')]")
    PASSWORD_FIELD = (By.XPATH, "//label[contains(text(),'Пароль')]")
    ACTIVE_PASSW_INPUT = (By.XPATH, "//div[@class = 'input pr-6 pl-6 input_type_password input_size_default input_status_active']/input")
    VISIBILITY_ELEM = (By.XPATH, "//div[@class = 'input__icon input__icon-action']")
    CODE_FIELD = (By.XPATH, "//label[contains(text(),'Введите код из письма')]")
    ACTIVE_FIELD_PASSW = (By.XPATH, "//label[@class = 'input__placeholder text noselect text_type_main-default input__placeholder-focused input__placeholder-filled']")


class ResetPasswPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def restore_passw_title_get_text(self):
        return self.find_element_wait(ResetPasswordLocators.RESTORE_PASSW_FIELD).text

    def restore_passw_input_field(self, password_new):
        self.find_element_wait(ResetPasswordLocators.PASSWORD_FIELD)
        self.find_element_click(ResetPasswordLocators.PASSWORD_FIELD)
        password_field = self.find_element_wait(ResetPasswordLocators.ACTIVE_PASSW_INPUT)
        return password_field.send_keys(password_new)

    def visible_element_click(self):
        self.find_element_click(ResetPasswordLocators.VISIBILITY_ELEM)

    def restore_active_password_field(self):
        if self.find_element_wait(ResetPasswordLocators.ACTIVE_FIELD_PASSW) != None:
            return True

