# 찾는 값에 해당하는 모든 위치를 반환


def seq(a, x):
    n = len(a)
    b = []
    for i in range(0, n):
        if a[i] == x:
            b.append(i)
    return b


a = [1, 23, 4, 5, 6, 4, 8, 4]

print(seq(a, 10))
