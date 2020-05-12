from board import *
from ai import *
from time import sleep
from random import randint, seed
dirs={
    "UP":UP,
    "DOWN":DOWN,
    "LEFT":LEFT,
    "RIGHT":RIGHT
}
temp=["UP","DOWN","LEFT","RIGHT"]
class CLIRunner:
    def __init__(self,type):
        self.board=GameBoard()
        self.init_game()
    
        if(type=="BOT"):
            self.print_board()
            self.runai()
#             self.board.move(AI().get_move(self.board))
            return;
        self.rungame()
        
    def runai(self):
        while(1):
            moves=self.board.get_available_moves()
            if(len(moves)==0):
                break
            a=AI().get_move(self.board)
            print(temp[a])
            self.board.move(a)
            self.insert_random_tile()
            self.print_board()
#             sleep(0.5)
    def rungame(self):
        self.print_board()
        self.over=False
        while(1):
            print("Enter your move")
            save=self.board.grid
            while((save==self.board.grid).all()):
                s=""
                while(s not in dirs):
                    s=input()
                save=self.board.grid
                self.board.grid=self.board.move(dirs[s])
#             if(self.board.grid==save)
            self.insert_random_tile()
            self.print_board()
            
    def init_game(self):
        self.insert_random_tile()
        self.insert_random_tile()

    
    def print_board(self):
        for i in range(4):
            for j in range(4):
                print("%6d  " % self.board.grid[i][j], end="")
            print("")
        print("")
    
    def insert_random_tile(self):
        value=4
        if randint(0,99)<100*0.9:
            value=2
        cells=self.board.get_available_cells()
        pos=cells[randint(0,len(cells)-1)] if cells else None
        if pos is None:
            return None
        else:
            self.board.insert_tile(pos,value)
            return pos
    