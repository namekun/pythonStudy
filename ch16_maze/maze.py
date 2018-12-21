maze = {
    'a': ['e'],
    'b': ['c', 'f'],
    'c': ['b', 'd'],
    'd': ['c'],
    'e': ['a', 'i'],
    'f': ['b', 'g', 'j'],
    'g': ['f', 'h'],
    'h': ['g', 'l'],
    'i': ['e', 'm'],
    'j': ['f', 'k', 'n'],
    'k': ['j', 'o'],
    'l': ['h', 'p'],
    'm': ['i', 'n'],
    'n': ['m', 'j'],
    'o': ['k'],
    'p': ['l']
}


# 이 문제는 탐색 문제이다.
# 출발점에서 도착점까지 미로를 헤쳐나가면된다.
# 도착점에 도달하면 끝낸다.
# 끝낼 수 없는 미로라면 ? 를 출력한다.

def mazeOut(g, start, end):
    queue = []  # 앞으로 이동해야할 이동경로를 큐에 저장한다.
    visited = set()  # 방문했던 꼭짓점들을 기록한다.

    # 시작점 추가
    queue.append(start)
    visited.add(start)

    while queue:
        x = queue.pop(0)  # 큐에 저장된 가장 첫번째 데이터를 꺼낸다.
        v = x[-1]  # 이동경로의 마지막 문자는 우리가 처리해야할 문자이다.

        if v == end:  # 만약 우리가 마지막으로 꺼낸 문자가 도착점과 같다면?
            return x
        for i in g[v]:  # 처리해야할 문자와 연결된 그래프 중에서
            if i not in visited:  # 아직 방문하지 않은 꼭짓점이 있다면
                queue.append(x + i)  # 큐에 있던 이동경로에 더해주고,
                visited.add(i)  # 방문했다는 것을 체크해줍니다.

    return "?"  # 도착점이 없는 미로라면 ? 를 리턴해줍니다.


print(mazeOut(maze, 'a', 'p'))
