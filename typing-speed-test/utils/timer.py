from utils.gui_helper import ResultDialog
from PyQt6.QtWidgets import QDialog
from utils.db_handler import DBHandler
from PyQt6.QtCore import QTimer

class Timer(QTimer):
    def __init__(self, view, state):
        super().__init__()
        self.view = view
        self.db_handler = DBHandler()
        self.time_left = 60
        self.state = state

    def start_timer(self):
        self.time_left = 60
        self.start(1000)
    
    def stop_timer(self):
        self.stop()
        self.time_left = 60
        self.state.timer_stopped = True
        self.state.space_locked = True  
        self.view.user_input.setReadOnly(True)
        self.view.text_label.setText("Drücke 'Reset' um neu zu starten.")

    def update_timer(self):
        self.time_left -= 1
        if self.time_left == 60:
            self.view.timer_label.setText("1:00")
        elif self.time_left > 9 and self.time_left < 60:
            self.view.timer_label.setText(f"0:{str(self.time_left)}")
        elif self.time_left > 0 and self.time_left < 10:
            self.view.timer_label.setText(f"0:0{str(self.time_left)}")
        elif self.time_left <= 0:
            self.stop_timer()
            self.view.timer_label.setText("0:00")
            dialog = ResultDialog(self.state)
            result = dialog.exec()
            if result == QDialog.DialogCode.Accepted:
                number_to_make_saving_possible = self.state.current_word_count_total * 0.75
                if self.state.current_word_count_correct >= number_to_make_saving_possible:
                    self.db_handler.save_result(self.state.current_wpm, self.state.current_keystroke_count, 
                                                self.state.current_word_count_total, self.state.current_word_count_correct, 
                                                self.state.current_word_count_wrong, self.state.current_user)
            else:
                pass