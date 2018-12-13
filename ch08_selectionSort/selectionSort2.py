# 선택정렬
# 입력 : 리스트 a
# 출력 : 없음(입력으로 주어진 a가 정렬된다)

def selSort(a):
    n = len(a)
    for i in range(0, n - 1):  # 0부터 n-2까지 반복
        # i번 위치부터 끝까지 자료 값 중에 최솟값의 위치를 먼저 찾는다.
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        # 찾은 최솟값을 i번 위치로
        a[i], a[min_idx] = a[min_idx], a[i]


d = [2, 4, 5, 1, 3]
selSort(d)

print(d)
