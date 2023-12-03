from base_page import BasePage
from locators_stellarburgers import OrderFeedLocators


class OrderFeedOptions(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def order_feed_get_text(self):
        return self.find_element_wait(OrderFeedLocators.ORDER_FEED_TEXT).text

    def order_feed_first_elem_click(self):
        self.find_element_wait(OrderFeedLocators.ORDER_HISTORY_FIRST)
        self.find_element_click(OrderFeedLocators.ORDER_HISTORY_FIRST)

    def modal_window_info_of_order_exist(self):
        self.find_element_wait(OrderFeedLocators.MODAL_WINDOW_ORDER)
        if self.find_element_wait(OrderFeedLocators.MODAL_WINDOW_ORDER) is not None:
            return True

    def created_for_all_time_counter_get_text(self):
        return self.find_element_wait(OrderFeedLocators.COMPLETED_FOR_ALL_TIME_COUNT).text

    def created_for_today_counter_get_text(self):
        return self.find_element_wait(OrderFeedLocators.COMPLETED_FOR_TODAY_COUNT).text

    def number_in_work_count_get_text(self):
        return self.find_element_wait(OrderFeedLocators.IN_WORK_COUNT).text

    def order_last_elem_get_text(self):
        self.find_element_wait(OrderFeedLocators.ORDER_FEED_TEXT)
        return self.find_element_wait(OrderFeedLocators.ORDER_HISTORY_FIRST).text
