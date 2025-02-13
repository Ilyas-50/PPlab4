def func(n):
    for i in range(0, n + 1):
        if i % 3 == 0 or i % 4 == 0:
            yield i

numb = func(7)
for i in numb:  
    print(i, end=' ')