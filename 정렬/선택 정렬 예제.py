# 선택 정렬 : 매번 가장 작은 데이터를 선택해서 앞으로 보내는 과정을 반복해서 수행
# 시간 복잡도 : O(n^2), 다른 정렬 알고리즘에 비해 비효율적이다. 따라서 데이터 개수가 작을 때 사용

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
        # 스와프 : 특정한 리스트가 주어졌을 때 두 변수의 위치를 변경하는 작업,
        # 다른 대부분의 프로그래밍 언어에서는 명시적으로 임시 저장용 변수를 만들어 두 원소의 값을 변경해야한다.
        array[i], array[min_index] = array[min_index], array[i]
