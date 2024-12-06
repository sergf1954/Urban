def all_variants(text):
    for i in text:
        yield i
        
    n = 2
    while n < len(text):
        for j in range(len(text)):
            if j < len(text) - 1 and j+n-1 < len(text):
                yield text[j:j+n]
            else:
                continue

        n = n + 1
        if n == len(text):
            yield text
            break
a = all_variants('ABCDEF')

for i in a:
    print(i)
