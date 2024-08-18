import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager as cd
from webdriver_manager.firefox import GeckoDriverManager as fd
from selenium.webdriver.chrome.service import Service as cs
from selenium.webdriver.firefox.service import Service as fs
from pages.login_page import LoginPage


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        options = webdriver.FirefoxOptions()
        service = fs(executable_path=fd().install())
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox(service=service, options=options)
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
        service = cs(executable_path=cd().install())
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def log_in(driver):
    LoginPage(driver).login()
