from PyQt6.QtCore import QSize, Qt, QDir
from PyQt6.QtWidgets import (QDialogButtonBox, QApplication, QDialog, QWidget, 
                             QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, 
                             QHBoxLayout, QFileDialog)
import random

# ------------------------------- To Do's ----------------------------------- #

# TODO: GUI erstellen
# TODO: Wörterliste erstellen und einfügen über Button
# TODO: Erstes Wort markieren und durch Leertaste auf das nächste springen
# TODO: Text mit eingabe vergleichen (nach Leertaste eingabefeld leer und zum 
#       nächsten Wort springen und rot oder grün markieren)
# TODO: Richtige und falsche Wörter zählen (GUI erweitern)
# TODO: Wörter pro Minute zählen
# TODO: Keystrokes zählen
# TODO: Falsche und Richtige Wörter anzeigen

# TODO: Countdown von 60 Sekunden runterzählen
# TODO: Neustart Knopf Funktion fertigstellen
# TODO: Result Fenster öffnen nach einem Run, als QDialog
# TODO: Record über alle Ergebnisse in CSV Speichern und Highscore anzeigen

# ------------------------------- Constants --------------------------------- #

BACKGROUND_COLOR       = "#ECEFF4"  # Sehr helles, kühles Grau – angenehmer Hintergrund
TEXT_COLOR             = "#2E3440"  # Dunkles Blau-Grau – hohe Lesbarkeit
BUTTON_BACKGROUND      = "#5E81AC"  # Kühles Mittelblau – moderne Primärfarbe
BUTTON_TEXT_COLOR      = "#FFFFFF"  # Weiß – klassisch und kontrastreich
BUTTON_PRESSED_COLOR   = "#4C6A92"  # Wenn Button gedrückt wird
INPUT_BACKGROUND       = "#E5E9F0"  # Sanftes Hellgrau-Blau – ideal für Eingabefelder
HIGHLIGHT_COLOR        = "#81A1C1"  # Helleres Blau – z. B. für Hover-Zustände
BORDER_COLOR           = "#D8DEE9"  # Weiches Grau-Blau für unaufdringliche Rahmen
WORD_HIGHLIGHT         = "#E0E0E0"  # Für noch nicht geprüfte oder aktuelle Wörter
CORRECT_HIGHLIGHT      = "#C8E6C9"  # Für korrekt geschriebene Wörter
WRONG_HIGHLIGHT        = "#FFCDD2"  # Für falsch geschriebene Wörter


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

# -------------------- Space Bar Function in LineEdit ------------------------ #

class SpaceDetectingLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            global current_word

            window.check_full_word()
            current_word = current_word + 1
            
            window.show_words()
            
        super().keyPressEvent(event)  # wichtig, damit der Text trotzdem erscheint

# ------------------------------- Main Window --------------------------------- #

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Typing Speed Test")

        self.title_label = QLabel("Starte deinen Typing Speed Test jetzt!")
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

        self.keystrokes_name = QLabel("KPM: ")
        self.keystrokes_name.setObjectName("keystrokes_name")
        self.keystrokes_name.setFixedHeight(50)
        self.keystrokes_name.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.keystrokes_label = QLabel("0")
        self.keystrokes_label.setObjectName("keystrokes_label")
        self.keystrokes_label.setFixedHeight(50)
        self.keystrokes_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

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
        self.text_label.setFixedHeight(100)
        self.text_label.setFixedWidth(710)
        self.text_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.user_input = SpaceDetectingLineEdit()
        self.user_input.textChanged.connect(self.check_word)
        self.user_input.setObjectName("input")
        self.user_input.setPlaceholderText("Tippe die Wörter so schnell es geht nach...")
        self.user_input.setFixedWidth(400)
        self.user_input.setFixedHeight(50)
    
        self.generate_words_btn = QPushButton("Wörter generieren")
        self.generate_words_btn.clicked.connect(self.generate_words)
        self.generate_words_btn.setFixedWidth(200)
        self.generate_words_btn.setFixedHeight(50)

        self.restart_btn = QPushButton("Reset")
        self.restart_btn.clicked.connect(self.restart_game)
        self.restart_btn.setFixedWidth(200)
        self.restart_btn.setFixedHeight(50)

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
        layout_three.addWidget(self.timer_name)
        layout_three.addWidget(self.timer_label)
        layout.addLayout(layout_three)
        layout.addWidget(self.text_label)
        layout.addWidget(self.user_input, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_four = QHBoxLayout()
        layout_four.addWidget(self.generate_words_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_four.addWidget(self.restart_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addLayout(layout_four)
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
        QPushButton:pressed {{
            background-color: #4C6A92;
        }}
        QLineEdit {{
            border: 1px solid {BORDER_COLOR};
            border-radius: 5px;
            padding: 5px;
            background: {INPUT_BACKGROUND};
        }}
        QLabel#title {{
            font-size: 25px;
        }}
        QLabel#text {{
            font-size: 25px;
            border: 3px solid {BORDER_COLOR};
            padding: 5px;
            border-radius: 4px;
        }}
        QLabel#timer, QLabel#timer_name, QLabel#words_name, QLabel#words_label, QLabel#correct_name, QLabel#correct_label,
        QLabel#wrong_name, QLabel#wrong_label, QLabel#keystrokes_name, QLabel#keystrokes_label {{
            font-size: 16px;
        }}

        """)

    # ------------------------ Functions ---------------------------- #

    def restart_game(self):
        self.text_label.setText("Klicke auf 'Wörter generieren' um zu starten.")
        global current_word_list
        current_word_list = []
        global current_row
        current_row = 0
        global current_word 
        current_word = 0
        global current_text
        current_text = ""
        self.user_input.clear()

    def generate_words(self):
        global current_word_list
        global current_row

        current_word_list = random.sample(WOERTER, len(WOERTER))
        print(current_word_list)

        for i in range(1,201):
            if i % 6 == 0:
                current_word_list[i-1] = current_word_list[i-1] + " \n"
            else: 
                current_word_list[i-1] = current_word_list[i-1] + " "

        self.show_words()
        
    def show_words(self):
        global current_text
        current_text = ""
        self.user_input.clear()

        for word in current_word_list[current_word:]:
                current_text = current_text + word

        self.highlight_grey()

    def check_word(self):
        global current_keystroke_count
        current_keystroke_count += 1
        self.keystrokes_label.setText(str(current_keystroke_count))

        current_input = self.user_input.text()
        current_input = current_input.lstrip()
        input_length = len(current_input)
        
        if current_input == current_word_list[current_word][:input_length]:
            self.highlight_green()
        elif current_input != current_word_list[current_word][:input_length]:
            self.highlight_red()

    def check_full_word(self):
        global current_keystroke_count
        current_keystroke_count -= 1
        global current_word_count_total
        global current_word_count_correct
        global current_word_count_wrong

        current_input = self.user_input.text()
        current_input = current_input.replace(" ", "")

        word_to_compare = current_word_list[current_word].replace(" ", "")

        if current_input == word_to_compare:
            current_word_count_total += 1
            current_word_count_correct += 1
        elif current_input != word_to_compare:
            current_word_count_total += 1
            current_word_count_wrong += 1
        
        self.words_correct_label.setText(str(current_word_count_correct))
        self.words_wrong_label.setText(str(current_word_count_wrong))
        self.words_total_label.setText(str(current_word_count_total))

    def highlight_grey(self):
        global current_text
        current_text = current_text.replace(current_word_list[current_word], 
                                            f'<span style="background-color: {WORD_HIGHLIGHT};">{current_word_list[current_word]}</span>')
        self.text_label.setText(current_text) 
    
    def highlight_green(self):
        global current_text
        current_text = current_text.replace(current_word_list[current_word], 
                                            f'<span style="background-color: {CORRECT_HIGHLIGHT};">{current_word_list[current_word]}</span>')
        self.text_label.setText(current_text) 

    def highlight_red(self):
        global current_text
        current_text = current_text.replace(current_word_list[current_word], 
                                            f'<span style="background-color: {WRONG_HIGHLIGHT};">{current_word_list[current_word]}</span>')
        self.text_label.setText(current_text) 



# ------------------------------- Program Loop ----------------------------------- #

app = QApplication([])

window = MainWindow()
window.show()

current_text = ""
current_word_list = []
current_row = 0
current_word = 0

current_word_count_total = 0
current_word_count_correct = 0
current_word_count_wrong = 0
current_keystroke_count = 0



app.exec()
