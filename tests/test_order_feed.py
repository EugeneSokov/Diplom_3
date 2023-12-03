import allure
from base_page import BasePage
from main_page import MainPageForm
from personal_area_page import PersonalAreaPage
from order_feed_page import OrderFeedOptions


class TestOrderFeed:

    @allure.title('Проверка открытия модального окна с деталями заказа')
    @allure.description('После нажатия на последний заказ (первый в списке) появляется модальное'
                        ' окно с деталями заказа, наличие которого проверяется')
    def test_modal_window_of_order_info_is_opened(self, driver):
        page_rest_pass = BasePage(driver)
        page_rest_pass.go_on_page_stellar_burger()
        main_page = MainPageForm(driver)
        main_page.order_list_click()
        order_page = OrderFeedOptions(driver)
        order_page.order_feed_first_elem_click()
        assert order_page.modal_window_info_of_order_exist() == True

    @allure.title('Проверка увеличения счётчика "Выполнено за всё время" после создания заказа')
    @allure.description('После нажатия на "Оформить заказ" сравниваем предыдущее число счётчика'
                        ' "Выполнено за всё время" с обновлённым после заказа. Разность будет = 1')
    def test_order_counter_for_all_time_check(self, driver):
        page_rest_pass = BasePage(driver)
        page_rest_pass.go_on_page_stellar_burger()
        main_page = MainPageForm(driver)
        main_page.personal_cabinet_click()
        personal_area = PersonalAreaPage(driver)
        personal_area.personal_area_login_password('cynthia18@example.org', 'qwerty123456')
        personal_area.personal_area_click_on_enter()
        main_page.order_list_click()
        order_page = OrderFeedOptions(driver)
        counter_before = int(order_page.created_for_all_time_counter_get_text())
        main_page.constructor_button_click()
        main_page.drag_drop_bun()
        main_page.order_button_click()
        main_page.order_close_button_click()
        main_page.order_list_click()
        counter_after = int(order_page.created_for_all_time_counter_get_text())
        numb_diff = counter_after - counter_before
        assert numb_diff == 1

    @allure.title('Проверка увеличения счётчика "Выполнено за сегодня" после создания заказа')
    @allure.description('После нажатия на "Оформить заказ" сравниваем предыдущее число счётчика'
                        ' "Выполнено за сегодня" с обновлённым после заказа. Разность будет = 1')
    def test_order_counter_for_today_check(self, driver):
        page_rest_pass = BasePage(driver)
        page_rest_pass.go_on_page_stellar_burger()
        main_page = MainPageForm(driver)
        main_page.personal_cabinet_click()
        personal_area = PersonalAreaPage(driver)
        personal_area.personal_area_login_password('cynthia18@example.org', 'qwerty123456')
        personal_area.personal_area_click_on_enter()
        main_page.order_list_click()
        order_page = OrderFeedOptions(driver)
        counter_before = int(order_page.created_for_today_counter_get_text())
        main_page.constructor_button_click()
        main_page.drag_drop_bun()
        main_page.sauces_click()
        main_page.drag_drop_sauce()
        main_page.toppings_click()
        main_page.drag_drop_cutlet()
        main_page.order_button_click()
        main_page.order_close_button_click()
        main_page.order_list_click()
        counter_after = int(order_page.created_for_today_counter_get_text())
        numb_diff = counter_after - counter_before
        assert numb_diff == 1

    @allure.title('Проверка появления номера заказа в разделе "В работе"')
    @allure.description('После нажатия на "Оформить заказ" сравнивапроверяем,'
                        ' что офрмленный заказ появился в разделе "В работе"')
    def test_order_counter_in_work_check(self, driver):
        page_rest_pass = BasePage(driver)
        page_rest_pass.go_on_page_stellar_burger()
        main_page = MainPageForm(driver)
        main_page.personal_cabinet_click()
        personal_area = PersonalAreaPage(driver)
        personal_area.personal_area_login_password('cynthia18@example.org', 'qwerty123456')
        personal_area.personal_area_click_on_enter()
        main_page.order_list_click()
        main_page.constructor_button_click()
        main_page.drag_drop_bun()
        main_page.sauces_click()
        main_page.drag_drop_sauce()
        main_page.toppings_click()
        main_page.drag_drop_cutlet()
        main_page.order_button_click()
        number_window = int(main_page.order_number_get_text())
        main_page.order_close_button_click()
        main_page.order_list_click()
        order_page = OrderFeedOptions(driver)
        number_in_work = int(order_page.number_in_work_count_get_text())
        assert number_window == number_in_work

    @allure.title('Проверка отображения на странице «Лента заказов» заказов из "История заказов"')
    @allure.description('После нажатия на "Оформить заказ" сравнивапроверяем, что оформленный заказ появился в разделе "В работе"')
    def test_history_order_list_orders_check(self, driver, create_user):
        page_rest_pass = BasePage(driver)
        page_rest_pass.go_on_page_stellar_burger()
        main_page = MainPageForm(driver)
        main_page.personal_cabinet_click()
        personal_area = PersonalAreaPage(driver)
        personal_area.personal_area_login_password('BilboBeggins1@sheer.net', 'qwertyzxcv123')
        personal_area.personal_area_click_on_enter()
        main_page.order_list_click()
        main_page.constructor_button_click()
        main_page.drag_drop_bun()
        main_page.sauces_click()
        main_page.drag_drop_sauce()
        main_page.toppings_click()
        main_page.drag_drop_cutlet()
        main_page.order_button_click()
        main_page.order_close_button_click()
        main_page.personal_cabinet_click()
        personal_area.personal_area_order_history_click()
        text_history = personal_area.last_order_number_get_text()
        text_history_cut = text_history.replace('Выполнен\n', '')
        main_page.order_list_click()
        order_page = OrderFeedOptions(driver)
        text_order_list = order_page.order_last_elem_get_text()
        assert text_history_cut == text_order_list
