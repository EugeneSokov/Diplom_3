from selenium.webdriver.common.by import By


class MainPageLocators:
    PERS_AREA = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")  # Кнопка "Личный кабинет" на главной странице
    CONSTRUCTOR_LABEL = (By.XPATH, "//h1[contains(text(),'Соберите бургер')] ")  # Заголовок "Соберите бургер"
    ORDER_FEED = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")  # Кнопка "Лента заказов"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")  # Кнопка "Конструктор"
    ELEM_SAUCES = (By.XPATH, "//span[contains(text(),'Соусы')]")  # Раздел "Соусы"
    ELEM_SAUCE_GALACTIC = (By.XPATH, "//p[contains(text(),'Соус традиционный галактический')]")  # Элемент "Соус традиционный галактический"
    ELEM_BUN_N200 = (By.XPATH, "//p[contains(text(),'Краторная булка N-200i')]")  # Элемент "Краторная булка N-200i"
    ELEM_TOPPING_METEORIT = (By.XPATH, "//p[contains(text(), 'Говяжий метеорит (отбивная)')]") # Элемент "Говяжий метеорит (отбивная)"
    TITLE_INGREDIENTS = (By.XPATH, "//h2[contains(text(),'Детали ингредиента')]")  #Заголовок "Детали ингредиента"
    TITLE_SAUCE_GALACTIC = (By.XPATH, "//p[@class = 'text text_type_main-medium mb-8']") # Элемент "Галактический соус"
    ELEM_TOPPINGS = (By.XPATH,"//span[contains(text(),'Начинки')]")  # Раздел "Начинки"
    CLOSE_INGREDIENTS_INFO = (By.XPATH, "//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']") # Элемент закрытия информации об ингредиенте (крестик)
    SECTION_FOR_ORDER_OLD = (By.XPATH, "//span[contains(text(),'Перетяните булочку сюда (верх)')]") # Cекция формирования заказа
    SECTION_FOR_ORDER = (By.XPATH, "//div[@class = 'constructor-element constructor-element_pos_top']")
    COUNTER_OF_BUN = (By.CSS_SELECTOR, "div.App_App__aOmNj main.App_componentContainer__2JC2W:nth-child(2) section.BurgerIngredients_ingredients__1N8v2 div.BurgerIngredients_ingredients__menuContainer__Xu3Mo:nth-child(3) ul.BurgerIngredients_ingredients__list__2A-mT:nth-child(2) a.BurgerIngredient_ingredient__1TVf6.ml-4.mr-4.mb-8:nth-child(2) div.counter_counter__ZNLkj.counter_default__28sqi > p.counter_counter__num__3nue1") # Счётчик в элементе булки
    BUTTON_CREATE_ORDER = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")  # Кнопка "Оформить заказ"
    BUTTON_CLOSE_ORDER_WINDOW = (By.XPATH, "//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']") # Кнопка закрытия модального окна заказа
    ORDER_MODAL_WINDOW = (By.XPATH, "//p[contains(text(),'Ваш заказ начали готовить')]")  #  Модальное окно с информацией об оформленном заказе
    ORDER_MODAL_WIN_NUMBER = (By.XPATH, "//h2[@class = 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']") # Номер заказа в модальном окне


class OrderFeedLocators:

    ORDER_FEED_TEXT = (By.XPATH, "//h1[contains(text(),'Лента заказов')]")  # Заголовок "Лента заказов"
    ORDER_HISTORY_FIRST = (By.XPATH, "//li[@class = 'OrderHistory_listItem__2x95r mb-6'][1]") # Первый элемент в списке ленты заказов
    MODAL_WINDOW_ORDER = (By.XPATH, "//div[@class = 'Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10']") # Модальное окно с информацией о заказе
    COMPLETED_FOR_ALL_TIME_COUNT = (By.CSS_SELECTOR, "div.App_App__aOmNj main.App_componentContainer__2JC2W:nth-child(2) div.OrderFeed_orderFeed__2RO_j div.OrderFeed_contentBox__3-tWb div.OrderFeed_ordersData__1L6Iv div.undefined.mb-15:nth-child(2) > p.OrderFeed_number__2MbrQ.text.text_type_digits-large") # Счётчик "Выполнено за всё время"
    COMPLETED_FOR_TODAY_COUNT = (By.CSS_SELECTOR, "div.App_App__aOmNj main.App_componentContainer__2JC2W:nth-child(2) div.OrderFeed_orderFeed__2RO_j div.OrderFeed_contentBox__3-tWb div.OrderFeed_ordersData__1L6Iv div:nth-child(3) > p.OrderFeed_number__2MbrQ.text.text_type_digits-large") # Счётчик "Выполнено за сегодня"
    IN_WORK_COUNT = (By.XPATH, "//ul[@class = 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']") # Счётчик "В работе"
    ORDER_LIST_LAST_ELEM = (By.XPATH, "//ul[@class = 'OrderFeed_list__OLh59']/li[1]")  # Последний заказ в списке заказов


class PersonalAreaLocators:

    RESTORE_PASSW = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]") # Текстровая ссылка на страницу "Восстановить пароль"
    EMAIL_AUTHOR = (By.XPATH, "//input[@type = 'text']")  # Поле ввода email на странице авторизации
    PASS_AUTHOR = (By.XPATH, "//input[@type = 'password']")  # Поле ввода пароля на странице авторизации
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]") # Кнопка "Войти"
    PROFILE_LABEL = (By.XPATH, "//a[contains(text(),'Профиль')]") # Ссылка на "Профиль"
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")  # Кнопка "Выход"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")  # Кнопка "Конструктор"
    ORDER_HISTORY_LABEL = (By.XPATH, "//a[contains(text(),'История заказов')]")  # Ссылка на "Историю заказов"
    ORDER_HISTORY_LIST = (By.XPATH, "//div[@class = 'OrderHistory_orderHistory__qy1VB']")  # Список в истории заказов
    ORDER_HISTORY_LAST_ELEM = (By.XPATH, "//ul[@class = 'OrderHistory_profileList__374GU OrderHistory_list__KcLDB']/li[last()]")  # Элемент последнего заказа


class ForgotPasswordLocators:

    RESTORE_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")  #  Кнопка "Восстановить" для восстановления пароля
    EMAIL_FIELD = (By.XPATH, "//input[@class = 'text input__textfield text_type_main-default']") #  Поле ввода email



