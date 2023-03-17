def check(arr,idx,total,target):
    global cnt

    if idx == len(arr) and total == target:
        cnt += 1
    else:
        if idx < len(arr):
            check(arr,idx+1,total-arr[idx],target)
            check(arr,idx+1,total+arr[idx],target)
        
cnt = 0
def solution(numbers, target):
    check(numbers,0,0,target)
    return cnt