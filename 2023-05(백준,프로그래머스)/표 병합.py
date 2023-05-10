def solution(commands):
    dic,result = {}, [] # 표를 저장할 딕셔너리와 결과를 담을 배열 생성

    # 표의 크기가 50 * 50으로 정해졌기에 미리 딕셔너리에 세팅해둔다.
    for i in range(1,51):
        for j in range(1,51):
            k = f"{str(i)}-{str(j)}"
            # 딕셔너리 벨류로는 해당 위치의 값과 병합된 애들의 좌표를 저장할set자료형
            dic.setdefault(k,['EMPTY',set()])
            dic[k][1].add(k)
    
    # 해당 좌표값 업데이트
    def update(xy,value):
        for i in dic[xy][1]:
                dic[i][0] = value
    
    # 해당 벨류값 업데이트
    def update1(v1,v2):  
        for k in dic.keys():
            if dic[k][0] == v1:
                dic[k][0] = v2
    
    # 각 좌표끼리 병합
    def merge(xy,xy2):
        v = dic[xy][0] if dic[xy][0] != 'EMPTY' else dic[xy2][0] # 병합될 셀의 대표값 설정
        # 각 좌표에 대표값 대입
        update(xy,v)
        update(xy2,v)
        # 병합된 셀의 좌표들 저장
        for i in dic[xy2][1]:
            dic[xy][1].add(i)
        for i in dic[xy][1]:
            dic[i][1] = dic[xy][1]
        for i in dic[xy2][1]:
            dic[i][1] = dic[xy][1]
    
    # 병합 해지
    def unmerge(xy):
        # 현재 좌표에 저장될값 미리 변수에 담는다.
        v = dic[xy][0]
        # 병합된 셀의 좌표를 돌면서 초기화
        for i in dic[xy][1]:
            dic[i] = ['EMPTY',set()]
            dic[i][1].add(i)
        dic[xy][0] = v
    
    for command in commands:
        c = command.split()
        
        if c[0] == 'UPDATE' and len(c) == 3:
            update1(c[1],c[2])
            continue
            
        xy = f"{c[1]}-{c[2]}"
        if c[0] == 'UPDATE':
            update(xy,c[3])
        elif c[0] == 'MERGE':
            xy2 = f"{c[3]}-{c[4]}"
            merge(xy,xy2)
        elif c[0] == 'UNMERGE':
            unmerge(xy)
        else:
            result.append(dic[xy][0])
            
    return result
    
solution(["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1","MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"])