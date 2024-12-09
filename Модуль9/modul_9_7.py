
# Задание: Декораторы в Python

def isprime(n):
    d = 2
    while d * d <= n and n % d != 0:
         d += 1
    return d * d > n


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

result = sum_three(2,3,6)
print(result)









#   d = 2
#   while n % d != 0:
#      d += 1
#   return d == n
#


#  d = 2
#  while d * d <= n and n % d != 0:
#      d += 1
#  return d * d > n

# простые числа заканчиваются всегда на 1,3,7,9
# Да есть исключение цифры 2 и 5
    # if (((str(n))[-1]) == '1' or ((str(n))[-1]) == '3'
    #         or ((str(n))[-1]) == '7' or ((str(n))[-1]) == '9'):
    #     return True
    # else:
    #     return False
