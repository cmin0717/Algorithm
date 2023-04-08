import sys
sys.setrecursionlimit(10**6)

def check(idx, link, visit):
    visit[idx] = True
    child = [i for i in link[idx] if visit[i] == False]

    # on - 현재 내가 등대를 on 했을경우 내 하위 등대를 몇개 더 켜야하는지 / 일단 내가 키니깐 디폴트값은 1이다.
    # off - 현재 내가 등대를 off 했을경우 내 하위 등대를 몇개 더 켜야하는지
    on,off = 1,0 

    # 자식 등대가 없다면 leaf노드이니깐 바로 반환
    if not child:
        return on,off

    for c in child:
        # 자식이 반환한 on off값
        on_c, off_c = check(c,link,visit)
        # 내가 켰다면 자식은 켜도되고 안켜도 된다. 그렇기에 min값을 더함
        on += min(on_c, off_c)
        # 내가 껐다면 내 자식은 다 켜야한다.
        off += on_c
    return on,off

def solution(n, lh):
    link = [[] for _ in range(n+1)]
    visit = [False]*(n+1)
    
    for x,y in lh:
        link[x].append(y)
        link[y].append(x)

    # 내가 켰을경우와 껐을 경우중 총 등대를 켜야하는 횟수가 작은값으로 리턴
    result = min(check(1,link,visit))    
        
    return result

solution(8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]])

# 음청 어려웠다....아직 트리구조 문제가 익숙하지 않다...