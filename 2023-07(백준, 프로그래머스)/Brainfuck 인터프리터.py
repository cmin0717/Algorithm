import sys
from collections import deque
input = sys.stdin.readline

test_case = int(input())

def find(arr):
    stack = []
    loops = {}
    for i in range(len(arr)):
        if arr[i] == '[':
            stack.append(i)
        elif arr[i] == ']':
            idx = stack.pop()
            loops[i] = idx
            loops[idx] = i

    return loops

for _ in range(test_case):
    m, c, i = map(int,input().split())
    arr = [0] * m
    commend = list(input().rstrip())
    put = deque(list(input().rstrip()))

    loops = find(commend)
    now_loop = []

    now, point, turn = 0, 0, 0

    while turn < 50000000:
        if now == c:
            print("Terminates")
            break
        
        cm = commend[now]

        if cm == '-' or cm == '+':
            arr[point] += 1 if cm == '+' else -1
            if arr[point] == -256 or arr[point] == 256:
                arr[point] = 0

        elif cm == '<' or cm == '>':
            point = (point-1 if cm == '<' else point + 1) % m

        elif cm == '[':
            if arr[point] == 0:
                now = loops[now]

        elif cm == ']':
            if arr[point] != 0:
                if (loops[now], now) not in now_loop:
                    now_loop.append((loops[now], now))
                now = loops[now]
            else:
                if (loops[now], now) in now_loop:
                    now_loop.pop()

        elif cm == ',':
            if put:
                arr[point] = ord(put.popleft())
            else:
                arr[point] = 255
                
        now += 1
        turn += 1
    else:
        print("Loops", *now_loop[0])