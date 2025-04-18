from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import Qt


class SideBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedWidth(200)  # Width of sidebar

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(15)
        layout.setAlignment(Qt.AlignTop)

        self.login_btn = QPushButton("Login")
        self.start_btn = QPushButton("Start")
        self.pause_btn = QPushButton("Pause")
        self.settings_btn = QPushButton("Settings")
        self.exit_btn = QPushButton("Exit")

        # Set button styles
        button_style = """
            QPushButton {
                font: bold 16px Arial;
                background-color: rgba(255, 255, 255, 100);
                border-radius: 10px;
                border: 2px solid teal;
                padding: 10px;

            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 150);
            }
            QPushButton:pressed {
                background-color: rgba(255, 255, 255, 200);
            }
        """

        # Set button styles to all buttons
        for btn in [self.login_btn, self.start_btn, self.pause_btn, self.settings_btn, self.exit_btn]:
            btn.setStyleSheet(button_style)
            btn.setFixedHeight(50)  # Fixed height for all buttons

            btn.setCursor(Qt.PointingHandCursor)
            btn.setObjectName(btn.text())

        # Add buttons to layout
        for btn in [self.login_btn, self.start_btn, self.pause_btn, self.settings_btn, self.exit_btn]:
            layout.addWidget(btn)

        # Signals will be connected in gui.py
