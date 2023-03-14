from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pytest

answer = str(math.log(int(time.time())))

link = "https://stepik.org/lesson/236895/step/1"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(7)
    browser.find_element(By.ID, "ember33").click()
    input1 = browser.find_element(By.ID, "id_login_email")
    input1.send_keys("s.logvinenko@quality-lab.ru")
    input2 = browser.find_element(By.ID, "id_login_password")
    input2.send_keys("1q2w3e4r5t6y")
    time.sleep(2)
    browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader").click()
    time.sleep(2)

    #browser.find_element(By.XPATH, "xpath=//div[@id='ember78']/div/section/div/div/div[3]/button[2]").click()
    #browser.find_element(By.XPATH, "xpath=//footer[@id='ember144']/button").click()

    input3 = browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea")
    input3.send_keys(answer)

    browser.find_element(By.XPATH, '//button[text()="Отправить"]').click()

    browser.find_element(By.XPATH, '//p[text()="Correct!"]')




finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла