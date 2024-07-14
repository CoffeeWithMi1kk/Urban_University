# Задание №1
def print_params(a=1, b="строка", c=True):
    print(a, b, c)


# Задание №2
values_list = [3, "Августа", True]
values_dict = {"a": 3, "b": "Августа", "c": True}
# Задание №3
values_list_2 = [3, "Августа"]

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
