from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
	
	# проверка элементов на странице
	def should_be_product_page(self):
		self.should_be_book_name()
		self.should_be_price_name()
		self.should_be_button_to_basket()
		self.should_not_be_success_message()
	
	# проверка названия книги
	def should_be_book_name(self):
		assert self.is_element_present(*ProductPageLocators.BOOK_NAME), "Book's name is not presented"
	
	# проверка цены книги
	def should_be_price_name(self):
		assert self.is_element_present(*ProductPageLocators.BOOK_PRICE), "Book's price is not presented"
		
	# проверка кнопки 'Добавить в корзину'
	def should_be_button_to_basket(self):
		assert self.is_element_present(*ProductPageLocators.BOOK_ADD_TO_BASKET), "Book's button 'Add to basket' is not presented"

	# получение имя книги	
	def get_name_book(self):
		return self.get_value_element(*ProductPageLocators.BOOK_NAME)
	
	# получение цены книги
	def get_price_book(self):
		return self.get_value_element(*ProductPageLocators.BOOK_PRICE)
	
	# добавление товара в корзину
	def click_add_to_basket(self):
		button = self.browser.find_element(*ProductPageLocators.BOOK_ADD_TO_BASKET)
		button.click()

	# сравнение имени добавленной книги и товара
	def compare_name_cart_and_basket(self, name):
		assert self.get_value_element(*ProductPageLocators.BOOK_NAME_ADD_TO_BASKET) == name, "Book's name in cart differs with book's name in basket"
		
	# сравнение цены добавленной книги и товара
	def compare_prise_cart_and_basket(self, price):
		assert self.get_value_element(*ProductPageLocators.BOOK_PRICE_ADD_TO_BASKET) == price, "Book's prose in cart differs with book's prise in basket"
	
	# проверка, что сообщения об успехе нет
	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

	# проверка, что сообщения исчезает после появления
	def should_disappeared_success_message(self):
		assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but should to disappeared"
#