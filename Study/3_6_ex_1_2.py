from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import pytest

answer = str(math.log(int(time.time())))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('lexus', ["236895"])
    #, "236896", "236897", "236898","236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, lexus):
    link = f"https://stepik.org/lesson/{lexus}/step/1"
    browser.get(link)
    browser.implicitly_wait(35)
    browser.find_element(By.ID, "ember33").click()
    input1 = browser.find_element(By.ID, "id_login_email")
    input1.send_keys("s.logvinenko@quality-lab.ru")
    input2 = browser.find_element(By.ID, "id_login_password")
    input2.send_keys("1q2w3e4r5t6y")
    browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader").click()

    input3 = browser.find_element(By.XPATH, '/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[1]/div[2]/div/div/div/textarea')
    input3.send_keys(answer)

    #input3 = browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea")
    #input3.send_keys(answer)

    browser.find_element(By.XPATH, '//button[text()="Отправить"]').click()

    time.sleep(10)
    browser.find_element(By.XPATH, '//p[text()="Correct!"]')