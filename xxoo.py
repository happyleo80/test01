"""A tiny terminal XXOO / tic-tac-toe game."""


WIN_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def print_board(board):
    print()
    for row in range(3):
        start = row * 3
        print(f" {board[start]} | {board[start + 1]} | {board[start + 2]} ")
        if row < 2:
            print("---+---+---")
    print()


def check_winner(board):
    for a, b, c in WIN_LINES:
        if board[a] == board[b] == board[c] and board[a] in ("X", "O"):
            return board[a]
    return None


def get_move(board, player):
    while True:
        choice = input(f"玩家 {player}，请选择位置 (1-9)，或输入 q 退出：").strip().lower()
        if choice == "q":
            return None
        if not choice.isdigit():
            print("请输入 1 到 9 之间的数字。")
            continue

        position = int(choice)
        if position < 1 or position > 9:
            print("位置必须在 1 到 9 之间。")
            continue

        index = position - 1
        if board[index] in ("X", "O"):
            print("这个位置已经被占用啦，换一个。")
            continue

        return index


def play_game():
    print("欢迎来到 XXOO 小游戏！")
    print("棋盘位置如下，输入数字即可落子：")

    board = [str(i) for i in range(1, 10)]
    current_player = "X"

    while True:
        print_board(board)
        move = get_move(board, current_player)
        if move is None:
            print("游戏已退出。")
            return

        board[move] = current_player
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"玩家 {winner} 获胜！")
            return

        if all(cell in ("X", "O") for cell in board):
            print_board(board)
            print("平局！")
            return

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()
