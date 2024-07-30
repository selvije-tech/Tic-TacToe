from src.game import TicTacToeGame
from src.gui import TicTacToeBoard
from src.sound import Sound


def main():
    game = TicTacToeGame()
    board = TicTacToeBoard(game)
    board.mainloop()
    sound_mana = Sound()
    sound_mana.cleanup()


if __name__ == "__main__":
    main()


