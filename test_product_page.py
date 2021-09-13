from pages.product_page import ProductPage
import time
import pytest

#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
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

#@pytest.mark.parametrize('promo_link', promo)
@pytest.mark.parametrize('promo_link', promo)
def test_guest_can_add_product_to_basket(browser, promo_link):
		
	# инициализируем Page Object
	page = ProductPage(browser, link + promo_link)
	
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
#