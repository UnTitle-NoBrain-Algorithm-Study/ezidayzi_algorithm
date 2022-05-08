from collections import deque


def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)

    queue.append([numbers[0], 0])
    queue.append([-1 * numbers[0], 0])

    # 다음 인덱스에 해당하는 numbers 원소를 더하거나 빼면서 방문하자
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp + numbers[idx], idx])
            queue.append([temp - numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer