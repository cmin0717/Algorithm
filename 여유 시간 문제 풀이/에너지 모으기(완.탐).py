import sys
input = sys.stdin.readline

n = int(input())

bead = list(map(int,input().split()))

result = []

def check(arr, energy):
    arr_len = len(arr)

    if arr_len == 2: # 배열의 크기가 2이면 더이상 할 수 없으니 result에 넣고 리턴 
        result.append(energy)
        return
    
    for i in range(1,arr_len-1):
        m = arr[i-1] * arr[i+1] # 해당 인덱스에서 모을수 있는 에너지
        pop_num = arr.pop(i) # 해당 인덱스를 지워주고 값을 저장
        check(arr, energy+m) # 인덱스를 지운 배열과 에너지에 m을 더해줘서 재귀
        arr.insert(i, pop_num) # 다시 해당 인덱스를 넣어주고 다음 인덱스로 넘어간다.

check(bead, 0)
print(max(result))