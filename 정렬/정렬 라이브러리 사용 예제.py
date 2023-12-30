# sorted() : 퀵 정렬과 동작 방식이 비슷한 병합 정렬을 기반으로 만들어졌다. 리스트, 딕셔너리 자료형 등을 입력받는다.
# 병합정렬은 일반적으로 퀵 정렬보다 느리지만 최악의 경우에도 시간 복잡도 O(NlogN)을 보장한다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
result = sorted(array)
print(array)

# 리스트 변수가 하나 있을 때 내부 원소를 바로 정렬할 수 있다.
array2 = [4, 6, 3, 9, 1, 2]
array2.sort()
print(array2)

# sorted()나 sort()를 이용할 때에는 key 매개변수를 입력으로 받을 수 있다.
array3 = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array3, key=setting)
print(result)