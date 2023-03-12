import sys
input = sys.stdin.readline

n = int(input())

sticks = [int(input()) for _ in range(n)]

see_stick = [sticks.pop()] # 맨 오른쪽 스틱은 무조건 보이니깐 미리 넣어준다.

for i in range(n-1):
    stick = sticks.pop()
    if stick > see_stick[-1]: 
        see_stick.append(stick)

print(len(see_stick))