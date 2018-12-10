# 숫자 n개를 리스트로 입력받아 최솟값을 구하는 프로그램을 만들어 보세요


def find_min(a):
    n = len(a)
    min_v = a[0]

    for i in range(1, n):
        if a[i] < min_v:
            min_v = a[i]
    return min_v


v = [17, 92, 18, 33, 58, 7, 33, 42]

print(find_min(v))
