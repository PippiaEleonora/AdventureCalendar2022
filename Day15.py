import re
import pandas as pd

if __name__ == "__main__":
    with open('input15.txt') as f:
        arrayRaw = f.readlines()
        
    Input = [re.findall(r'[-+]?\d+', line) for line in arrayRaw]
    X_sensor = []
    Y_sensor = []
    Beacon = set()
    Distance = []
    n = len(Input)
    for info in Input:
        X_sensor += [int(info[0])]
        Y_sensor += [int(info[1])]
        Beacon.add((int(info[2]), int(info[3])))
        Distance += [abs(int(info[0])-int(info[2])) + abs(int(info[1])-int(info[3]))]
    
    s = 2000000
    Lb = []
    Ub = []
    for i in range(n):
        if Y_sensor[i]-Distance[i]<s and Y_sensor[i]+Distance[i]>s:
            lb_curr = X_sensor[i]-abs(Distance[i]-abs(Y_sensor[i]-s))
            ub_curr = X_sensor[i]+abs(Distance[i]-abs(Y_sensor[i]-s))
            if len(Lb)==0:
                Lb += [lb_curr]
                Ub += [ub_curr]
            else:
                curr = 0
                stop = False
                while curr<len(Lb) and (not stop):
                    if ub_curr<Lb[curr]:
                        Lb.insert(curr, lb_curr)
                        Ub.insert(curr, ub_curr)
                        stop = True
                    elif lb_curr<Lb[curr]:
                        Lb[curr] = lb_curr
                        if ub_curr>Ub[curr]:
                            Ub[curr] = ub_curr
                            for k in range(curr+1,len(Lb)):
                                if Lb[k]<ub_curr:
                                    Ub[k-1] = Lb[k]-1
                        stop = True
                    elif lb_curr<=Ub[curr]:
                        if  ub_curr>Ub[curr]:
                            Ub[curr] = ub_curr
                            for k in range(curr+1,len(Lb)):
                                if Lb[k]<ub_curr:
                                    Ub[k-1] = Lb[k]-1
                        stop = True
                    else:
                        curr += 1
                if not stop:
                    Lb += [lb_curr]
                    Ub += [ub_curr]
    
    occupated = 0            
    for i in range(n):
        if Y_sensor[i]==s:
            occupated += sum([1 for j in range(len(Lb)) if X_sensor[i]>=Lb[j] and X_sensor[i]<=Ub[j]])                    
    for b in Beacon:
        if b[1]==s:
            occupated += sum([1 for j in range(len(Lb)) if b[0]>=Lb[j] and b[0]<=Ub[j]])
    free = sum([Ub[i]-Lb[i]+1 for i in range(len(Lb))])

    print(free-occupated)

    SensorInfo = [[x,y,z,y-z,y+z] for x,y,z in sorted(zip(X_sensor, Y_sensor, Distance), key=lambda pair: pair[1]-pair[2])]
    
    # Second Part
    
    
    for s in range(0,4000001):
        Lb = [0]
        Ub = [4000000]
        for i in range(n):
            if SensorInfo[i][3]<=s and SensorInfo[i][4]>=s:
                delta = abs(SensorInfo[i][2]-abs(SensorInfo[i][1]-s))
                lb_curr = SensorInfo[i][0]-delta
                ub_curr = SensorInfo[i][0]+delta
                idx=0
                stop = False
                while idx<len(Lb) and not stop:
                    if lb_curr<= Lb[idx] and ub_curr>=Ub[idx]:
                        del Ub[idx]
                        del Lb[idx]
                    elif lb_curr>Lb[idx]:
                        if ub_curr<Ub[idx]:
                            Lb.insert(idx+1, ub_curr+1)
                            Ub.insert(idx+1, Ub[idx])
                            Ub[idx] = lb_curr-1
                            stop = True
                        else:
                            Ub[idx] = lb_curr-1
                            idx += 1
                    else:
                        Lb[idx] = ub_curr+1
                        stop = True
        if len(Lb)>0:
            boh=1
            print(Lb[0]*4000000+s)
            break
