# Поиск и форматирование номеров телефонов на веб-страницах

Этот скрипт предназначен для загрузки веб-страниц с использованием Selenium, поиска и форматирования номеров телефонов на этих страницах.

## Требования

Для работы скрипта потребуется следующее программное обеспечение:

- Python 3
- Библиотеки: selenium, beautifulsoup4, phonenumbers
- Веб-драйвер для браузера Chrome (chromedriver)

## Установка зависимостей

Вы можете установить необходимые библиотеки Python с помощью pip:

```
pip install -r requirements.txt
```


Загрузите и установите веб-драйвер для браузера Chrome на официальном сайте ChromeDriver: https://sites.google.com/chromium.org/driver/

## Как использовать
1. Клонируйте репозиторий
```
git clone git@github.com:Xopeek/Parser_test_case.git
```
2. Замените urls на нужные для вас.
3. Запустите скрипт
```python
python parser.py
```
Скрипт будет загружать веб-страницы, искать и форматировать номера телефонов, а затем выводить их на экран.

## Настройки эмуляции мобильного устройства
Скрипт использует Selenium для эмуляции мобильного устройства при загрузке веб-страниц. Вы можете настроить параметры эмуляции, такие как размер окна и User-Agent, в функции download_page_with_selenium:

```python
chrome_options.add_argument("--window-size=375,667")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
)

```


# Скрипт написал Семляков Игорь(Xopek)
