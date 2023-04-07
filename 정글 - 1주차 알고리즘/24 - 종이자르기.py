def test():
    w,h = map(int,input().split())
    n = int(input())

    w_list = []
    h_list = []
    for i in range(n):
        a,b = map(int,input().split())
        if a == 1:
            h_list.append(b)
        else:w_list.append(b)
    cut = [[],[]]

    w_list.sort(reverse=True)
    h_list.sort(reverse=True)

    for i in w_list:
        cut[0].append(h-i)
        h = i
    cut[0].append(h)
    for i in h_list:
        cut[1].append(w-i)
        w = i
    cut[1].append(w)

    print(max(cut[0]) * max(cut[1]))

    return

test()


    

