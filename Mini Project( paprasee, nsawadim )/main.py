import sys
from checkmate import load_board_from_file, is_checkmate

def main():
    if len(sys.argv) < 2:
        print("No input provided. Using demo board:")
        board = [
            "R...",
            ".K..",
            "..P.",
            "...."
        ]
    else:
        filename = sys.argv[1]
        board = load_board_from_file(filename)
        if not board:
            return

    for row in board:
        print(row)

    print("\nResult:")
    if is_checkmate(board):
        print("Success")
    else:
        print("Fail")

if __name__ == "__main__":
    main()
