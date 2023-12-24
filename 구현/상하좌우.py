N = int(input())
A = list(input().split())
cnt = len(A)
X, Y = 1, 1

for i in range(cnt):
    if A[i] == 'L' and Y > 1:
        Y -= 1
    if A[i] == 'R' and Y < N:
        Y += 1
    if A[i] == 'U' and X > 1:
        X -= 1
    if A[i] == 'D' and X < N:
        X += 1

print(X, Y)



