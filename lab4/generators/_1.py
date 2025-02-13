def func(N):
    for i in range(1, N + 1):
        yield i ** 2

arr = func(4) 
for i in arr: 
    print(i, end = " ")