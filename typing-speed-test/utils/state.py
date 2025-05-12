class State():
    def __init__(self):
        self.current_user = ""
        self.current_text = ""
        self.current_word_list = []
        self.current_word = 0
        self.current_word_count_total = 0
        self.current_word_count_correct = 0
        self.current_word_count_wrong = 0
        self.current_keystroke_count = 0
        self.current_wpm = 0

        self.reset_happened = True
        self.first_space = True
        self.timer_stopped = False
        self.space_locked = True   

        self.first_time_open_stats = True