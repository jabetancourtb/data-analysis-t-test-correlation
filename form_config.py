from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import subprocess
import os

from events import  events_buttons
from core.correlations.__app import  correlacion_app
import asyncio
import time

class form_config(object):
    def __init__(self, root):
        # Create Panedwindow
        self.root = root
        
        #configuration panel rigth
        self._data = {}
        self._index = 0
        
        self._events_buttons = events_buttons()
        
    def __del__(self):
        print("Object deleted")
        
    def create_panel(self):
        self.panedwindow = ttk.Panedwindow(self.root, orient=HORIZONTAL)
        self.panedwindow.pack(fill=BOTH, expand=True)
        
        self.form_left = ttk.Frame(self.panedwindow, width=130, height=300, relief=SUNKEN, style='Frame1.TFrame')
        self.form_rigth = ttk.Frame(self.panedwindow, width=400, height=400, relief=SUNKEN, style='Frame2.TFrame')
                 
           
    def see_panel(self):      
        self.panedwindow.add(self.form_left, weight=1)
        self.panedwindow.add(self.form_rigth, weight=4)
        
        # create scrollbars
        self.yscrollbar = Scrollbar(self.form_rigth, orient='vertical')  # create Y axis scrollbar and assign to frame2
        self.yscrollbar.pack( side = RIGHT, fill=Y )  # right side vertical scrollbar
        
        self.canvas = Text(self.form_rigth, wrap = 'none', yscrollcommand = self.yscrollbar.set)
        self.canvas.pack(expand=True, fill='both')
        self.panedwindow.update()
        
        
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
            self.button_correlation = ttk.Button(self.form_left, text="Correlation Test", command=lambda: self.open_modal_correlation())                   
            self.button_correlation.place(relx=0.5,y=20, anchor=CENTER)
            
            #self.button_correlation2 = ttk.Button(self.form_left, text="generate pdf", command=lambda: self.generate_pdf())                   
            #self.button_correlation2.place(relx=0.5,y=60, anchor=CENTER)            
            
    
    def open_modal_correlation(self):   
        result = []
        app_correlation = correlacion_app(self.root)
        app_correlation.init_form(self._events_buttons.data_head, self._events_buttons.data_file)
        app_correlation.show()
        result = app_correlation.get_result()
        self.show_result(result)
    
    def show_result(self, result):        
        for r in result:
            if "title" in r:
                self.add_title(r['title'])
            
            if "text" in r:
                self.add_text(r['text'])
            
            if "image" in r:
                self.add_image(r['image'], r['image_width'], r['image_height'])
                
            index = 2
            for x in range(10):
                if f'text{index}' in r:
                    self.add_text(r[f'text{index}'])                
                else:
                    break                
                index = index + 1
                
    
    def get_index(self):
        self._index = self._index + 1
        return self._index
    
    
    def add_title(self, texto):
        
        index = self.get_index()        
        self._data[f'root_tile_{index}'] = ttk.Label(self.form_rigth, text= f'\n{texto}', font=("Helvetica", 13))
        
        self.canvas.insert("end", "\n\n")
        self.canvas.window_create("end", window=self._data[f'root_tile_{index}'])
        self.canvas.insert("end", "\n\n")
        self.panedwindow.update()
    
    
    def add_text(self, texto):
        index = self.get_index()
        self._data[f'root_text_{index}'] = ttk.Label(self.form_rigth, text= f'\n{texto}', font=("Helvetica", 10))
        
        self.canvas.window_create("end", window=self._data[f'root_text_{index}'])
        self.canvas.insert("end", "\n")        
        self.panedwindow.update()
    
    
    def add_image(self, path_image, width, height):
        
        index = self.get_index()
        
        image = Image.open(path_image)
        resize_image = image.resize((width, height))
        
        img = ImageTk.PhotoImage(resize_image)
        
        self._data[f'root_image_{index}'] = ttk.Label(self.form_rigth, image=img)
        self._data[f'root_image_{index}'].photo = img        
        self.canvas.window_create("end", window=self._data[f'root_image_{index}'])
        self.canvas.insert("end", "\n")        
        self.panedwindow.update()
             
    
        
    
        
    