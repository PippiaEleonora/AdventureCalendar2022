
class Tetris:
    def __init__(self,Flux) -> None:
        self.Borad = []
        self.Flux = str(Flux[0])
        self.column = []
        self.repeatFlux = []
        self.saveFlux = -1
        self.repeat = 0
        self.count = 1
        self.max_count = 1
        
    def fall(self,rock_type,n_flow,heigh):
        
        for i in range(3- (len(self.Borad)-heigh)):
            self.Borad.insert(0,[0,0,0,0,0,0,0])
   
        if rock_type == 1:
            position = [3,2]
        else:
            position = [2,2]
        shift = 0
        for i in range(3):
            if self.Flux[n_flow] == '<':
                shift = -1
            elif self.Flux[n_flow] == '>':
                shift = 1
            else:
                print('error!')
            
            if rock_type == 0:
                position[0] = max(0,min(3,position[0]+shift))
            elif rock_type == 1:
                position[0] = max(1,min(5,position[0]+shift))
            elif rock_type == 2:
                position[0] = max(0,min(4,position[0]+shift))
            elif rock_type == 3:
                position[0] = max(0,min(6,position[0]+shift))
            else:
                position[0] = max(0,min(5,position[0]+shift))
                
            n_flow += 1
            if n_flow == len(self.Flux):
                n_flow  = 0
               
        
        
        falling = True
        while falling:
            if rock_type == 0: 
                ####
                if self.Flux[n_flow] == '<' and position[0]>0:
                    if not self.Borad[position[1]][position[0]-1]:
                        position[0] -= 1
                elif self.Flux[n_flow] == '>' and position[0]+3<6:
                    if not self.Borad[position[1]][position[0]+4]:
                        position[0] += 1

                if position[1]+1 == len(self.Borad) or any(self.Borad[position[1]+1][position[0]:position[0]+4]):
                    for i in range(4):
                        self.Borad[position[1]][position[0]+i] = 1
                    return max(heigh, len(self.Borad)-position[1]), n_flow
                else:
                    position[1] += 1
                
            elif rock_type == 1: 
                 #
                ###
                 #
                if self.Flux[n_flow] == '<' and position[0]-1>0:
                    if not any([self.Borad[position[1]][position[0]-1],self.Borad[position[1]-1][position[0]-2],self.Borad[position[1]-2][position[0]-1]]):
                        position[0] -= 1
                elif self.Flux[n_flow] == '>' and position[0]+1<6:
                    if not any([self.Borad[position[1]][position[0]+1],self.Borad[position[1]-1][position[0]+2],self.Borad[position[1]-2][position[0]+1]]):
                        position[0] += 1

                if position[1]+1 == len(self.Borad) or any([self.Borad[position[1]+1][position[0]], self.Borad[position[1]][position[0]-1], self.Borad[position[1]][position[0]+1]]):
                    self.Borad[position[1]][position[0]] = 2
                    for i in range(3):
                        self.Borad[position[1]-1][position[0]-1+i] = 2
                    self.Borad[position[1]-2][position[0]] = 2
                    return max(heigh, len(self.Borad)-position[1]+2), n_flow
                else:
                    position[1] += 1

            elif rock_type == 2:
                  #
                  #
                ###    
                if self.Flux[n_flow] == '<' and position[0]>0:
                    if not any([self.Borad[position[1]][position[0]-1],self.Borad[position[1]-1][position[0]+1],self.Borad[position[1]-2][position[0]+1]]):
                        position[0] -= 1
                elif self.Flux[n_flow] == '>' and position[0]+2<6:
                    if not any([self.Borad[position[1]][position[0]+3], self.Borad[position[1]-1][position[0]+3], self.Borad[position[1]-2][position[0]+3]]):
                        position[0] += 1

                if position[1] == len(self.Borad)-1 or any(self.Borad[position[1]+1][position[0]:position[0]+3]):
                    self.Borad[position[1]][position[0]] = 3
                    self.Borad[position[1]][position[0]+1] = 3
                    for i in range(3):
                        self.Borad[position[1]-i][position[0]+2] = 3
                    return max(heigh, len(self.Borad)-position[1]+2), n_flow
                else:
                    position[1] += 1
                
            elif rock_type == 3:
                #
                #
                #
                #
                if self.Flux[n_flow] == '<' and position[0]>0:
                    if not any([self.Borad[position[1]][position[0]-1],self.Borad[position[1]-1][position[0]-1],self.Borad[position[1]-2][position[0]-1],self.Borad[max(0,position[1]-3)][position[0]-1]]):
                        position[0] -= 1
                elif self.Flux[n_flow] == '>' and position[0]<6:
                    if not any([self.Borad[position[1]][position[0]+1],self.Borad[position[1]-1][position[0]+1],self.Borad[position[1]-2][position[0]+1],self.Borad[max(0,position[1]-3)][position[0]+1]]):
                        position[0] += 1

                if position[1] == len(self.Borad)-1 or self.Borad[position[1]+1][position[0]]:
                    for i in range(4):
                        if position[1]-i<0:
                            self.Borad.insert(0,[0,0,0,0,0,0,0])
                            self.Borad[0][position[0]] = 4
                            position[1] += 1
                        else:
                            self.Borad[position[1]-i][position[0]] = 4
                    return max(heigh, len(self.Borad)-position[1]+3), n_flow
                else:
                    position[1] += 1
            
            elif rock_type == 4:
                ##
                ##
                if self.Flux[n_flow] == '<' and position[0]>0:
                    if not any([self.Borad[position[1]][position[0]-1],self.Borad[position[1]-1][position[0]-1]]):
                        position[0] -= 1
                elif self.Flux[n_flow] == '>' and position[0]+1<6:
                    if not any([self.Borad[position[1]][position[0]+2],self.Borad[position[1]-1][position[0]+2]]):
                        position[0] += 1

                if position[1] == len(self.Borad)-1 or any([self.Borad[position[1]+1][position[0]], self.Borad[position[1]+1][position[0]+1]]):
                    for i in range(2):
                        self.Borad[position[1]-i][position[0]] = 5
                        self.Borad[position[1]-i][position[0]+1] = 5
                    

                    if n_flow == self.saveFlux:
                        if self.count == self.max_count:
                            self.repeatFlux += [n_flow]
                            self.column += [max(heigh, len(self.Borad)-position[1]+1)] 
                            idx = [i for i in range(len(self.repeatFlux)) if self.repeatFlux[i]==n_flow]
                            if self.Borad[len(self.Borad)-self.column[idx[self.max_count*2]]:len(self.Borad)-self.column[idx[self.max_count]]] == self.Borad[len(self.Borad)-self.column[idx[self.max_count]]:len(self.Borad)-self.column[idx[0]]]:
                                self.repeat = 1
                                return max(heigh, len(self.Borad)-position[1]+1), n_flow
                            else:
                                del self.repeatFlux[len(self.repeatFlux)-1]
                                del self.column[len(self.column)-1]
                                del self.repeatFlux[0:idx[1]]
                                del self.column[0:idx[1]]
                                self.max_count += 1
                                self.count = 0
                        else:
                            self.count += 1
                    if n_flow in self.repeatFlux and self.saveFlux==-1:
                        self.saveFlux = n_flow
                    self.repeatFlux += [n_flow]
                    self.column += [max(heigh, len(self.Borad)-position[1]+1)]    
                    
                    return max(heigh, len(self.Borad)-position[1]+1), n_flow
                else:
                    position[1] += 1
            
            n_flow += 1
            if n_flow==len(self.Flux):
                n_flow = 0

                
                    

if __name__ == "__main__":
    with open('input17.txt') as f:
        arrayRaw = f.readlines()
        
    t = Tetris(arrayRaw)
    
    rock_type = 0
    n_flow = 0
    heigh = 0
    for i in range(1000000000000):
        start_flow = n_flow
        heigh_old = heigh
        heigh, n_flow = t.fall(rock_type,n_flow,heigh)
        if t.repeat:
            idx = [i for i in range(len(t.repeatFlux)) if t.repeatFlux[i]==n_flow]
            h_add = t.column[idx[t.max_count]]-t.column[idx[0]]
            missing_rocks = 1000000000000 - i-1
            rocks_rep = (idx[t.max_count]-idx[0])*5
            n_complete_rep = missing_rocks//rocks_rep
            id_last_rocks = (missing_rocks-n_complete_rep*rocks_rep)//5
            print(h_add*n_complete_rep + heigh + t.column[idx[0]+id_last_rocks]-t.column[idx[0]])
            break
        rock_type += 1
        n_flow += 1
        if len(t.Flux) == n_flow:
            n_flow = 0

        if rock_type == 5:
            rock_type = 0
    print(heigh)
        
