def palindrom(s):
    queue = []
    stack = []

    for x in s:  # 굳이 parse해주지 않아도 된다.
        if x.isalpha():  # x가 알파벳인가?
            queue.append(x)
            stack.append(x)

    while queue:
        if queue.pop(0) != stack.pop():
            return False;

        return True


print(palindrom("wow"))
print(palindrom("dsfadsf"))
