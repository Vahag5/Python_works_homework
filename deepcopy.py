
def deepcopy(ls):
    qan = len(ls)
    ls2 = []
    for i in range(qan): 
        if type(ls[i]) == list:
            ls2.append(ls[i].copy())     #karanq  senc el ls2[i] = ls[i].copy()
            for j in range(len(ls[i])):
                if type(ls[i][j]) == list:
                    ls2[i][j] = ls[i][j].copy()
        else:
            ls2.append(ls[i])
    
    print(ls2)
    return ls2

ls = [1, 2, [4, 6], 'hello']
deepcopy(ls)
