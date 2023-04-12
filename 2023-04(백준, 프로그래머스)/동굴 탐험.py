def solution(n, path, order):
    link = [[] for _ in range(n)]

    for x,y in path:
        link[x].append(y)
        link[y].append(x)
    
    # 선행 조건이 있는 애들은 미리 선행조건리스트에 넣어둔다.
    orders = [0] *n
    for x,y in order:
        orders[y] = x
    
    cnt = 0
    visit = [0]*n
    check = [0] # 0을 루트 노드로 시작
    after = {} # 현재 선행조건을 만족하지 못해 가지 못하는 노드를 저장

    while check:
        now = check.pop()

        # 만일 선행 조건이 있고 그 조건을 방문하지 않았다면 after에 넣어두고 다른 노드부터 간다.
        if orders[now] and not visit[orders[now]]:
            after[orders[now]] = now
            continue
        # 현재 갈수 있다면 cnt,visit 처리 해준다.
        cnt += 1
        visit[now] = 1

        # 현재 노드에 연결된 노드들중에 방문하지 않은 노드들만 check에 넣어준다.
        for i in link[now]:
            if not visit[i]:
                check.append(i)

        # 만일 현재 노드가 선행조건에 해당하는 노드라면 after에서 선행조건이 완료된 노드를 check에 넣어준다.
        if now in after:
            check.append(after[now])

    # 다 확인후 방문 노드가 총 노드랑 같다면 True아니라면 어딘가에서 사이클이 형성되었기에 가지 못하는 상황이다.
    return cnt == n