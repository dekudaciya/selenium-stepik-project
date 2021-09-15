import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
	parser.addoption('--browser_name', action='store', default="chrome",
		help="Choose browser: chrome or firefox")
	parser.addoption('--language', action='store', default="en", 
		help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
	browser_name = request.config.getoption("browser_name")
	browser = None
	if browser_name == "chrome":
		print("\nstart chrome browser for test..")
		browser = webdriver.Chrome()
		#browser = webdriver.Chrome(r"D:\chromedriver\chromedriver.exe")
	elif browser_name == "firefox":
		print("\nstart firefox browser for test..")
		#browser = webdriver.Firefox()
		browser = webdriver.Firefox(executable_path = r"D:\geckodriver\geckodriver.exe")
	else:
		raise pytest.UsageError("--browser_name should be chrome or firefox")
	yield browser
	# этот код выполнится после завершения теста
	print("\nquit browser..")
	browser.quit()
#