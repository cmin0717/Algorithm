def solution(n, build_frame):
    result = []
    
    def check(x,y,ty):
        # 기둥을 건설하기 위해서는 바닥이거나, 아래 기둥이 있거나, 아래 보가 깔려있을때만 가능하다.
        if ty == 0:
            if y == 0 or [x-1,y,1] in result or [x,y-1,0] in result or [x,y,1] in result:
                return [x,y,ty]
        # 보를 설치하기 위해서는 사이드에 기둥이 하나라도 있거나, 양쪽으로 보가 있을때만 가능하다.
        else:
            if [x,y-1,0] in result or [x+1,y-1,0] in result or ([x-1,y,1] in result and [x+1,y,1] in result):
                return [x,y,ty]
        return False
    
    for x,y,ty,p in build_frame:
        # 설치할때는 check함수를 이용하여 설치가 가능한지 판단후 가능하면 result에 넣어준다.
        if p == 1:
            temp = check(x,y,ty)
            if temp:
                result.append(temp)
        # 삭제시에는 일단 삭제하고 현재 건설된 애들을 다시한번 체크한다. 만일 체크 도중 건설된 애들중 실패하는 애들이 있다면 삭제를 다시 추가
        else:
            result.remove([x,y,ty])
            for i in result:
                if not check(*i):
                    result.append([x,y,ty])
                    break

    return sorted(result)
solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])