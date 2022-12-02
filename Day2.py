
with open('input2.txt') as f:
    arrayRaw = f.readlines()

game = [line.replace("\n", "").split(" ") for line in arrayRaw]

Player1 = [int(x[0].replace("A","1").replace("B","2").replace("C","3")) for x in game]
Player1_lose = [int(x[0].replace("A","2").replace("B","3").replace("C","1")) for x in game]
Player2 = [int(x[1].replace("X","1").replace("Y","2").replace("Z","3")) for x in game]
drew = [1 if x1==x2 else 0 for x1,x2 in zip(Player1,Player2) ]
win = [1 if x1==x2 else 0 for x1,x2 in zip(Player1_lose,Player2) ]
print(sum(Player2)+sum(drew)*3+sum(win)*6)

game_temp = ["".join(x) for x in game]
Player2 = [x if y[1]=="Y" else x%3+1 if y[1]=="Z" else (x-2)%3+1 for x,y in zip(Player1,game)]
# Player2 = [int(x.replace("AX","3").replace("AY","1").replace("AZ","2").replace("BX","1").replace("BY","2").replace("BZ","3").replace("CX","2").replace("CY","3").replace("CZ","1")) for x in game_temp]
drew = [1 if x[1]=="Y" else 0 for x in game ]
win = [1 if x[1]=="Z" else 0 for x in game ]

print(sum(Player2)+sum(drew)*3+sum(win)*6)