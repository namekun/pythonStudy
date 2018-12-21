# Use Recursion BinarySearch


def binarySearch(a, start, end, x):
    # 종료 조건
    # 탐색 대상이 비어 있다면 탐색할 필요 없다.
    if a == []:
        return None

    mid = (start + end) // 2

    if x == a[mid]:
        return mid
    elif x > a[mid]:
        start = mid + 1
    else:
        end = mid - 1

    return binarySearch(a, start, end, x)


if __name__ == '__main__':
    d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
    print(binarySearch(d, 0, len(d) - 1, 36))
