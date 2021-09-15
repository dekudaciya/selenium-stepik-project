from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
	def register_new_user(self, email, password):
		# заполняем поле email
		input1 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
		input1.send_keys(email)
		# заполняем поле пароль
		input2 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
		input2.send_keys(password)
		# заполняем поле повтор пароля
		input3 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD2)
		input3.send_keys(password)
		# Отправляем заполненную форму
		button = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_BUTTON)
		button.click()
	
	def should_be_login_page(self):
		self.should_be_login_url()
		self.should_be_login_form()
		self.should_be_register_form()

	def should_be_login_url(self):
		# проверку на корректный url адрес
		assert "login" in self.browser.current_url, "'login' not contains in URL-page"
	
	def should_be_login_form(self):
		# проверка, что есть форма логина
		assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
	
	def should_be_register_form(self):
		# проверка, что есть форма регистрации на странице
		assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
#