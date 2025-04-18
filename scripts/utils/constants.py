CLASS_NAMES = {
    0: "w_pawn",
    1: "w_knight",
    2: "w_bishop",
    3: "w_rook",
    4: "w_queen",
    5: "w_king",
    6: "b_pawn",
    7: "b_knight",
    8: "b_bishop",
    9: "b_rook",
    10: "b_queen",
    11: "b_king"
}

# Optionally, reverse mapping for convenience
PIECE_IDS = {v: k for k, v in CLASS_NAMES.items()}

# For use in grid calculations
GRID_ROWS = 8
GRID_COLS = 8
