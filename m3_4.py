# Вимоги до завдання:
# Параметр функції users - це список словників, де кожен словник містить ключі name (ім'я користувача, рядок) та birthday (день народження, рядок у форматі 'рік.місяць.дата').
# Функція має визначати, чиї дні народження випадають вперед на 7 днів включаючи поточний день.
# Якщо день народження припадає на вихідний, дата привітання переноситься на наступний понеділок.
# Функція повертає список словників, де кожен словник містить інформацію про користувача (ключ name) та дату привітання.
# (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата').
# author Глінський Артем Валерійович
from datetime import datetime, timedelta

def get_upcoming_birthdays(users) -> list:
    try:
        today = datetime.today().date()
        next_week = today + timedelta(days=7)
        upcoming_birthdays = []

        for user in users:
            try:
                birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            except ValueError:
                print(f"Помилка: Невірний формат дати для користувача {user['name']}. Пропускаю. формат дати повинен бути %Y.%m.%d")
                continue

            birthday_this_year = birthday.replace(year=today.year)

            # iгноруемо тих укого вже був день народження у цьому роцi
            if birthday_this_year < today:
                print (f"У {user['name']} день народження вже було. Пропускаю")

            # процесiм тих у кого день народження буде в найближчи 7 днiв
            elif birthday_this_year < next_week:
                print (f"У {user['name']} день народження буде найближчим часом. Додаю iнформацiю до списку вiтань")

                # Якщо день народження буде у вихiдний - переносимо дату вiттання на найближчий понедiлок
                if birthday_this_year.weekday() >= 5:
                    while birthday_this_year.weekday() != 0:
                        birthday_this_year += timedelta(days=1)

                # додаемо iмя та дату вiтання
                upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })

            # iгноруемо тих укого день народження , пipyше нiж через 7 днiв.
            else:
                print (f"У {user['name']} день народження буде не скоро.")

        return upcoming_birthdays
    except Exception as error:
        print(f"Помилка: ", error)
        return []

# Приклад використання функції:
users = [
    {"name": "Іван", "birthday": "2000.02.05"}, # день народження вже було.
    {"name": "Марія", "birthday": "1995.03.09"}, # припадае на вiхiдний
    {"name": "Олексій", "birthday": "1994-03-20"},  # Невірний формат дати
    {"name": "Петро", "birthday": "1987.03.25"}, # буде не скоро
    {"name": "Максим", "birthday": "1997.03.08"} # звичайний випадок

]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
