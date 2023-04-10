def solution(board, moves):
    box = [[] for _ in range(len(board[0]))]
    for i in board[::-1]:
        for j in range(len(i)):
            if i[j] != 0:
                box[j].append(i[j])
    result = 0
    check = []
    
    for i in moves:
        if box[i-1]:
            check.append(box[i-1].pop())
        else:
            continue
        
        while len(check) > 1:
            if check[-1] == check[-2]:
                result += 2
                check.pop()
                check.pop()
            else:
                break
                
    return result