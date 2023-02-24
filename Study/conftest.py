import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # задаем опцию браузера при запуске, дефолтный хром
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: firefox or chrome")
    # задаем опцию языка при запуске: ru, fr и тд.
    parser.addoption('--language', action='store', default=None, help="Say language name to select")



@pytest.fixture(scope="function")
def browser(request):
    # проверяем какой язык и браузер (если есть)
    choosen_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        # мутим chrome с нужными параметрами
        opts = Options()
        opts.add_experimental_option('prefs', {'intl.accept_languages': choosen_language})
        opts.add_experimental_option('w3c', False)
        browser = webdriver.Chrome(options=opts)
    elif browser_name == "firefox":
        # мутим мозилу фаерфокс с нужными параметрами
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", choosen_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    yield browser
    # закрытие браузера после работы
    browser.quit()