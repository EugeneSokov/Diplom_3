import allure
from base_page import BasePage
from main_page import MainPageForm
from personal_area_page import PersonalAreaPage
from order_feed_page import OrderFeedOptions


class TestBasicFunctional:

    @allure.title('Проверка перехода по клику на «Конструктор»')
    @allure.description('После перехода на "Конструктор" проверяем наличие текста "Соберите бургер" на странице')
    def test_constructor_click_check(self, driver):
        page_rest_pass = BasePage(driver)
        page_rest_pass.go_on_page_stellar_burger()
        main_page = MainPageForm(driver)
        main_page.personal_cabinet_click()
        pers_area_page = PersonalAreaPage(driver)
        pers_area_page.personal_area_constructor_click()
        assert main_page.constructor_label_text() == 'Соберите бургер'

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    @allure.description('После перехода на "Конструктор" проверяем наличие текста "Лента заказов" на странице')
    def test_order_feed_click_check(self, driver):
        page_rest_pass = BasePage(driver)
        page_rest_pass.go_on_page_stellar_burger()
        main_page = MainPageForm(driver)
        main_page.order_list_click()
        order_page = OrderFeedOptions(driver)
        assert order_page.order_feed_get_text() == 'Лента заказов'

    @allure.title('Проверка клика на ингредиент с появлением модального окна с информацией об ингредиенте')
    @allure.description('После клика по ингредиенту проверяем наличие текста "Детали ингредиента",'
                        'а также совпадение с ожидаемым названием ингредиента')
    def test_ingredient_information_check(self, driver):
        page_rest_pass = BasePage(driver)
        page_rest_pass.go_on_page_stellar_burger()
        main_page = MainPageForm(driver)
        main_page.sauces_click()
        main_page.sauces_galactic_click()
        assert (main_page.title_ingredients_get_text() == 'Детали ингредиента' and
                main_page.title_ingredients_sauces_galactic_get_text() == 'Соус традиционный галактический')

    @allure.title('Проверка закрытия модального окна с информацией об ингредиенте по клику на крестик')
    @allure.description('После клика на элемент закрытия(крестик) проверяем наличие отсутствие модального окна'
                        ' с заголовком "Детали ингредиента"')
    def test_ingredient_information_close_on_click_check(self, driver):
        page_rest_pass = BasePage(driver)
        page_rest_pass.go_on_page_stellar_burger()
        main_page = MainPageForm(driver)
        main_page.toppings_click()
        main_page.topping_biocutlet_click()
        main_page.close_info_ingredients_click()
        assert main_page.invisibility_element() == True

    @allure.title('Проверка работы счётчика ингредиента, добавленного в заказ')
    @allure.description('После добавления ингредиента(булки) в заказ проверяем, что счётчик ингредиента стал равен "2"')
    def test_ingredient_information_close_on_click_check(self, driver):
        page_rest_pass = BasePage(driver)
        page_rest_pass.go_on_page_stellar_burger()
        main_page = MainPageForm(driver)
        main_page.drag_drop_bun()
        assert main_page.counter_bun() == '2'

    @allure.title('Проверка возможности оформить заказ залогиненному пользователю')
    @allure.description('После нажатия на "Оформить заказ" появляется модальное окно с текстом'
                        ' "Ваш заказ начали готовить"')
    def test_order_creation_by_user_check(self, driver, create_user):
        page_rest_pass = BasePage(driver)
        page_rest_pass.go_on_page_stellar_burger()
        main_page = MainPageForm(driver)
        main_page.personal_cabinet_click()
        personal_area = PersonalAreaPage(driver)
        personal_area.personal_area_login_password('BilboBeggins1@sheer.net', 'qwertyzxcv123')
        personal_area.personal_area_click_on_enter()
        main_page.order_button_click()
        assert main_page.order_info_get_text() == 'Ваш заказ начали готовить'
