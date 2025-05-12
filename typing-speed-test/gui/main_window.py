# ----------------- Imports ----------------- #
from PyQt6.QtCore import QSize, Qt, QTimer
from PyQt6.QtWidgets import (QWidget, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, 
                             QHBoxLayout, QStackedWidget, QComboBox, QListView, QFrame)
from PyQt6.QtGui import QPixmap
from utils.gui_helper import *
from constants import *
from utils.timer import Timer
from utils.game_logic import GameLogic
from utils.view_helper import ViewHelper
from utils.db_handler import DBHandler

# ----------------- Class ----------------- #

class MainWindow(QMainWindow):
    def __init__(self, state):
        super().__init__()

        self.timer = Timer(self)
        self.state = state
        self.game_logic = GameLogic(self)
        self.view_helper = ViewHelper(self)
        self.db_handler = DBHandler()
        
        self.setWindowTitle("KeyTap")
        self.ui_setup()

        
    def ui_setup(self):

        self.title_label = QLabel(f"Hallo {self.state.current_user}, starte jetzt mit deinem Test!")
        self.title_label.setObjectName("title")
        self.title_label.setFixedHeight(50)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.words_total_name = QLabel("Wörter (Gesamt): ")
        self.words_total_name.setObjectName("words_name")
        self.words_total_name.setFixedHeight(50)
        self.words_total_name.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.words_total_label = QLabel("0")
        self.words_total_label.setObjectName("words_label")
        self.words_total_label.setFixedHeight(50)
        self.words_total_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.words_correct_name = QLabel("Wörter (Richtig): ")
        self.words_correct_name.setObjectName("correct_name")
        self.words_correct_name.setFixedHeight(50)
        self.words_correct_name.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.words_correct_label = QLabel("0")
        self.words_correct_label.setObjectName("correct_label")
        self.words_correct_label.setFixedHeight(50)
        self.words_correct_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.words_wrong_name = QLabel("Wörter (Falsch): ")
        self.words_wrong_name.setObjectName("wrong_name")
        self.words_wrong_name.setFixedHeight(50)
        self.words_wrong_name.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.words_wrong_label = QLabel("0")
        self.words_wrong_label.setObjectName("wrong_label")
        self.words_wrong_label.setFixedHeight(50)
        self.words_wrong_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.keystrokes_name = QLabel("Klicks: ")
        self.keystrokes_name.setObjectName("keystrokes_name")
        self.keystrokes_name.setFixedHeight(50)
        self.keystrokes_name.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.keystrokes_label = QLabel("0")
        self.keystrokes_label.setObjectName("keystrokes_label")
        self.keystrokes_label.setFixedHeight(50)
        self.keystrokes_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.wpm_count_name = QLabel("WPM: ")
        self.wpm_count_name.setObjectName("wpm_name")
        self.wpm_count_name.setFixedHeight(50)
        self.wpm_count_name.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.wpm_count_label = QLabel("0")
        self.wpm_count_label.setObjectName("wpm_label")
        self.wpm_count_label.setFixedHeight(50)
        self.wpm_count_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.timer_name = QLabel("Timer: ")
        self.timer_name.setObjectName("timer_name")
        self.timer_name.setFixedHeight(50)
        self.timer_name.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.timer_label = QLabel("1:00")
        self.timer_label.setObjectName("timer")
        self.timer_label.setFixedHeight(50)
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.timer.update_timer(self.state))

        self.text_label = QLabel("Klicke auf 'Wörter generieren' um zu starten.")
        self.text_label.setObjectName("text")
        self.text_label.setTextFormat(Qt.TextFormat.RichText)
        self.text_label.setFixedHeight(100)
        self.text_label.setFixedWidth(710)
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.user_input = SpaceDetectingLineEdit(view=self, parent=self, game_logic=self.game_logic, state=self.state)
        self.user_input.textChanged.connect(lambda: self.game_logic.show_words(self.state))
        self.user_input.setObjectName("input")
        self.user_input.setPlaceholderText("Tippe die Wörter so schnell es geht ab...")
        self.user_input.setMaxLength(18)
        self.user_input.setFixedWidth(400)
        self.user_input.setFixedHeight(50)
    
        self.generate_words_btn = QPushButton("Wörter generieren")
        self.generate_words_btn.clicked.connect(lambda: self.game_logic.generate_words(self.state))
        self.generate_words_btn.setFixedWidth(200)
        self.generate_words_btn.setFixedHeight(50)

        self.restart_btn = QPushButton("Reset")
        self.restart_btn.clicked.connect(lambda: self.game_logic.restart_game(self.state))
        self.restart_btn.setFixedWidth(200)
        self.restart_btn.setFixedHeight(50)

        self.statistic_btn = QPushButton("Statistiken")
        self.statistic_btn.clicked.connect(lambda: self.view_helper.show_statistics(self.state))
        self.statistic_btn.setFixedWidth(150)
        self.statistic_btn.setFixedHeight(50)

        self.logout_btn = QPushButton("Ausloggen")
        self.logout_btn.clicked.connect(lambda: self.view_helper.show_login(self.state))
        self.logout_btn.setFixedWidth(150)
        self.logout_btn.setFixedHeight(50)


        # Layout Design
        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout_two = QHBoxLayout()
        layout_two.addWidget(self.words_total_name)
        layout_two.addWidget(self.words_total_label)
        layout_two.addWidget(self.words_correct_name)
        layout_two.addWidget(self.words_correct_label)
        layout_two.addWidget(self.words_wrong_name)
        layout_two.addWidget(self.words_wrong_label)
        layout.addLayout(layout_two)
        layout_three = QHBoxLayout()
        layout_three.addWidget(self.keystrokes_name)
        layout_three.addWidget(self.keystrokes_label)
        layout_three.addWidget(self.wpm_count_name)
        layout_three.addWidget(self.wpm_count_label)
        layout_three.addWidget(self.timer_name)
        layout_three.addWidget(self.timer_label)
        layout.addLayout(layout_three)
        layout.addWidget(self.text_label)
        layout.addWidget(self.user_input, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_four = QHBoxLayout()
        layout_four.addWidget(self.generate_words_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_four.addWidget(self.restart_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addLayout(layout_four)
        layout_five = QHBoxLayout()
        layout_five.addWidget(self.statistic_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_five.addWidget(self.logout_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addLayout(layout_five)

        layout.setContentsMargins(20,20,20,20)
        layout.setSpacing(20)

        # Main Window
        container = QWidget()    
        container.setLayout(layout)

        # Statistic Page 
        self.title_stats_label = QLabel("Statistiken")
        self.title_stats_label.setObjectName("title_stats")
        self.title_stats_label.setFixedHeight(50)
        self.title_stats_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        
        self.home_btn = QPushButton("Zurück")
        self.home_btn.clicked.connect(self.view_helper.show_home)
        self.home_btn.setFixedHeight(50)
        self.home_btn.setFixedWidth(200)

        self.layout_stats = QVBoxLayout()
        self.layout_stats.addWidget(self.title_stats_label)

        self.layout_stats.setContentsMargins(20, 20, 20, 20)
        self.layout_stats.setSpacing(20)

        container_stats = QWidget()
        container_stats.setLayout(self.layout_stats)

        # Login Page
        self.logo_label = QLabel(self)
        pixmap_logo = QPixmap("typing-speed-test/assets/logo.png")
        scaled_pixmap_logo = pixmap_logo.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.logo_label.setPixmap(scaled_pixmap_logo)
        self.logo_label.setFixedHeight(80)
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.title_login_label = QLabel("Wähle einen Benutzer aus:")
        self.title_login_label.setObjectName("title_login")
        self.title_login_label.setFixedHeight(50)
        self.title_login_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.user_selector = QComboBox()
        self.user_selector.addItems(self.db_handler.load_all_user())
        self.user_selector.setFixedHeight(50)
        self.user_selector.setFixedWidth(250)
        self.user_selector.setView(QListView())

        self.login_btn = QPushButton("Anmelden")
        self.login_btn.clicked.connect(lambda: self.view_helper.login(self.state))
        self.login_btn.setFixedHeight(50)
        self.login_btn.setFixedWidth(200)

        self.line = QFrame()
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setStyleSheet("color: {BORDER_COLOR}; background-color: {BORDER_COLOR}; height: 1px;")
        self.line.setFixedHeight(3) 
        self.line.setFixedWidth(450)

        self.new_user_label = QLabel("Kein passender Benutzer vorhanden, erstelle hier einen neuen:")
        self.new_user_label.setObjectName("new_user_label")
        self.new_user_label.setFixedHeight(75)
        self.new_user_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.new_user_input = QLineEdit()
        self.new_user_input.setObjectName("new_user_input")
        self.new_user_input.setPlaceholderText("Neuer Benutzername")
        self.new_user_input.setMaxLength(20)
        self.new_user_input.setFixedWidth(250)
        self.new_user_input.setFixedHeight(50)

        self.new_user_btn = QPushButton("Benutzer erstellen")
        self.new_user_btn.clicked.connect(lambda: self.view_helper.add_user_and_login(self.state, self.db_handler))
        self.new_user_btn.setFixedHeight(50)
        self.new_user_btn.setFixedWidth(250)

        layout_login = QVBoxLayout()
        layout_login.addWidget(self.logo_label)
        layout_login.addWidget(self.title_login_label)
        layout_login.addWidget(self.user_selector, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_login.addWidget(self.login_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_login.addWidget(self.line, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_login.addWidget(self.new_user_label)
        layout_login_two = QHBoxLayout()
        layout_login_two.addWidget(self.new_user_input)
        layout_login_two.addWidget(self.new_user_btn)
        layout_login.addLayout(layout_login_two)

        layout_login.setContentsMargins(20, 20, 20, 20)
        layout_login.setSpacing(20)

        container_login = QWidget()
        container_login.setLayout(layout_login)
        

        # Pages
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(container_login)
        self.stacked_widget.addWidget(container_stats)
        self.stacked_widget.addWidget(container)
        
        self.setFixedSize(QSize(750, 600))

        self.setCentralWidget(self.stacked_widget)

        # ------------------------ Styling ---------------------------- #

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
        QComboBox {{
        border: 1px solid {BORDER_COLOR};
        border-radius: 6px;
        padding: 6px 24px 6px 8px;
        background-color: #f8f9fa;
        color: #2E3440;
        font-size: 14px;
        }}
        QComboBox:hover {{
            border: 1px solid #5E81AC;
            background-color: #ffffff;
        }}
        QComboBox::drop-down {{
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 20px;
            border-left: 1px solid {BORDER_COLOR};
            background: transparent;
        }}
        QComboBox::down-arrow {{
            image: url(assets/down.png);
            width: 12px;
            height: 12px;
        }}
        QComboBox QAbstractItemView {{
            background-color: #ffffff;
            border: 1px solid {BORDER_COLOR};
            padding: 4px;
            outline: 0px;
            selection-background-color: #5E81AC;
            selection-color: #ffffff;
            font-size: 14px;
            show-decoration-selected: 1;
            min-height: 32px;
        }}
        QComboBox QAbstractItemView::item {{
            padding: 8px 12px;
            height: 28px;
            border: none;
            background-color: #ffffff;
            color: #2E3440; 
        }}

        QComboBox QAbstractItemView::item:hover {{
            background-color: #D8DEE9;
            color: #2E3440;
        }}
        QPushButton:hover {{
            background-color: {HIGHLIGHT_COLOR};
        }}
        QPushButton:pressed {{
            background-color: {CLICKED_COLOR};
        }}
        QLineEdit, QLineEdit#input, QLineEdit#new_user_input {{
            border: 1px solid {BORDER_COLOR};
            border-radius: 5px;
            padding: 5px;
            background: {INPUT_BACKGROUND};
        }}
        QLabel#title, QLabel#title_stats, QLabel#title_login {{
            font-size: 25px;
        }}
        QLabel#text {{
            font-size: 25px;
            border: 3px solid {BORDER_COLOR};
            padding: 5px;
            border-radius: 4px;
        }}
        QLabel#timer, QLabel#timer_name, QLabel#words_name, QLabel#words_label, QLabel#correct_name, QLabel#correct_label,
        QLabel#wrong_name, QLabel#wrong_label, QLabel#keystrokes_name, QLabel#keystrokes_label, QLabel#wpm_label QLabel#wpm_name {{
            font-size: 16px;
        }}
        QLabel#new_user_label {{
            font-size: 18px;
            margin-top: 20px;
        }}
        QLabel#correct_label {{
            color: #388E3C
        }}
        QLabel#wrong_label {{
            color: #D32F2F
        }}
        """)


    

