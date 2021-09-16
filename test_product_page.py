from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import time
import pytest

#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link_for_tree_tests = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?"
promo = [
	"promo=offer0", 
	"promo=offer1", 
	"promo=offer2", 
	"promo=offer3", 
	"promo=offer4", 
	"promo=offer5", 
	"promo=offer6", 
	pytest.param("promo=offer7", marks=pytest.mark.xfail),#"promo=offer7", 
	"promo=offer8", 
	"promo=offer9"
]

#@pytest.mark.skip
@pytest.mark.need_review
@pytest.mark.parametrize('promo_link', promo)
def test_guest_can_add_product_to_basket(browser, promo_link):
#def test_guest_can_add_product_to_basket(browser):
		
	# инициализируем Page Object
	page = ProductPage(browser, link + promo_link)
	#page = ProductPage(browser, link)
	
	# открываем страницу
	page.open()
		
	# Проверяем элементы на странице
	page.should_be_product_page()
	
	# Получаем название книги
	name = page.get_name_book()
	
	# Получаем цену
	price = page.get_price_book()
	
	# Нажимаем на кнопку "Добавить в корзину"
	page.click_add_to_basket()
	
	# Считаем результат математического выражения и вводим ответ.
	page.solve_quiz_and_get_code()

	# проверяем название товара, добавленного в корзину
	page.compare_name_cart_and_basket(name)
	
	# проверяем стоимость корзины 
	page.compare_prise_cart_and_basket(price)
	
	#time.sleep(230)

@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	# инициализируем Page Object
	page = ProductPage(browser, link_for_tree_tests)
	
	# открываем страницу
	page.open()
	
	# Проверяем элементы на странице
	#page.should_be_product_page()
	
	# Нажимаем на кнопку "Добавить в корзину"
	page.click_add_to_basket()
	
	# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
	page.should_not_be_success_message()
	
	#time.sleep(60)

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
	# инициализируем Page Object
	page = ProductPage(browser, link_for_tree_tests)
	
	# открываем страницу
	page.open()
	
	# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
	page.should_not_be_success_message()

@pytest.mark.skip
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
	# инициализируем Page Object
	page = ProductPage(browser, link_for_tree_tests)
	
	# открываем страницу
	page.open()
	
	# Проверяем элементы на странице
	#page.should_be_product_page()
	
	# Нажимаем на кнопку "Добавить в корзину"
	page.click_add_to_basket()
	
	# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
	page.should_disappeared_success_message()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()

#@pytest.mark.skip
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()

#@pytest.mark.skip
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	# Гость открывает страницу товара
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	# Переходит в корзину по кнопке в шапке 
	page.go_to_basket_page()
	# инициализируем страницу корзины
	basket_page = BasketPage(browser, browser.current_url)
	# Ожидаем, что в корзине нет товаров
	basket_page.should_see_empty_basket()
	# Ожидаем, что есть текст о том что корзина пуста 
	basket_page.should_be_text_about_empty()

@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage():
	# предварительное создание пользователей для каждого теста
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		# открыть страницу регистрации
		page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/accounts/login/")
		page.open()
		# зарегистрировать нового пользователя
		page.register_new_user(str(time.time()) + "@fakemail.org", "nzfEdNWSYz2JFwi")
		# проверить, что пользователь залогинен
		page.should_be_authorized_user()	

	def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
		# инициализируем Page Object
		page = ProductPage(browser, link_for_tree_tests)
		
		# открываем страницу
		page.open()
		
		# Проверяем, что нет сообщения об успехе с помощью is_not_element_present
		page.should_not_be_success_message()
	
	@pytest.mark.need_review
	def test_user_can_add_product_to_basket(self, browser):
		# инициализируем Page Object
		page = ProductPage(browser, link)
		
		# открываем страницу
		page.open()
			
		# Проверяем элементы на странице
		page.should_be_product_page()
		
		# Получаем название книги
		name = page.get_name_book()
		
		# Получаем цену
		price = page.get_price_book()
		
		# Нажимаем на кнопку "Добавить в корзину"
		page.click_add_to_basket()
		
		# Считаем результат математического выражения и вводим ответ.
		#page.solve_quiz_and_get_code()

		# проверяем название товара, добавленного в корзину
		page.compare_name_cart_and_basket(name)
		
		# проверяем стоимость корзины 
		page.compare_prise_cart_and_basket(price)
#