# 삽입정렬
# 입력 : 리스트 a
# 출력 : 없음 (입력으로 주어지는  a가 정렬된다.)


def insSort(a):
    n = len(a)

    for i in range(1, n):
        k = a[i]  # key value
        j = i - 1

        while j >= 0 and a[j] > k:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = k


d = [2, 4, 5, 1, 3]
insSort(d)

print(d)
