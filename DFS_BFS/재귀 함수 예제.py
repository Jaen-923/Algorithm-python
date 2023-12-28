# 재귀 함수를 문제 풀이에서 사용할 때는 재귀 함수의 종료 조건을 꼭 명시할 것
# 재귀 함수는 컴퓨터 내부적으로 스택 자료구조와 동일하다.

def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i+1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')

recursive_function(1)