# 입력 조건
# 첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다.(1<=N<=500)
# 둘째 줄부터 N+1번째 줄까지 N개의 수가 입력된다. 수의 범위는 1이상 100,000 이하의 자연수이다.

# 출력 조건
# 입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다. 동일한 수의 순서는 자유롭게 출력한다.

# 라이브러리 사용
N = int(input())
array = []
for i in range(N):
    array.append(int(input()))

array.sort(reverse = True)
print(array)

# 선택 정렬
for i in range(len(array)-1, 0, -1):
    max_index = i
    for j in range(i+1, len(array)):
        if array[max_index] < array[j]:
            max_index = j
    array[i], array[max_index] = array[max_index], array[i]

print(array)

# 삽입 정렬
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] > array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)

