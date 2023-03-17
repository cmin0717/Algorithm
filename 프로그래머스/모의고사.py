def solution(aw):
    a = [1,2,3,4,5] * (len(aw) //  5 + 1)
    b = [2,1,2,3,2,4,2,5] * (len(aw) //  8 + 1)
    c = [3,3,1,1,2,2,4,4,5,5] * (len(aw) // 10 + 1)
    answer = [0,0,0]
    for i in range(len(aw)):
        if a[i] == aw[i] : answer[0] += 1
        if b[i] == aw[i] : answer[1] += 1
        if c[i] == aw[i] : answer[2] += 1
    answer = [i+1 for i in range(len(answer)) if answer[i] == max(answer)]
    return answer