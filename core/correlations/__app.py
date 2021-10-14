from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from core.correlations.correlation_test import correlacion_test
import pandas as pd
import os

class correlacion_app(object):
    
    def __init__(self, root):
                
        self.toplevel = Toplevel(root)
        self.toplevel.title("Confirmation")
        self.toplevel.geometry("500x300")
        self.toplevel.config(bg="white")        
    
    
    def init_form(self, headers, data_file):
        self.init_variable()
        
        #datos de retorno
        self.data_result = []
        self.data_result.append({'title': 'CORRELATION'})
        
        #Filter value numeric
        filet_head_numeric = data_file.select_dtypes(include='number')
        self.headers = filet_head_numeric
        self.data_file = data_file                
                   
        for idx, valx in enumerate(self.headers):
            _headers.set(_headers.get() + " " + valx)
                         
        radio1 = Radiobutton(self.toplevel, text="Pearson correlation", variable=_seleccionRadio, value=1)
        radio1.grid(row=2, column=0)
        
        radio2 = Radiobutton(self.toplevel, text="Spearman correlation", variable=_seleccionRadio, value=2)
        radio2.grid(row=3, column=0)
        _seleccionRadio.set(1)
                
        self.list_box = Listbox(self.toplevel, listvariable=_headers, selectmode=MULTIPLE, width=20, height=10)
        self.list_box.grid(row=1, column=1, columnspan=2)
        
        # Add Button for making selection
        buttonAceptar = Button(self.toplevel, text="Seleccionar", command=lambda: self.generate_correlation(), bg="blue", fg="white")    
        buttonAceptar.grid(row=4, column=0)
        
        buttonCancel = Button(self.toplevel, text="Cancelar", command=lambda: self.cancel_correlation(), bg="blue", fg="white")
        buttonCancel.grid(row=5, column=0)    


    def init_variable(self):
        global _headers
        global _seleccionRadio
        
        _headers = StringVar() 
        _seleccionRadio = IntVar()

    
    def cancel_correlation(self):
        self.data_result.append({'text': 'Cancel correlation'})
        self.toplevel.destroy()
        
        
    def generate_correlation(self):    
        
        options = []
        
        for i in self.list_box.curselection():
            options.append(self.list_box.get(i))
                
        if len(options) > 1:            
            for idx, valx in enumerate(options):
                for idy, valy in enumerate(options):
                    if idx < idy:                        
                        returl_pearson = {}
                        #Pearson correlation
                        if _seleccionRadio.get() == 1:
                            
                            returl_pearson['text'] = f'Pearson correlation of: "{valx}" and "{valy}"'
                            returl_pearson['text2'] = correlacion_test(self.data_file).pearson_cor(valx, valy)                      
                            returl_pearson['text3'] = ''
    
                        #Spearman correlation
                        if _seleccionRadio.get() == 2:
                            returl_pearson['text'] = 'Spearman correlation of, "{valx}" and "{valy}"'
                            returl_pearson['text2'] = correlacion_test(self.data_file).spearman_cor(valx, valy) 
                            returl_pearson['text3'] = ''
                            
                        self.data_result.append(returl_pearson)
                                                        
        self.toplevel.destroy()
            
        
    def show(self):           
        self.toplevel.deiconify()
        self.toplevel.wait_window()
        
        
    def get_result(self):        
        returl = self.data_result
        return returl