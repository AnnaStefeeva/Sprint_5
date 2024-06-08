from selenium.webdriver.common.by import By

# Таб "Булки"
BUN_TAB = (By.XPATH, ".//div[span[text()='Булки']]")
# Таб "Соусы"
SOUCES_TAB = (By.XPATH, ".//div[span[text()='Соусы']]")
# Таб "Начинки"
FILLINGS_TAB = (By.XPATH, ".//div[span[text()='Начинки']]")
# Ссылка "Личный Кабинет"
ACCOUNT_LINK = (By.XPATH, ".//a[@href='/account']")
# Кнопка "Войти в аккаунт"
ACCOUNT_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]')
# Ссылка "Зарегистрироваться"
REGISTER_LINK = (By.XPATH, ".//a[@href='/register']")
# Поле ввода "Имя"
INPUT_NAME = (By.XPATH, "//input[../label='Имя']")
# Поле ввода "Email"
INPUT_EMAIL = (By.XPATH, "//input[../label='Email']")
# Поле ввода "Пароль"
INPUT_PASSWORD = (By.XPATH, "//input[../label='Пароль']")
# Кнопка "Зарегистрироваться"
REGISTER_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]')
# Кнопка "Войти"
ENTER_BUTTON = (By.XPATH, './/button[text()="Войти"]')
# Ссылка "Восстановить пароль"
RESTORE_PASSWORD_LINK = (By.XPATH, ".//a[@href='/forgot-password']")
# Ссылка "Войти" на странице восстановления пароля
LOGIN_LINK = (By.XPATH, ".//a[@href='/login']")
# Кнопка "Оформить заказ"
MAKE_ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')
# Ссылка "Конструктор" в верхней части страницы
CONSTRUCTOR_TITLE = (By.XPATH, ".//p[text()='Конструктор']")
# Заголовок "Соберите бургер" на главной странице
MAKE_BURGER_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']")
# Главный логотип
MAIN_LOGO = (By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]")
# Ссылка "Личный кабинет" на главной странице
ACCOUNT_TITLE = (By.XPATH, ".//p[text()='Личный Кабинет']")
# Кнопка "Выход" в личном кабинете
EXIT_BUTTON = (By.XPATH, './/button[text()="Выход"]')
# Сообщение об ошибке в форме
INPUT_ERROR_TEXT = (By.XPATH, './/p[@class="input__error text_type_main-default"]')
