
calls = 0
def count_calls():
    global calls
    calls = calls + 1
def string_info(name):

    count_calls()
    string = list()
    string.append(len(str(name)))
    string.append(name.upper())
    string.append(name)

    return tuple(string)


def is_contains(string, list_to_search ):
    count_calls()

    string = string.upper()
    for i in list_to_search:
        if i.upper() == string:
            return True
    else:
        return False



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

