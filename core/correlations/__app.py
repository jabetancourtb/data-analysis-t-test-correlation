from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from core.correlations.correlation_test import correlacion_test
import pandas as pd
import os

class correlacion_app(object):
    
    def __init__(self, root, headers, data_file):
              
        def white_title_result_correlation(title):
            _result.set(_result.get() + "\n\n" + title)
        
        def whire_result_correlation(text):
            _result.set(_result.get() +  "\n" + text)    
        
        def return_correlation():
            return _result
        
        def cancel_correlation():
            self.toplevel.destroy()
            
        def generate_correlation():    
            
            options = []
            
            for i in _list_box.curselection():
                options.append(_list_box.get(i))
                    
            if len(options) > 1:            
                for idx, valx in enumerate(options):
                    for idy, valy in enumerate(options):
                        if idx < idy:
                            print(_seleccionRadio.get())
                            #Pearson correlation
                            if _seleccionRadio.get() == 1:
                                white_title_result_correlation("Pearson correlation, '" + valx + "' and '" + valy + "'")
                                whire_result_correlation(correlacion_test(data_file).pearson_cor(valx, valy))                        
                
                            #Spearman correlation
                            if _seleccionRadio.get() == 2:
                                white_title_result_correlation("Spearman correlation, '" + valx + "' and '" + valy + "'")
                                whire_result_correlation(correlacion_test(data_file).spearman_cor(valx, valy)) 
                                
            self.toplevel.destroy()
                
        
        global _headers
        global _result
        global _list_box
        global _seleccionRadio
        
        _headers = StringVar()    
        for idx, valx in enumerate(headers):
            _headers.set(_headers.get() + " " + valx)
        
        _seleccionRadio = IntVar()
        _result = StringVar()             
        
        self.toplevel = Toplevel(root)
        self.toplevel.title("Confirmation")
        self.toplevel.geometry("500x300")
        self.toplevel.config(bg="white")
    
        #pop.columnconfigure(0, weight=3)
        #pop.columnconfigure(1, weight=3)
        
        radio1 = Radiobutton(self.toplevel, text="Pearson correlation", variable=_seleccionRadio, 
                    value=1)
        radio1.grid(row=2, column=0)
        
        radio2 = Radiobutton(self.toplevel, text="Spearman correlation", variable=_seleccionRadio,
                    value=2)
        radio2.grid(row=3, column=0)
    
            
        print(_headers)
        
    
        _list_box = Listbox(self.toplevel, listvariable=_headers, selectmode=MULTIPLE, width=20, height=10)
        _list_box.grid(row=1, column=1, columnspan=2)
    
        
        # Add Button for making selection
        buttonAceptar = Button(self.toplevel, text="Seleccionar", command=generate_correlation, bg="blue", fg="white")    
        buttonAceptar.grid(row=4, column=0)
        
        buttonCancel = Button(self.toplevel, text="Cancelar", command=cancel_correlation, bg="blue", fg="white")
        buttonCancel.grid(row=5, column=0)    

          
            
        
    def show(self):        
        
        self.toplevel.deiconify()
        self.toplevel.wait_window()
        value = _result.get()
        return value