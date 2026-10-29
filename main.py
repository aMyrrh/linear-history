print("Hello, World!")

def fib(n):
    if n == 1:
        print(0)
    else:
        lst = [0, 1]
        for i in range(2, n):
            lst.append(lst[i - 2] + lst[i - 1])
        print(*lst, sep='\n')

fib(10)