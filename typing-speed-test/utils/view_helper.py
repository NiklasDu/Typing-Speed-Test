from constants import *
from utils.gui_helper import WPMChart
from PyQt6.QtCore import Qt
import json
import os
 
class ViewHelper():
    def __init__(self, view):
        self.view = view
        
    def refresh_statistics(self, state):
        if state.first_time_open_stats == True:
            self.stats_chart = WPMChart(FILEPATH, state.current_user)
            self.view.layout_stats.addWidget(self.stats_chart)
            self.view.layout_stats.addWidget(self.view.home_btn, alignment=Qt.AlignmentFlag.AlignHCenter)
            
            state.first_time_open_stats = False
        else:
            self.view.layout_stats.removeWidget(self.stats_chart)
            self.view.layout_stats.removeWidget(self.view.home_btn)   
            self.stats_chart = WPMChart(FILEPATH, state.current_user)
            self.view.layout_stats.addWidget(self.stats_chart)
            self.view.layout_stats.addWidget(self.view.home_btn, alignment=Qt.AlignmentFlag.AlignHCenter)

    def show_statistics(self, state):
        self.refresh_statistics(state)
        self.view.stacked_widget.setCurrentIndex(1)

    def show_home(self):
        self.view.stacked_widget.setCurrentIndex(2)
        self.view.user_input.setFocus()

    def show_login(self, state, game_logic):
        self.view.stacked_widget.setCurrentIndex(0)
        state.current_user = ""

        game_logic.restart_game(state)
        

    def login(self, state):
        user_to_login = self.view.user_selector.currentText()
        state.current_user = user_to_login

        self.view.title_label.setText(f"Hallo {state.current_user}, starte jetzt mit deinem Test!")

        self.view.stacked_widget.setCurrentIndex(2)
        self.view.user_input.setFocus()
        

    def add_user_and_login(self, state, db_handler):
        new_user = self.view.new_user_input.text()
        db_handler.add_user(new_user)

        state.current_user = new_user

        self.view.new_user_input.clear()
        self.view.title_label.setText(f"Hallo {state.current_user}, starte jetzt mit deinem Test!")

        self.view.stacked_widget.setCurrentIndex(2)
        self.view.user_input.setFocus()

        self.update_user_combobox()
        self.refresh_statistics(state)

    def update_user_combobox(self):
        self.view.user_selector.clear()
        if os.path.exists(FILEPATH_USER):
            with open(FILEPATH_USER, "r") as file:
                data = json.load(file)
                usernames = [user["user"] for user in data]
                self.view.user_selector.addItems(usernames)