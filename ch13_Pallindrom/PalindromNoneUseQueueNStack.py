# 큐와 스택을 사용하지 않고 팰린드롬 알고리즘 구현하기


def palindrom(s):
    lenS = len(s)

    for x in range(lenS // 2):
        if s[x] != s[lenS - x - 1]:
            return False
    return True


print(palindrom("wow"))
print(palindrom("dsfadsf"))
