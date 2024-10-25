import fake_math as m1
import  true_math as m2

def f_divide(first, second):
    return m1.divide(first,second)

def t_divide(first, second):
    return m2.divide(first, second)


result1 = f_divide(69, 3)
result2 = f_divide(3, 0)
result3 = t_divide(49, 7)
result4 = t_divide(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)



