import numpy as np

with open('input20.txt') as f:
    arrayRaw = f.readlines()
    
Input =[int(l.replace('\n',''))*811589153 for l in arrayRaw]
Sorted = Input.copy()
Index = np.array([i for i in range(len(Input))])

for i in range(len(Input)*10):
    index_i = Index[i%len(Input)]
    del Sorted[index_i]
    Index[Index>index_i] = Index[Index>index_i]-1
    new = (index_i+Input[i%len(Input)]) % (len(Input)-1)
    if new == 0:
        new = len(Input)-1
    Sorted.insert(new,Input[i%len(Input)])
    Index[Index>=new] = Index[Index>=new]+1
    Index[i%len(Input)] = new
# print(Sorted)
id0 = Sorted.index(0)
print(Sorted[(id0+1000)%len(Sorted)]+Sorted[(id0+2000)%len(Sorted)]+Sorted[(id0+3000)%len(Sorted)])
