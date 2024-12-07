
# Задание: Декораторы в Python

def isprime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

def is_prime(func):
    def wrapper(*numbers):
        result = func(*numbers)
        if isprime(result):
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper


@is_prime
def sum_three(*numbers):
    return sum(numbers)
#sum_three = is_prime(sum_three)

result = sum_three(2,3,6,10,2)
print(result)

