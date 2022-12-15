def visibleTree(Visit,TreeGrid,n):
    for i in range(1,n-1):
        for j in range(1,n-1):
            if Visit[i][j] == -1:
                idX = [range(i), range(i+1,n), [i], [i]]
                idY = [[j], [j], range(j), range(j+1,n)]
                Check = [1 if all([TreeGrid[deltaX][deltaY]<TreeGrid[i][j] for deltaX in idX[k] for deltaY in idY[k]]) else 0 for k in range(4)]
                if Check==[0, 0, 0, 0]:
                    Visit[i][j] = 0
                else:
                    Visit[i][j] = 1
    return Visit

def scoreTree(Score,TreeGrid,n):
    for i in range(1,n-1):
        for j in range(1,n-1):
            idX = [range(i-1,-1,-1), range(i+1,n), [i], [i]]
            idY = [[j], [j], range(j-1,-1,-1), range(j+1,n)]
            
            ScoreDirection = [1, 1, 1, 1]
            for k in range(4):
                if len(idX[k])==1 and len(idY[k]) == 1: #We have just one tree to look at
                    ScoreDirection[k] = 1
                else:
                    tree_direction = [TreeGrid[deltaX][deltaY] for deltaX in idX[k] for deltaY in idY[k]]
                    stop = False
                    t = 0
                    while not stop and t <len(tree_direction):
                        if tree_direction[t]>=TreeGrid[i][j]:
                            ScoreDirection[k] = t+1
                            stop = True
                        t += 1
                    if not stop:
                        ScoreDirection[k] = t
            Score[i][j] = ScoreDirection[0]*ScoreDirection[1]*ScoreDirection[2]*ScoreDirection[3]
                    
    return Score

if __name__ == "__main__":
    with open('input8.txt') as f:
        arrayRaw = f.readlines()
        
    TreeGrid = []
    for line in arrayRaw:
        line = line.replace("\n","")
        TreeGrid += [[int(i) for i in line]]
        
    n = len(TreeGrid)
    # -1 not decided
    # 0 not seeing
    # 1 seeing

    Visit = [[1 if i==0 or i==n-1 else -1 for i in range(n)] if j<n-1 and j>0 else [1 for i in range(n)] for j in range(n)]
    Visit = visibleTree(Visit,TreeGrid,n)
        
    print(sum([sum(r) for r in Visit]))

    # Second Part
    ViewScore = [[0 for j in range(n)] for i in range(n)]
    ViewScore = scoreTree(ViewScore,TreeGrid,n)
    
    print(max([max(V) for V in ViewScore]))
    
