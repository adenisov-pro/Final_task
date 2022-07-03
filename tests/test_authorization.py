import time
from settings import valid_email, valid_password, URL
import pytest
from selenium import webdriver


driver = webdriver.Chrome(executable_path=r'.\tests\chromedriver.exe')


@pytest.fixture(autouse=True)
def testing():
    # Переходим на страницу авторизации
    driver.get(URL)
    yield
    driver.quit()


def test_authorization(web_browser):
    # Откройте страницу поиска labirint:
    web_browser.get(URL)
    time.sleep(5)

    # Нажать на элемент "Мой Лабиринт":
    element = web_browser.find_element_by_css_selector(
        'li.b-header-b-personal-e-list-item.have-dropdown.b-header-b-personal-e-list-item_cabinet')
    element.click()
    time.sleep(1)

    # Введите email:
    email_field = web_browser.find_element_by_css_selector('input.full-input__input.formvalidate-error')
    email_field.clear()
    email_field.send_keys(valid_email)
    time.sleep(1)

    # Нажмите кнопку "Войти":
    search_button = web_browser.find_element_by_css_selector('input#g-recap-0-btn')
    search_button.submit()
    time.sleep(1)

    #  Введите код скидки ("password")
    password_field = web_browser.find_element_by_css_selector('input[placeholder="Введите свой код скидки"]')
    password_field.clear()
    password_field.send_keys(valid_password)

    # Нажмите кнопку "Проверить код и войти":
    search_button = web_browser.find_element_by_css_selector('input[data-default-value="Проверить код и войти"]')
    search_button.submit()
    time.sleep(5)

    # Сделайте скриншот окна браузера:
    web_browser.save_screenshot('cabinet.png')


#  path: python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_authorization.py