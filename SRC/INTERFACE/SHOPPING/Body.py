"""
Body.py

Configure MarcoNeo's body on its shopping menu.
"""

#-------------------------------------------------------------------#

import tkinter as tk

#-------------------------------------------------------------------#

class Body(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(bg="#333333")
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
        tk.Label(self, text="Navbar").pack()
    
    def setup_buttons(self):
        """
        Defines the buttons used in the main menu.
        """
        self.lunch_btn = tk.Button(self, text="Lunch", command=None)
        self.snack_btn = tk.Button(self, text="Snack", command=None)
        self.party_btn = tk.Button(self, text="Party", command=None)
        self.back_btn = tk.Button(self, text="Back", command=lambda: self.master.gui.change_menu(self.master.gui.main_menu))
        
        for btn in [self.lunch_btn, self.snack_btn, self.party_btn, self.back_btn]:
            btn.pack()