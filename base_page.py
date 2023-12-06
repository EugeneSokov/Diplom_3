import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://stellarburgers.nomoreparties.site/'

    @allure.step('Открываем страницу StellarBurgers')
    def go_on_page_stellar_burgers(self):
        return self.driver.get(self.base_url)

    @allure.step('Поиск элемента на странице с задержкой=14')
    def find_element_wait(self, locator, time=14):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator),
                                                      message=f'Not found{locator}')

    @allure.step('Поиск элемента на странице и клик по нему')
    def find_element_click(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Скроллинг до элемента на странице')
    def scrolling_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Отсутствие элемента на странице')
    def invisibility_of_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.invisibility_of_element(locator),
                                                      message=f'Not found{locator}')

    @allure.step('Перемещение элемента методом drag and drop')
    def drag_and_drop_element(self, locator1, locator2):
        element = self.driver.find_element(*locator1)
        target = self.driver.find_element(*locator2)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, target).perform()
