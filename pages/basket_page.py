from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
	
	# проверка элементов на странице
	def should_be_product_page(self):
		pass
		
	# получить количество книг в корзине
	def get_count_books_of_basket(self):
		try:
			elm = self.browser.find_elements(*BasketPageLocators.ROW_OF_ITEM)
		except (NoSuchElementException):
			return 0
		return len(elm)
	
	def should_be_not_text_about_empty(self):
		assert self.is_not_element_present(*BasketPageLocators.EMPTY_TEXT), "Text of empty basket is presented"
	
	# проверка показа текста, что корзина пуста
	def should_be_text_about_empty(self):
		assert self.is_element_present(*BasketPageLocators.EMPTY_TEXT), "Text of empty basket is not presented"	
#