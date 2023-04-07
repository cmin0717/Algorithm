import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

sensor = list(map(int, input().split()))
sensor.sort()
section = [sensor[i+1] - sensor[i] for i in range(n-1)] #앞뒤 간격으로 리스트를 만듬
section.sort() 

total = sum(section[:n-k]) # 간격이 큰거 부터 차례로 뺴면 답 나옴옴
print(total)