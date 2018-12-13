# 오름차순이 아닌 내림차순으로 정렬하기

def selSort(a):
    n = len(a)
    for i in range(0, n - 1):  # 0부터 n-2까지 반복
        # i번 위치부터 끝까지 자료 값 중에 최솟값의 위치를 먼저 찾는다.
        max_idx = i
        for j in range(i + 1, n):
            if a[j] > a[max_idx]:
                max_idx = j
        # 찾은 최솟값을 i번 위치로
        a[i], a[max_idx] = a[max_idx], a[i]


d = [2, 4, 5, 1, 3]
selSort(d)

print(d)
