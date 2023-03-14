from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    def test_abs1():
        assert abs(-42) == 42, "Should be absolute value of a number"

    def test_abs2():
        assert abs(-42) == -42, "Should be absolute value of a number"


finally:
    # успеваем скопировать код за 1 секунд
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    #browser.quit()

# не забываем оставить пустую строку в конце файла