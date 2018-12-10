# factorial

def fac(a):
    f = 1
    for i in range(1, a+1):
        f = f * i
    return f

print(fac(5))