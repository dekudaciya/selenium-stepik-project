from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

class BasePage():
	
	# конструктор стандартной страницы
	def __init__(self, browser, url, timeout=10):
		self.browser = browser
		self.url = url
		#self.browser.implicitly_wait(timeout)
	
	# получение значения элемента
	def get_value_element(self, how, what):
		try:
			elm = self.browser.find_element(how, what)
		except (NoSuchElementException):
			return None
		return elm.text
	
	# переход на страницу корзины
	def go_to_basket_page(self):
		link = self.browser.find_element(*BasePageLocators.HEAD_BASKET_LINK)
		link.click()
	
	# переход на страницу авторизации
	def go_to_login_page(self):
		link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
		link.click()
	
	# ожидание исчезания элемента
	def is_disappeared(self, how, what, timeout=4):
		try:
			WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return False
		return True
	
	# поиск элемента на странице
	def is_element_present(self, how, what):
		try:
			self.browser.find_element(how, what)
		except (NoSuchElementException):
			return False
		return True

	# поиск элемента, что он не появится в течении заданного времени
	def is_not_element_present(self, how, what, timeout=4):
		try:
			WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return True
		return False
	
	# открытие страницы
	def open(self):
		self.browser.get(self.url)
	
	# проверка ссылки на страницу авторизации
	def should_be_login_link(self):
		assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
	
	def solve_quiz_and_get_code(self):
		alert = self.browser.switch_to.alert
		x = alert.text.split(" ")[2]
		answer = str(math.log(abs((12 * math.sin(float(x))))))
		alert.send_keys(answer)
		alert.accept()
		try:
			alert = self.browser.switch_to.alert
			alert_text = alert.text
			print(f"Your code: {alert_text}")
			alert.accept()
		except NoAlertPresentException:
			print("No second alert presented")
#