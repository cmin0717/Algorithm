def solution(arr):
    arr = arr + [-1]
    answer = [arr[i] for i in range(len(arr)) if arr[i] != arr[i+1]]
    return answer