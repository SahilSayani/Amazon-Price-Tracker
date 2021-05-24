from selenium import webdriver

DIRECTORY = 'reports'
NAME = input("Enter product")
CURRENCY = input("Enter currency")
MIN_PRICE = input("Enter minimum price")
MAX_PRICE = input("Enter maximum price")
FILTERS = {
    'min': MIN_PRICE,
    'max': MAX_PRICE
}
BASE_URL = "http://www.amazon.in/"


def get_chrome_web_driver(options):
    return webdriver.Chrome("C:/Users/Apeksha/AppData/Local/Temp/Temp1_chromedriver_win32.zip/chromedriver.exe", chrome_options=options)


def get_web_driver_options():
    return webdriver.ChromeOptions()


def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')


def set_browser_as_incognito(options):
    options.add_argument('--incognito')


def set_automation_as_head_less(options):
    options.add_argument('--headless')