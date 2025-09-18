def load_board_from_file(filename):
    try:
        with open(filename, "r") as f:
            
            lines = [line.strip() for line in f.readlines() if line.strip()]
    except Exception as e:
        print(f"Could not read file: {e}")
        return None

    if len(lines) != 4 or any(len(line) != 4 for line in lines):
        print("Error: Board must have exactly 4 rows of 4 characters each.")
        return None

    return lines


def is_checkmate(board):
    """
    เช็คว่า King (K) โดน Checkmate หรือไม่
    R = Rook, P = Pawn, K = King
    """
    king_pos = None
    rooks = []
    pawns = []

    for i in range(4):
        for j in range(4):
            if board[i][j] == "K":
                king_pos = (i, j)
            elif board[i][j] == "R":
                rooks.append((i, j))
            elif board[i][j] == "P":
                pawns.append((i, j))

    if not king_pos:
        return False

    ki, kj = king_pos

    
    for ri, rj in rooks:
        if ri == ki or rj == kj:
            return True

    
    for pi, pj in pawns:
     if (pi - 1, pj - 1) == king_pos or (pi - 1, pj + 1) == king_pos:
        return True

    return False
