import sys
from collections import deque
input = sys.stdin.readline

n, w, l = map(int, input().split())

trucks = deque(list(map(int, input().split())))
bridge = deque([])
sum_bridge, land, time = 0, 0, 0

while land != n:
    time += 1

    # 다리에 있는 애들중에 다리를 다 넘었다면 다리에서 뺴준다.
    if bridge and time-bridge[0][0] == w:
        sum_bridge -= bridge[0][1]
        bridge.popleft()
        land += 1

    # 현재 다리에 트럭을 더 넣을수 있다면 넣는다.
    if trucks and sum_bridge + trucks[0] <= l:
        truck = trucks.popleft()
        bridge.append([time, truck])
        sum_bridge += truck

print(time)

