# 리스트 a에서 어디부터 어디까지가 정렬 대상인지
# 범위를 지정하여 정렬하는 재귀 호출 함수

def quickSortSub(a, start, end):

    # 종료 조건
    if end - start <= 0:
        return


    # 기준값
    pivot = a[end]

    i = start

    # 정렬
    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1

    a[i], a[end] = a[end], a[i]

    # 재귀 호출
    quickSortSub(a, start, i - 1)
    quickSortSub(a, i + 1, end)



def quickSort(a):
    quickSortSub(a, 0, len(a) - 1)


d = [6, 8, 5, 9, 10, 1, 4, 3, 2, 7]

quickSort(d)

print(d)