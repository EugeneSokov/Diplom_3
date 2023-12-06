import allure
from main_page import MainPageForm
from personal_area_page import PersonalAreaPage
from user_data import UserData


class TestPersonalAreaSettings:
    @allure.title('Проверка перехода на страницу «Личный кабинет»')
    @allure.description('На странице личного кабинета,на которую переходим, проверяем наличие кнопки с текстом "Войти"')
    def test_restore_password_page_check(self, driver, create_user):
        pers_area_label = MainPageForm(driver)
        pers_area_label.go_on_stellar_burgers_page()
        pers_area_label.personal_cabinet_click()
        pers_area_enter = PersonalAreaPage(driver)
        pers_area_enter.personal_area_login_password(UserData.user_test_email, UserData.user_test_password)
        pers_area_enter.personal_area_click_on_enter()
        pers_area_label.personal_cabinet_click()
        assert pers_area_enter.personal_area_profile_check() == 'Профиль'

    @allure.title('Проверка перехода в раздел «История заказов»')
    @allure.description('На странице личного кабинета,переходим на "Историю заказов" и'
                        ' проверяем наличие области со списком заказов')
    def test_restore_history_orders_check(self, driver, create_user):
        pers_area_label = MainPageForm(driver)
        pers_area_label.go_on_stellar_burgers_page()
        pers_area_label.personal_cabinet_click()
        pers_area_enter = PersonalAreaPage(driver)
        pers_area_enter.personal_area_login_password(UserData.user_test_email, UserData.user_test_password)
        pers_area_enter.personal_area_click_on_enter()
        pers_area_label.personal_cabinet_click()
        assert pers_area_enter.personal_area_order_history_check() == True

    @allure.title('Проверка выхода из аккаунта')
    @allure.description('На странице личного кабинета нажимаем на "Выход" и проверяем,'
                        ' что перешли на страницу авторизации')
    def test_restore_logout_check(self, driver, create_user):
        pers_area_label = MainPageForm(driver)
        pers_area_label.go_on_stellar_burgers_page()
        pers_area_label.personal_cabinet_click()
        pers_area_enter = PersonalAreaPage(driver)
        pers_area_enter.personal_area_login_password(UserData.user_test_email, UserData.user_test_password)
        pers_area_enter.personal_area_click_on_enter()
        pers_area_label.personal_cabinet_click()
        pers_area_enter.personal_area_logout_click()
        assert pers_area_enter.personal_area_login_button_text() == 'Войти'
