import re   
import numpy as np    

if __name__ == "__main__":
    with open('input18.txt') as f:
        arrayRaw = f.readlines()
    Cubes = [re.findall(r'[-+]?\d+', line) for line in arrayRaw]
    Cubes = [np.array([int(i) for i in line]) for line in Cubes]
    
    tot_sides = 6*len(Cubes)
    touch = 0
    MIN = np.min(Cubes,axis=0)
    MAX = np.max(Cubes,axis=0)
    for i in range(len(Cubes)-1):
        val = np.sum(abs(Cubes[i+1:len(Cubes)]-Cubes[i]),axis=1)
        touch += sum(val==1)*2
    print(tot_sides-touch)
    external_surf = tot_sides-touch
    # Second Part
    Cubes_set = set([tuple(int(i) for i in line) for line in Cubes])
    All_set = set([(i+MIN[0],j+MIN[1],k+MIN[2]) for i in range(MAX[0]-MIN[0]+1) for j in range(MAX[1]-MIN[1]+1) for k in range(MAX[2]-MIN[2]+1)])
    Remain_set = All_set - Cubes_set
    n = 0
    extra_surf = 0
    while len(Remain_set)>0:
        c = Remain_set.pop()
        Group = {c}
        visit = {c}
        outside = 0
        while len(visit)>0:
            curr = visit.pop()
            if curr[0]==MIN[0] or curr[1] ==MIN[1]or curr[2] == MIN[2] or curr[0]==MAX[0] or curr[1] ==MAX[1]or curr[2] == MAX[2] :
                outside = 1
            Adj_set = {tuple(np.array(curr)+np.array([1,0,0])),tuple(np.array(curr)+np.array([-1,0,0])),tuple(np.array(curr)+np.array([0,1,0])),
                tuple(np.array(curr)+np.array([0,-1,0])),tuple(np.array(curr)+np.array([0,0,1])),tuple(np.array(curr)+np.array([0,0,-1]))}
            adj = Adj_set.intersection(Remain_set)
            Remain_set = Remain_set - adj
            Group = Group.union(adj)
            visit = visit.union(adj)
        if not outside:
            surf = 6*len(Group)
            touch = 0
            Group = list(Group)
            for i in range(len(Group)-1):
                val = np.sum(abs(np.array(Group[i+1:len(Group)])-np.array(Group[i])),axis=1)
                touch += sum(val==1)*2
            extra_surf += surf-touch

    print(external_surf-extra_surf)
            

        
        
    
