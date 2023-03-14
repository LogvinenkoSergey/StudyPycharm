
import time
import pytest
@pytest.mark.need_review
def test_user_can_add_product_to_basket(self, browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    book_name = page.get_book_name()
    book_price = page.get_book_price()
    page.compare_books_name_in_basket_and_in_cataloge(book_name)
    page.compare_price_in_basket_and_in_cataloge(book_price)
    time.sleep(2)