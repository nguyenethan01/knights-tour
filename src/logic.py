#this is where all of the back-tracking logic of the knight's tour will reside
import board


def knights_tour(row,col,board:board.Board):
    #these two arrays represent all possible moves a knight can make when both accessed with an index at the same time. For example, accessing index 0 would represent the move in which the x value is increased by two and the y value is increased by 1 
    x_moves = [2,1,-1,-2,-2,-1,1,2]
    y_moves = [1,2,2,1,-1,-2,-2,-1]

    #set initial position (col,row) to 0
    board.make_move(row,col,0)

    #initialize move counter
    curr_move = 1

    #see if solution exists and handle accordingly
    if(knights_tour_helper(board,row,col,x_moves,y_moves,curr_move)):
        print(board.solution)
        print(board)
    else:
        print("NO SOLUTION")

def knights_tour_helper(board:board.Board,x_curr,y_curr,x_moves,y_moves,curr_move)->bool:
    """
    This function calculates the solution to the knight's tour given starting position (col,row) and a chess board. This function returns true if there is a valid solution, else false
    """

    #if all moves have been completed, return list of moves
    if(board.get_currMove() == board.get_col()*board.get_row()):
        return True

    #try all next moves
    for i in range(8):
        x_next = x_curr + x_moves[i]
        y_next = y_curr + y_moves[i]
        if(board.is_valid(x_next,y_next)):
            board.make_move(x_next,y_next) = curr_move
            board.add_solution((x_next,y_next))
            if(knights_tour_helper(board,x_next,y_next,x_moves,y_moves,curr_move+1)):
                return True
            board.array[x_next][y_next] = -1
            board.solution.pop()
    return False
