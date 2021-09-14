from selenium.webdriver.common.by import By

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

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