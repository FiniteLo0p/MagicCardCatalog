# Created by Jason Smith
# August 18, 2022

# Description: The purpose of this program is to store and display a catalog of
# owned "Magic: The Gathering" cards in my collection.

from fileinput import filename
import tkinter as tk
from tkinter import Menubutton, StringVar, ttk, Menu
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
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
        
        # menubar
        self.menubar = Menu(self)
        self.file_menu = Menu(self, tearoff=False)
        
        self.file_menu.add_command(label='Create New File', 
                                   command=self.create_new_file)
        self.file_menu.add_command(label='Open Existing File', 
                                   command=self.open_existing_file)
        self.file_menu.add_command(label='Close Current File', 
                                   command=self.close_current_file)
        
        self.file_menu.add_separator()
        
        self.file_menu.add_command(label='Exit', command=self.quit)
        self.menubar.add_cascade(label='File', menu=self.file_menu)
        self.config(menu=self.menubar)
        
    def create_new_file(self):
        """Takes no parameters and create a new card catalog file."""
        with open('card_catalog.txt', 'w') as file:
            file.write('text here')
           
    def open_existing_file(self):
        """Takes no parameters and opens an existing card catalog file."""
        filename = askopenfilename()
        print(filename) 

    def close_current_file(self, file_name):
        """Takes no parameter parameter and closes card catalog file."""
        messagebox.askokcancel('Are you sure?', 'Are you sure you want to \n'
                            'close this file? Any unsaved data will be lost.')
        
        
def main():
    """Main loop function."""
    app = App()
    frame = MainFrame(app)
    
    app.mainloop()


if __name__ == "__main__":
    main()
    