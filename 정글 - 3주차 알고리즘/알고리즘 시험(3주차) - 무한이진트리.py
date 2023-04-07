import sys
input = sys.stdin.readline

a,b = map(int,input().split())

left = 0 # 왼쪽 트리 저장
right = 0 # 오른쪽 트리 저장

while True: 
    if a == b == 1: # 둘다 1이 되면 루트로 온거니깐 스탑!
        break
    if a < b: # b가 더 크다면 오른쪽 노드
        if a == 1: # 한쪽 노드가 1이 되면 어차피 1씩 줄어드니깐 한꺼번에 계산
            right += b//a -1
            b = 1
        else:
            b = b - a 
            right += 1
    else: # 왼쪽 노드
        if b == 1:
            left += a//b -1
            a = 1
        else:
            a = a - b
            left += 1
print(left, right)