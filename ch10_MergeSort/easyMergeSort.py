# easy merge sort
# input : list a
# output : sorted new List

def mergeSort(a):

    n = len(a)

    # end condition
    if n <= 1:
        return a

    # 그룹을 나누어 각각 병합 정렬을 호출하는 과정
    mid = n // 2  # 중간을 기준으로 두 그룹으로 나눈다.
    g1 = mergeSort(a[:mid])  # 재귀 호출로 첫 번째 그룹을 정렬
    g2 = mergeSort(a[mid:])  # 재귀 호출로 두 번째 그룹을 정렬

    # 두 그룹을 하나로 병합
    result = []  # 병합할 리스트

    while g1 and g2:  # 두 그룹에 모두 자료가 남아 있는 동안 반복
        if g1[0] < g2[0]:  # 두 그룹의 맨 앞 자료 값을 비교
            # g1 값이 더 작으면 그 값을 빼내어 결과로 추가한다.
            result.append(g1.pop(0))
        else:
            # 그 반대면 g2에
            result.append(g2.pop(0))
        # 아직 남아 있는 자료들을 result에 추가
        # g1과 g2 중 이미 빈 것은  while을 바로 지나감
    while g1:
            result.append(g1.pop(0))
    while g2:
            result.append(g2.pop(0))
    return result


d = [6, 8, 4, 9, 10, 1, 2, 3, 7, 5]

print(mergeSort(d))