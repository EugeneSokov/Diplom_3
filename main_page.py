from base_page import BasePage
from locators_stellarburgers import MainPageLocators


class MainPageForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def personal_cabinet_click(self):
        self.find_element_wait(MainPageLocators.PERS_AREA)
        self.find_element_click(MainPageLocators.PERS_AREA)

    def constructor_label_text(self):
        return self.find_element_wait(MainPageLocators.CONSTRUCTOR_LABEL).text

    def order_list_click(self):
        self.find_element_click(MainPageLocators.ORDER_FEED)

    def constructor_button_click(self):
        self.find_element_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    def sauces_click(self):
        self.find_element_wait(MainPageLocators.ELEM_SAUCES)
        self.find_element_click(MainPageLocators.ELEM_SAUCES)

    def toppings_click(self):
        self.find_element_click(MainPageLocators.ELEM_TOPPINGS)

    def sauces_galactic_click(self):
        self.find_element_click(MainPageLocators.ELEM_SAUCE_GALACTIC)

    def title_ingredients_get_text(self):
        return self.find_element_wait(MainPageLocators.TITLE_INGREDIENTS).text

    def title_ingredients_sauces_galactic_get_text(self):
        return self.find_element_wait(MainPageLocators.TITLE_SAUCE_GALACTIC).text

    def topping_biocutlet_click(self):
        self.find_element_wait(MainPageLocators.ELEM_TOPPING_METEORIT)
        self.find_element_click(MainPageLocators.ELEM_TOPPING_METEORIT)

    def close_info_ingredients_click(self):
        self.find_element_wait(MainPageLocators.TITLE_INGREDIENTS)
        self.find_element_click(MainPageLocators.CLOSE_INGREDIENTS_INFO)

    def invisibility_element(self):
        if self.invisibility_of_element(MainPageLocators.TITLE_INGREDIENTS) is not None:
            return True

    def drag_drop_bun(self):
        self.find_element_wait(MainPageLocators.ELEM_BUN_N200)
        self.drag_and_drop_element(MainPageLocators.ELEM_BUN_N200, MainPageLocators.SECTION_FOR_ORDER)

    def drag_drop_cutlet(self):
        self.find_element_wait(MainPageLocators.ELEM_TOPPING_METEORIT)
        self.drag_and_drop_element(MainPageLocators.ELEM_TOPPING_METEORIT, MainPageLocators.SECTION_FOR_ORDER)

    def drag_drop_sauce(self):
        self.find_element_wait(MainPageLocators.ELEM_SAUCE_GALACTIC)
        self.drag_and_drop_element(MainPageLocators.ELEM_SAUCE_GALACTIC, MainPageLocators.SECTION_FOR_ORDER)

    def counter_bun(self):
        return self.find_element_wait(MainPageLocators.COUNTER_OF_BUN).text

    def order_button_click(self):
        self.find_element_wait(MainPageLocators.BUTTON_CREATE_ORDER)
        self.find_element_click(MainPageLocators.BUTTON_CREATE_ORDER)

    def order_info_get_text(self):
        return self.find_element_wait(MainPageLocators.ORDER_MODAL_WINDOW).text

    def order_close_button_click(self):
        self.find_element_wait(MainPageLocators.ORDER_MODAL_WINDOW)
        self.find_element_click(MainPageLocators.BUTTON_CLOSE_ORDER_WINDOW)

    def order_number_get_text(self):
        self.find_element_wait(MainPageLocators.ORDER_MODAL_WINDOW)
        return self.find_element_wait(MainPageLocators.ORDER_MODAL_WIN_NUMBER).text
