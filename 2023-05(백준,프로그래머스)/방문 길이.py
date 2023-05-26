def solution(dirs):
    dic = {}
    x,y = 0,0
    for c in dirs:
        if c == 'U':
            if y+1 <= 5:
                dic[(x,y,x,y+1)] = 1
                dic[(x,y+1,x,y)] = 1
                y += 1
        elif c == 'D':
            if y-1 >= -5:
                dic[(x,y,x,y-1)] = 1
                dic[(x,y-1,x,y)] = 1
                y -= 1
        elif c == 'L':
            if x-1 >= -5:
                dic[(x,y,x-1,y)] = 1
                dic[(x-1,y,x,y)] = 1
                x -= 1
        else:
            if x+1 <= 5:
                dic[(x,y,x+1,y)] = 1
                dic[(x+1,y,x,y)] = 1
                x += 1
    return len(dic.keys()) // 2