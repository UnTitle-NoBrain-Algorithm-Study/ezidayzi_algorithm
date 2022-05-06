def isCorrect(str):
    stack = []

    for s in str:
        if s == '(':
            stack.append('(')
        elif s == ')':
            if len(stack) > 0:
                p = stack[-1]

                if p == '(':
                    stack.pop()
                elif p == ')':
                    stack.append(s)
            else:
                stack.append(s)

    if len(stack) > 0:
        print('NO')
    else:
        print('YES')


for i in range(int(input())):
    isCorrect(input())
