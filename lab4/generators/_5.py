def func(n):
    i = n
    while(i!=-1):
        yield i
        i -= 1

result = func(6)
for i in result:
    print(i, end = ' ')