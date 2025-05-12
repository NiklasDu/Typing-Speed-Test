# -------------- Imports ------------- #
from constants import *
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QDialog, QPushButton, QLabel, QLineEdit, QVBoxLayout, 
                             QHBoxLayout, QSplashScreen)
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from collections import defaultdict
from matplotlib.ticker import MultipleLocator
import json
from datetime import datetime

# -------------- Class -------------- #

class WPMChart(FigureCanvas):
    def __init__(self, json_path, user):
        self.fig = Figure(figsize=(5, 4))
        self.fig.patch.set_facecolor(BACKGROUND_COLOR)
        super().__init__(self.fig)
        self.ax = self.fig.add_subplot(111)
        self.plot_from_json(json_path, user)

    def plot_from_json(self, json_path, user):
        with open(json_path, 'r') as f:
            data = json.load(f)

        print(user)
        # Berechne die höchsten WPM pro Tag
        wpm_per_day = defaultdict(float)
        for entry in data:
            if entry.get("user") == user:
                date = entry["date"]
                wpm = entry["wpm"]
                if wpm > wpm_per_day[date]:
                    wpm_per_day[date] = wpm
        # Sortiere nach Datum
        sorted_dates = sorted(wpm_per_day.keys(), key=lambda d: datetime.strptime(d, "%Y-%m-%d"))
        sorted_wpm = [wpm_per_day[date] for date in sorted_dates]
        # Zeichne das Diagramm
        self.ax.clear()
        self.ax.plot(sorted_dates, sorted_wpm, marker='o', color=f'{BUTTON_BACKGROUND}')
        self.ax.set_title("Höchste WPM pro Tag")
        self.ax.set_xlabel("Datum")
        self.ax.set_ylabel("WPM")
        self.ax.tick_params(axis='x', rotation=45)  # Datumseinteilung rotieren
        self.ax.yaxis.set_major_locator(MultipleLocator(10))
        self.ax.grid(True)

        self.ax.set_ylim(0, 140)

        self.fig.autofmt_xdate()
        self.draw()

# -------------------- Space Bar Function in LineEdit ------------------------ #

class SpaceDetectingLineEdit(QLineEdit):
    def __init__(self, view, game_logic, state, parent=None):
        super().__init__(parent)
        self.view = view
        self.game_logic = game_logic
        self.state = state

    def keyPressEvent(self, event):
        if not self.view.state.space_locked:
            if event.key() == Qt.Key.Key_Space:
                if self.view.state.first_space:
                    self.state.current_keystroke_count -= 1
                    if self.state.current_keystroke_count < 0:
                        self.state.current_keystroke_count = 0
                else:
                    self.state.current_keystroke_count -= 2
                    self.game_logic.check_full_word()
                    self.state.current_word = self.state.current_word + 1
                    self.view.user_input.clear()
                    self.game_logic.show_words()
            super().keyPressEvent(event)  # wichtig, damit der Text trotzdem erscheint
        else:
            pass # Falls space_locked aktiv ist, keine Aktion

# ------------------------------- Result Window ------------------------------- #

class ResultDialog(QDialog):
    def __init__(self, state):
        super().__init__()

        self.state = state
        self.setWindowTitle("Ergebnis")
        self.setup_ui()

    def setup_ui(self):
        # Labels
        correct_result = QLabel(f"Richtige Wörter: {self.state.current_word_count_correct}")
        correct_result.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        wrong_result = QLabel(f"Falsche Wörter: {self.state.current_word_count_wrong}")
        wrong_result.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        wpm_count = QLabel(f"Wörter pro Minute: {self.state.current_keystroke_count / 5}")
        wpm_count.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        
        # Buttons
        save_btn = QPushButton("Speichern")
        close_btn = QPushButton("Abbrechen")

        save_btn.clicked.connect(self.accept)   # OK → gibt exec_() = QDialog.Accepted zurück
        close_btn.clicked.connect(self.reject)   # Cancel → gibt exec_() = QDialog.Rejected zurück

        # Layouts
        layout = QVBoxLayout()
        layout.addWidget(correct_result)
        layout.addWidget(wrong_result)
        layout.addWidget(wpm_count)

        button_layout = QHBoxLayout()
        button_layout.addWidget(save_btn)
        button_layout.addWidget(close_btn)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.setFixedSize(QSize(300, 200))

        self.setStyleSheet(f"""
        QWidget {{
            background-color: {BACKGROUND_COLOR};
            color: {TEXT_COLOR};
            font-family: Roboto;
            font-size: 15px;
        }}
        QPushButton {{
            background-color: {BUTTON_BACKGROUND};
            color: {BUTTON_TEXT_COLOR};
            border-radius: 8px;
            padding: 8px;
        }}
        QPushButton:hover {{
            background-color: {HIGHLIGHT_COLOR};
        }}
        QPushButton:pressed {{
            background-color: {CLICKED_COLOR};
        }}
        QLabel {{
            font-size: 14px;
            padding: 5px;
        }}
        """)

# ------------------------------- Start Animation --------------------------------- #

class SplashScreen(QSplashScreen):
    def __init__(self, pixmap):
        super().__init__(pixmap)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        