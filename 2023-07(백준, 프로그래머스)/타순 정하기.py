import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
inning = [list(map(int, input().split())) for _ in range(n)]

def play(arr):
    point,now = 0, 0
    arr.insert(3, 0)

    for i in range(n):
        count = 0
        b1, b2, b3 = 0, 0, 0
        while count != 3:

            cost = inning[i][arr[now]]

            if cost == 0:
                count += 1
            elif cost == 1:
                point += b3
                b1, b2, b3 = 1, b1, b2
            elif cost == 2:
                point += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif cost == 3:
                point += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            else:
                point += b1 + b2 + b3 +1
                b1, b2 ,b3 = 0, 0, 0

            now = (now+1) % 9

    return point

result = 0
for arr in permutations([1,2,3,4,5,6,7,8]):
    result = max(result, play(list(arr)))
print(result)