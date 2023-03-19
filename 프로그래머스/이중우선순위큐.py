from collections import deque

def solution(op):
    result = deque([])
    
    for i in op:
        x,num = i.split(' ')
        # 요소 삽입(삽입 정렬 이용)
        if x == 'I':
            if len(result) == 0:
                result.append(int(num))
                continue
            for j in range(len(result)):
                if int(num) <= result[j]:
                    result.insert(j,int(num))
                    break
            else:
                result.insert(j+1,int(num))
        # 최댓값 삭제        
        elif x == 'D' and num == '1' and result:
            result.pop()
        # 최솟값 삭제
        elif result:
            result.popleft()

    if result:
        return [result[-1],result[0]]
    else:
        return [0,0]

solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])