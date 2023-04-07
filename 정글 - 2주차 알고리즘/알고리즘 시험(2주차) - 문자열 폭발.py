import sys
input = sys.stdin.readline

word = input().rstrip()
bomb = input().rstrip()

stack = []

for i in word:
    stack.append(i)
    if len(stack) >= len(bomb):
        check = stack[len(stack) - len(bomb):]

        if ''.join(check) == bomb:
            for _ in range(len(bomb)):
                stack.pop()

if not stack:
    print('FRULA')
else:
    print(''.join(stack))
