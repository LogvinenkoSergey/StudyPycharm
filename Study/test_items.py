import pytest
from selenium.webdriver.common.by import By
import time


class TestShopPage:
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    def test_add_to_basket_button(self, browser):
        browser.implicitly_wait(8)
        browser.get(self.link)
        btn_add_to_basket = browser.find_elements(By.XPATH, '//button[contains(@class,"btn-add-to-basket")]')
        msg = ''
        if len(btn_add_to_basket) == 0:
            msg = 'Button not found'
        if len(btn_add_to_basket) > 1:
            msg = 'Locator is not uniq'
        assert msg is '', msg
