f = open("/uploads/Input10.txt")
Array = f.readlines()

count = [1]
curr_tot = [1]
time = [0]
time_real = 0
for line in Array:
    if "noop" in line:
        count.append(0)
        curr_tot.append(sum(count))
        time.append(time_real + 1)
        time_real += 1
    else:
        line = line.replace("\n","").replace("addx ", "")
        count. append(int(line)) 
        curr_tot.append(sum(count)) 
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

#Second part
Board = [['.']*40, ['.']*40, ['.']*40, ['.']*40, ['.']*40, ['.']*40]
t = 0
for i in range(240):
    if i == time[t+1]:
        t += 1
    if abs(curr_tot[t]-(i%40)) < 2:
        Board[i//40][i%40] = '#'
        

Board2 = ["".join(k) for k in Board]
print("\n".join(Board2))
