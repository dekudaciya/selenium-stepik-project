# selenium-stepik-project
Тестовый проект для финального задания

pytest -v --tb=line --language=en test_main_page.py

pytest -v --tb=line -m login_guest --language=en test_main_page.py

pytest -s test_product_page.py

pytest -v --tb=line -m "user_add_to_basket" test_product_page.py

Без pytest.ini запускать следующей строкой
pytest -v --tb=line test_product_page.py -m user_add_to_basket --disable-warnings
