#this is where all of the back-tracking logic of the knight's tour will reside

def isValid(x,y,board:[[]]) -> bool:
    """
    Used to check if proposed move / position is valid on the given chess board
    """
    if(x >=0 and y>=0 and x<len(board[0]) and y<len(board)):
        return True
    return False

