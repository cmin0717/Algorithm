import sys
input = sys.stdin.readline # 안해주니 시간 초과뜸

n = int(input())

result = []

for _ in range(n):
    order = input().rstrip().split()
    if order[0] == 'push':
        result.append(order[1])
    elif order[0] == 'pop':
        if len(result) == 0:
            print(-1)
        else:
            print(result.pop())
    elif order[0] == 'size':
        print(len(result))
    elif order[0] == 'empty':
        if len(result) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])
