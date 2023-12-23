import timeit

start_time = timeit.default_timer()

N, K = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while N >= K:
    # N이 K로 나누어 떨어지지 않을 때
    while N % K != 0:
        N -= 1
        result += 1
    N //= K
    result += 1

while N>1:
    N -= 1
    result += 1

print(result)

end_time = timeit.default_timer()
execution_time = end_time - start_time

print(f"Execution Time: {execution_time} seconds")
