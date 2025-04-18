from win32api import GetSystemMetrics


def scale_boxes_to_overlay(boxes, overlay_size, sidebar_width=300):
    screen_size = [
        GetSystemMetrics(0) - sidebar_width,
        GetSystemMetrics(1)
    ]


    # Calculate the scaling factors
    # Note: GetSystemMetrics returns the screen size in pixels
    scale_x = overlay_size[0] / screen_size[0]
    scale_y = overlay_size[1] / screen_size[1]
    return [
        {
            "bbox": (
                int(box["bbox"][0] * scale_x),
                int(box["bbox"][1] * scale_y),
                int(box["bbox"][2] * scale_x),
                int(box["bbox"][3] * scale_y),
            ),
            "class": box["class"],
            "conf": box["conf"]
        }
        for box in boxes
    ]

from .constants import GRID_ROWS, GRID_COLS

def boxes_to_board_state(boxes, overlay_size):
    board = [["" for _ in range(8)] for _ in range(8)]

    for box in boxes:
        x1, y1, x2, y2 = box["bbox"]
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2

        square_width = overlay_size[0] / 8
        square_height = overlay_size[1] / 8

        col = int(center_x / square_width)
        row = int(center_y / square_height)

        if 0 <= row < 8 and 0 <= col < 8:
            board[row][col] = box["class"]

    return board
