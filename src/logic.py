#this is where all of the back-tracking logic of the knight's tour will reside
import board


def knightsTour(col,row,board:board.Board):
    """
    This function calculates the solution to the knight's tour given starting position (col,row) and a chess board
    """
    #these two arrays represent all possible moves a knight can make when both accessed with an index at the same time. For example, accessing index 0 would represent the move in which the x value is increased by two and the y value is increased by 1 
    x_moves = [2,1,-1,-2,-2,-1,1,2]
    y_moves = [1,2,2,1,-1,-2,-2,-1]



    #set initial position (x,y) to 0
    board.make_move()