f = open("/uploads/Input10.txt")
Array = f.readlines()

count = [1]
time = [0]
time_real = 0
for line in Array:
    if "noop" in line:
        count.append(0)
        time.append(time_real + 1)
        time_real += 1
    else:
        line = line.replace("\n","").replace("addx ", "")
        count.append(int(line))
        time.append(time_real + 2)
        time_real += 2
        


Position = 0
TOT = 0
for t in range(6):
    Id = [i for i in range(Position,len(time)) if time[i]<=(20+40*t)]        
    Position = Id[len(Id)-1]
    if time[Position]==20+40*t and count[Position]>0:
        Position -= 1
    TOT += (20+40*t)*sum(count[0:Position+1])


print(TOT) 
