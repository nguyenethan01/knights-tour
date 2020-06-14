#this file holds the declaration of the board class, a way to modularize code

class Board:
    def __init__(self,row:int,col:int):
        self.row = row
        self.col = col
        self.currMove = 0
        self.array = [[-1 for x in range(col)] for x in range(row)] 

    def __str__(self):
        """
            print string representation of current board
        """
        ans = ""
        for i in range(self.row):
            for j in range(self.col):
                ans+=str(self.array[i][j])+" "
            ans+="\n"
        return ans

    def make_move(self, row:int, col:int):
        """
            Given an row and col coordinate, move the knight to the given position and update array pos to currMove and increment currMove
        """
        self.array[row][col] = self.currMove
        self.currMove+=1

    def is_valid(self,row,col) -> bool:
        """
            Used to check if proposed move / position is valid in the given board dimensions
        """
        if(row >=0 and col>=0 and row<self.row and col<self.col):
            return True
        return False

    def get_row(self):
        return self.row
    
    def get_col(self):
        return self.get_col
    
    def get_currMove(self):
        return self.currMove