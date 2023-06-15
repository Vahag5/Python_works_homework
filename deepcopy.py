def deepcopy(ls):
    qanak = len(ls)
    ls2 = []
    for i in range(qanak): 
        if type(ls[i]) == list:
            ls2.append(ls[i].copy())     #karanq  senc el ls2[i] = ls[i].copy()
            for j in range(len(ls[i])):
                if type(ls[i][j]) == list:
                    ls2[i][j] = ls[i][j].copy()
        else:
            ls2.append(ls[i])
    
    return ls2

# Phordzenq ashxatacnenq

ls = [1, 2, [[1,2,3], 4, 6], 'hello']
ls2 = deepcopy(ls)
ls2[2][0][1] = 5
print(ls) # tpeluya ` [1, 2, [[1, 2, 3], 4, 6], 'hello']
print(ls2) # tpeluya ` [1, 2, [[1, 5, 3], 4, 6], 'hello']
