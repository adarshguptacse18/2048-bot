import numpy as np
n=4
dirs=[UP,DOWN,LEFT,RIGHT]=range(4)

def merge(a):
    for i in range(4):
        for j in range(3):
            if(a[i][j]==a[i][j+1] and a[i][j]!=0):
                a[i][j]*=2
                a[i][j+1]=0
    return a
def justify_left(a):
    out=np.zeros((n,n))
    for i in range(4):
        c=0
        for j in range(4):
            if(a[i][j]):
                out[i][c]=a[i][j]
                c+=1
    return out

class GameBoard:
    def __init__(self):
        self.grid=np.zeros((n,n))

    def clone(self):
        grid_copy=GameBoard()
        grid_copy.grid=np.copy(self.grid)
        return grid_copy

    def insert_tile(self,pos,value):
        self.grid[pos[0]][pos[1]]=value
    
    def get_available_cells(self):
        cells=[]
        for i in range(4):
            for j in range(4):
                if(self.grid[i][j]==0):
                    cells.append((i,j))
        return cells
    
    def get_max_tile(self):
        return np.max(self.grid)
    
    def move(self,dir):
        if(dir==UP):
            self.grid=self.grid.T
            self.grid=justify_left(self.grid)
            self.grid=merge(self.grid)
            self.grid=justify_left(self.grid)
            self.grid=self.grid.T
        if(dir==DOWN):
            self.grid=self.grid[::-1,::]
            self.grid=self.move(UP)
            self.grid=self.grid[::-1,::]
        if(dir==RIGHT):
            self.grid=self.grid[::,::-1]
            self.grid=justify_left(self.grid)
            self.grid=merge(self.grid)
            self.grid=justify_left(self.grid)
            self.grid=self.grid[::,::-1]
        if(dir==LEFT):
            self.grid=justify_left(self.grid)
            self.grid=merge(self.grid)
            self.grid=justify_left(self.grid)
        return self.grid
    def get_available_moves(self):
        a=self.clone()
        moves=[]
        save=np.copy(a.grid)
        a.move(UP)
        if((save==a.grid).all()):
            pass
        else:
            moves.append(UP)
        a.grid=np.copy(save)
        a.move(DOWN)
        if((save==a.grid).all()):
            pass
        else:
            moves.append(DOWN)
        a.grid=np.copy(save)
        a.move(LEFT)
        if((save==a.grid).all()):
            pass
        else:
            moves.append(LEFT)
        a.grid=np.copy(save)
        a.move(RIGHT)
        if((save==a.grid).all()):
            pass
        else:
            moves.append(RIGHT)
        return moves