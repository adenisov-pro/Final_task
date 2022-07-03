from pages.base import WebPage
from pages.elements import WebElement
from settings import URL


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = URL
        super().__init__(web_driver, url)
    element = WebElement(css_selector=
                         'li.b-header-b-personal-e-list-item.have-dropdown.b-header-b-personal-e-list-item_cabinet')

    email = WebElement(css_selector='input.full-input__input.formvalidate-error')

    password = WebElement(css_selector='input[placeholder="Введите свой код скидки"]')


    btn = WebElement(css_selector='input#g-recap-0-btn')

    btn1 = WebElement(css_selector='input[data-default-value="Проверить код и войти"]')


