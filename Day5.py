import re   
    

class Game():
    def __init__(self) -> None:
        self.Board = [['N', 'B', 'D', 'T', 'V', 'G', 'Z', 'J'],  
                    ['S', 'R', 'M', 'D', 'W', 'P', 'F'],
                    ['V', 'C', 'R', 'S', 'Z'],
                    ['R', 'T', 'J', 'Z', 'P', 'H', 'G'],
                    ['T', 'C', 'J', 'N', 'D', 'Z', 'Q', 'F'],
                    ['N', 'V', 'P', 'W', 'G', 'S', 'F', 'M'],
                    ['G', 'C', 'V', 'B', 'P', 'Q'],
                    ['Z', 'B', 'P', 'N'],
                    ['W', 'P', 'J']]
        
    def play_reverse(self, move):
        n = move[0]
        from_id = move[1]-1
        to_id = move[2]-1
        self.Board[to_id] += self.Board[from_id][-1:-n-1:-1]
        self.Board[from_id] = self.Board[from_id][:len(self.Board[from_id]) - n]

    def play_ordered(self, move):
        n = move[0]
        from_id = move[1]-1
        to_id = move[2]-1
        self.Board[to_id] += self.Board[from_id][len(self.Board[from_id]) - n:]
        self.Board[from_id] = self.Board[from_id][:len(self.Board[from_id]) - n]

    def topColumn(self):
        return [b[-1] for b in self.Board]
        

if __name__ == "__main__":
    with open('input5.txt') as f:
        arrayRaw = f.readlines()
        
    Move = [re.findall(r'\d+', line) for line in arrayRaw]
    Move = [[int(i) for i in line] for line in Move]
    Board = Game()
    for i in range(len(Move)):
        Board.play_reverse(Move[i])

    print("".join(Board.topColumn()))
    
    #Second part
    Board = Game()
    for i in range(len(Move)):
        Board.play_ordered(Move[i])

    print("".join(Board.topColumn()))
        
    
