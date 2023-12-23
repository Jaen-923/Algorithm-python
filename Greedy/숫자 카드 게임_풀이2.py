# min() 함수를 이용
import timeit

start_time = timeit.default_timer()

N, M = map(int, input().split())

result = 0
for i in range(N):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

end_time = timeit.default_timer()
execution_time = end_time - start_time

print(f"Execution Time: {execution_time} seconds")