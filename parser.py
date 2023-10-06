import phonenumbers
import re

from selenium import webdriver
from bs4 import BeautifulSoup


def download_page_with_selenium(url):
    """Функция для загрузки веб-страницы по URL с помощью Selenium"""
    try:
        # Настройки Chrome для эмуляции мобильного устройства
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=375,667")
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)"
            " AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
        )

        # Запуск браузера Chrome с настройками
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        page_content = driver.page_source
        return page_content
    except Exception as e:
        print(f"Ошибка при загрузке страницы с помощью Selenium: {e}")
        return None
    finally:
        driver.quit()


def find_and_validate_phone_numbers_on_page(url):
    """Функция поиска и форматирования номеров."""
    page_content = download_page_with_selenium(url)
    if page_content:
        soup = BeautifulSoup(page_content, 'html.parser')
        text = soup.get_text()
        text = re.sub(r'\D', '', text)

        pattern = r'[78]\d{10}'

        numbers = str(re.findall(pattern, text))
        phone_numbers = phonenumbers.PhoneNumberMatcher(numbers, "RU")

        unique_numbers = set()

        if phone_numbers:
            print(f"Найдены номера на странице {url}:")
            for match in phone_numbers:
                formatted_phone = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
                if formatted_phone not in unique_numbers:
                    print(formatted_phone)
                    unique_numbers.add(formatted_phone)
        else:
            print(f"На странице {url} не найдены номера телефонов.")
    else:
        print(f"Не удалось загрузить страницу {url}.")


if __name__ == '__main__':
    urls = [
        "https://hands.ru/company/about",
        "https://repetitors.info",
    ]

    for url in urls:
        find_and_validate_phone_numbers_on_page(url)
