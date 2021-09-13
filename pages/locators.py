from selenium.webdriver.common.by import By

class MainPageLocators():
	#ссылка на страницу авториазции
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	#форма для регистрации
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
	
	#форма для авторизации
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
#