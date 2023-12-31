# 두 배열의 원소 교체 : 두 개의 배열 A와 B를 가지고 있다. 두 배열은 N개의 원소로 구성되어 있다. 최대 K번의 바꿔치기 연산을 수행할 수 있으며 배열 A의 모든 원소의 합이 최대가 되도록 해야한다.

# 입력 조건
# 첫 번째 줄에 N, K가 공백으로 구분되어 입력된다. (1<=N<=100,000, 0<=K<=N)
# 두 번째 줄에 배열 A의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000보다 작은 자연수이다.
# 세 번째 줄에 배열 B의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000보다 작은 자연수이다.

# 출력 조건
# 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력한다.

N, K = map(int, input().split())
cnt = 0

A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(K):
    min_value = min(A)
    A.remove(min_value)
    max_value = max(B)
    B.remove(max_value)
    A.append(max_value)

print(sum(A))






