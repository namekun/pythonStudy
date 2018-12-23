def solution(phone_book):
    n = len(phone_book)
    phone_book = sorted(phone_book)

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if phone_book[i] in phone_book[j]:
                return False
    return True


def solutionUseHash(phone_book):
    n = len(phone_book)
    answer = True

    phone_book = sorted(phone_book, key=lambda x: len(x))
    for i, phone1 in enumerate(phone_book):
        hash_map = {}
        for phone2 in phone_book[i + 1:]:
            hash_map[phone2[:len(phone1)]] = phone2
        if phone1 in hash_map:
            answer = False
            break
    return answer


def solutionUseStartswith(phone_book):
    phone_book = sorted(phone_book)

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False

    return True


p = ["119", "97674223", "1195524421"]
p2 = ["123", "456", "789"]
p3 = ["12232332", "12", "222222"]

print(solutionUseStartswith(p3))
