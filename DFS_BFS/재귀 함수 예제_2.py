# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print('반복적으로 구현 : ', factorial_iterative(5))
print('재귀적으로 구현 : ', factorial_recursive(5))

# 반목문 대신에 재귀 함수를 사용했을 때 얻을 수 있는 장점 : 코드의 간결성
# 재귀 함수의 코드와 점화식이 매우 유사
# 점화식 : 특정한 함수를 자신보다 더 작은 변수에 대한 함수와의 관계를 표현한 것