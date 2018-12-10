# 1-1 : 연속한 숫자의 제곱의 합을 구하는 프로그램을 만들어보자

import math


def Sum1(n):
    s = 0
    for i in range(1, n + 1):
        s += i * i
    return s


print(Sum1(10))


# 1-2 : 연습 문제 1-1 의 계산 복잡도는?
# O(n)

# 1-3 : 1부터 n까지의 연속된 숫자의 제곱의 합을 구하는 프로그램을 공식을 사용해서 만드시오
# 공식 : n(n+1)(2n + 1) / 6

def sum2(n):
    return n * (n + 1) * (2 * n + 1) // 6


print(sum2(10))








