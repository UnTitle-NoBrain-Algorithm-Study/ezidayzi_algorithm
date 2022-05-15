def isCorrect(str):
    stack = []
    for s in str:
        if s not in '()[]':
            continue
        if s == '(' or s == '[':
            stack.append(s)
        elif (s == ')' and stack and stack[-1] == '(') or (s == ']' and stack and stack[-1] == '['):
            stack.pop()
        else:
            stack.append(0)
            break
    print('no' if stack else 'yes')


while (True):
    i = input()
    if i == '.':
        break
    isCorrect(i)
