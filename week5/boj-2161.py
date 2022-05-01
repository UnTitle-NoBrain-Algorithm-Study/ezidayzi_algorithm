n = int(input())

arr = [i+1 for i in range(n)]
result = []

while n > 1:
    a = arr.pop(0)
    result.append(a)
    b = arr.pop(0)
    arr.append(b)
    n = n-1


for i in result:
    print(i, end= ' ')

print(arr[0])