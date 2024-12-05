def all_variants(text):
    for i in text:
        yield i
    for j in range(len(text)):
        if j < len(text) - 1:
            yield text[j:j+2]
        else:
            yield text

a = all_variants('ABCDE')

for i in a:
    print(i)
