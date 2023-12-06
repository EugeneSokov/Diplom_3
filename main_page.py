import allure
from base_page import BasePage
from locators_stellarburgers import MainPageLocators


class MainPageForm(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем страницу Stellar Burgers')
    def go_on_stellar_burgers_page(self):
        self.go_on_page_stellar_burgers()

    @allure.step('Нажатие на кнопку "Личный кабинет" в заголовке')
    def personal_cabinet_click(self):
        self.find_element_wait(MainPageLocators.PERS_AREA)
        self.find_element_click(MainPageLocators.PERS_AREA)

    @allure.step('Получение текста заголовка "Соберите бургер"')
    def constructor_label_text(self):
        return self.find_element_wait(MainPageLocators.CONSTRUCTOR_LABEL).text

    @allure.step('Нажатие на кнопку "Лента заказов" в заголовке')
    def order_list_click(self):
        self.find_element_click(MainPageLocators.ORDER_FEED)

    @allure.step('Нажатие на кнопку конструктора "Конструктор" в заголовке')
    def constructor_button_click(self):
        self.find_element_click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Нажатие на кнопку конструктора "Соусы"')
    def sauces_click(self):
        self.find_element_wait(MainPageLocators.ELEM_SAUCES)
        self.find_element_click(MainPageLocators.ELEM_SAUCES)

    @allure.step('Нажатие на кнопку конструктора "Начинки"')
    def toppings_click(self):
        self.find_element_click(MainPageLocators.ELEM_TOPPINGS)

    @allure.step('Выбор элемента "Соус традиционный галактический" в разделе "Соусы"')
    def sauces_galactic_click(self):
        self.find_element_click(MainPageLocators.ELEM_SAUCE_GALACTIC)

    @allure.step('Получение текста заголовка "Детали ингредиента"')
    def title_ingredients_get_text(self):
        return self.find_element_wait(MainPageLocators.TITLE_INGREDIENTS).text

    @allure.step('Получение текста элемента "Соус традиционный галактический"')
    def title_ingredients_sauces_galactic_get_text(self):
        return self.find_element_wait(MainPageLocators.TITLE_SAUCE_GALACTIC).text

    @allure.step('Выбор элемента "Говяжий метеорит (отбивная)" в разделе "Начинки"')
    def topping_biocutlet_click(self):
        self.find_element_wait(MainPageLocators.ELEM_TOPPING_METEORIT)
        self.find_element_click(MainPageLocators.ELEM_TOPPING_METEORIT)

    @allure.step('Нажатие на крестик(закрытие) информации об ингредиенте')
    def close_info_ingredients_click(self):
        self.find_element_wait(MainPageLocators.TITLE_INGREDIENTS)
        self.find_element_click(MainPageLocators.CLOSE_INGREDIENTS_INFO)

    @allure.step('Проверка того, что после закрытия окна с информаций об ингредиенте,окно пропадает со страницы')
    def invisibility_element_check(self):
        if self.invisibility_of_element(MainPageLocators.TITLE_INGREDIENTS) is not None:
            return True

    @allure.step('Перетаскивание элемента из раздела "Булки" в поле для заказа')
    def drag_drop_bun(self):
        self.find_element_wait(MainPageLocators.ELEM_BUN_N200)
        self.drag_and_drop_element(MainPageLocators.ELEM_BUN_N200, MainPageLocators.SECTION_FOR_ORDER)

    @allure.step('Перетаскивание элемента из раздела "Начинки" в поле для заказа')
    def drag_drop_cutlet(self):
        self.find_element_wait(MainPageLocators.ELEM_TOPPING_METEORIT)
        self.drag_and_drop_element(MainPageLocators.ELEM_TOPPING_METEORIT, MainPageLocators.SECTION_FOR_ORDER)

    @allure.step('Перетаскивание элемента из раздела "Соусы" в поле для заказа')
    def drag_drop_sauce(self):
        self.find_element_wait(MainPageLocators.ELEM_SAUCE_GALACTIC)
        self.drag_and_drop_element(MainPageLocators.ELEM_SAUCE_GALACTIC, MainPageLocators.SECTION_FOR_ORDER)

    @allure.step('Получение счётчика элемента из раздела "Булки"')
    def counter_bun(self):
        return self.find_element_wait(MainPageLocators.COUNTER_OF_BUN).text

    @allure.step('Нажатие на кнопку "Оформить заказ"')
    def order_button_click(self):
        self.find_element_wait(MainPageLocators.BUTTON_CREATE_ORDER)
        self.find_element_click(MainPageLocators.BUTTON_CREATE_ORDER)

    @allure.step('Получение текста из открывшегося модального окна с деталями заказа')
    def order_info_get_text(self):
        return self.find_element_wait(MainPageLocators.ORDER_MODAL_WINDOW).text

    @allure.step('Нажатие на кнопку закрытия (крестик) модального окна с деталями заказа')
    def order_close_button_click(self):
        self.find_element_wait(MainPageLocators.ORDER_MODAL_WINDOW)
        self.find_element_click(MainPageLocators.BUTTON_CLOSE_ORDER_WINDOW)

    @allure.step('Получение текста номера оформленного заказа в модальном окне с деталями заказа')
    def order_number_get_text(self):
        self.find_element_wait(MainPageLocators.ORDER_MODAL_WINDOW)
        return self.find_element_wait(MainPageLocators.ORDER_MODAL_WIN_NUMBER).text
