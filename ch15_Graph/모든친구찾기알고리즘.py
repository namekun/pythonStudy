# 1. 앞으로 처리할 사람을 저장할 큐를 만든다.
# 2. 이미 큐에 추가한 사람을 저장할 집합을 따로 만든다.
# 3. 검색의 출발점이 될 사람을 큐와 집합에 추가한다.
# 4. 큐에 사람이 남아있다면, 큐에서 처리할 사람을 계속 꺼낸다.
# 5. 꺼낸 사람을 출력한다.
# 6. 꺼낸 사람의 친구들 중, 아직 큐에 추가된 적이 없는 사람을 골라 큐와 집합에 추가한다.
# 7. 큐에 처리할 사람이 남아있다면, 4번부터 다시 반복

def findFre(g, name):
    usedName = []
    already = set()

    usedName.append(name)
    already.add(name)

    while usedName:
        fre = usedName.pop(0)
        print(fre)
        for x in g[fre]:
            if x not in already:
                usedName.append(x)
                already.add(x)


freInfo = {
    'summer': ['john', 'justin', 'mike'],
    'john': ['summer', 'justin'],
    'justin': ['john', 'summer', 'mike', 'may'],
    'mike': ['summer', 'justin'],
    'may': ['justin', 'kim'],
    'kim': ['may'],
    'tom': ['jerry'],
    'jerry': ['tom']
}

findFre(freInfo, 'summer')
print()
findFre(freInfo,'tom')