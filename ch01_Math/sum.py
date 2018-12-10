# 일반적인 방식

def sum(a):
    s = 0
    for i in range(1, a + 1):
        s += i
    return s


print(sum(10))
print(sum(100))


# 가우스 방식

def gaus(a):
    return a * (a + 1) // 2
    # // 는 정수나눗셈을 의미한다.


print(gaus(10))
print(gaus(100))
