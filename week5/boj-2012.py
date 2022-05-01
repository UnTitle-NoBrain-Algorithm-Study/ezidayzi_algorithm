import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()
answer = 0

for index, item in enumerate(arr):
    grade = index + 1
    answer += grade-item if grade > item else item - grade

print(answer)