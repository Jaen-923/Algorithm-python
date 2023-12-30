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

