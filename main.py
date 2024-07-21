from src.game import TicTacToeGame
from src.gui import TicTacToeBoard


def main():
    game = TicTacToeGame()
    board = TicTacToeBoard(game)
    board.mainloop()

if __name__ == "__main__":
    main()

