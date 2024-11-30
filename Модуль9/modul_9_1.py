

def apply_all_func(int_list, *function):
    results  ={}
    for i in function:
        results.update({i.__name__: i(int_list)})
    return results

print(apply_all_func([6, 20, 15, 9],min, max),end=' ')
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))


