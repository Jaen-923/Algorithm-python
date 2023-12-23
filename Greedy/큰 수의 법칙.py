# 큰 수의 법칙 : 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙

# 입력조건
# 1. 첫째 줄에 N(2<=N<=1000), M(1<=M<=10000), K(1<=K<=10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
# 2. 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다.
# 3. 입력으로 주어지는 K는 항상 M보다 작거나 같다.

# 출력조건
# 첫째 줄에 큰 수의 법칙에 따라 더해진 답을 출력한다.


a = []
cnt = 0
total = 0

N, M, K = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
num = a.pop()

for i in range(N - 1):
    if a[i] == num:
        cnt += 1

num2 = a.pop()

# 최대 숫자가 한 개만 존재할 때
if cnt == 0:
    for i in range(M // K * K):
        total += num
    for i in range(M - (M // K * K)):
        total += num2

# 최대 숫자가 여러 개 존재할 때
else:
    total = num * M

print(total)












