#this file holds the declaration of the board class, a way to modularize code

class Board:
    def __init__(self,x:int,y:int):
        self.x = x
        self.y = y
        self.currMove = 0
        self.array = [[-1 for x in range(y)] for x in range(x)] 

    def make_move(self, x:int, y:int):
        """
            Given an x and y coordinate, move the knight to the given position and update array pos to currMove and increment currMove
        """
        self.array[x][y] = self.currMove
        self.currMove+=1

