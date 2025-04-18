import os
import sys
from PySide6.QtWidgets import QApplication, QLabel

os.environ["QT_PLUGIN_PATH"] = os.path.join(os.path.dirname(sys.executable), "Lib", "site-packages", "PySide6", "plugins")

app = QApplication(sys.argv)

label = QLabel("Hello, PySide6!")
label.ser
label.show()
app.exec()
