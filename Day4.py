with open('input4.txt') as f:
    arrayRaw = f.readlines()
    
array = [[y.split("-") for y in x.replace("\n","").split(",")] for x in arrayRaw]
Camp = [[int(id) for id in pair[0]+pair[1]] for pair in array ]

Overlap = [1 if field[0]<=field[2] and field[1]>=field[3] else 1 if field[2]<=field[0] and field[3]>=field[1] else 0 for field in Camp]
print(sum(Overlap))

NoOverlap = [1 if field[1]<field[2] else 1 if field[0]>field[3] else 0 for field in Camp]
print(len(NoOverlap) - sum(NoOverlap))
