# Задание №1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
# Задание №2
for num in numbers:
    if num == 1:
        continue
    is_prime = True
    # Задание №3
    for i in range(2, num):
        if num % i == 0:
            # Задание №4
            is_prime = False
            break
            # Задание №5
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)
# Задание №6
print("Primes:", primes)
print("Not Primes:", not_primes)
