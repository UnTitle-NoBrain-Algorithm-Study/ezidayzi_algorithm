n = int(input())
lst = list(map(int, input().split()))


dp = [[0] * n for _ in range(2)]

dp[0][0], dp[1][0] = lst[0], lst[0]

for i in range(1, n):
    # 이전에 제거된 배열과 본인의 합 중 더 큰 값
    # 제거하지 않고 구하는 연속합
    dp[0][i] = max(dp[1][i - 1], dp[0][i - 1] + lst[i])
    # 본인과 이전의 합중 최대
    # 제거하고 구하는 연속합
    dp[1][i] = max(dp[1][i - 1] + lst[i], lst[i])

print(max(max(dp[0]), max(dp[1])))