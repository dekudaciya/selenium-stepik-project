class BasePage():
	
	# конструктор стандартной страницы
	def __init__(self, browser, url):
		self.browser = browser
		self.url = url
	
	# открытие страницы
	def open(self):
		self.browser.get(self.url)
#