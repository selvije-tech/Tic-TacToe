import tkinter as tk
from tkinter import font
from .game import TicTacToeGame, Move

class TicTacToeBoard(tk.Tk):
    def __init__(self, game: TicTacToeGame):
        super().__init__()
        self.title("Tic-Tac-Toe Game")
        self._cells = {}
        self._game = game
        self._create_layout()

    def _create_layout(self):
        main_frame = tk.Frame(master=self)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Top display with game status
        top_frame = tk.Frame(master=main_frame)
        top_frame.pack(side=tk.TOP, fill=tk.X, pady=10)
        self.display = tk.Label(
            master=top_frame,
            text="Tic-Tac-Toe - Ready?",
            font=font.Font(size=28, weight="bold"),
            bg="lightgrey",
            padx=10,
            pady=10
        )
        self.display.pack()

        # Frame for the grid (left side)
        grid_frame = tk.Frame(master=main_frame)
        grid_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
        self._create_board_grid(grid_frame)

        # Frame for the control buttons (right side)
        control_frame = tk.Frame(master=main_frame)
        control_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)
        self._create_control_buttons(control_frame)

        # Frame for the score display
        score_frame = tk.Frame(master=main_frame)
        score_frame.pack(side=tk.TOP, fill=tk.X, pady=5)
        self.score_display = tk.Label(
            master=score_frame,
            text=self._get_score_text(),
            font=font.Font(size=24, weight="bold"),
            bg="lightgrey",
            padx=10,
            pady=10
        )
        self.score_display.pack()

    def _create_board_grid(self, master):
        for row in range(self._game.board_size):
            master.rowconfigure(row, weight=1)
            master.columnconfigure(row, weight=1)
            for col in range(self._game.board_size):
                button = tk.Button(
                    master=master,
                    text="",
                    font=font.Font(size=24, weight="bold"),
                    fg="black",
                    bg="white",
                    width=4,
                    height=2,
                    highlightbackground="lightblue",
                    relief="raised",
                    bd=2
                )
                self._cells[button] = (row, col)
                button.bind("<ButtonPress-1>", self.play)
                button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def _create_control_buttons(self, master):
        self.score_button = tk.Button(
            master=master,
            text="Score",
            font=font.Font(size=16, weight="bold"),
            bg="lightblue",
            fg="black",
            command=self._update_score_display,
            relief="raised",
            bd=2
        )
        self.score_button.pack(pady=5)

        self.play_again_button = tk.Button(
            master=master,
            text="Play Again",
            font=font.Font(size=16, weight="bold"),
            bg="lightgreen",
            fg="black",
            command=self.reset_board,
            relief="raised",
            bd=2
        )
        self.play_again_button.pack(pady=5)

        self.exit_button = tk.Button(
            master=master,
            text="Exit",
            font=font.Font(size=16, weight="bold"),
            bg="salmon",
            fg="white",
            command=self.quit,
            relief="raised",
            bd=2
        )
        self.exit_button.pack(pady=5)

    def play(self, event):
        clicked_btn = event.widget
        row, col = self._cells[clicked_btn]
        move = Move(row, col, self._game.current_player.label)
        if self._game.is_valid_move(move):
            self._update_button(clicked_btn)
            self._game.process_move(move)
            if self._game.is_tied():
                self._update_display(msg="Tied game!", color="red")
            elif self._game.has_winner():
                self._highlight_cells()
                msg = f'Player "{self._game.current_player.label}" won!'
                color = self._game.current_player.color
                self._update_display(msg, color)
                self._update_score_display()
            else:
                self._game.toggle_player()
                msg = f"{self._game.current_player.label}'s turn"
                self._update_display(msg)

    def _update_button(self, clicked_btn):
        clicked_btn.config(text=self._game.current_player.label)
        clicked_btn.config(fg=self._game.current_player.color)

    def _update_display(self, msg, color="black"):
        self.display["text"] = msg
        self.display["fg"] = color

    def _update_score_display(self):
        self.score_display["text"] = self._get_score_text()

    def _highlight_cells(self):
        for button, coordinates in self._cells.items():
            if coordinates in self._game.winner_combo:
                button.config(highlightbackground="red")

    def reset_board(self):
        self._game.reset_game()
        self._update_display(msg="Tic-Tac-Toe - Ready?")
        self._update_score_display()
        for button in self._cells.keys():
            button.config(highlightbackground="lightblue")
            button.config(text="")
            button.config(fg="black")

    def _get_score_text(self):
        scores = self._game.scores
        return f"Scores - X: {scores['X']}  O: {scores['O']}"
