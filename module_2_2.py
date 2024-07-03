# Задание №1
first = input("Введите первое число: ")
second = input("Введите второе число: ")
third = input("Введите третье число: ")
# Задание №2
if first == second or second == third or first == third:
    print(2)
# Задание №3
elif first == second == third:
    print(3)
# Задание №4
else:
    print(0)