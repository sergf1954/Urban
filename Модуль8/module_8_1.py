
def add_everything_up(a, b):
    try:
        return round((a + b),3)
    except TypeError as exc:
        if type(a) == float and type(b) == str:
            return str(a) + b
        elif type(a) == str and type(b) == int:
            return a + str(b)
        else:
            return f' Hello {exc}'

    #
    # finally:
    #     print(' finally Завершили урок')

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up('123.456', '7'))


