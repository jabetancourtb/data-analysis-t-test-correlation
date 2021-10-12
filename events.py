from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from window.upload_file import upload_file,init
import asyncio
import time

class events_buttons(object):
    def __init__(self):
        self.file_path = ""
        # Create Panedwindow
       
    def search_files(self):
        self.file_path = filedialog.askopenfilename(initialdir="/", title="Seleccione archivo",filetypes=(("CSV Files", "*.csv"),))
        self.get_data_file()
        self.get_data_file_head()        
        return self.file_path
    
    def get_data_file(self):
        self.data_file = upload_file(self.file_path)
        return self.data_file
    
    def get_data_file_head(self):
        self.data_head = []
        for idx, valx in enumerate(self.data_file.columns):
            self.data_head.append(valx)
       