n, r, c = map(int,input().split())

num = 0

def z(n,r,c):
    global num
    if n == 2: # 2*2 최소판에 왔을때 값 더해주고 재귀 종료
        min_pan = [[0,1],[2,3]]
        num += min_pan[r-1][c-1]
        return
    else:
        h = n//2 # z판을 4분면하기 위한 한변의/2 길이
        if r > h :
            if c > h: # 좌표가 4분면에 있을 경우
                num += (h**2)*3 # 1,2,3 분면에 있는 값들을 더해준다
                z(h, r-h, c-h) # 4분면을 다시 4조각으로 분할하기 위해 z함수에 입력
            else: # 좌표가 3분면에 있을 경우
                num += (h**2)*2
                z(h, r-h, c)
        else:
            if c > h: # 2분면에 있을 경우
                num += h**2
                z(h, r, c-h)
            else: # 1분면에 있을 경우
                z(h, r, c)
    
z(2**n,r+1,c+1) # 계산하기 쉽게 0,0 시작이 아닌 1,1시작으로 하기위해 +1씩 해주었다.
print(num)