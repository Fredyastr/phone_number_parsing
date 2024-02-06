import requests
import re

def phone_number_parsing(url):
    response = requests.get(url)
    phone_pattern = re.compile(r'\b8\s?\(?(\d{3})\)?\s?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})\b', re.VERBOSE)

    if response.status_code == 200:
        phone_numbers = set(phone_pattern.findall(response.text))

        print('Найденные номера телефона: ')
        for number in phone_numbers:
            print('8'+''.join(number))
    else:
        print('Не удалось загрузить страницу')




