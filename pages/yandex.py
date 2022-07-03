#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://market.yandex.ru/'

        super().__init__(web_driver, url)

    # Main search field Основное поле поиска
    search = WebElement(id='header-search')

    # Search button Кнопка поиска
    search_run_button = WebElement(xpath='//button[@type="submit"]')

    # Titles of the products in search results Названия товаров в результатах поиска
    products_titles = ManyWebElements(xpath='//a[contains(@href, "/product-") and @title!=""]')

    # Button to sort products by price Кнопка для сортировки товаров по цене
    sort_products_by_price = WebElement(css_selector='button[data-autotest-id="dprice"]')

    # Prices of the products in search resultsь  Цены на товары в результатах поиска
    products_prices = ManyWebElements(xpath='//div[@data-zone-name="price"]//span/*[1]')
