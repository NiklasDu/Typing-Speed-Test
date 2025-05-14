from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPixmap
from gui.main_window import MainWindow
from utils.gui_helper import SplashScreen
from state import State

# ------------------------------- Program Loop ----------------------------------- #

app = QApplication([])

pixmap = QPixmap("typing-speed-test/assets/logo.png").scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
splash = SplashScreen(pixmap)
splash.show()

QTimer.singleShot(1500, splash.close)

state = State()
window = MainWindow(state)

QTimer.singleShot(1500, window.show)

app.exec()