import sys
input = sys.stdin.readline # 이거 안했다고 시간이 4000이상 차이가 난다.ㅎ

n = int(input())

conference = [list(map(int,input().split())) for _ in range(n)]
conference.sort(key=lambda x:(x[1],x)) # 정렬 기준을 끝나는 시간, 시작 시간을 기준으로 오름차순이로 정렬

standard = 0
count = 0

for start,end in conference:
    if start >= standard: # 시작 시간이 전 끝나는 시간보다 같거나 클 경우만 진행
        count += 1 # 회의수에 +1해주고
        standard = end # 기준점을 현재 회의가 끝나는 시간으로 갱신

print(count)
