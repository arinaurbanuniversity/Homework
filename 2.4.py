numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for num in numbers:
    if num < 2:
        not_primes.append(num)
        continue

    is_primes = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_primes = False
            break

    if is_primes:
        primes.append(num)
    else:
        not_primes.append(num)

print('Простые числа: ', *primes)
print('Сложные числа: ', *not_primes)