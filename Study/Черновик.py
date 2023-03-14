from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.common.exceptions import NoAlertPresentException

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def calc(x):
    return str(math.log(abs((12 * math.sin(float(x))))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    button1.click()

    alert = x.browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")






finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла