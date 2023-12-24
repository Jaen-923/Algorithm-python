N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort() # 리스트 오름차순 정렬
first = data[N-1] # 가장 큰 수
second = data[N-2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(K): # 가장 큰 수 K번 더하기
        if M==0:
            break
        result += first
        M-=1
    if M==0:
        break
    result += second # 두 번째로 큰 수 한 번 더하기
    M -= 1

print(result)
