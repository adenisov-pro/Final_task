import time
from settings import URL


def test_book_reviews(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Клуб":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.b-toggle.analytics-click-js[data-event-content="Клуб"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Книжные обзоры"
    element = selenium.find_element_by_css_selector(
        'a.mm-link.mm-link-big.mm-link-big-m-sub[href="/news/books/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('reviews.png')


def test_readers_reviews(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Клуб":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.b-toggle.analytics-click-js[data-event-content="Клуб"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Рецензии читателей"
    element = selenium.find_element_by_css_selector(
        'li.top-main-menu-item>a[href="/reviews/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('readers_reviews.png')


def test_collections_of_readers(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Клуб":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.b-toggle.analytics-click-js[data-event-content="Клуб"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент Подборки читателей"
    element = selenium.find_element_by_css_selector(
        'li.top-main-menu-item>a[href="/recommendations/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('collections_readers.png')


def test_littests(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Клуб":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.b-toggle.analytics-click-js[data-event-content="Клуб"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Литтесты""
    element = selenium.find_element_by_css_selector(
        'li.top-main-menu-item>a[href="/littest/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('littests.png')


def test_new_reviews(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Клуб":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.b-toggle.analytics-click-js[data-event-content="Клуб"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Рецензии читателей"
    element = selenium.find_element_by_css_selector(
        'li.top-main-menu-item>a[href="/reviews/"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Рецензии"
    element = selenium.find_element_by_css_selector(
        'li.b-stab-e-slider-item>a[href="/reviews/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('new_reviews.png')


def test_applications_reviews(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Клуб":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.b-toggle.analytics-click-js[data-event-content="Клуб"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Рецензии читателей"
    element = selenium.find_element_by_css_selector(
        'li.top-main-menu-item>a[href="/reviews/"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Заявки на рецензии"
    element = selenium.find_element_by_css_selector(
        'li.b-stab-e-slider-item>a[href="/reviews/applications"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('applications.png')


def test_review_authors(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Клуб":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.b-toggle.analytics-click-js[data-event-content="Клуб"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Рецензии читателей"
    element = selenium.find_element_by_css_selector(
        'li.top-main-menu-item>a[href="/reviews/"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Авторы рецензий"
    element = selenium.find_element_by_css_selector(
        'li.b-stab-e-slider-item>a[href="/reviews/users"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('review_authors.png')


def test_number_reviews(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Клуб":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.b-toggle.analytics-click-js[data-event-content="Клуб"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Рецензии читателей"
    element = selenium.find_element_by_css_selector(
        'li.top-main-menu-item>a[href="/reviews/"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Количество рецензий"
    element = selenium.find_element_by_css_selector(
        'li.b-stab-e-slider-item.b-stab-e-slider-item-m-active>a')
    element.click()
    time.sleep(2)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('number_reviews.png')


def test_postponed(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Отложено":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-personal-e-list-item.have-dropdown>a[href="/cabinet/putorder/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('postponed.png')


def test_postponed_choice(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Отложено":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-personal-e-list-item.have-dropdown>a[href="/cabinet/putorder/"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Читатели выбирают сегодня":
    element = selenium.find_element_by_css_selector(
        'div.best-block-carousel.today-block[data-title="Читатели выбирают сегодня"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('choice.png')


def test_postponed_main_books(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Отложено":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-personal-e-list-item.have-dropdown>a[href="/cabinet/putorder/"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Главные книги":
    element = selenium.find_element_by_css_selector(
        'div#cabinet>div>span>a[href="/best/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('main_books.png')


def test_postponed_discounts_gifts(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Отложено":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-personal-e-list-item.have-dropdown>a[href="/cabinet/putorder/"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Скидки и подарки":
    element = selenium.find_element_by_css_selector(
        'div#cabinet>div>span>a[href="/search/?discount=1&available=1&wait=1&no=1&order=actd&way=back"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('discounts_gifts.png')


def test_basket(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Корзина":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-personal-e-list-item.have-dropdown.last-child')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('basket.png')


def test_deferred(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Корзина":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-personal-e-list-item.have-dropdown.last-child')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Отложенные":
    element = selenium.find_element_by_css_selector(
        'li.ui-state-default.ui-corner-top>a[href="#step1-put"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('deferred.png')


def test_what_to_read(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Что почитать?":
    element = selenium.find_element_by_css_selector(
        'span.b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('recommend.png')


def test_best_buy(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Главное 2022":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.analytics-click-js[data-event-content="Главное"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Лучшая покупка"
    element = selenium.find_element_by_css_selector(
        'h2.autodiscounts__title.autodiscounts__padding>a[href="/best/sale/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('best_buy.png')


def test_buy_book(selenium):
    # Найдите в labirint книгу и поместите ее в корзину

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(10)

    # Найдите поле для ввода текста поиска:
    search_input = selenium.find_element_by_css_selector('input#search-field.b-header-b-search-e-input')

    # Введите текст для поиска:
    search_input.clear()
    search_input.send_keys(u"Приключения Тома Сойера")
    time.sleep(3)

    # Нажмите кнопку "Поиск":
    search_button = selenium.find_element_by_css_selector('button.b-header-b-search-e-btn')
    search_button.submit()
    time.sleep(5)

    # Нажмите элемент "В корзину":
    element = selenium.find_element_by_css_selector('div>a#buy680464')
    element.click()
    time.sleep(1)

    # Нажмите элемент "Оформить":
    element = selenium.find_element_by_css_selector(
        'div.b-basket-popinfo-e-text-row>a')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('buy_book.png')


def test_buy_book1(selenium):
    # Найдите в labirint книгу, поместите ее в корзину
    # и перейдите к оформлению заказа

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(10)

    # Найдите поле для ввода текста поиска:
    search_input = selenium.find_element_by_css_selector('input#search-field.b-header-b-search-e-input')

    # Введите текст для поиска:
    search_input.clear()
    search_input.send_keys(u"Мастер и Маргарита")
    time.sleep(3)

    # Нажмите кнопку "Поиск":
    search_button = selenium.find_element_by_css_selector('button.b-header-b-search-e-btn')
    search_button.submit()
    time.sleep(5)

    # Нажмите элемент "В корзину":
    element = selenium.find_element_by_css_selector('div>a#buy606810')
    element.click()
    time.sleep(1)

    # Нажмите элемент "Оформить":
    element = selenium.find_element_by_css_selector(
        'div.b-basket-popinfo-e-text-row>a')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('buy_book1.png')


def test_full_cycle(selenium):
    # Найдите в labirint 2 книги, поместите их в корзину
    # ек совершая покупки, очистите корзину

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(10)

    # Найдите поле для ввода текста поиска:
    search_input = selenium.find_element_by_css_selector('input#search-field.b-header-b-search-e-input')

    # Введите текст для поиска:
    search_input.clear()
    search_input.send_keys(u"Трудно быть богом")
    time.sleep(3)

    # Нажмите кнопку "Поиск":
    search_button = selenium.find_element_by_css_selector('button.b-header-b-search-e-btn')
    search_button.submit()
    time.sleep(5)

    # Нажмите элемент "В корзину":
    element = selenium.find_element_by_css_selector('div>a#buy721080')
    element.click()
    time.sleep(1)

    # Нажмите элемент "Оформить":
    element = selenium.find_element_by_css_selector(
        'div.b-basket-popinfo-e-text-row>a')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('book11.png')

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(10)

    # Найдите поле для ввода текста поиска:
    search_input = selenium.find_element_by_css_selector('input#search-field.b-header-b-search-e-input')

    # Введите текст для поиска:
    search_input.clear()
    search_input.send_keys(u"Град обреченный")
    time.sleep(3)

    # Нажмите кнопку "Поиск":
    search_button = selenium.find_element_by_css_selector('button.b-header-b-search-e-btn')
    search_button.submit()
    time.sleep(5)

    # Нажмите элемент "В корзину":
    element = selenium.find_element_by_css_selector('div>a#buy724765')
    element.click()
    time.sleep(1)

    # Нажмите элемент "Оформить":
    element = selenium.find_element_by_css_selector(
        'div.b-basket-popinfo-e-text-row>a')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('book12.png')

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(10)

    # Нажать на элемент "Корзина":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-personal-e-list-item.have-dropdown.last-child')
    element.click()
    time.sleep(3)

    # Нажмите элемент "Очистить корзину":
    element = selenium.find_element_by_css_selector(
        'div.empty-basket-link-cont>div.text-regular.empty-basket-link>a.b-link-popup')
    element.click()
    time.sleep(3)

    assert selenium.get_current_url() == URL + '/cart'


# path: python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_labirint_positive1.py
