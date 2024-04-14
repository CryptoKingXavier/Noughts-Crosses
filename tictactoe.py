from random import randint

class TicTacToe(object):
    def __init__(self) -> None:
        self.player_choice: str = "O"
        self.computer_choice: str = "X"
        self.available: list[int] = list()
        self.game_board: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.board_entry(5, self.computer_choice)

    # Check Win
    def check_win(self) -> str:
        # Row-Checker
        # Row-1
        if (self.game_board[0][0] == "X" and self.game_board[0][1] == "X" and self.game_board[0][2] == "X"): return "Computer Wins!"
        elif (self.game_board[0][0] == "O" and self.game_board[0][1] == "O" and self.game_board[0][2] == "O"): return "Player Wins!"

        # Row-2
        if (self.game_board[1][0] == "X" and self.game_board[1][1] == "X" and self.game_board[1][2] == "X"): return "Computer Wins!"
        elif (self.game_board[1][0] == "O" and self.game_board[1][1] == "O" and self.game_board[1][2] == "O"): return "Player Wins!"

        # Row-3
        if (self.game_board[2][0] == "X" and self.game_board[2][1] == "X" and self.game_board[2][2] == "X"): return "Computer Wins!"
        elif (self.game_board[2][0] == "O" and self.game_board[2][1] == "O" and self.game_board[2][2] == "O"): return "Player Wins!"

        # Column-Checker
        # Column-1
        if (self.game_board[0][0] == "X" and self.game_board[1][0] == "X" and self.game_board[2][0] == "X"): return "Computer Wins!"
        elif (self.game_board[0][0] == "O" and self.game_board[1][0] == "O" and self.game_board[2][0] == "O"): return "Player Wins!"

        # Column-2
        if (self.game_board[0][1] == "X" and self.game_board[1][1] == "X" and self.game_board[2][1] == "X"): return "Computer Wins!"
        elif (self.game_board[0][1] == "O" and self.game_board[1][1] == "O" and self.game_board[2][1] == "O"): return "Player Wins!"

        # Column-3
        if (self.game_board[0][2] == "X" and self.game_board[1][2] == "X" and self.game_board[2][2] == "X"): return "Computer Wins!"
        elif (self.game_board[0][2] == "O" and self.game_board[1][2] == "O" and self.game_board[2][2] == "O"): return "Player Wins!"

        # Diagonal-Checker
        # Left-Diagonal
        if (self.game_board[0][0] == "X" and self.game_board[1][1] == "X" and self.game_board[2][2] == "X"): return "Computer Wins!"
        elif (self.game_board[0][0] == "O" and self.game_board[1][1] == "O" and self.game_board[2][2] == "O"): return "Player Wins!"

        # Right-Diagonal
        if (self.game_board[0][2] == "X" and self.game_board[1][1] == "X" and self.game_board[2][0] == "X"): return "Computer Wins!"
        elif (self.game_board[0][2] == "O" and self.game_board[1][1] == "O" and self.game_board[2][0] == "O"): return "Player Wins!"

    # Board Design
    def board_design(self) -> None:
        board: str = f'''
+-------+-------+-------+
|       |       |       |
|   {self.game_board[0][0]}   |   {self.game_board[0][1]}   |   {self.game_board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {self.game_board[1][0]}   |   {self.game_board[1][1]}   |   {self.game_board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {self.game_board[2][0]}   |   {self.game_board[2][1]}   |   {self.game_board[2][2]}   |
|       |       |       |
+-------+-------+-------+
'''
        print(board, end="\n\n")
    # Board Entry
    def board_entry(self, position: int, state: str) -> None:
        for row in self.game_board:
            if position in row: row[row.index(position)] = state

    # Available Slots
    def get_available(self) -> None:
        self.available.clear()
        self.available = [cell for row in self.game_board for cell in row if cell not in ["X", "O"]]

    # Compute Entry
    def compute_entry(self, position: int | None, state_ref: str) -> None:
        self.get_available()

        if len(self.available) != 0 and self.check_win() != "Computer Wins!" and self.check_win() != "Player Wins!":
            if state_ref == "Computer":
                randIdx: int = randint(0, len(self.available) - 1)
                self.board_entry(self.available[randIdx], self.computer_choice)

            elif state_ref == "Player":
                if position in self.available: self.board_entry(position, self.player_choice)

    # Check Draw
    def check_draw(self) -> bool:
        # Check if any cell is still a number
        for i in range(len(self.game_board)):
            for j in range(len(self.game_board[i])):
                if isinstance(self.game_board[i][j], int): return False

        # Check if there is a winner
        if self.check_win() == "Computer Wins!" or self.check_win() == "Player Wins!": return False

        return True   # No empty cells and no winner, game is a draw
    
    # Gameplay
    def gameplay(self) -> None:
        while not self.check_draw():
            self.get_available()
            self.board_design()

            # User Input
            position: int = int(input("Enter your move: "))

            while position not in self.available:
                print("⛔ Invalid Position! ⛔")
                position: int = int(input("Enter your move: "))

                if position in self.available: break

            self.compute_entry(position, "Player")
            self.board_design()

            # Computer Input
            self.compute_entry(None, "Computer")

            # Endloop on Win
            if self.check_win() == "Computer Wins!" or self.check_win() == "Player Wins!":
                print(f"{self.check_win()} 🔥")
                break

            # Endloop on Draw
            if self.check_draw():
                print("Tie 🔥! Game Over...")
                break


# Game Instance
TicTacToe().gameplay()

