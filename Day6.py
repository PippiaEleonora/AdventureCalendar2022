with open('input6.txt') as f:
    arrayRaw = f.readlines()

Array = list(arrayRaw[0])
n = len(Array)

startId = 0
checkId = 0

while checkId-startId < 3 and checkId<n:
    char_check = Array[checkId+1]
    for i in range(startId,checkId+1):
        if char_check == Array[i]:
            startId = i+1
    
    checkId = checkId+1
print(checkId+1)
        
# Second part
startId = 0
checkId = 0

while checkId-startId < 13 and checkId<n:
    char_check = Array[checkId+1]
    for i in range(startId,checkId+1):
        if char_check == Array[i]:
            startId = i+1
    
    checkId = checkId+1
print(checkId+1)
        
