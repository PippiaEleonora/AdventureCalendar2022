
def ComputeVal(Graph, node):
    if type(Graph[node]) == str:
        if '/' in Graph[node]:
            nodes = Graph[node].split(' / ')
            v1 = ComputeVal(Graph,nodes[0])
            v2 = ComputeVal(Graph,nodes[1])
            Graph[node] = v1/v2
        elif '*' in Graph[node]:
            nodes = Graph[node].split(' * ')
            v1 = ComputeVal(Graph,nodes[0])
            v2 = ComputeVal(Graph,nodes[1])
            Graph[node] = v1*v2
        elif '+' in Graph[node]:
            nodes = Graph[node].split(' + ')
            v1 = ComputeVal(Graph,nodes[0])
            v2 = ComputeVal(Graph,nodes[1])
            Graph[node] = v1+v2
        elif '-' in Graph[node]:
            nodes = Graph[node].split(' - ')
            v1 = ComputeVal(Graph,nodes[0])
            v2 = ComputeVal(Graph,nodes[1])
            Graph[node] = v1-v2

    return Graph[node]


def EvalEq(Lista,value):
    if len(Lista)==3:
        if Lista[1] == '*':
            if type(Lista[0]) == list or type(Lista[0]) == str:
                return EvalEq(Lista[0], value/Lista[2])
            else:
                return EvalEq(Lista[2], value/Lista[0])
        elif Lista[1] == '+':
            if type(Lista[0]) == list or type(Lista[0]) == str:
                return EvalEq(Lista[0], value-Lista[2])
            else:
                return EvalEq(Lista[2], value-Lista[0])
        elif Lista[1] == '-':
            if type(Lista[0]) == list or type(Lista[0]) == str:
                return EvalEq(Lista[0], value+Lista[2])
            else:
                return EvalEq(Lista[2], Lista[0]-value)
        elif Lista[1] == '/':
            if type(Lista[0]) == list or type(Lista[0]) == str:
                return EvalEq(Lista[0], value*Lista[2])
            else:
                return EvalEq(Lista[2], value/Lista[0])
    else:
        return value

def ComputeExpression(Graph, node):
    if type(Graph[node]) == str:
        if '/' in Graph[node]:
            nodes = Graph[node].split(' / ')
            v1 = ComputeExpression(Graph,nodes[0])
            v2 = ComputeExpression(Graph,nodes[1])
            if type(v1) == str or type(v2) == str or type(v1)== list or type(v2) == list:
                Graph[node] = [v1, '/' ,v2]
            else:
                Graph[node] = v1/v2
        elif '*' in Graph[node]:
            nodes = Graph[node].split(' * ')
            v1 = ComputeExpression(Graph,nodes[0])
            v2 = ComputeExpression(Graph,nodes[1])
            if type(v1) == str or type(v2) == str or type(v1)== list or type(v2) == list:
                Graph[node] = [v1, '*' ,v2]
            else:
                Graph[node] = v1*v2
        elif '+' in Graph[node]:
            nodes = Graph[node].split(' + ')
            v1 = ComputeExpression(Graph,nodes[0])
            v2 = ComputeExpression(Graph,nodes[1])
            if type(v1) == str or type(v2) == str or type(v1)== list or type(v2) == list:
                Graph[node] = [v1, '+' ,v2]
            else:
                Graph[node] = v1+v2
        elif '-' in Graph[node]:
            nodes = Graph[node].split(' - ')
            v1 = ComputeExpression(Graph,nodes[0])
            v2 = ComputeExpression(Graph,nodes[1])
            if type(v1) == str or type(v2) == str or type(v1)== list or type(v2) == list:
                Graph[node] = [v1, '-' ,v2]
            else:
                Graph[node] = v1-v2
        elif '=' in Graph[node]:
            nodes = Graph[node].split(' = ')
            v1 = ComputeExpression(Graph,nodes[0])
            v2 = ComputeExpression(Graph,nodes[1])
            
            if type(v1) == list:
                Lista = v1
                value = v2
            else:
                Lista = v2
                value = v1
            EvalEq(Lista,value)
            Graph[node] = EvalEq(Lista,value)

    return Graph[node]

if __name__ == "__main__":
    with open('input21.txt') as f:
        arrayRaw = f.readlines()
        
    Monkeys = dict()    
    for i in arrayRaw:
        val = i.replace('\n','').split(': ')
        if val[1].isdigit():
            val[1] = int(val[1])
        Monkeys.update({val[0]: val[1]})
    
    print(ComputeVal(Monkeys,'root'))
    
    # Second Part
    Monkeys = dict()    
    for i in arrayRaw:
        val = i.replace('\n','').split(': ')
        if val[1].isdigit():
            val[1] = int(val[1])
        Monkeys.update({val[0]: val[1]})
    
    Monkeys['root'] = Monkeys['root'].replace('+','=').replace('-','=').replace('*','=').replace('/','=')
    Monkeys['humn'] = 'x'
    print(ComputeExpression(Monkeys,'root'))
