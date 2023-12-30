# 최악의 경우 O(NlogN)을 보장하는 알고리즘을 이용하거나 O(N)을 보장하는 계수 정렬을 이용한다.

N = int(input())

array = []
for i in range(N):
    input_data = input().split()
    array.append(input_data[0], int(input_data[1]))

# key를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key = lambda student: student[1])

# 정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end=' ')