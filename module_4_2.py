# Задание №1
def test_function():
    # Задание №2
    def inner_function():
        print("Я в области видимости функции test_function")

    # Задание №3
    inner_function()


# Вызов функции test_function
test_function()

# Задание №4 Попытка вызова inner_function вне функции test_function
inner_function()
