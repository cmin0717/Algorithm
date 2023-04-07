import sys
input = sys.stdin.readline

n,k = map(int,input().split())

turn = list(map(int,input().split()))
count = 0

if n >= len(set(turn)):  # 사용할 장비보다 멀티탭이 더 많다면 그냥 다 쓰면 된다.
    pass
else:
    now = [] # 현재 사용중인 장비들
    for item in range(k): # 처음에 순서대로 멀티탭에 꽂아 준다.
        if item not in now:
            now.append(item)
        if len(now) == n:
            break
    for i in range(n,k): 
        if turn[i] in now: # 다음 장비가 이미 꽂혀있으면 continue
            continue
        check = [] # 무엇을 뺄지 정할 리스트
        rest = turn[i:] # 앞으로 남아 있는 장비
        for j in range(n):
            if now[j] in rest: # 앞으로 사용할 장비에 있다면 언제 사용하는지, 장비 이름을 넣어준다.
                check.append([rest.index(now[j]), now[j]])
            else:
                check.append([k,now[j]]) # 없다면 이따 뺄수있게 k값과 이름을 넣어준다. 그냥 최대값을 넣어주면 된다 의미 없다.
        check.sort(reverse=True) # 내림차순으로 정렬
        now.remove(check[0][1]) # 현재 사용중에서 앞으로 쓸일이 없거나 제일 늦게 쓰는 경우를 빼준다.
        now.append(turn[i]) # 현재 사용해야할 장비를 꽂는다.
        count += 1

print(count)