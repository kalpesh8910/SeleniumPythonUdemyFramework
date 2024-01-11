import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = None


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":

        service_obj = Service("D:\\new\\chromedriver-win64\\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)

    elif browser_name == "firefox":
        service_obj1 = Service("D:\\new\\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj1)

    elif browser_name == "IE":
        print("IE driver")
    driver.get("https://www.filechannels.net/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call, pytest_html=None):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        try:
            driver = item.funcargs['driver']
            extra = getattr(rep, 'extra', [])
            extra.append(pytest_html.extras.url(driver.current_url))
            rep.extra = extra
        except Exception as e:
            print("Exception in pytest_runtest_makereport hook:", e)


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="firefox")
