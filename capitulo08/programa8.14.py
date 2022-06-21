def soma(*args):
    s = 0
    for i in args:
        s += i
    return s
print(soma(1,2,3,4,5))
print(soma(2))
print(soma(1,2))
print(soma(1,2,3)) 

a = lambda x: x * 2
print(a(3))

aumento = lambda a, b: (a * b / 100)
print(aumento(100, 5))
