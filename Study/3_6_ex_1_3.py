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


@pytest.mark.parametrize('lexus', ["236895", "236896", "236897", "236898","236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, lexus):
    link = f"https://stepik.org/lesson/{lexus}/step/1"
    browser.get(link)
    browser.implicitly_wait(45)
    browser.find_element(By.ID, "ember33").click()
    input1 = browser.find_element(By.ID, "id_login_email")
    input1.send_keys("s.logvinenko@quality-lab.ru")
    input2 = browser.find_element(By.ID, "id_login_password")
    input2.send_keys("1q2w3e4r5t6y")
    time.sleep(15)
    browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader").click()

    #input3 = browser.find_element(By.XPATH, '/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[1]/div[2]/div/div/div/textarea')
    #input3.send_keys(answer)

    browser.find_element(By.XPATH, '/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div/article/div/div/div[2]/div/section/div/div[1]/div[2]/div/div/div/textarea').send_keys(answer)



    browser.find_element(By.XPATH, '//button[text()="Отправить"]').click()

    time.sleep(5)
    #browser.find_element(By.XPATH, '//p[text()="Correct!"]')
        # Найти появившееся поле с текстом и сравнить тест на значение
    correct_text_elt = browser.find_element_by_class_name('smart-hints__hint')
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    correct_text = correct_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert correct_text == "Correct!", "Текст:'{}' не совпадает у текстом успешного выполненного задания".format(
        correct_text)