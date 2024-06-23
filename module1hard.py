# Задание "Средний балл"
# Вводные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Сортировка
students = sorted(students)
# Словарь
average_point = {}
# Решение
for a, students in enumerate(students): average_point[students] = sum(grades[a]) / len(grades[a])
# for - перебирает каждый элемент списка
# a - переменная, индекс элемента списка
# in - проверяет вхождение элемента в последовательность
# enumerate - использование этой функции позволяет получить как сам элемент списка так и его индекс
# Вывод
print(average_point)