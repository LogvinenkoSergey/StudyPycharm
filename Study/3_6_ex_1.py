from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

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
    browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader").click()
    time.sleep(2)



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла