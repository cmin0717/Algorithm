def solution(info, edges):
    
    link = [[] for _ in range(len(info))]
    for x,y in edges:
        link[x].append(y)
    
    result = set([1]) # 루트는 무조건 양이니 1은 디폴트값이다.
    def find(idx,sheep,wolf):
        # 현재 위치가 양이면서 아직 찾지 않은 양 일 경우
        if idx not in sheep and info[idx] == 0:
            result.add(len(sheep)+1)
            find(0,sheep+[idx],wolf) # 현재까지 정보를 가지고 루트부터 다시 탐색
        
        # 현재 위치에서 연결된 다른 노드 탐색
        for i in link[idx]:
            if info[i] == 0:
                find(i,sheep,wolf)
            else:
                if len(sheep)-1 > len(wolf): # 현재 늑대의 수가 양보다 적을때만 늑대가 있는곳으로 갈수있다.
                    if i not in wolf:
                        find(i,sheep,wolf+[i])
                    else:
                        find(i,sheep,wolf)
    # 루트 부터 시작
    find(0,[0],[])
    return max(result)

solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]])