def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        cut_list = array[commands[i][0]-1:commands[i][1]]
        cut_list.sort()
        answer.append(cut_list[commands[i][2]-1])
    return answer