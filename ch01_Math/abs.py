import math


# 절댓값 알고리즘 1(부호판단)
# input: 실수 a
# output: a의 절대값

def abs_sign(a):
    if a >= 0:
        return a
    else:
        return -a


# 절댓값 알고리즘 2(제곱-제곱근)
# input : 실수 a
# output : a의 절댓값

def abs_square(a):
    b = a * a
    return math.sqrt(b) # 수학 모듈의 제곱근 함수


print(abs_sign(5))
print(abs_sign(-5))
print(abs_square(5))
print(abs_square(-5))
