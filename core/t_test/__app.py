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
            self.property_head.append((valx))
                                 
        label_titulo = ttk.Label(self.toplevel, text="T-Test one sample and T-Test paired", font=("Helvetica", 13))
        label_titulo.place(y=10,x=120)
        
        label_list = ttk.Label(self.toplevel, text="Seleccione los campos para T-Test")
        label_list.place(x=20, y=40)
        
        label_radio = ttk.Label(self.toplevel, text="Is T-Test one or Paired sample")
        label_radio.place(x=280, y=40)
            
        self.list_box = Listbox(self.toplevel, listvariable=_headers, selectmode=MULTIPLE, width=20, height=10)
        self.list_box.place(x=20, y=60, width=200, height=300)  
        self.list_box.bind('<<ListboxSelect>>', self.select_listbox_column)
        
        # Add Button for making selection
        buttonAceptar = Button(self.toplevel, text="Seleccionar", command=lambda: self.get_t_test_method(), bg="blue", fg="white")    
        buttonAceptar.place(x=280, y=220)
        
        buttonCancel = Button(self.toplevel, text="Cancelar", command=lambda: self.cancel_t_test(), bg="blue", fg="white")
        buttonCancel.place(x=360, y=220)
        
        radio1 = Radiobutton(self.toplevel, text="One sample T Test", variable=_seleccionRadio, value=1, command=self.change_sample_size_input)
        radio1.place(x=280, y=70)
        
        radio2 = Radiobutton(self.toplevel, text="Paired T Test", variable=_seleccionRadio, value=2, command=self.change_sample_size_input)
        radio2.place(x=280, y=100)
        
        _seleccionRadio.set(1)
        
        self.change_sample_size_input()
        
    
    # -- Create the input for sample size
    def change_sample_size_input(self):
        if _seleccionRadio.get() == 1:
            self.sample_size_label = Label(self.toplevel, text="Enter the sample size")
            self.sample_size_label.place(x=280, y=150)
            
            self.sample_size_input = ttk.Entry(self.toplevel)
            self.sample_size_input.place(x=280, y=180)
            
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
        self.cola_list = []
        self.property_head = []
        
        _headers = StringVar() 
        _seleccionRadio = IntVar()

    
    def cancel_t_test(self):
        self.data_result.append({'text': 'Cancel t test'})
        self.toplevel.destroy()
    
    def deseleccionar_list(self, options, num):
        index = -1
        for idx, valx in enumerate(options):      
            if valx not in self.cola_list:                    
                self.cola_list.append(valx)   
                print(self.cola_list)
                if len(self.cola_list) == num + 1:
                    index = self.property_head.index(self.cola_list[0])
                        
        if index != -1:
            self.list_box.selection_clear(index)
            self.cola_list.remove(self.cola_list[0]) 
        
    def select_listbox_column(self, avent):
        options = []
        
        for i in self.list_box.curselection():
            options.append(self.list_box.get(i))
        
        if len(self.cola_list) == 0:
            self.cola_list = options
        
        else:
            self.deseleccionar_list(options, _seleccionRadio.get())        
        #self.list_box.selection_clear(0)
        #self.list_box.select_set(10)
     
        
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