# 이진 탐색 문제는 입력 데이터가 많거나, 탐색 범위가 매우 넓은 편이다.
# 입력 데이터의 개수가 많은 문제에 input() 함수를 사용하면 동작 속도가 느려 시간 초과될 수 있다.
# 입력 데이터가 많은 문제는 sys 라이브러리의 readline() 함수를 이용

import sys
# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip() # readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되므로 rstrip() 사용
print(input_data)