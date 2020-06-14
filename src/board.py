#this file holds the declaration of the board class, a way to modularize code

class Board:
    def __init__(self,col:int,row:int):
        self.col = col
        self.row = row
        self.currMove = 0
        self.array = [[-1 for x in range(row)] for x in range(col)] 

    def make_move(self, col:int, row:int):
        """
            Given an col and row coordinate, move the knight to the given position and update array pos to currMove and increment currMove
        """
        self.array[col][row] = self.currMove
        self.currMove+=1

    def isValid(self,col,row) -> bool:
    """
    Used to check if proposed move / position is valid in the given board dimensions
    """
    if(col >=0 and row>=0 and col<self.col and row<self.row):
        return True
    return False