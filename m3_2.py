# Вимоги до завдання:
# Параметри функції:
# min - мінімальне можливе число у наборі (не менше 1).
# max - максимальне можливе число у наборі (не більше 1000).
# quantity - кількість чисел, які потрібно вибрати (значення між min і max).
# Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
# Функція повертає список випадково вибраних, відсортованих чисел. Числа в наборі не повинні повторюватися. Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.
# # author Глінський Артем Валерійович

import random

def get_numbers_ticket(min_val, max_val, quantity) -> set:
    try:
        # Перевірка коректності вхідних даних на цілі числа
        if not isinstance(min_val, int) or not isinstance(max_val, int) or not isinstance(quantity, int):
            raise ValueError("Аргументи функції повинні бути цілими числами.")

        # Перевірка коректності деапозона вхідних даних
        if not (1 <= min_val <= max_val <= 1000) or not (min_val <= quantity <= max_val):
            raise ValueError("Некоректні параметри функції. Перевірте діапазон значень")

        # Генерування унікальних випадкових чисел у заданому діапазоні
        numbers = set()
        while len(numbers) < quantity:
            numbers.add(random.randint(min_val, max_val))

        # Повернення відсортованого списку унікальних чисел
        return sorted(list(numbers))

    except Exception as error:
        print("Помилка:", error)
        return []

# Приклад використання

print(get_numbers_ticket(1, 49, 6)) # -> [4, 13, 27, 33, 39, 46]
print(get_numbers_ticket(1, 49, 60)) # -> [] Помилка: Некоректні параметри функції. Перевiрте деапозон значень.
print(get_numbers_ticket(1, 49, "6")) # -> [] Помилка: Аргументи функції повинні бути цілими числами.