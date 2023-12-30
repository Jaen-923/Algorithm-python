# 삽입 정렬 : 특정한 데이터를 적절한 위치에 삽입하여 수행. 필요할 때만 위치를 바꾸므로 선택 정렬보다 훨씬 효율적이다.
# 시간 복잡도 : O(n^2), 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다.
# 최선의 경우 시간 복잡도 : O(N)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)