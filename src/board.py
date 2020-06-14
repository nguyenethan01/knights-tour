#this file holds the declaration of the board class, a way to modularize code

class Board:
    def __init__(self,x:int,y:int):
        self.x = x
        self.y = y
        self.array = [[0 for x in range(y)] for x in range(x)] 
