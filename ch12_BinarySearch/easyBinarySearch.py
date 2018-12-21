# 리스트에서 특정 숫자 위치 찾기(이분 탐색)
# input : list a, find Val X
# output : 찾으면 그 값의 위치, 찾지 못하면 -1

def binarySearch(a, x):
    # 탐색할 범위를 저장하는 변수 start, end
    # 리스트 전체를 범위로 탐색 시작(0 ~ len(a) - 1)

    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2 # 탐색의 중간 위치
        if x == a[mid]:
            # Find!
            return mid
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1

d = [1, 4, 9, 16, 25, 36, 49, 64, 81]

print(binarySearch(d, 36))