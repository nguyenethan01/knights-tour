import board
import logic




if __name__ == "__main__":
    test = board.Board(6,6)
    logic.knights_tour(2,3,test)
