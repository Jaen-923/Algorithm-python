# 반복되는 수열 파악하기
# 가장 큰 수와 두 번째로 큰 수가 더해지는 경우엔 특정한 수열 형태로 일정하게 반복해서 더해지는 특징이 있다.
# 반복되는 수열의 길이 : K+1 (K는 더해지는 가장 큰 수의 개수, 1은 두 번째로 큰 수의 개수)
# 수열이 반복되는 횟수 : M/(K+1) -> 만약 나누어 떨어지지 않는다면 나머지만큼 가장 큰 수가 추가로 더해진다.

N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort() # 오름차순 정렬
first = data[N-1]
second = data[N-2]

# 가장 큰 수가 더해지는 횟수 계산
count = int(M/(K+1)) * K
count += M % (K+1)

result = 0
result += (count) * first
result += (M-count) * second

print(result)


