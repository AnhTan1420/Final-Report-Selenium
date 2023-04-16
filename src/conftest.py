import time

import pytest
from selenium import webdriver

# browser = "chrome"
from src import settings
from src.pages.base_page import BasePage
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage
from src.pages.register_page import RegisterPage
from src.utility import xlReader

driver = None


def pytest_addoption(parser):
    # parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--browser", action="store", default=settings.browser)
    parser.addoption("--env", action="store", default=settings.env)


@pytest.fixture
def getBrowser(request):
    _browser = request.config.getoption("--browser")
    return _browser


@pytest.fixture
def getDriver(request, getBrowser):
    global driver
    print("browser from getBrowser method - " + getBrowser)
    if getBrowser == "chrome":
        driver = webdriver.Chrome(executable_path="./Report-Final/webdriver/chromdriver")
    elif getBrowser == "firefox":
        driver = webdriver.Firefox(executable_path="./Report-Final/webdriver/chromdriver")
    # env = request.config.getoption("--env")
    # _driver.get("https://www." + env + ".saucedemo.com/index.html")
    xlReader.load_excel()
    url = xlReader.get_cell_data(7, 3)
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    # request.cls.basePage = BasePage(driver)
    request.cls.loginPage = LoginPage(driver)
    request.cls.homePage = HomePage(driver)
    request.cls.registerPage = RegisterPage(driver)
    # request.cls.driver = _driver
    # yield request.cls.driver
    yield driver
    time.sleep(2)
    driver.quit()


