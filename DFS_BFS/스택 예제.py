# 파이썬에서 스택을 이용할 때에는 별도의 라이브러리를 사용할 필요 X
# 기본 리스트에서 append()와 pop() 메서드를 이용한다.

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력

# 첫 번째 콜론(:)은 시작 인덱스
# 두 번째 콜론(:)은 끝 인덱스
# 마지막에 오는 -1은 스텝(step)