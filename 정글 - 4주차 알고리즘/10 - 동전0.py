import sys
input = sys.stdin.readline

n,k = map(int,input().split())

coin = [int(input()) for _ in range(n)]

result = 0

while True: # 입력 받은 코인들중 큰 코인부터 사용한다.
    c = coin.pop()
    result += k // c
    k = k % c
    if k == 0:
        print(result)
        break
