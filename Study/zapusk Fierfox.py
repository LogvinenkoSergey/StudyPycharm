from selenium import webdriver

from selenium.webdriver.common.by import By


# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Firefox(executable_path=r'C:\geckodriverz\geckodriver.exe')

driver.get("https://stepik.org/lesson/25969/step/8")
