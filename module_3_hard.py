def calculate_structure_sum(structure):
    # Инициализируем переменную для хранения общей суммы
    total_sum = 0

    # Определяем внутреннюю рекурсивную функцию для подсчета суммы
    def recursive_sum(item):
        nonlocal total_sum
        # Если элемент является целым числом, добавляем его к общей сумме
        if isinstance(item, int):
            total_sum += item
        # Если элемент является строкой, добавляем длину строки к общей сумме
        elif isinstance(item, str):
            total_sum += len(item)
        # Если элемент является списком, кортежем или множеством,
        # рекурсивно обрабатываем каждый элемент
        elif isinstance(item, (list, tuple, set)):
            for elem in item:
                recursive_sum(elem)
        # Если элемент является словарем, рекурсивно обрабатываем каждый ключ и значение
        elif isinstance(item, dict):
            for key, value in item.items():
                recursive_sum(key)
                recursive_sum(value)

    # Вызов внутренней рекурсивной функции для изначальной структуры данных
    recursive_sum(structure)

    # Возвращаем общую сумму
    return total_sum


# Пример структуры данных
data_structure = [
    [1, 2, 3],  # Список
    {'a': 4, 'b': 5},  # Словарь
    (6, {'cube': 7, 'drum': 8}),  # Кортеж, содержащий число и словарь
    "Hello",  # Строка
    ((), [{(2, 'Urban', ('Urban2', 35))}])  # Кортеж, содержащий пустой кортеж и список, который содержит множество
]

# Вызов функции calculate_structure_sum и вывод результата
result = calculate_structure_sum(data_structure)
print(result)  # Ожидаемый результат: 99
