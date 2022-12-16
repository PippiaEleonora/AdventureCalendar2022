import re
import pandas as pd

def addSand(Board,Cmin):
    startL = 0
    startC = 500-Cmin
    stop = False
    nL = len(Board)
    nC = len(Board[0])
    Father = [[[-1,-1] for i in range(nC)] for j in range(nL)]
    
    firstBlock = [l for l in range(nL) if Board[l][startC] == '#']

    for l in range(firstBlock[0]):
        Father[l][startC] = [l-1,startC]
    startL = firstBlock[0]-1
    TotSand = 0
    while not stop:
        if startC==0 or startC==nC-1:
            stop = True
        elif Board[startL+1][startC-1] == '#' and Board[startL+1][startC+1] == '#':
            if startL-1 < 0:
                stop = True
                TotSand += 1
            else:
                Board[startL][startC] = '#'
                TotSand += 1
                firstBlock = [l for l in range(nL) if Board[l][500-Cmin] == '#']
                startL = firstBlock[0]-1
                startC = 500-Cmin
        elif Board[startL+1][startC-1] == '.':
            Father[startL][startC-1] = [startL,startC]
            startC -= 1
            firstBlock = [l for l in range(startL+1,nL) if Board[l][startC] == '#']
            if firstBlock == []:
                stop = True
            else:
                for l in range(startL,firstBlock[0]):
                    Father[l][startC] = [l-1,startC]
                startL = firstBlock[0]-1
        else:
            Father[startL+1][startC+1] = [startL,startC]
            startC += 1
            firstBlock = [l for l in range(startL+1,nL) if Board[l][startC] == '#']
            if firstBlock == []:
                stop = True
            else:
                for l in range(startL,firstBlock[0]):
                    Father[l][startC] = [l-1,startC]
                startL = firstBlock[0]-1
                
        # print(pd.DataFrame(Board))
    return TotSand



if __name__ == "__main__":
    with open('input14.txt') as f:
        arrayRaw = f.readlines()
        
    Path = []
    for line in arrayRaw:
        Path += [re.findall(r'\d+', line)]
        
    PathC = [[int(l[i]) for i in range(0,len(l),2)] for l in Path]
    PathL = [[int(l[i]) for i in range(1,len(l),2)] for l in Path]
    
    Lmax = max([max(t) for t in PathL])
    Cmax = max([max(t) for t in PathC])
    Cmin = min([min(t) for t in PathC])
    
    Board = [['.' for i in range(Cmax-Cmin+1)] for j in range(Lmax+1+2)]
    Emptyness = [['.' for i in range(Cmax-Cmin+1)] for j in range(Lmax+1+2)]
    for l in range(len(PathL)):
        for i in range(1,len(PathC[l])):
            if PathC[l][i-1]==PathC[l][i]:
                if PathL[l][i]>PathL[l][i-1]:
                    for v in range(PathL[l][i-1],PathL[l][i]+1):
                        Board[v][PathC[l][i]-Cmin] = '#'
                        Emptyness[v][PathC[l][i]-Cmin] = '#'
                else:
                    for v in range(PathL[l][i],PathL[l][i-1]+1):
                        Board[v][PathC[l][i]-Cmin] = '#'
                        Emptyness[v][PathC[l][i]-Cmin] = '#'
            elif PathL[l][i-1]==PathL[l][i]:
                if PathC[l][i]>PathC[l][i-1]:
                    if PathC[l][i]-PathC[l][i-1]>1:
                        for v in range(PathC[l][i-1]+1,PathC[l][i]):
                            Emptyness[PathL[l][i]+1][v-Cmin] = '#'
                    for v in range(PathC[l][i-1],PathC[l][i]+1):
                        Board[PathL[l][i]][v-Cmin] = '#'
                        Emptyness[PathL[l][i]][v-Cmin] = '#'
                else:
                    if PathC[l][i-1]-PathC[l][i]>1:
                        for v in range(PathC[l][i]+1,PathC[l][i-1]):
                            Emptyness[PathL[l][i]+1][v-Cmin] = '#'
                    for v in range(PathC[l][i],PathC[l][i-1]+1):
                        Board[PathL[l][i]][v-Cmin] = '#'
                        Emptyness[PathL[l][i]][v-Cmin] = '#'
            else:
                diagonal = 1
    
     
    print(pd.DataFrame(Board))
    
    empty = sum([1 for j in Emptyness for i in j if i == '#'])
    for l in range(len(Emptyness)-2):
        if '###' in ''.join(Emptyness[l]):
            for i in range(len(Emptyness[l])-2):
                if Emptyness[l][i] == '#' and Emptyness[l][i+1] == '#' and Emptyness[l][i+2] == '#' and not Board[l+1][i+1] == '#':
                    Emptyness[l+1][i+1] = '#'
    empty = sum([1 for j in Emptyness for i in j if i == '#'])
    
    
    
    # First part
    nSand = addSand(Board,Cmin)
    print(nSand)
    
    
    
    # Second Part
    print((Lmax+2)*(Lmax+2)-empty)

