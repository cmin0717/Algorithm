def solution(places):
    
    def check(arr,x,y):
        xy = [[x,y,0]]
        while xy:
            a,b,c = xy.pop()
            
            if c == 2:continue
            
            for i,j in [a+1,b],[a-1,b],[a,b-1],[a,b+1]:
                if 0 <= i < 5 and 0 <= j < 5 and arr[i][j] != 'X':
                    if arr[i][j] == 'P':
                        return False
                    xy.append([i,j,c+1])
        return True
    
    result = []
    
    for i in places:
        place = []
        p = []
        for x in range(5):
            temp = []
            for y in range(5):
                if i[x][y] == 'P':
                    p.append([x,y])
                temp.append(i[x][y])
            place.append(temp)
            
        for a,b in p:
            place[a][b] = 'X'
            if not check(place,a,b):
                result.append(0)
                break
            place[a][b] = 'P'
        else:
            result.append(1)
            
    return result