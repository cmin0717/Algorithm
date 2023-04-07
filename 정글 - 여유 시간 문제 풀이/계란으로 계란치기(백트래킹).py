import sys
input = sys.stdin.readline

n = int(input())

eggs = [list(map(int,input().split())) for _ in range(n)]
check = [1] * n # 달걀의 상태 저장
result = 0

def break_egg(idx, count):
    global result
    if idx == n: # 가장 최근에 든 달걀이 마지막 달걀일때
        result = max(result, count)
        return
    if sum(check) <= 1: # 안 깨진 달걀이 1개 이하로 있을 때
        result = max(result, count)
        return
    if check[idx] == 0: # 깨진 달걀을 들고 있을 때
        break_egg(idx+1,count)
        return
        
    for i in range(n): # 어떤 달걀을 칠지 모르니 다 해봐야한다.
        if i != idx and check[i] == 1: # 자기 자신이 아니고 칠 달걀이 깨진 달걀이 아닐 때 실행
            eggs[idx][0] -= eggs[i][1]
            eggs[i][0] -= eggs[idx][1]
            if eggs[idx][0] <= 0:
                check[idx] = 0
                count += 1
            if eggs[i][0] <= 0:
                check[i] = 0
                count += 1

            break_egg(idx+1, count) # 다음 달걀로 넘어간다.

            if eggs[idx][0] <= 0: # 다시 원래 상태로 복구
                check[idx] = 1
                count -= 1
            if eggs[i][0] <= 0:
                check[i] = 1
                count -= 1
            eggs[i][0] += eggs[idx][1]
            eggs[idx][0] += eggs[i][1]
break_egg(0,0)
print(result)