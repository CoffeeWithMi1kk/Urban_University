# Задание №1
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
zero = 0
# Задание №2
while zero < len(my_list):
    number = my_list[zero]
    zero = zero + 1
# Задание №3
    if number == 0:
        continue
    if number > 0:
        print(number)
    if number < 0:
        break
