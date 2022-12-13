import ast

def checkPair (x,y):
    out = -1
    for i in range(len(x)):
        if len(y)<i+1:
            out =  0
            return out
        elif type(x[i]) == list:
            if type(y[i]) == list:
                out = checkPair(x[i],y[i])
                if not (out == -1):
                    return out
            else:
                out = checkPair(x[i],[y[i]])
                if not (out == -1):
                    return out
        elif type(y[i]) == list:
            out = checkPair([x[i]],y[i])
            if not (out == -1):
                return out
        else:
            if x[i]<y[i]:
                out =  1
                return out
            elif x[i]>y[i]:
                out = 0
                return out
    if len(y)>len(x):
            out =  1        
    return out


if __name__ == "__main__":
    with open('input13.txt') as f:
        arrayRaw = f.readlines()
        
    current = 1
    pair1 = []
    pair2 = []
    TotList = []
    for line in arrayRaw:
        if line == "\n":
            pass
        elif current == 1:
            TotList += [ast.literal_eval(line.replace('\n',''))]
            pair1 += [ast.literal_eval(line.replace('\n',''))]
            current = 2
        else:
            TotList += [ast.literal_eval(line.replace('\n',''))]
            pair2 += [ast.literal_eval(line.replace('\n',''))]
            current = 1

        
    Validation = []
    for i in range(len(pair1)):
        Validation.append(checkPair(pair1[i], pair2[i]))

    print(sum([i+1 for i in range(len(Validation)) if Validation[i]==1])) 
    
    
    
    # Second Part
    TotList += [[[2]], [[6]]]      
    Index = []
    OrderedList = [TotList[0]]
    n = len(OrderedList)
    for i in range(1,len(TotList)):
        j = 0
        assigned = False
        while j<n and not assigned:
            out = checkPair(TotList[i], OrderedList[j])
            if out == 1:
                OrderedList.insert(j, TotList[i])
                n += 1
                assigned = True
            else:
                j += 1
        if not assigned and j == n:
            OrderedList.append(TotList[i])
            n += 1
        
        if i == len(TotList)-1 or i == len(TotList)-2:
            Index.append(j+1)
            print("Index: "+str(j+1))
    
    print(Index[0]*Index[1])
