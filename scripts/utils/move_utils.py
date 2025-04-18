
def detect_move(prev_board, curr_board):
    from_square = to_square = None

    for row in range(8):
        for col in range(8):
            prev = prev_board[row][col]
            curr = curr_board[row][col]

            if prev != curr:
                if prev and not curr:
                    from_square = (row, col)
                elif not prev and curr:
                    to_square = (row, col)

    if from_square and to_square:
        return f"{coord_to_notation(from_square)} -> {coord_to_notation(to_square)}"

    return None

def coord_to_notation(coord):
    row, col = coord
    return f"{chr(ord('a') + col)}{8 - row}"
