# 왕실의 나이트 : 8 X 8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.
# 이때 왕실의 정원에서 행 위치를 표현할 때는 1부터 8로 표현하며, 열 위치를 표현할 때는 a부터 h로 표현한다.
# 나이트는 특정한 위치에서 다음과 같은 2가지 경우로 이동할 수 있다.
# 1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
# 2. 수직으로 두 칸 이동

# 입력 조건
# 첫째 줄에 8 X 8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입력된다.

# 출력 조건
# 첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오.

pos = input()
result = 0

posX = ord(pos[0]) - 97  # a의 아스키 코드값은 97
posY = int(pos[1]) - 1

if posY == 0 or posY == 7:
    if posX == 0 or posX == 7:
        result = 2
    elif posX == 1 or posX == 6:
        result = 3
    else:
        result = 4

elif posY == 1 or posY == 6:
    if posX == 0 or posX == 7:
        result = 3
    elif posX == 1 or posX == 6:
        result = 4
    else:
        result = 6

else:
    if posX == 0 or posX == 7:
        result = 4
    elif posX == 1 or posX == 6:
        result = 6
    else:
        result = 8

print(result)



