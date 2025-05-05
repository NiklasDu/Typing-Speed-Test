from PyQt6.QtCore import QSize, Qt, QDir
from PyQt6.QtWidgets import (QDialogButtonBox, QApplication, QDialog, QWidget, 
                             QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, 
                             QHBoxLayout, QFileDialog)
import random

# ------------------------------- To Do's ----------------------------------- #

# TODO: Text einfügen, der nachgeschrieben werden soll (zwei Zeilen)
# TODO: Text mit eingabe vergleichen (nach Leertaste eingabefeld leer und zum 
#       nächsten Wort springen und rot oder grün markieren)
# TODO: Countdown von 60 Sekunden runterzählen
# TODO: Wörter pro Minute zählen
# TODO: Keystrokes zählen
# TODO: Falsche und Richtige Wörter anzeigen
# TODO: Neustart Knopf Funktion
# TODO: Result Fenster öffnen nach einem Run, als QDialog
# TODO: Random generierten Text implementieren

# ------------------------------- Constants --------------------------------- #

BACKGROUND_COLOR       = "#ECEFF4"  # Sehr helles, kühles Grau – angenehmer Hintergrund
TEXT_COLOR             = "#2E3440"  # Dunkles Blau-Grau – hohe Lesbarkeit
BUTTON_BACKGROUND      = "#5E81AC"  # Kühles Mittelblau – moderne Primärfarbe
BUTTON_TEXT_COLOR      = "#FFFFFF"  # Weiß – klassisch und kontrastreich
INPUT_BACKGROUND       = "#E5E9F0"  # Sanftes Hellgrau-Blau – ideal für Eingabefelder
HIGHLIGHT_COLOR        = "#81A1C1"  # Helleres Blau – z. B. für Hover-Zustände
BORDER_COLOR           = "#D8DEE9"  # Weiches Grau-Blau für unaufdringliche Rahmen

WOERTER = [
    "und", "oder", "aber", "weil", "denn", "dass", "damit", "wenn", "ob", "auch",
    "es", "ist", "war", "sein", "haben", "werden", "kann", "muss", "soll", "dürfen",
    "ich", "du", "er", "sie", "wir", "ihr", "man", "dies", "das", "jener", "alle",
    "kein", "viele", "ein", "eine", "der", "die", "das", "mein", "dein", "unser",
    "dieser", "welcher", "jeder", "immer", "oft", "nie", "bald", "später", "heute",
    "gestern", "morgen", "jetzt", "hier", "dort", "oben", "unten", "drinnen", "draußen",
    "schnell", "langsam", "einfach", "schwer", "schön", "hässlich", "groß", "klein",
    "gut", "schlecht", "neu", "alt", "hell", "dunkel", "früh", "spät", "klar", "unscharf",
    "Arbeit", "Freunde", "Familie", "Haus", "Auto", "Wetter", "Internet", "Computer",
    "Programm", "E-Mail", "Bildschirm", "Tastatur", "Maus", "Datei", "Ordner", "Text",
    "Schreiben", "Lesen", "Lernen", "Spielen", "Sport", "Musik", "Film", "Buch",
    "Welt", "Stadt", "Land", "Schule", "Universität", "Kollege", "Lehrer", "Kind",
    "Eltern", "Mutter", "Vater", "Bruder", "Schwester", "Hund", "Katze", "Zimmer",
    "Fenster", "Tür", "Straße", "Telefon", "Kamera", "Reise", "Urlaub", "Zug", "Bus",
    "Fahrrad", "Flugzeug", "Ziel", "Idee", "Gedanke", "Sprache", "Wort",
    "Frage", "Antwort", "Name", "Adresse", "System", "Drucker", "Daten", "Fehler",
    "Lösung", "Taste", "Link", "Button", "Seite", "Browser", "Bild", "Farbe", "Form",
    "Größe", "Sicherheit", "Passwort", "Benutzer", "Download", "Upload", "Projekt",
    "Nachricht", "Erfolg", "Plan", "Vertrag", "Papier", "Mail", "Server", "Update",
    "Start", "Stopp", "Pause", "Klick", "Hinweis", "Tipp", "Anleitung", "Termin",
    "Uhr", "Kalender", "Woche", "Tag", "Monat", "Jahr", "Sekunde", "Minute",
    "Morgen", "Abend", "Mittag", "Wasser", "Saft", "Kaffee", "Tee", "Pizza", "Brot",
    "Butter", "Preis", "Geld", "Euro", "Bank", "Konto", "Karte", "Zahlung", "Produkt",
    "Bestellung", "Service", "Hilfe", "Test", "Check", "Einstellung",
    "denken", "öffnen", "schließen", "spielen", "lesen", "schreiben", "lernen",
    "fragen", "antworten", "sehen", "hören", "fühlen", "laufen", "gehen", "fahren",
    "sitzen", "liegen", "stehen", "geben", "nehmen", "brauchen", "machen", "nutzen",
    "arbeiten", "träumen", "planen", "glauben", "wünschen", "hoffen", "suchen",
    "finden", "erklären", "vergessen", "erinnern", "beginnen", "enden"
]

# ------------------------------- Main Window --------------------------------- #

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Typing Speed Test")

        self.title_label = QLabel("Starte deinen Typing Speed Test jetzt!")
        self.title_label.setObjectName("title")
        self.title_label.setFixedHeight(50)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.timer_name = QLabel("Timer: ")
        self.timer_name.setObjectName("timer_name")
        self.timer_name.setFixedHeight(50)
        self.timer_name.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        self.timer_label = QLabel("1:00")
        self.timer_label.setObjectName("timer")
        self.timer_label.setFixedHeight(50)
        self.timer_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.text_label = QLabel("Klicke auf 'Wörter generieren' um zu starten.")
        self.text_label.setObjectName("text")
        self.text_label.setFixedHeight(150)
        self.text_label.setFixedWidth(710)
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.user_input = QLineEdit()
        self.user_input.setObjectName("input")
        self.user_input.setPlaceholderText("Tippe die Wörter so schnell es geht nach...")
        self.user_input.setFixedWidth(400)
        self.user_input.setFixedHeight(50)
    
        self.generate_words_btn = QPushButton("Wörter generieren")
        self.generate_words_btn.clicked.connect(self.generate_words)
        self.generate_words_btn.setFixedWidth(200)
        self.generate_words_btn.setFixedHeight(50)

        self.restart_btn = QPushButton("Restart")
        self.restart_btn.clicked.connect(self.restart_game)
        self.restart_btn.setFixedWidth(200)
        self.restart_btn.setFixedHeight(50)

        # Layout Design
        layout = QVBoxLayout()
        layout.addWidget(self.title_label)
        layout_two = QHBoxLayout()
        layout_two.addWidget(self.timer_name)
        layout_two.addWidget(self.timer_label)
        layout.addLayout(layout_two)
        layout.addWidget(self.text_label)
        layout.addWidget(self.user_input, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_three = QHBoxLayout()
        layout_three.addWidget(self.generate_words_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_three.addWidget(self.restart_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addLayout(layout_three)
        layout.setContentsMargins(20,20,20,20)
        layout.setSpacing(20)

        # Main Window
        container = QWidget()    
        container.setLayout(layout)

        self.setFixedSize(QSize(750, 500))

        self.setCentralWidget(container)

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
        QPushButton:hover {{
            background-color: {HIGHLIGHT_COLOR};
        }}
        QLineEdit {{
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 5px;
            background: {INPUT_BACKGROUND};
        }}
        QLabel#title {{
            font-size: 25px;
        }}
        QLabel#text {{
            font-size: 25px;
            border: 3px solid #cccccc;
            padding: 5px;
            border-radius: 4px;
        }}
        QLabel#timer#timer_name {{
            font-size: 25px;
        }}

        """)

    # ------------------------ Functions ---------------------------- #

    def restart_game(self):
        pass

    def generate_words(self):
        global current_word_list
        global current_row
        
        for _ in range(150):
            current_word_list.append(random.choice(WOERTER))

        current_row = 0
        
    def show_word(self):
        if current_row == 0:
            self.text_label.setText("Hallo")






# ------------------------------- Program Loop ----------------------------------- #

app = QApplication([])

window = MainWindow()
window.show()

current_word_list = []
current_row = 0




app.exec()
