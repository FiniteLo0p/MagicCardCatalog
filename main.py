# Created by Jason Smith
# August 18, 2022

# Description: The purpose of this program is to store and display a catalog of
# owned "Magic: The Gathering" cards in my collection.

import tkinter as tk
from tkinter import Menubutton, StringVar, ttk, Menu
from tkinter.messagebox import showinfo
        
        
class MainFrame(ttk.Frame):
    """Represents a frame instance and inherits from ttk.Frame."""
    def __init__(self, container):
        super().__init__(container)
        options = {'pady': 5}
               
        # top label
        self.label = ttk.Label(self, text='Enter the name of the card:')
        self.label.pack(**options)
        
        # card name entry
        self.card_name = StringVar()
        self.card_entry = ttk.Entry(self, textvariable=self.card_name)
        self.card_entry.pack()
        
        # button for card name
        self.card_name_button = ttk.Button(self, text='Submit Card Name')
        self.card_name_button['command'] = self.submit_name_button_clicked
        self.card_name_button.pack(**options)
        
        # show the frame on the container
        self.pack(**options)
        
    def submit_name_button_clicked(self):
        """Asks user if they are sure they want to add the name to the catalog.
        If yes, compares the name to the catalog text file. If the name exists, 
        let the user know that the amount of that card will be incremented."""
        #if len(self.card_name) <= 0:
        #    self.submit_name_button.state(['disabled'])
        #else:
        #    self.submit_name_button.state(['!disabled'])
        
        
class App(tk.Tk):
    """Represents an app instance and inherits from tkinter."""
    def __init__(self) -> None:
        super().__init__()
        
        # root window
        self.title("Magic Card Catalog")
        self.geometry('800x500')
        
        # file menu
        self.menubar = Menu(self)
        self.file_menu = Menu(self, tearoff=False)
        
        self.file_menu.add_command(label='Create New File', 
                                   command=self.create_new_file)
        self.file_menu.add_command(label='Open Existing File')
        self.file_menu.add_command(label='Close Current File')
        
        self.file_menu.add_separator()
        
        self.file_menu.add_command(label='Exit', command=self.quit)
        self.menubar.add_cascade(label='File', menu=self.file_menu)
        self.config(menu=self.menubar)
        
    def create_new_file(self):
        """"""
        with open('Documents/Magic_Card_Catalog.txt', 'w') as f:
            f.write('Creatting text file...')
    
    def open_existing_file(self):
        """"""
        pass

    def close_current_file(self):
        """"""
        pass        
        
def main():
    """Main loop function."""
    app = App()
    frame = MainFrame(app)
    
    app.mainloop()


if __name__ == "__main__":
    main()
    