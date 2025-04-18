from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt, QPoint

class DraggableButton(QPushButton):
    def __init__(self, text="☰", parent=None):
        super().__init__(text, parent)
        self._mouse_press_pos = None
        self._mouse_move_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._mouse_press_pos = event.globalPosition().toPoint()
            self._mouse_move_pos = event.globalPosition().toPoint()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            curr_pos = self.mapToGlobal(self.pos())
            global_pos = event.globalPosition().toPoint()
            diff = global_pos - self._mouse_move_pos
            new_pos = self.mapFromGlobal(curr_pos + diff)
            self.move(new_pos)

            self._mouse_move_pos = global_pos
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self._mouse_press_pos is not None:
            moved = event.globalPosition().toPoint() - self._mouse_press_pos
            if moved.manhattanLength() > 3:
                # Treat as drag, ignore click
                event.ignore()
                return
        super().mouseReleaseEvent(event)

