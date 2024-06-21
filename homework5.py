# Задание №1
immutable_var = 26, "Ilya", True # Возраст, Имя, Правда/Ложь
# Задание №2
print(immutable_var)
# Задание №3
immutable_var.append(27)
print(immutable_var) # Выдает ошибку так как это неизменяемый список данных (tuple), дополнять чем-либо или убирать что-либо в нем нельзя.
# Задание №4
mutable_list = [26, "Ilya", True]
# Задание №5
mutable_list.remove(26)
mutable_list.remove(True)
mutable_list.append(27)
mutable_list.append(False)
mutable_list.extend("huhu")
# Задание №6
print(mutable_list)