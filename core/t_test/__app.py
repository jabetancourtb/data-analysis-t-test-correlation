from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from core.t_test.t_test import t_test
import pandas as pd
import os

class t_test_app(object):
    
    def __init__(self, root):
        self.toplevel = Toplevel(root)
        self.toplevel.title("Confirmation")
        self.toplevel.geometry("500x300")
        self.toplevel.config(bg="white")        
    
    
    def init_form(self, headers, data_file):
        self.init_variable()
        
        #datos de retorno
        self.data_result = []
        self.data_result.append({'title': 'T TEST'})
        
        #Filter value numeric
        filet_head_numeric = data_file.select_dtypes(include='number')
        self.headers = filet_head_numeric
        self.data_file = data_file                
                   
        for idx, valx in enumerate(self.headers):
            _headers.set(_headers.get() + " " + valx)
                         
        self.list_box = Listbox(self.toplevel, listvariable=_headers, selectmode=MULTIPLE, width=20, height=10)
        self.list_box.grid(row=1, column=1, columnspan=2)
        self.list_box.bind('<<ListboxSelect>>', self.select_listbox_column)
        
        # Add Button for making selection
        buttonAceptar = Button(self.toplevel, text="Seleccionar", command=lambda: self.get_t_test_method(), bg="blue", fg="white")    
        buttonAceptar.grid(row=4, column=0)
        
        buttonCancel = Button(self.toplevel, text="Cancelar", command=lambda: self.cancel_t_test(), bg="blue", fg="white")
        buttonCancel.grid(row=5, column=0) 
        
        radio1 = Radiobutton(self.toplevel, text="One sample T Test", variable=_seleccionRadio, value=1, command=self.change_sample_size_input)
        radio1.grid(row=2, column=0)
        
        radio1 = Radiobutton(self.toplevel, text="Paired T Test", variable=_seleccionRadio, value=2, command=self.change_sample_size_input)
        radio1.grid(row=3, column=0)
        
        _seleccionRadio.set(1)
        
        self.change_sample_size_input()
        
    
    # -- Create the input for sample size
    def change_sample_size_input(self):
        if _seleccionRadio.get() == 1:
            self.sample_size_label = Label(self.toplevel, text="Enter the sample size")
            self.sample_size_label.grid(row=0, column=3)
            
            self.sample_size_input = ttk.Entry(self.toplevel)
            self.sample_size_input.grid(row=1, column=3)
            
        elif _seleccionRadio.get() == 2:
            self.sample_size_label.destroy()
            self.sample_size_input.destroy()
       
        
    # -- Execute the method depending on the selected radiobutton
    def get_t_test_method(self):
        if _seleccionRadio.get() == 1:
            self.generate_one_sample_t_test()
        elif _seleccionRadio.get() == 2:
            self.generate_paired_t_test()
        

    def init_variable(self):
        global _headers
        global _seleccionRadio
        
        _headers = StringVar() 
        _seleccionRadio = IntVar()

    
    def cancel_t_test(self):
        self.data_result.append({'text': 'Cancel t test'})
        self.toplevel.destroy()
        
        
    def select_listbox_column(self, event):
        if _seleccionRadio.get() == 1:
            self.options = ""

            self.list_box.bind('<FocusOut>', lambda e: self.list_box.selection_clear(9, END))
            
            for i in self.list_box.curselection():
                list_box_length = len(self.list_box.curselection()) + 1
                self.options = self.list_box.get(i)
                
        elif _seleccionRadio.get() == 2:
            options = []
        
            for i in self.list_box.curselection():
                options.append(self.list_box.get(i))
        
        
    def generate_one_sample_t_test(self):
        self.sample_size = int(self.sample_size_input.get())
             
        if self.options != "":            
            t_statictic = t_test(self.data_file).one_sample_t_test(self.sample_size, self.options)[0]
            p_value = t_test(self.data_file).one_sample_t_test(self.sample_size, self.options)[1]
            return_t_test = {}
            return_t_test['text'] = f'T Test of: "{self.options}" with "{self.sample_size}" samples'
            return_t_test['text2'] = f'Test statistic: {t_statictic}, p-value: {p_value}'                  
            return_t_test['text3'] = '' 
            self.data_result.append(return_t_test)
                
        print(self.data_result)                                             
        self.toplevel.destroy()
        
        
    def generate_paired_t_test():
        if len(options) > 1:            
            for idx, valx in enumerate(options):
                for idy, valy in enumerate(options):
                    if idx < idy:
                        t_statictic = t_test(self.data_file).paired_t_test(self.options[0], self.options[1])[0]
                        p_value = t_test(self.data_file).paired_t_test(self.options[0], self.options[1])[1]
                        return_t_test = {}
                        return_t_test['text'] = f'T Test of: "{self.options}" with "{self.sample_size}" samples'
                        return_t_test['text2'] = f'Test statistic: {t_statictic}, p-value: {p_value}'                  
                        return_t_test['text3'] = ''                  
                        self.data_result.append(return_t_test)
                                                        
        self.toplevel.destroy()
            
        
    def show(self):           
        self.toplevel.deiconify()
        self.toplevel.wait_window()
        
        
    def get_result(self):        
        returl = self.data_result
        return returl