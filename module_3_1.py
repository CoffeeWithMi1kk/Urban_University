# Задание №1
calls = 0


# Задание №2
def count_calls():
    global calls
    calls = calls + 1


# Задание №3
def string_info(string):
    count_calls()  # Увеличиваем счётчик вызовов
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return length, upper_case, lower_case


# Задание №4
def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счётчик вызовов
    normalized_string = string.lower()
    normalized_list = [item.lower() for item in list_to_search]
    return normalized_string in normalized_list


# Задание №5
print(string_info('Ilya'))
print(string_info('Valentinov'))
print(is_contains('Python', ['Python', 'Thon', 'Py']))
print(is_contains('Telegram', ['Gram', 'Tele']))

# Задание №6
print(calls)
