from collections import deque

def solution(n, t, m, timetable):
    
    time = []
    
    # 주어진 시간을 분으로 모두 변환후 정렬시킨다.
    for i in timetable:
        hour,minute = i.split(':') 
        time.append(int(hour)*60 + int(minute))
    time.sort()
    
    time = deque(time)
    bus = []
    now = 540 # 첫 버스는 항상 9시 고정
    
    for i in range(n):
        check = []
        # 버스가 주어진 순서대로 오면 넣을수 있을만큼 태워서 보낸다.
        while len(check) < m:
            if time and time[0] <= now:
                check.append(time.popleft())
            else:
                break
        # 만일 버스자리가 남는다면 맥스 시간으로 채워넣는다.
        check += [now+1]*(m-len(check))
        bus.append([now,check])
        now += t

    # 마지막 버스의 마지막 사람보다 빠르게 가면 제일 늦게 탈수있으므로 마지막 버스 마지막 사람의 시간에서 -1한 시간을 출력
    hour, minute = divmod(bus[-1][1][-1]-1, 60)  
    hour = '0'+str(hour) if len(str(hour)) == 1 else str(hour)
    minute = '0'+str(minute) if len(str(minute)) == 1 else str(minute)
    return hour + ':' + minute
        
        
            
        