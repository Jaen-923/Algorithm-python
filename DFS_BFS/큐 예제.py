# 파이썬으로 큐를 구현할 때에는 collections 모듈에서 제공하는 deque 자료구조를 활용 (queue 라이브러리보다 간단)
# deque는 스택과 큐의 장점을 모두 채택한 것으로 데이터의 삽입과 추출의 속도가 리스트 자료형에 비해 효율적이다.
# deque 객체를 리스트 자료형으로 변경하고자 한다면 list() 메서드를 이용

from collections import deque

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)