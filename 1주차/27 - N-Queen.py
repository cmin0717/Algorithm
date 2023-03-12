n = int(input())

pan = [0]*n # 배열 하나를 이용하여 2차배열로 사용한다.

count = 0

def queen(x): # queen함수에 같이 넣어준 x가 판의 행을 담당한다.
    global count
    if x == n: # 판에 놓여진 퀸이 n개가 될경우 n개의 퀸을 다 놓은거기에 count += 1 해준다.
        count += 1
        return
    else:
        for i in range(n): # 여기 for문에서는 판의 열을 담당
            pan[x] = i # x행,i열에 퀸
            if x == 0: # x = 0 일 경우에는 처음 놓은 퀸이므로 바로 다음 퀸을 놓을 준비
                queen(x+1)
            else:
                for j in range(x): # 앞서 놓은 퀸만 보면 되므로 퀸의 개수만큼만 for문을 돌려준다.
                    if pan[x] == pan[j] or abs(pan[x]-pan[j]) == abs(x-j): # 같은 행에는 있을수가 없으니 각 퀸의 열과 대각선만 피해준다.
                        break
                else:
                    queen(x+1) # 안걸리면 다음 퀸
queen(0) # 처음 퀸을 첫 행부터 넣어줘야 함으로 queen()에 0을 넣어 시작
print(count)

# 같은 풀이법인데 시간은 2배가 차이난다. 함수를 하나더 넣어서 그런가? 이유는 모르겠다.
# def check(x):
#     for i in range(x):
#         if pan[x] == pan[i] or abs(pan[x]-pan[i]) == abs(x-i):
#             return False
#     else:
#         return True
# count = 0
# def queen(m):
#     global count
#     if m == n:
#         count += 1
#         return
#     else:
#         for i in range(n):
#             pan[m] = i
#             if check(m):
#                 queen(m+1)
#         return

# queen(0)
# print(count)