import allure
from base_page import BasePage
from locators_stellarburgers import PersonalAreaLocators


class PersonalAreaPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Получение текста названия ссылки "Восстановить пароль"')
    def personal_area_get_text(self):
        return self.find_element_wait(PersonalAreaLocators.RESTORE_PASSW).text

    @allure.step('Нажатие на ссылку "Восстановить пароль"')
    def personal_area_click_on_restore_link(self):
        self.find_element_click(PersonalAreaLocators.RESTORE_PASSW)

    @allure.step('Нажатие на кнопку "Войти"')
    def personal_area_click_on_enter(self):
        self.find_element_click(PersonalAreaLocators.LOGIN_BUTTON)

    @allure.step('Получение текста кнопки "Войти"')
    def personal_area_login_button_text(self):
        self.find_element_wait(PersonalAreaLocators.PROFILE_LABEL)
        return self.find_element_wait(PersonalAreaLocators.LOGIN_BUTTON).text

    @allure.step('Авторизация пользователя с вводом email и password')
    def personal_area_login_password(self, email, password):
        self.find_element_wait(PersonalAreaLocators.LOGIN_BUTTON)
        self.find_element_click(PersonalAreaLocators.EMAIL_AUTHOR)
        email_field = self.find_element_wait(PersonalAreaLocators.EMAIL_AUTHOR)
        email_field.send_keys(email)
        self.find_element_click(PersonalAreaLocators.PASS_AUTHOR)
        email_field = self.find_element_wait(PersonalAreaLocators.PASS_AUTHOR)
        email_field.send_keys(password)

    @allure.step('Получение текста "Профиль" на личной странице пользователя')
    def personal_area_profile_check(self):
        return self.find_element_wait(PersonalAreaLocators.PROFILE_LABEL).text

    @allure.step('Проверка появления на странице списка истории заказов')
    def personal_area_order_history_check(self):
        self.find_element_wait(PersonalAreaLocators.PROFILE_LABEL)
        self.find_element_click(PersonalAreaLocators.ORDER_HISTORY_LABEL)
        if self.find_element_wait(PersonalAreaLocators.ORDER_HISTORY_LIST) is not None:
            return True

    @allure.step('Нажатие на кнопку "Выйти"')
    def personal_area_logout_click(self):
        self.find_element_wait(PersonalAreaLocators.PROFILE_LABEL)
        self.find_element_click(PersonalAreaLocators.LOGOUT_BUTTON)

    @allure.step('Нажатие на кнопку "Конструктор" в заголовке')
    def personal_area_constructor_click(self):
        self.find_element_click(PersonalAreaLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Получение текста последнего сделанного заказа в "Истории заказов"')
    def last_order_number_get_text(self):
        self.find_element_wait(PersonalAreaLocators.ORDER_HISTORY_LIST)
        return self.find_element_wait(PersonalAreaLocators.ORDER_HISTORY_LAST_ELEM).text
