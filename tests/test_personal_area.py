import allure
from base_page import BasePage
from main_page import MainPageForm
from personal_area_page import PersonalAreaPage


class TestPersonalAreaSettings:
    @allure.title('Проверка перехода на страницу «Личный кабинет»')
    @allure.description('На странице личного кабинета, на которую переходим, проверяем наличие кнопки с текстом "Войти"')
    def test_restore_password_page_check(self, driver, create_user):
        page_rest_pass = BasePage(driver)
        page_rest_pass.go_on_page_stellar_burger()
        pers_area_label = MainPageForm(driver)
        pers_area_label.personal_cabinet_click()
        pers_area_enter = PersonalAreaPage(driver)
        pers_area_enter.personal_area_login_password('BilboBeggins1@sheer.net', 'qwertyzxcv123')
        pers_area_enter.personal_area_click_on_enter()
        pers_area_label.personal_cabinet_click()
        assert pers_area_enter.personal_area_profile_check() == 'Профиль'

    @allure.title('Проверка перехода в раздел «История заказов»')
    @allure.description('На странице личного кабинета,переходим на "Историю заказов" и проверяем наличие области со списком заказов')
    def test_restore_history_orders_check(self, driver, create_user):
        page_rest_pass = BasePage(driver)
        page_rest_pass.go_on_page_stellar_burger()
        pers_area_label = MainPageForm(driver)
        pers_area_label.personal_cabinet_click()
        pers_area_enter = PersonalAreaPage(driver)
        pers_area_enter.personal_area_login_password('BilboBeggins1@sheer.net', 'qwertyzxcv123')
        pers_area_enter.personal_area_click_on_enter()
        pers_area_label.personal_cabinet_click()
        assert pers_area_enter.personal_area_order_history_click() == True

    @allure.title('Проверка выхода из аккаунта')
    @allure.description('На странице личного кабинета нажимаем на "Выход" и проверяем, что перешли на страницу авторизации')
    def test_restore_logout_check(self, driver, create_user):
        page_rest_pass = BasePage(driver)
        page_rest_pass.go_on_page_stellar_burger()
        pers_area_label = MainPageForm(driver)
        pers_area_label.personal_cabinet_click()
        pers_area_enter = PersonalAreaPage(driver)
        pers_area_enter.personal_area_login_password('BilboBeggins1@sheer.net', 'qwertyzxcv123')
        pers_area_enter.personal_area_click_on_enter()
        pers_area_label.personal_cabinet_click()
        pers_area_enter.personal_area_logout_click()
        assert pers_area_enter.personal_area_login_button_text() == 'Войти'
