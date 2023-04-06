# 문자열 시간을 인트형 분시간으로 변경
def trans(t):
    h,m = t.split(':')
    return int(h) * 60 + int(m)

def solution(time):
    answer = [[] for _ in range(len(time))]
    time.sort() # 입실 시간이 빠른것부터 처리

    for s,e in time:
        s = trans(s)
        e = trans(e)
        
        for i in range(len(time)):
            if len(answer[i]) == 0 or answer[i][-1] <= s: # 방이 비어있거나 이미 퇴실한 방이면 입실
                answer[i].append(int(e+10)) # 청소시간 까지 더 한 값으로 변경
                break

    for i in range(len(time)):
        if len(answer[i]) == 0:
            return i
    return len(time)

solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]])