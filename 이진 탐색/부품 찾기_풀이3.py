# 계수 정렬을 이용해 풀이

N = int(input())
array = [0]*1000001

for i in input().split():
    array[int(i)] = 1

M = int(input())
X = list(map(int, input().split()))

for i in X:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')
        