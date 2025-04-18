from PySide6.QtWidgets import QApplication
from gui.gui import MainApp
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
