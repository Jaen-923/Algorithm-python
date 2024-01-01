# 떡볶이 떡 만들기 : 손님이 왔을 때 요청한 떡의 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램

# 입력 조건
# 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다.(1<=N<=1,000,000, 1<=M<=2,000,000,000)
# 둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다. 높이는 10억보다 작거나 같은 양의 정수 또는 0이다.

# 출력 조건
# 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

# 파라메트릭 서치 유형의 문제 : 최적화 문제를 결정 문제로 바꾸어 해결하는 기법 -> 이진 탐색을 이용하여 해결

N, M = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 -> 왼쪽 부분 탐색
    if total < M:
        end = mid - 1
    # 떡의 양이 충분한 경우 -> 오른쪽 부분 탐색
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result 기록
        start = mid + 1

print(result)




