
def add_everything_up(a, b):
    try:
        #return round((a + b),3)
        return a + b
    except TypeError as exc:

        if isinstance(a, float) and isinstance(b,str):
            return str(a) + b
        elif isinstance(a,str) and isinstance(b, int):
            return a + str(b)


        else:
            return f' Hello {exc}'


    # finally:
    #    print(' finally Завершили урок')

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
#print(add_everything_up([123.456], 7))


