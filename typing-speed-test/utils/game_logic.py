from constants import *
import random

class GameLogic():
    def __init__(self, view, timer,  state):
        self.view = view
        self.timer = timer
        self.state = state

    def restart_game(self):
        self.state.current_word_list = []
        self.state.current_word = 0
        self.state.current_text = ""
        self.state.current_keystroke_count = 0
        self.state.current_word_count_correct = 0
        self.state.current_word_count_wrong = 0
        self.state.current_word_count_total = 0
        self.state.reset_happend = True
        self.state.first_space = True
        self.state.timer_stopped = False
        self.state.space_locked = True
        self.state.current_wpm = 0

        self.timer.stop_timer()

        self.view.timer_label.setText("1:00")
        self.view.generate_words_btn.setEnabled(True) 
        self.view.text_label.setText("Klicke auf 'Wörter generieren' um zu starten.") 
        self.view.words_correct_label.setText(str(self.state.current_word_count_correct))
        self.view.words_wrong_label.setText(str(self.state.current_word_count_wrong))
        self.view.words_total_label.setText(str(self.state.current_word_count_total))
        self.view.keystrokes_label.setText(str(self.state.current_keystroke_count))
        self.view.wpm_count_label.setText(str(self.state.current_wpm))
        self.view.user_input.clear()

    def generate_words(self):
        self.state.reset_happend = False
        self.state.space_locked = False

        self.view.user_input.setReadOnly(False)
        self.view.generate_words_btn.setEnabled(False)

        self.state.current_word_list = random.sample(WOERTER, len(WOERTER))

        for i in range(1, len(WOERTER)):
            self.state.current_word_list[i-1] = self.state.current_word_list[i-1] + " "

        self.view.text_label.setText("Drücke 'Leertaste' um zu starten.")
        
    def show_words(self):
        self.state.current_text = ""

        if self.state.first_space == True and self.state.space_locked == False:
            self.state.current_keystroke_count -= 1
            self.timer.start_timer()
            self.state.first_space = False
        else:
            if self.timer.time_left != 60 and self.timer.time_left != 0:
                current_wpm = round((self.state.current_keystroke_count / 5) * (60 / (60 - self.timer.time_left)), 2)
                self.state.current_wpm = current_wpm
                self.view.wpm_count_label.setText(str(self.state.current_wpm))

        for word in self.state.current_word_list[self.state.current_word:]:
                self.state.current_text = self.state.current_text + word

        self.check_word()

    def check_word(self):
        if not self.state.reset_happend:
            self.state.current_keystroke_count += 1
            self.view.keystrokes_label.setText(str(self.state.current_keystroke_count))

            current_input = self.view.user_input.text()
            current_input = current_input.lstrip()
            input_length = len(current_input)
            
            if current_input == " " or current_input == "":
                self.highlight_grey()
            elif current_input == self.state.current_word_list[self.state.current_word][:input_length]:
                self.highlight_green()
            elif current_input != self.state.current_word_list[self.state.current_word][:input_length]:
                self.highlight_red()

    def check_full_word(self):
        current_input = self.view.user_input.text()
        current_input = current_input.replace(" ", "")

        word_to_compare = self.state.current_word_list[self.state.current_word].replace(" ", "")

        if current_input == " " or current_input == "":
            print("Empty Word submitted.")
            if self.state.current_keystroke_count > 0:
                self.state.current_keystroke_count -= 1
        elif current_input == word_to_compare:
            self.state.current_word_count_total += 1
            self.state.current_word_count_correct += 1
        elif current_input != word_to_compare:
            self.state.current_word_count_total += 1
            self.state.current_word_count_wrong += 1
        
        self.view.words_correct_label.setText(str(self.state.current_word_count_correct))
        self.view.words_wrong_label.setText(str(self.state.current_word_count_wrong))
        self.view.words_total_label.setText(str(self.state.current_word_count_total))

    def highlight_grey(self):
        self.state.current_text = self.state.current_text.replace(self.state.current_word_list[self.state.current_word], 
                                            f'<span style="background-color: {WORD_HIGHLIGHT};">{self.state.current_word_list[self.state.current_word].strip()}</span> ')
        self.view.text_label.setText(self.state.current_text) 
    
    def highlight_green(self):
        self.state.current_text = self.state.current_text.replace(self.state.current_word_list[self.state.current_word], 
                                            f'<span style="background-color: {CORRECT_HIGHLIGHT};">{self.state.current_word_list[self.state.current_word].strip()}</span> ')
        self.view.text_label.setText(self.state.current_text) 

    def highlight_red(self):
        self.state.current_text = self.state.current_text.replace(self.state.current_word_list[self.state.current_word], 
                                            f'<span style="background-color: {WRONG_HIGHLIGHT};">{self.state.current_word_list[self.state.current_word].strip()}</span> ')
        self.view.text_label.setText(self.state.current_text) 
