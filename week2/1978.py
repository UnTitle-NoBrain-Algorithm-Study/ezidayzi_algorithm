import math


def is_prime_num(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

a = input()
input_list = list(map(int, input().split()))
count = 0
for item in input_list:
    if is_prime_num(item):
        count = count+1

print(count)