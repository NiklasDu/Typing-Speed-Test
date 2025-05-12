# ------------------------------- Constants --------------------------------- #

BACKGROUND_COLOR       = "#ECEFF4"  # Sehr helles, kühles Grau – angenehmer Hintergrund
TEXT_COLOR             = "#2E3440"  # Dunkles Blau-Grau – hohe Lesbarkeit
BUTTON_BACKGROUND      = "#5E81AC"  # Kühles Mittelblau – moderne Primärfarbe
BUTTON_TEXT_COLOR      = "#FFFFFF"  # Weiß – klassisch und kontrastreich
BUTTON_PRESSED_COLOR   = "#4C6A92"  # Wenn Button gedrückt wird
INPUT_BACKGROUND       = "#E5E9F0"  # Sanftes Hellgrau-Blau – ideal für Eingabefelder
HIGHLIGHT_COLOR        = "#81A1C1"  # Helleres Blau – z. B. für Hover-Zustände
CLICKED_COLOR          = "#4C6A92"  # # Wenn Button gedrückt wird
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
    "schnell", "langsam", "einfach", "schwer", "schön", "groß", "klein", "gut", "schlecht",
    "neu", "alt", "hell", "dunkel", "früh", "spät", "klar", "unscharf", "Arbeit", "Freunde",
    "Familie", "Haus", "Auto", "Wetter", "Internet", "Computer", "Programm", "Wort",
    "Bildschirm", "Tastatur", "Maus", "Datei", "Ordner", "Text", "Sprache", "Frage",
    "Antwort", "Name", "Adresse", "System", "Drucker", "Daten", "Fehler", "Lösung",
    "Taste", "Link", "Button", "Seite", "Browser", "Bild", "Farbe", "Form", "Größe",
    "Sicherheit", "Passwort", "Benutzer", "Download", "Upload", "Projekt", "Nachricht",
    "Erfolg", "Plan", "Vertrag", "Papier", "Mail", "Server", "Update", "Start", "Stopp",
    "Pause", "Klick", "Hinweis", "Tipp", "Anleitung", "Termin", "Uhr", "Kalender", "Woche",
    "Tag", "Monat", "Jahr", "Sekunde", "Minute", "Morgen", "Abend", "Mittag", "Wasser",
    "Saft", "Kaffee", "Tee", "Pizza", "Brot", "Butter", "Preis", "Geld", "Euro", "Bank",
    "Konto", "Karte", "Zahlung", "Produkt", "Bestellung", "Service", "Hilfe", "Test",
    "Check", "Einstellung", "Tisch", "Stuhl", "Lampe", "Boden", "Decke", "Wand", "Spiegel",
    "Fenster", "Tür", "Straße", "Buch", "Zeitung", "Film", "Musik", "Sport", "Spiel",
    "Reise", "Ziel", "Ort", "Welt", "Stadt", "Land", "Schule", "Universität", "Lehrer",
    "Kind", "Eltern", "Mutter", "Vater", "Bruder", "Schwester", "Hund", "Katze", "Zimmer",
    "denken", "öffnen", "schließen", "spielen", "lesen", "schreiben", "lernen", "fragen",
    "antworten", "sehen", "hören", "fühlen", "laufen", "gehen", "fahren", "sitzen",
    "liegen", "stehen", "geben", "nehmen", "brauchen", "machen", "nutzen", "arbeiten",
    "träumen", "planen", "glauben", "wünschen", "hoffen", "suchen", "finden", "erklären",
    "vergessen", "erinnern", "beginnen", "enden", "zeigen", "drücken", "senden", "empfangen",
    "drucken", "rechnen", "messen", "reparieren", "testen", "kochen", "backen", "putzen",
    "telefonieren", "reisen", "zahlen", "laufen", "sparen", "wechseln", "denken", "reden",
    "schlafen", "träumen", "wecken", "essen", "trinken", "laufen", "springen", "fahren",
    "fliegen", "bauen", "zeichnen", "malen", "fotografieren", "organisieren", "lernen",
    "trainieren", "entspannen", "planen", "notieren", "üben", "kaufen", "verkaufen",
    "bestellen", "suchen", "speichern", "löschen", "kopieren", "einfügen", "installieren",
    "aktualisieren", "erstellen", "bearbeiten", "teilen", "verbinden", "trennen"
]

FILEPATH = "typing-speed-test/db/results.json"
FILEPATH_USER = "typing-speed-test/db/user.json"