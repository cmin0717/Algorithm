import sys
input = sys.stdin.readline

n = int(input())

b_h = [int(input()) for _ in range(n)]

result = [0] * n # 각 위치마다 볼수 있는 옥상의 수 저장

check = []

for i in range(n-1,-1,-1): # 역순으로 조회
    if i == n-1: # 맨 오른쪽은 항상 아무것도 못보니깐 바로 스택에 저장후 continue
        check.append([b_h[i], i])
        continue

    while check:
        h, idx = check.pop()
        if b_h[i] <= h: # 만일 stack에서 꺼내온 h보다 현재가 더 낮거나 같을때
            result[i] = idx - i - 1 # 두 건물 사이의 옥상 만큼만 result[i]에 저장
            check.append([h, idx]) # 방금 빼온 건물이 더 높기에 다시 넣어준다.
            check.append([b_h[i], i]) # 현재 건물도 넣어준다. 
            break
    else: # else문으로 왔다는건 현재 건물 보다 큰 건물이 없다는 말이다.
        result[i] = (n-1) - i # 현재 건물 위치에서 마지막 건물까지 더해준다.
        check.append([b_h[i], i])

print(sum(result))