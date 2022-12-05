f = open("/uploads/Input4.txt", "r")
Packs = f.readlines()
#Packs = Packs[0].split(" ") 

## First part
dimension = [len(p)-1 for p in Packs]
Front = [p[0:round(d/2) ] for d, p in zip(dimension,Packs)] 
Back = [p[round(d/2)::].replace("\n","") for d, p in zip(dimension,Packs)]

Obj = [""]*len(Front)
for i in range(len(Front)):
    for f in Front[i]:
        if f in Back[i]:
            Obj[i] = f
Priority = [ord(x)-96 if ord(x)>96 else ord(x) - 64+26 for x in Obj]
print(sum(Priority))

# Mode 2                
Obj = [list(set(x).intersection(set(y)))[0] for x, y in zip(Front, Back)]
Priority = [ord(x)-96 if ord(x)>96 else ord(x) - 64+26 for x in Obj]
print(sum(Priority))

            


## Second part
Elf1 = [Packs[i].replace("\n","")  for i in range(len(Packs))  if i%3==0] 
Elf2 = [Packs[i].replace("\n","")  for i in range(len(Packs))  if i%3==1] 
Elf3 = [Packs[i].replace("\n","") for i in range(len(Packs))  if i%3==2] 

Obj = [""]*len(Elf1)
for i in range(len(Elf1)):
    for f in Elf1[i]:
        if f in Elf2[i] and f in Elf3[i]:
            Obj[i] = f
                
            
Priority = [ord(x)-96 if ord(x)>96 else ord(x) - 64+26 for x in Obj]
print(sum(Priority))

#Mode 2
Obj = [list(set(x).intersection(set(y).intersection(set(z))))[0] for x, y, z in zip(Elf1, Elf2, Elf3)]
Priority = [ord(x)-96 if ord(x)>96 else ord(x) - 64+26 for x in Obj]
print(sum(Priority)) 
