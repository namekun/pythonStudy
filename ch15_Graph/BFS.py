# 위에서 배운 그래프 탐색 알고리즘을 이용해서 다음 그래프를 탐색하는 프로그램을 만들어보자
# BFS & DFS

graphInfo = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1],
    4: [2],
    5: [2]
}


# BFS - 너비 우선 탐색
# 탐색의 순서 : 1, 2, 3, 4, 5


def bfs(g, start):
    visited = set()
    queue = []

    queue.append(start)
    visited.add(start)

    while queue:
        n = queue.pop(0)
        for x in g[n]:
            if x not in visited:
                queue.append(x)
                visited.add(x)
    return visited


print(bfs(graphInfo, 1))

