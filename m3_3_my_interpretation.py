# Розробіть функцію normalize_phone(phone_number), що нормалізує телефонні номери до стандартного формату
# оскiльки це не обов'язкове завдання я зробив його по своiму
# як би я його робив
# author Глінський Артем Валерійович

import re

def normalize_phone(phone_number):
    try:
        # Видаляємо всі символи, крім цифр
        cleaned_number = re.sub(r'\D', '', phone_number)

        # Видiляємо тiло номеру 7 чисел + 3 код оператора
        raw_number = cleaned_number[-10:]

        # Номер повинний бути iз 10 символiв i починатися с нуля
        if len(raw_number) < 10:
            raise ValueError("Некоректний номер.")

        # Перевiряемо чи е номер мобiльного оператора , а не номером мiста наприклад +044

        pattern = r'^050|095|063|066|067|068|096|097|098\d{7}$'
        if not bool(re.match(pattern, raw_number)):
            raise ValueError("Номер не є номером мобільного оператора України")



        # Додаемо до номера код Украiни +38
        sanitized_number = f"+38{raw_number}"

        return sanitized_number
    except ValueError as error:
        print(f"Помилка: {phone_number} - {error}")
        return None

# Приклад використання
phone_number = "+380501234567"
print(normalize_phone(phone_number))  # -> +38501234567

# Приклад використання
phone_number = "05234567"
print(normalize_phone(phone_number))  # -> Помилка: 05234567 - Некоректний номер

# Приклад використання
phone_number = "+380441238567"
print(normalize_phone(phone_number))  # -> Помилка: +380441238567 - Номер не є номером мобільного оператора України


# контрольний тест
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)