numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes  = []
not_primes = []
is_prime = True  # True - в primes, False - в not_primes

for i in range(len(numbers)):
    if numbers[i] != 1:
        for j in range(1, int(numbers[i] / 2) + 1):
            if numbers[i] % (j + 1) == 0 and numbers[i] != 2:
                is_prime = False
                break
            else:
                is_prime = True
        if is_prime :
            primes.append(numbers[i])
        else:
            is_prime = False
            not_primes.append(numbers[i])

print('Primes     - ', primes)
print("Not_primes - ", not_primes)

