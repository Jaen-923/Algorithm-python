# 이진 탐색 알고리즘으로 구현
# N개의 부품을 번호를 기준으로 정렬해야한다.

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

N = int(input())
array = list(map(int, input().split()))

M = int(input())
X = list(map(int, input().split()))

for i in X:
    result = binary_search(array, i, 0, N-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')