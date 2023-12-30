# 입력 조건
# 첫 번째 줄에 학생의 수 N이 입력된다. (1<=N<=100,000)
# 두 번째 줄부터 N+1번째 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다.
# 문자열 A의 길이와 학생의 성적은 100이하의 자연수이다.

# 출력 조건
# 모든 학생의 이름을 성적이 낮은 순서대로 출력한다. 성적이 동일한 학생들의 순서는 자유롭게 출력한다.

N = int(input())
array = []
score = []

for i in range(N):
    array.append((input().split()))

for i in range(len(array)):
    score.append(int(array[i][1]))

score = sorted(score)

while True:
    for i in range(len(score)):
        for j in range(len(array)):
            if score[i] == int(array[j][1]):
                print(array[j][0], end=' ')
    break


