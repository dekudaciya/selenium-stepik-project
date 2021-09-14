﻿from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
		
	# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
	page = MainPage(browser, link)
	
	# открываем страницу
	page.open()
	
	# выполняем метод страницы — переходим на страницу логина
	#login_page = page.go_to_login_page()
	#проверяем страницу авторизации
	#login_page.should_be_login_page()
	
	page.go_to_login_page()
	
	login_page = LoginPage(browser, browser.current_url)
	login_page.should_be_login_page()

@pytest.mark.skip
def test_guest_should_see_login_link(browser):
		
	page = MainPage(browser, link)
	
	page.open()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
	
	# инициализируем главную страницу
	page = MainPage(browser, link)
	
	# Гость открывает главную страницу 
	page.open()
	
	# Переходит в корзину по кнопке в шапке сайта
	page.go_to_basket_page()
	
	# инициализируем страницу корзины
	basket_page = BasketPage(browser, browser.current_url)
	
	# Ожидаем, что в корзине нет товаров
	assert basket_page.get_count_books_of_basket() == 0, "There is an item in the basket"
	
	# Ожидаем, что есть текст о том что корзина пуста 
	basket_page.should_be_text_about_empty()
#