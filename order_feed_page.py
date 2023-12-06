import allure
from base_page import BasePage
from locators_stellarburgers import OrderFeedLocators


class OrderFeedOptions(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Получение текста заголовка "Лента заказов"')
    def order_feed_get_text(self):
        return self.find_element_wait(OrderFeedLocators.ORDER_FEED_TEXT).text

    @allure.step('Нажатие на первый элемент из списка "Ленты заказов"')
    def order_feed_first_elem_click(self):
        self.find_element_wait(OrderFeedLocators.ORDER_HISTORY_FIRST)
        self.find_element_click(OrderFeedLocators.ORDER_HISTORY_FIRST)

    @allure.step('Проверка появления модального окна с деталями заказа')
    def modal_window_info_of_order_exist(self):
        self.find_element_wait(OrderFeedLocators.MODAL_WINDOW_ORDER)
        if self.find_element_wait(OrderFeedLocators.MODAL_WINDOW_ORDER) is not None:
            return True

    @allure.step('Получение текста счётчика количества заказов за всё время')
    def created_for_all_time_counter_get_text(self):
        return self.find_element_wait(OrderFeedLocators.COMPLETED_FOR_ALL_TIME_COUNT).text

    @allure.step('Получение текста счётчика количества заказов за сегодня')
    def created_for_today_counter_get_text(self):
        return self.find_element_wait(OrderFeedLocators.COMPLETED_FOR_TODAY_COUNT).text

    @allure.step('Получение номера/номеров заказа/заказов, находящихся "В работе"')
    def number_in_work_count_get_text(self):
        return self.find_element_wait(OrderFeedLocators.IN_WORK_COUNT).text

    @allure.step('Получение текста из поля последнего сделанного заказа в "Ленте заказов"')
    def order_last_elem_get_text(self):
        self.find_element_wait(OrderFeedLocators.ORDER_FEED_TEXT)
        return self.find_element_wait(OrderFeedLocators.ORDER_HISTORY_FIRST).text
