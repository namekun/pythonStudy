# 리스트에 숫자가 n개 있을 때, 가장 큰 값이 있는 위치 번호를 돌려주는 알고리즘을 만드시오.

def find_max(a):
    n = len(a)

    max_idx = 0

    for i in range(1, n):
        if a[i] > a[max_idx]:
            max_idx = i
    return max_idx


v = [17, 92, 18, 33, 58, 7, 33, 42]

print(find_max(v))
