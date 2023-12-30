# 미로 탈출 : 미로를 탈출하기 위해 움직여야하는 최소 칸의 개수를 구하시오.

# 입력 조건
# 첫쨰 줄에 두 정수 N, M(4<=N, M<=200)이 주어진다. N개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어진다.
# 각각의 수들은 공백 없이 붙어서 입력으로 제시된다. 또한 시작과 마지막 칸은 항상 1개이다.

# 출력 조건
# 첫째 줄에 최소 이동 칸의 개수를 출력한다.

from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 공간 범위에 벗어난 경우 무시
            if nx < 0  or ny < 0  or nx >= N or ny >= M:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[N-1][M-1] # 가장 오른쪽 아래까지의 최단 거리 반환

# BFS를 수행한 결과 출력
print(bfs(0, 0))


