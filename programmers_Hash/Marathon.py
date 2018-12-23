def solution(participant, completion):
    n = len(participant)
    nameDict = dict()

    for x in range(0, n):
        if participant[x] not in nameDict:
            nameDict[participant[x]] = 1
        else:
            nameDict[participant[x]] += 1

    for y in completion:
        if y in nameDict:
            nameDict[y] -= 1

    for z in nameDict:
        if nameDict[z] == 1:
            answer = z

    return answer


p = ['mislav', 'stanko', 'mislav', 'ana']
c = ['stanko', 'ana', 'mislav']

print(solution(p, c))
