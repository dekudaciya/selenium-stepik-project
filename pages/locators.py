from selenium.webdriver.common.by import By

class BasePageLocators():
	# ссылка на страницу авторизации
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	# ошибочная ссылка на страницу авторизации
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	# ссылка на корзину из шапки сайта
	HEAD_BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")

class BasketPageLocators():
	# текст о пустоте корзины
	EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
	# строка с товаром
	ROW_OF_ITEM = (By.CSS_SELECTOR, ".basket-items .row")
	

class MainPageLocators():
	#ссылка на страницу авториазции
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	#форма для регистрации
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	#форма для авторизации
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
	# Название книги
	BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
	# Цена книги
	BOOK_PRICE = (By.CSS_SELECTOR, ".product_main  .price_color")
	# Кнопка 'Добавить в корзину'
	BOOK_ADD_TO_BASKET = (By.CSS_SELECTOR, ".product_main .btn-add-to-basket")
	# Название добавленной книги в корзину
	BOOK_NAME_ADD_TO_BASKET = (By.CSS_SELECTOR, "#messages .alert-success:first-child strong")
	# Цена добавленной книги в корзину
	BOOK_PRICE_ADD_TO_BASKET = (By.CSS_SELECTOR, "#messages .alert-info strong")
	# Название добавленной книги в корзину
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:first-child")
#