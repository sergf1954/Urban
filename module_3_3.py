def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c=[1,2,3])
print_params()


values_list = [41, {'tel': 9171138214, 'sity': "Samara"}, [4,4,3,0,2,3]]
print_params(*values_list)

values_dict = {'a':443023, 'b': "Samara", 'c': 'РФ'}
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2,42)

