# 숫자 카드 게임
# 1. 숫자가 쓰인 카드들이 N X M 형태로 놓여 있다. 이때 N은 행의 개수를 의미하며, M의 열의 개수를 의미
# 2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
# 3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
# 4. 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

# 입력 조건
# 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다. (1<=N, M<=100)
# 둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10000 이하의 자연수이다.

# 출력 조건
# 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.

import timeit

start_time = timeit.default_timer()

N, M = map(int, input().split())
a = [[0]*N for _ in range(M)]
c = []
d = []
for i in range(N):
    a[i][0:] = map(int, input().split())

for i in range(N):
    for j in range(M):
        c.append(a[i][j])
    c.sort()
    d.append(c[0])
    c = []

d.sort()
print(d[len(d)-1])

end_time = timeit.default_timer()
execution_time = end_time - start_time

print(f"Execution Time: {execution_time} seconds")






