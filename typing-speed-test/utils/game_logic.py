from constants import *
from utils.timer import Timer
import random

class GameLogic():
    def __init__(self, view, timer):
        self.view = view
        self.timer = timer

    def restart_game(self, state):
        state.current_word_list = []
        state.current_word = 0
        state.current_text = ""
        state.current_keystroke_count = 0
        state.current_word_count_correct = 0
        state.current_word_count_wrong = 0
        state.current_word_count_total = 0
        state.reset_happend = True
        state.first_space = True
        state.timer_stopped = False
        state.space_locked = True
        state.current_wpm = 0

        self.timer.stop_timer(state)

        self.view.timer_label.setText("1:00")
        self.view.generate_words_btn.setEnabled(True) 
        self.view.text_label.setText("Klicke auf 'Wörter generieren' um zu starten.") 
        self.view.words_correct_label.setText(str(state.current_word_count_correct))
        self.view.words_wrong_label.setText(str(state.current_word_count_wrong))
        self.view.words_total_label.setText(str(state.current_word_count_total))
        self.view.keystrokes_label.setText(str(state.current_keystroke_count))
        self.view.wpm_count_label.setText(str(state.current_wpm))
        self.view.user_input.clear()

    def generate_words(self, state):
        state.reset_happend = False
        state.space_locked = False

        self.view.user_input.setReadOnly(False)
        self.view.generate_words_btn.setEnabled(False)

        state.current_word_list = random.sample(WOERTER, len(WOERTER))

        for i in range(1, len(WOERTER)):
            state.current_word_list[i-1] = state.current_word_list[i-1] + " "

        self.view.text_label.setText("Drücke 'Leertaste' um zu starten.")
        
    def show_words(self, state):
        state.current_text = ""

        if state.first_space == True and state.space_locked == False:
            state.current_keystroke_count -= 1
            self.timer.start_timer()
            state.first_space = False
        else:
            if self.timer.time_left != 60 and self.timer.time_left != 0:
                current_wpm = round((state.current_keystroke_count / 5) * (60 / (60 - self.timer.time_left)), 2)
                self.view.wpm_count_label.setText(str(current_wpm))

        for word in state.current_word_list[state.current_word:]:
                state.current_text = state.current_text + word

        self.check_word(state)

    def check_word(self, state):
        if state.reset_happend == False:
            state.current_keystroke_count += 1
            self.view.keystrokes_label.setText(str(state.current_keystroke_count))

            current_input = self.view.user_input.text()
            current_input = current_input.lstrip()
            input_length = len(current_input)
            
            if current_input == " " or current_input == "":
                self.highlight_grey(state)
            elif current_input == state.current_word_list[state.current_word][:input_length]:
                self.highlight_green(state)
            elif current_input != state.current_word_list[state.current_word][:input_length]:
                self.highlight_red(state)

    def check_full_word(self, state):
        current_input = self.view.user_input.text()
        current_input = current_input.replace(" ", "")

        word_to_compare = state.current_word_list[state.current_word].replace(" ", "")

        if current_input == " " or current_input == "":
            print("Empty Word submitted.")
            if state.current_keystroke_count > 0:
                state.current_keystroke_count -= 1
        elif current_input == word_to_compare:
            state.current_word_count_total += 1
            state.current_word_count_correct += 1
        elif current_input != word_to_compare:
            state.current_word_count_total += 1
            state.current_word_count_wrong += 1
        
        self.view.words_correct_label.setText(str(state.current_word_count_correct))
        self.view.words_wrong_label.setText(str(state.current_word_count_wrong))
        self.view.words_total_label.setText(str(state.current_word_count_total))

    def highlight_grey(self, state):
        state.current_text = state.current_text.replace(state.current_word_list[state.current_word], 
                                            f'<span style="background-color: {WORD_HIGHLIGHT};">{state.current_word_list[state.current_word].strip()}</span> ')
        self.view.text_label.setText(state.current_text) 
    
    def highlight_green(self,state):
        state.current_text = state.current_text.replace(state.current_word_list[state.current_word], 
                                            f'<span style="background-color: {CORRECT_HIGHLIGHT};">{state.current_word_list[state.current_word].strip()}</span> ')
        self.view.text_label.setText(state.current_text) 

    def highlight_red(self, state):
        state.current_text = state.current_text.replace(state.current_word_list[state.current_word], 
                                            f'<span style="background-color: {WRONG_HIGHLIGHT};">{state.current_word_list[state.current_word].strip()}</span> ')
        self.view.text_label.setText(state.current_text) 
