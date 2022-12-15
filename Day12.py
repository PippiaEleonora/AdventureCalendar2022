
def calculateDistance(Grid,start,end):
    m = len(Grid)
    n = len(Grid[0])
    Visited = [[0 for i in range(n)] for j in range(m)]
    Distance = [[None for i in range(n)] for j in range(m)]
    queue = {start}
    reachEnd = False
    Distance[start[0]][start[1]] = 0
    while len(queue)>0 and not reachEnd:
        current = queue.pop()
        Visited[current[0]][current[1]] = 1
        if current == end:
            reachEnd = True
        if current[0] == 0:
            idX = [current[0]+1]
            if current[1] == 0:
                adj = [(current[0]+1,current[1]), (current[0],current[1]+1)]
            elif current[1] == n-1:
                adj = [(current[0]+1,current[1]), (current[0],current[1]-1)]
            else: 
                adj = [(current[0]+1,current[1]), (current[0],current[1]-1), (current[0],current[1]+1)]
        elif current[0] == m-1:
            if current[1] == 0:
                adj = [(current[0]-1,current[1]), (current[0],current[1]+1)]
            elif current[1] == n-1:
                adj = [(current[0]-1,current[1]), (current[0],current[1]-1)]
            else: 
                adj = [(current[0]-1,current[1]), (current[0],current[1]-1), (current[0],current[1]+1)]
        else: 
            if current[1] == 0:
                adj = [(current[0]+1,current[1]), (current[0]-1,current[1]), (current[0],current[1]+1)]
            elif current[1] == n-1:
                adj = [(current[0]+1,current[1]), (current[0]-1,current[1]), (current[0],current[1]-1)]
            else: 
                adj = [(current[0]+1,current[1]), (current[0]-1,current[1]), (current[0],current[1]-1), (current[0],current[1]+1)]
    

        for node in adj:
            if Grid[node[0]][node[1]]<=Grid[current[0]][current[1]]+1:
                if not Visited[node[0]][node[1]]:
                    if Distance[node[0]][node[1]] is None:
                        Distance[node[0]][node[1]] = Distance[current[0]][current[1]]+1
                    else:
                        Distance[node[0]][node[1]] = min(Distance[node[0]][node[1]], Distance[current[0]][current[1]]+1)
                    
                    if not node in queue:
                        queue.add(node)
    return Distance

if __name__ == "__main__":
    with open('input12.txt') as f:
        arrayRaw = f.readlines()
      
    Grid = []   
    Visited = [] 
    Distance = []
    count = 0
    for line in arrayRaw:
        line = line.replace("\n","")
        if "S" in line:
            start = (count, line.index("S"))
            line = line.replace("S","a")
        if "E" in line:
            end = (count, line.index("E"))
            line = line.replace("E","z")
        Grid += [[ord(w)-97 for w in line]]
        n = len(line)
        Visited += [[0 for i in range(n)]]
        Distance += [[None for i in range(n)]]
        count += 1
    
    
    Distance = calculateDistance(Grid,start,end)
    print(Distance[end[0]][end[1]])
    
    
    # Second Part
    PossibleStarts = [(i,j) for i in range(len(Grid)) for j in range(n) if Grid[i][j]==0 and not (i,j)==start]   
    
    currVal =  Distance[end[0]][end[1]]
    for s in PossibleStarts:
        Distance = calculateDistance(Grid,s,end)
        if not  Distance[end[0]][end[1]] is None and Distance[end[0]][end[1]]<currVal:
            currVal = Distance[end[0]][end[1]]
    
    print(currVal)
