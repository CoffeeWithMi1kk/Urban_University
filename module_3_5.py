def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Если длина строки 1, возвращаем это число как целое число
    if len(str_number) == 1:
        return int(str_number)

    # Получаем первую цифру и оставшуюся часть строки
    first = int(str_number[0])
    rest = int(str_number[1:])

    # Рекурсивно умножаем первую цифру на результат работы функции для оставшейся части
    return first * get_multiplied_digits(rest)


# Пример использования
result = get_multiplied_digits(40203)
print(result)