import time
from settings import valid_email, valid_password, URL


def test_authorization(selenium):
    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Мой Лабиринт":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-personal-e-list-item.have-dropdown.b-header-b-personal-e-list-item_cabinet')
    element.click()
    time.sleep(1)

    # Введите email:
    email_field = selenium.find_element_by_css_selector('input.full-input__input.formvalidate-error')
    email_field.clear()
    email_field.send_keys(valid_email)
    time.sleep(1)

    # Нажмите кнопку "Войти":
    search_button = selenium.find_element_by_css_selector('input#g-recap-0-btn')
    search_button.submit()
    time.sleep(1)

    #  Введите код скидки ("password")
    password_field = selenium.find_element_by_css_selector('input[placeholder="Введите свой код скидки"]')
    password_field.clear()
    password_field.send_keys(valid_password)

    # Нажмите кнопку "Проверить код и войти":
    search_button = selenium.find_element_by_css_selector('input[data-default-value="Проверить код и войти"]')
    search_button.submit()
    time.sleep(5)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('cabinet.png')
    # assert page.get_current_url() == URL + '/cabinet'


def test_auth_google(selenium):
    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(3)

    # Нажать на элемент "Сообщения":
    element = selenium.find_element_by_css_selector(
        'a.b-header-b-personal-e-link.top-link-main.have-dropdown-touchlink.top-link-main_notification')
    element.click()

    # Нажать на элемент "Другие способы входа":
    element = selenium.find_element_by_css_selector('div.new-auth__show-soc')
    element.click()

    # Нажать на иконку "Google":
    element = selenium.find_element_by_css_selector(
        'span.new-auth__auth-social__text.header-sprite.new-auth__auth-social_gl')
    element.click()

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('auth-google.png')


def test_page_books(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)
    # Нажать на элемент "Книги":
    element = selenium.find_element_by_css_selector(
        'span.b-header-b-menu-e-link.top-link-menu.first-child>a')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('page_book.png')


def test_search_book(selenium):
    """ Search some phrase in labirint and make a screenshot of the page. """
    # Найдите в labirint книгу и сделайте скриншот страницы

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(10)

    # Найдите поле для ввода текста поиска:
    search_input = selenium.find_element_by_css_selector('input#search-field.b-header-b-search-e-input')

    # Введите текст для поиска:
    search_input.clear()
    search_input.send_keys(u"Приключения Алисы в стране чудес")

    time.sleep(5)

    # Click Search (Нажмите кнопку Поиск):
    search_button = selenium.find_element_by_css_selector('button.b-header-b-search-e-btn')
    search_button.submit()
    time.sleep(5)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('book.png')


def test_page_main(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)
    # Нажать на элемент "Главное 2022":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.analytics-click-js[data-event-content="Главное"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('page_main.png')


def test_page_delivery(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(3)
    # Нажать на элемент "Доставка и оплата":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-sec-menu-e-list-item.first-child.analytics-click-js')
    element.click()

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('delivery.png')


def test_page_certificates(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(3)
    # Нажать на элемент "Сертификаты":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-sec-menu-e-list-item.analytics-click-js[data-event-content="Сертификаты"]')
    element.click()

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('certificates.png')


def test_page_ratings(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(3)
    # Нажать на элемент "Рейтинги":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-sec-menu-e-list-item.analytics-click-js[data-event-content="Рейтинги"]')
    element.click()

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('ratings.png')


def test_page_new_products(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(3)
    # Нажать на элемент "Новинки":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-sec-menu-e-list-item.analytics-click-js[data-event-content="Новинки"]')
    element.click()

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('newproducts.png')


def test_page_discount(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(3)
    # Нажать на элемент "Скидки":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-sec-menu-e-list-item.analytics-click-js[data-event-content="Скидки"]')
    element.click()

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('discount.png')


def test_page_telephone(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(3)
    # Нажать на элемент "8 800 600-95-25":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-sec-menu-e-list-item.have-dropdown.have-dropdown-clickable.analytics-click-js[data-event-content="Звонок"]')
    element.click()

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('telephone.png')


def test_page_contacts(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(3)
    # Нажать на элемент "Контакты":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-sec-menu-e-list-item.analytics-click-js[data-event-content="Контакты"]')
    element.click()

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('contacts.png')


def test_page_support(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(3)
    # Нажать на элемент "Поддержка":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-sec-menu-e-list-item.analytics-click-js[data-event-content="Поддержка"]')
    element.click()

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('support.png')


def test_page_points_of_export(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(3)
    # Нажать на элемент "362 пункта самовывоза":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-sec-menu-e-list-item.last-child.analytics-click-js[data-event-content="Пункты самовывоза"]')
    element.click()

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('points.png')


def test_messages(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(3)

    # Нажать на элемент "Сообщения":
    element = selenium.find_element_by_css_selector(
        'a.b-header-b-personal-e-link.top-link-main.have-dropdown-touchlink.top-link-main_notification')
    element.click()

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('messag.png')


def test_product_type(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(3)

    # Нажать на элемент "Книги":
    element = selenium.find_element_by_css_selector(
        'span.b-header-b-menu-e-link.top-link-menu.first-child>a')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Тип товара"
    element = selenium.find_element_by_css_selector(
        'span.navisort-part.navisort-filter.navisort-part-1.fleft')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('product_type.png')


def test_page_all_book(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Главное 2022":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.analytics-click-js[data-event-content="Главное"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Все книги"
    element = selenium.find_element_by_css_selector(
        'li.swiper-slide.selected.swiper-slide-active')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('all_book.png')


def test_page_discounts_today(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Главное 2022":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.analytics-click-js[data-event-content="Главное"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Скидки сегодня"
    element = selenium.find_element_by_css_selector(
        'li.swiper-slide.swiper-slide-next')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('discounts_today.png')


def test_page_for_children(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Главное 2022":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.analytics-click-js[data-event-content="Главное"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Детям"
    element = selenium.find_element_by_css_selector(
        'li.swiper-slide>a[href="/best/kids/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('for_children.png')


def test_page_artistic_literature(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Главное 2022":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.analytics-click-js[data-event-content="Главное"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Художественная литература"
    element = selenium.find_element_by_css_selector(
        'li.swiper-slide>a[href="/best/fiction/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('literature.png')


def test_page_nonfiction(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Главное 2022":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.analytics-click-js[data-event-content="Главное"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Нонфикшн"
    element = selenium.find_element_by_css_selector(
        'li.swiper-slide>a[href="/best/nonfiction/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('nonfiction.png')


def test_page_gift_editions(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Главное 2022":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.analytics-click-js[data-event-content="Главное"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Подарочные издания"
    element = selenium.find_element_by_css_selector(
        'li.swiper-slide>a[href="/best/giftbooks/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('editions.png')


def test_club_now(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Клуб":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.b-toggle.analytics-click-js[data-event-content="Клуб"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Лабиринт. Сейчас"
    element = selenium.find_element_by_css_selector(
        'a.mm-link.mm-link-big.mm-link-big-m-sub[href="/now/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('club_now.png')


def test_children_navigator(selenium):
    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Клуб":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.b-toggle.analytics-click-js[data-event-content="Клуб"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Детский навигатор"
    element = selenium.find_element_by_css_selector(
        'a.mm-link.mm-link-big.mm-link-big-m-sub[href="/child-now/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('children_navigator.png')


def test_club_magazines(selenium):

    # Откройте страницу поиска labirint:
    selenium.get(URL)
    time.sleep(5)

    # Нажать на элемент "Клуб":
    element = selenium.find_element_by_css_selector(
        'li.b-header-b-menu-e-list-item.b-toggle.analytics-click-js[data-event-content="Клуб"]')
    element.click()
    time.sleep(1)

    # Нажать на элемент "Журналы"
    element = selenium.find_element_by_css_selector(
        'a.mm-link.mm-link-big.mm-link-big-m-sub[href="/journals/"]')
    element.click()
    time.sleep(1)

    # Сделайте скриншот окна браузера:
    selenium.save_screenshot('magazines.png')


# path: python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_labirint_positive.py
