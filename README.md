Тестируем сайт Лабиринт

Окружение Microsoft Windows 10 Enterprise 2019 LTSC 10.0.17763.2366.
Версия браузера: Google Chrome 103.0.5060.66 (Официальная сборка), (64 бит)

Тесты содержаться в следующих файлах, в папке tests:
test_authorization.py
path: python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_authorization.py

test_labirint_positive.py
path: python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_labirint_positive.py

test_labirint_positive1.py
path: python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_labirint_positive1.py


В этой же папке находится драйвер для запуска тестов: chromedriver.exe

В файле requirements.txt указаны все необходимые, для тестирорвания, библиотеки.

В файле settings.py указанs URL, email и password для регистрации на сайте,
а также невалидные email и password.
