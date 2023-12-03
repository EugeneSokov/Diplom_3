import allure
from base_page import BasePage
from main_page import MainPageForm
from personal_area_page import PersonalAreaPage
from forgot_password_page import PasswordRestorePage
from reset_password_page import ResetPasswPage


class TestRestorePassword:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description('На странице личного кабинета, на которую переходим,'
                        ' проверяем наличие кнопки с текстом "Восстановить"')
    def test_restore_password_page_check(self, driver):
        page_rest_pass = BasePage(driver)
        page_rest_pass.go_on_page_stellar_burger()
        pers_area_label = MainPageForm(driver)
        pers_area_label.personal_cabinet_click()
        pers_area_enter = PersonalAreaPage(driver)
        pers_area_enter.personal_area_click_on_restore_link()
        restore_page = PasswordRestorePage(driver)
        assert restore_page.restore_password_get_text() == 'Восстановить'

    @allure.title('Проверка ввода почты и клик по кнопке «Восстановить»')
    @allure.description('На странице восстановления пароля, на которую переходим, проверяем наличие текста'
                        ' в заголовке "Восстановление пароля" ')
    def test_insert_email_check(self, driver):
        page_rest_pass = BasePage(driver)
        page_rest_pass.go_on_page_stellar_burger()
        pers_area_label = MainPageForm(driver)
        pers_area_label.personal_cabinet_click()
        pers_area_enter = PersonalAreaPage(driver)
        pers_area_enter.personal_area_click_on_restore_link()
        restore_page = PasswordRestorePage(driver)
        restore_page.enter_email('abcdefg@nnt.net')
        restore_page.restore_button_click()
        restore_passw = ResetPasswPage(driver)
        assert restore_passw.restore_passw_title_get_text() == 'Восстановление пароля'

    @allure.title('Проверка перевода в активное состояние поля ввода обновлённого пароля'
                  ' по клику на значок показать/скрыть')
    @allure.description('На странице восстановления пароля, на которую переходим, проверяем'
                        ' наличие текста в заголовке "Восстановление пароля" ')
    def test_password_change_visible_check(self, driver):
        page_rest_pass = BasePage(driver)
        page_rest_pass.go_on_page_stellar_burger()
        pers_area_label = MainPageForm(driver)
        pers_area_label.personal_cabinet_click()
        pers_area_enter = PersonalAreaPage(driver)
        pers_area_enter.personal_area_click_on_restore_link()
        restore_page = PasswordRestorePage(driver)
        restore_page.enter_email('abcdefg@nnt.net')
        restore_page.restore_button_click()
        restore_passw = ResetPasswPage(driver)
        restore_passw.restore_passw_input_field('superpasswordnew321')
        restore_passw.visible_element_click()
        assert restore_passw.restore_active_password_field() == True
