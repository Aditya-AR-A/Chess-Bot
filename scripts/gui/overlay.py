from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Qt
from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QColor, QPen

class Overlay(QWidget):
    def __init__(self):
        super().__init__()

        # Fullscreen overlay setup
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        self.setGeometry(0, 0, screen_geometry.width() - 300, screen_geometry.height())

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )

        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, True)

        self.boxes = []

    def update_boxes(self, boxes):
        self.boxes = boxes
        self.update()  # Trigger paint event

    def paintEvent(self, event):
        painter = QPainter(self)
        neon_pen = QPen(QColor(57, 255, 20), 2)
        neon_pen.setCosmetic(True)
        painter.setPen(neon_pen)

        for box in self.boxes:
            x1, y1, x2, y2 = box["bbox"]
            painter.drawRect(QRect(x1, y1, x2 - x1, y2 - y1))

        painter.end()
