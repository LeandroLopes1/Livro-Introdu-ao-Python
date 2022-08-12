# sequencia fibonacci sem usar recursao


def fibonacci(n):
    p = 0
    s = 1
    while n > 0:
        p, s = s, p + s
        n -= 1
    return p


for i in range(10):
    print(f"{i} = {fibonacci(i)}")


# sequencia fibonacci com recursao
def fibonacci_rec(n):
    if n <= 1:
        return n
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


for i in range(10):
    print(f"{i} = {fibonacci_rec(i)}")
