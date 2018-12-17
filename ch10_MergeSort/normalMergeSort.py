# merge sort
# input : list a
# output : sorted list a

def mergeSort(a):
    n = len(a)
    # end condition : 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요가 없다.

    if n <= 1:
        return
    # 그룹을 나누어 각각 병합 정렬하는 과정
    mid = n // 2
    g1 = a[:mid]
    g2 = a[mid:]

    mergeSort(g1)
    mergeSort(g2)

    z = 0 # i1
    x = 0 # i2
    c = 0 # ia

    while z < len(g1) and x < len(g2):
        if g1[z] < g2[x]:
            a[c] = g1[z]
            z += 1
            c += 1
        else:
            a[c] = g2[x]
            x += 1
            c += 1
    # 아직 남아 있는 자료들을 결과에 추가
    while z < len(g1):
        a[c] = g1[z]
        z += 1
        c += 1
    while x < len(g2):
        a[c] = g2[x]
        x += 1
        c += 1


d = [6, 8, 4, 9, 10, 1, 2, 3, 7, 5]

mergeSort(d)

print(d)
