# easy quick sort
# input : list a
# output : sorted new List


def quickSort(a):
    n = len(a)
    # 종료 조건 : 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬 X
    if n <= 1:
        return a

    # 기준 값을 정하고 기준에 맞춰 그룹을 나누는 과정
    pivot = a[-1]  # 기준은 자기 마음대로지만, 마지막 값으로 하기로 한다.
    g1 = []  # 기준보다 작은 값을 담을 리스트
    g2 = []  # 기준보다 큰 값을 담을 리스트

    for i in range(0, n - 1):
        if a[i] < pivot:
            g1.append(a[i])
        else:
            g2.append(a[i])

    # 각 그룹에 대해서 재귀 호출로 퀵 정렬을 하고
    # 기준 값과 합쳐 하나의 리스트로 결과값 변환

    return quickSort(g1) + [pivot] + quickSort(g2)  # 더러운데; 아무튼 리스트를 이렇게 더해서 해볼수도 있다.


d = [6, 8, 5, 9, 10, 1, 4, 3, 2, 7]

print(quickSort(d))
