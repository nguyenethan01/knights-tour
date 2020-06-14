#this file holds the declaration of the board class, a way to modularize code

class Board:
    def __init__(self,x:int,y:int):
        self.x = x
        self.y = y
        self.array = [[-1 for x in range(y)] for x in range(x)] 

    def make_move(self, x:int, y:int, currMove:int):
        """
            Given an x and y coordinate, move the knight to the given position and update array pos to currMove.
        """
        self.array[x][y] = currMove

