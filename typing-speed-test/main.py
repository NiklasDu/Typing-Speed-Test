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
# TODO: Neustart Knopf mit Daten verknüpft
# TODO: Leertaste am Ende von jedem Wort nicht mit markieren
# TODO: Richtig und Falsch Menge grün und rot färben (bessere UX) 
# TODO: Countdown von 60 Sekunden runterzählen
# TODO: Reset Knopf Funktion fertigstellen (Zeit und Anzeige)
# TODO: Allgemeine Fehlerbehebung
# TODO: Result Fenster öffnen nach einem Run, als QDialog
# TODO: Aktuelle WPM anzeigen, nach jedem Keystroke kalkulieren und anzeigen
# TODO: Wörter Liste verbessern, Verben klein schreiben mehr Wörter
# TODO: Input Feld Zeichen begrenzen (je nach längstem Wort (13 Buchstaben, auf 18 gesetzt))
# TODO: Icon für die App erstellen
# TODO: Record über alle Ergebnisse in CSV Speichern und Highscore anzeigen (
#       unter Result Fenster auswählen, ob speichern soll oder nicht)
#       (nur speicherbar, wenn 75 % der Worte richtig waren)
#       Datum mit Zeit, WPM, KPM, Gesamt, Richtige, Falsche,
# TODO: Diagramme erstellen, um zu sehen, ob man sich verbessert hat
# TODO: Loading Screen wenn App startet (SplashScreen)
# TODO: Verschiedene Profile erstellen und zwischen ihnen wählen können
# TODO: Code Refactoring
        # TODO: Timer und WPM laufen wieder 
        # TODO: Beim erneuten Start geht leerzeile nicht mehr zum nächsten Wort.
        # TODO: lambda entfernen und in jeder Klasse state referenzieren
# TODO: 