import os
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout, QSpacerItem, QSizePolicy

from gui.sidebar import SideBar
from gui.overlay import Overlay
from gui.draggable_button import DraggableButton as D

from qt_material import apply_stylesheet

from model.board_detector import BoardDetector
from utils.screen_capture import ScreenCapture
from utils.image_utils import scale_boxes_to_overlay, boxes_to_board_state
from utils.move_utils import detect_move, coord_to_notation
from PySide6.QtCore import QTimer


# Set the QT_PLUGIN_PATH to the PySide6 plugins directory
# This is necessary for PySide6 to find the required plugins
os.environ["QT_PLUGIN_PATH"] = os.path.join(os.path.dirname(sys.executable), "Lib", "site-packages", "PySide6", "plugins")


class MainApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )
        self.prev_board_state = None


        self.capture = ScreenCapture()
        self.detector = BoardDetector()
        self.timer = QTimer()
        self.timer.timeout.connect(self.process_frame)


        # get screen geometry
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # set window geometry to the right side of the screen
        self.setGeometry(screen_width - 300, 0, 300, screen_height)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Create sidebar instance
        self.sidebar = SideBar()
        self.sidebar.setVisible(False)  # Hidden by default

        # Create overlay instance
        self.overlay = Overlay()
        self.overlay.setVisible(False)  # Hidden by default
        self.overlay.setAttribute(Qt.WA_TransparentForMouseEvents , True)
        self.overlay.setAttribute(Qt.WA_NoSystemBackground, True)  # To prevent flickering


        self.toggle_btn = D("☰", self)
        self.toggle_btn.setParent(self)  # Ensure it’s outside layout
        self.toggle_btn.raise_()  # always keep above the sidebar
        self.toggle_btn.setFixedSize(100, 100)
        self.toggle_btn.setStyleSheet("font: bold 32px Arial; background-color: rgba(255, 255, 255, 100); border-radius: 20px; border: 2px solid teal;")
        self.toggle_btn.clicked.connect(self.toggle_sidebar)


        # Main layout holding everything
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 100, 0, 50)  # left, top, right, bottom
        main_layout.setSpacing(0)

        # Sidebar stays on the right
        main_layout.addWidget(self.sidebar)

        self.connect_sidebar_buttons()


    def showEvent(self, event):
        super().showEvent(event)
        screen_height = QApplication.primaryScreen().geometry().height()
        btn_x = 10
        btn_y = screen_height - self.toggle_btn.height() - 50
        self.toggle_btn.move(btn_x, btn_y)


    def toggle_sidebar(self):
        is_visible = self.sidebar.isVisible()
        self.sidebar.setVisible(not is_visible)
        self.toggle_btn.raise_()  # always keep above the sidebar
        self.toggle_btn.setText("|||" if not is_visible else "☰")


    def connect_sidebar_buttons(self):
        self.sidebar.login_btn.clicked.connect(self.login)
        self.sidebar.start_btn.clicked.connect(self.start)
        self.sidebar.pause_btn.clicked.connect(self.pause)
        self.sidebar.settings_btn.clicked.connect(self.settings)
        self.sidebar.exit_btn.clicked.connect(self.exit_app)


    # Placeholder functions
    def login(self):
        print("Login clicked")

    def start(self):
        self.overlay.setVisible(True)
        self.overlay.raise_()
        self.timer.start(100)
        print("Start clicked")


    def pause(self):
        self.overlay.setVisible(False)
        self.timer.stop()
        print("Pause clicked")


    def settings(self):
        print("Settings clicked")

    def exit_app(self):
        self.close()
        self.overlay.close()
        self.overlay.deleteLater()
        QApplication.quit()

    def process_frame(self):
        frame = self.capture.get_frame()
        detections = self.detector.detect(frame)

        screen_size = (frame.shape[1], frame.shape[0])
        overlay_size = (self.overlay.width(), self.overlay.height())
        scaled_boxes = scale_boxes_to_overlay(detections, overlay_size)


        self.overlay.update_boxes(scaled_boxes)

        board_state = boxes_to_board_state(scaled_boxes, self.overlay.size().toTuple())

        if self.prev_board_state:
            move = detect_move(self.prev_board_state, board_state)
            if move:
                print("Detected move:", move)

        self.prev_board_state = board_state




if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    app.setStyle("Fusion")
    window = MainApp()
    window.show()
    sys.exit(app.exec())
