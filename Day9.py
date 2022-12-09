f = open("/uploads/Input9.txt")
Array = f.readlines()

x_H, y_H = 0, 0
x_T, y_T = 0, 0

Visited = [[0,0]]
for line in Array:
    move = line.replace("\n","").split(" ")
    for k in range(int(move[1])):
        if move[0] == "U":
            y_H += 1
            if y_H > y_T + 1:
                y_T += 1
                x_T = x_H
        elif move[0] == "D":
            y_H -= 1
            if y_H < y_T - 1:
                y_T -= 1
                x_T = x_H
        elif move[0] == "L":
            x_H -= 1
            if x_H < x_T - 1:
                x_T -= 1
                y_T = y_H
        elif move[0] == "R":
            x_H += 1
            if x_H > x_T + 1:
                x_T += 1
                y_T = y_H
        if not [x_T, y_T] in Visited:
            Visited.append([x_T, y_T])
       
#print(Visited)  
print(len(Visited))

x_R, y_R = [0]*10, [0]*10

Visited = [[0,0]]
for line in Array:
    move = line.replace("\n","").split(" ")
    for k in range(int(move[1])):
        if move[0] == "U":
            y_R[0] += 1
        elif move[0] == "D":
            y_R[0] -= 1
        elif move[0] == "L":
            x_R[0] -= 1
        elif move[0] == "R":
            x_R[0] += 1
        for t in range(1,10):
            if move[0] == "U":
                if y_R[t-1] > y_R[t] + 1:
                    y_R[t] += 1
                    x_R[t] = x_R[t-1]
            elif move[0] == "D":
               if y_R[t-1] < y_R[t] - 1:
                y_R[t] -= 1
                x_R[t] = x_R[t-1]
            elif move[0] == "L":
                if x_R[t-1] < x_R[t] - 1:
                   x_R[t] -= 1
                   y_R[t] = y_R[t-1]
            elif move[0] == "R":
               if x_R[t-1] > x_R[t] + 1:
                x_R[t] += 1
                y_R[t] = y_R[t-1]
        if not [x_R[9], y_R[9]] in Visited:
            Visited.append([x_R[9], y_R[9]])
       
print(len(Visited))
