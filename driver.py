from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException

def ie(opts):
	return webdriver.Ie(options=opts)


def opera(opts):
	return webdriver.Opera(options=opts)

def chrome(opts):
	return webdriver.Chrome(options=opts)

def firefox(opts):
	return webdriver.Firefox(options=opts)

def start_driver():
	options = Options()
	options.headless = True

	funcs = [firefox, chrome, opera, ie]

	for func in funcs:
		try:
			driver = func(options)
			return driver
		except WebDriverException:
			pass

   # If function is here it means that no driver was sucessfully initiated
	raise WebDriverException("No web driver found")