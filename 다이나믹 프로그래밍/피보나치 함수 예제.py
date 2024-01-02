# 재귀 함수를 사용
# 문제점 : 함수의 매개변수 값이 커지면 커질수록 수행 시간이 기하급수적으로 늘어남
# 시간 복잡도 : O(2^2)

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))