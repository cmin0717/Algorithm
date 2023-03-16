def solution(participant, completion):
    names = {}
    
    for i in participant:
        if names.get(i) == None:
            names[i] = 1
        else:
            names[i] += 1

    for i in completion:
        names[i] -= 1

    for i in participant:
        if names[i] != 0:
            return i