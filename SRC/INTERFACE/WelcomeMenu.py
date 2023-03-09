"""
WelcomeMenu.py

Configure MarcoNeo's welcome page.
"""

#-------------------------------------------------------------------#

import tkinter as tk

#-------------------------------------------------------------------#

class WelcomeMenu(tk.Frame):
    def __init__(self, gui=None):
        super().__init__(gui)
        self.gui = gui
        
        self.setup_images()
        self.setup_label()
        self.setup_buttons()
        
    def setup_images(self):
        """
        Defines the images used in the main menu.
        """
        return
    
    def setup_label(self):
        """
        Defines the labels used in the main menu.
        """
        tk.Label(self, text="MarcoNeo").pack()
    
    def setup_buttons(self):
        """
        Defines the buttons used in the main menu.
        """
        self.enter_btn = tk.Button(self, text="Enter", command=lambda: self.gui.change_menu(self.gui.main_menu))
        self.settings_btn = tk.Button(self, text="Settings", command=lambda: self.gui.change_menu(self.gui.settings_menu))
        self.credits_btn = tk.Button(self, text="Credits", command=lambda: self.gui.change_menu(self.gui.credits_menu))
        self.power_btn = tk.Button(self, text="Power off", command=lambda: self.gui.app.close())
        
        for btn in [self.enter_btn, self.settings_btn, self.credits_btn, self.power_btn]:
            btn.pack()
        