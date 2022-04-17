n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort(reverse=True)
b.sort()

sum = 0

for x, y in zip(a, b):
    sum = sum + x*y

print(sum)