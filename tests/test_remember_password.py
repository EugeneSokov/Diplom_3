import allure
from main_page import MainPageForm
from personal_area_page import PersonalAreaPage
from forgot_password_page import PasswordRestorePage
from reset_password_page import ResetPasswPage
from user_data import UserData


class TestRestorePassword:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description('На странице личного кабинета, на которую переходим,'
                        ' проверяем наличие кнопки с текстом "Восстановить"')
    def test_restore_password_page_check(self, driver):
        main_page = MainPageForm(driver)
        main_page.go_on_stellar_burgers_page()
        main_page.personal_cabinet_click()
        pers_area_enter = PersonalAreaPage(driver)
        pers_area_enter.personal_area_click_on_restore_link()
        restore_page = PasswordRestorePage(driver)
        assert restore_page.restore_password_get_text() == 'Восстановить'

    @allure.title('Проверка ввода почты и клик по кнопке «Восстановить»')
    @allure.description('На странице восстановления пароля, на которую переходим, проверяем наличие текста'
                        ' в заголовке "Восстановление пароля" ')
    def test_insert_email_check(self, driver):
        main_page = MainPageForm(driver)
        main_page.go_on_stellar_burgers_page()
        main_page.personal_cabinet_click()
        pers_area_enter = PersonalAreaPage(driver)
        pers_area_enter.personal_area_click_on_restore_link()
        restore_page = PasswordRestorePage(driver)
        restore_page.enter_email(UserData.email_for_recovery)
        restore_page.restore_button_click()
        restore_passw = ResetPasswPage(driver)
        assert restore_passw.restore_passw_title_get_text() == 'Восстановление пароля'

    @allure.title('Проверка перевода в активное состояние поля ввода обновлённого пароля'
                  ' по клику на значок показать/скрыть')
    @allure.description('На странице восстановления пароля, на которую переходим, проверяем'
                        ' наличие текста в заголовке "Восстановление пароля" ')
    def test_password_change_visible_check(self, driver):
        main_page = MainPageForm(driver)
        main_page.go_on_stellar_burgers_page()
        main_page.personal_cabinet_click()
        pers_area_enter = PersonalAreaPage(driver)
        pers_area_enter.personal_area_click_on_restore_link()
        restore_page = PasswordRestorePage(driver)
        restore_page.enter_email(UserData.email_for_recovery)
        restore_page.restore_button_click()
        restore_passw = ResetPasswPage(driver)
        restore_passw.restore_passw_input_field(UserData.password_for_recovery)
        restore_passw.visible_element_click()
        assert restore_passw.restore_active_password_field() == True
