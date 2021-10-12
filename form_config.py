from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from events import  events_buttons
from core.correlations.__app import  correlacion_app
import asyncio
import time

class form_config(object):
    def __init__(self, root):
        # Create Panedwindow
        self.root = root
        self._events_buttons = events_buttons()
        
    def create_panel(self):
        self.panedwindow = ttk.Panedwindow(self.root, orient=HORIZONTAL)
        self.panedwindow.pack(fill=BOTH, expand=True)
        
        self.form_left = ttk.Frame(self.panedwindow, width=100, height=300, relief=SUNKEN, style='Frame1.TFrame')
        self.form_rigth = ttk.Frame(self.panedwindow, width=400, height=400, relief=SUNKEN, style='Frame2.TFrame')
        
    def see_panel(self):      
        self.panedwindow.add(self.form_left, weight=1)
        self.panedwindow.add(self.form_rigth, weight=4)
        
    def config_style(self):     
        self.styles = ttk.Style()
        self.styles.configure('Frame1.TFrame', background='white')
        self.styles.configure('Frame2.TFrame', background='white')
        self.styles.configure('Test.TLabel', background= 'white')
        
        self.styles.configure('TButton.info', background='lime', foreground='black', width=20, borderwidth=1, focusthickness=3,focuscolor='none')
        self.styles.map('TButton.info', background=[('active', 'green')])
    
    def load_header(self):
        self.file_path = StringVar()
        
        self.file_path.trace_add("write", self.change_file_path)
        
        self.button_file = ttk.Button(self.root, text="Cargar Archivo", command=lambda: self.file_path.set(self._events_buttons.search_files()))
        self.button_file.pack() 

        self.label_file_path = ttk.Label(self.root, textvariable=self.file_path)
        self.label_file_path.pack()
           
    def change_file_path(self, name='', index='', mode=''):
        if len(self.file_path.get()) > 0:
            self.button_correlation = ttk.Button(self.form_left, text="Correlation Test", command=lambda: self.load_correlation())        
            self.button_correlation.place(x=20, y=20)
    
    def load_correlation(self):
        print("entra?")
        self.open_modal_correlation()
        
    def open_modal_correlation(self):        
        #asyncio.ensure_future(self._events_buttons.generate_correlation(self.root))
        #select_correlation(root)
        print( self._events_buttons)
        result = correlacion_app(self.root, self._events_buttons.data_head, self._events_buttons.data_file).show()
        print(result)
        return result
        
        
         
        
    
    #def create_label_titulo(self):
        
    
        
    