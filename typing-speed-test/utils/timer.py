from utils.gui_helper import ResultDialog
from PyQt6.QtWidgets import QDialog
from utils.db_handler import DBHandler
from PyQt6.QtCore import QTimer

class Timer(QTimer):
    def __init__(self, view):
        super().__init__()
        self.view = view
        self.db_handler = DBHandler()
        self.time_left = 60

    def start_timer(self):
        print("Timer gestartet")
        self.time_left = 60
        self.start(1000)
    
    def stop_timer(self, state):
        print("Timer gestoppt.")
        self.stop()
        self.time_left = 60
        state.timer_stopped = True
        state.space_locked = True  
        self.user_input.setReadOnly(True)
        self.text_label.setText("Drücke 'Reset' um neu zu starten.")

    def update_timer(self, state):
        self.time_left -= 1
        if self.time_left == 60:
            self.timer_label.setText("1:00")
        elif self.time_left > 9 and self.time_left < 60:
            self.timer_label.setText(f"0:{str(self.time_left)}")
        elif self.time_left > 0 and self.time_left < 10:
            self.timer_label.setText(f"0:0{str(self.time_left)}")
        elif self.time_left <= 0:
            self.stop_timer(state)
            self.timer_label.setText("0:00")
            dialog = ResultDialog(state)
            result = dialog.exec()
            if result == QDialog.DialogCode.Accepted:
                number_to_make_saving_possible = state.current_word_count_total * 0.75
                if state.current_word_count_correct >= number_to_make_saving_possible:
                    print("Saved")
                    self.db_handler.save_result(state.current_wpm, state.current_keystroke_count, state.current_word_count_total, 
                                state.current_word_count_correct, state.current_word_count_wrong, state.current_user)
            else:
                pass