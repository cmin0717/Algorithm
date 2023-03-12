import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())

n = int(input())

qube = [list(map(int,input().split())) for _ in range(n)]

count = 0
rest_vol = a*b*c # 박스의 부피
check_vol = 0 # 전 큐브가 채운 부피

for vol,cnt in qube[::-1]:
    if vol == 0: # 한변의 길이가 1이면 남은 부피랑 cnt를 비교해서 작은값을 더해주고 박스 부피에서 빼준다.
        if rest_vol >= cnt:
            count += cnt
            rest_vol -= cnt
        else:
            count += rest_vol
            rest_vol = 0
    else:
        vol = (2**vol)
        l = a//vol
        w = b//vol
        h = c//vol
        if 0 in [l,w,h]: # 0이 있다면 넣을 수 없는 큐브니깐 패쓰
            continue
        vol = vol**3
        prev_cnt = check_vol//vol # 전 큐브가 채운 부피를 현 큐브가 채울려면 소모하는 개수
        if l*w*h - prev_cnt > cnt: # 넣을 수 있는 큐브의 수보다 cnt가 적을때
            check_vol += vol * cnt
            rest_vol -= vol * cnt
            count += cnt
        else:
            check_vol += vol * (l*w*h - prev_cnt)
            rest_vol -= vol * (l*w*h - prev_cnt)
            count += l*w*h -prev_cnt

if rest_vol == 0: # for문이 끝나고도 박스의 부피가 남아있다면 다 못채운거다
    print(count)
else:
    print(-1)
            


