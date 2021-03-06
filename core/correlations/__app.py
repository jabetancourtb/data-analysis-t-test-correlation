from tkinter import ttk, StringVar, IntVar, Button, Listbox, Radiobutton, Toplevel, MULTIPLE
from core.correlations.correlation_test import correlacion_test
from logic_graphics import logic_graphics
import time


class correlacion_app(object):
    
    def __init__(self, root):
                
        self.toplevel = Toplevel(root)
        self.toplevel.title("Confirmation")
        self.toplevel.geometry("500x500")
        self.toplevel.config(bg="white")          
    
    
    def init_form(self, headers, data_file):
        self.init_variable()
        
        #datos de retorno
        self.data_result = []
        
        #Filter value numeric
        filet_head_numeric = data_file.select_dtypes(include='number')
        self.headers = filet_head_numeric
        self.data_file = data_file                
                   
        for idx, valx in enumerate(self.headers):
            _headers.set(_headers.get() + " " + valx)
        
        ttk.Label(self.toplevel, text="CORRELATION", font=("Helvetica", 13)).place(y=10,x=200)
        
        label_list = ttk.Label(self.toplevel, text="Seleccione los campos para la correlación").place(x=20, y=40)
        #label_list.pack()
        
        label_radio = ttk.Label(self.toplevel, text="Seleccione el tipo de correlación").place(x=280, y=40)
        #label_radio.pack()
        
        radio1 = Radiobutton(self.toplevel, text="Pearson correlation", variable=_seleccionRadio, value=1)
        radio1.place(x=280, y=60)
        
        radio2 = Radiobutton(self.toplevel, text="Spearman correlation", variable=_seleccionRadio, value=2)
        radio2.place(x=280, y=100)
        _seleccionRadio.set(1)


        radio3 = Radiobutton(self.toplevel, text="Full View", variable=_seleccionRadioFullView, value=1)
        radio3.place(x=280, y=200)

        radio4 = Radiobutton(self.toplevel, text="Reduce View", variable=_seleccionRadioFullView, value=2)
        radio4.place(x=280, y=260)
        _seleccionRadioFullView.set(1)

        
        
        self.list_box = Listbox(self.toplevel, listvariable=_headers, selectmode=MULTIPLE, width=20, height=10)
        self.list_box.place(x=20, y=60, width=200, height=300)                #grid(row=1, column=1, columnspan=2)
        #self.list_box.bind('<<ListboxSelect>>', self.prueba)
        
        # Add Button for making selection
        buttonAceptar = Button(self.toplevel, text="Generar", command=lambda: self.generate_correlation(), bg="blue", fg="white")    
        buttonAceptar.place(x=280, y=150)
        
        buttonCancel = Button(self.toplevel, text="Cancelar", command=lambda: self.cancel_correlation(), bg="blue", fg="white")
        buttonCancel.place(x=360, y=150)

    #def prueba(self, event):
    #    print("entra?")

    def init_variable(self):
        global _headers
        global _seleccionRadio
        global _seleccionRadioFullView

        _headers = StringVar() 
        _seleccionRadio = IntVar()
        _seleccionRadioFullView = IntVar()

    
    def cancel_correlation(self):
        self.data_result.append({'title': 'CORRELATION'})
        self.data_result.append({'text': 'Cancel correlation'})
        self.toplevel.destroy()
        
        
    def generate_correlation(self):

        options = []
        
        for i in self.list_box.curselection():
            options.append(self.list_box.get(i))
                
        self.data_result.append({'title': 'CORRELATION'})  
        if len(options) > 1:          
            for idx, valx in enumerate(options):
                for idy, valy in enumerate(options):
                    if idx < idy:                        
                        returl_pearson = {}
                        returl_spearman = {}
                        #Pearson correlation
                        if _seleccionRadio.get() == 1:
                            time_start = time.time()
                            returl_pearson['text'] = f'Pearson correlation of: "{valx}" and "{valy}"'
                            if _seleccionRadioFullView.get() == 1:
                                returl_pearson['text3'] = correlacion_test(self.data_file).pearson_cor(valx, valy)
                                returl_pearson['text2'] = logic_graphics().graphyc_scatter(self.data_file[valx], self.data_file[valy], returl_pearson['text'],valx,valy)
                                returl_pearson['image'] = returl_pearson['text2']
                                time_end = time.time()
                                returl_pearson['text4'] = f'Process time: {time_end - time_start}'
                                returl_pearson['text5'] = ''
                            else:
                                returl_pearson['text2'] = correlacion_test(self.data_file).pearson_cor(valx, valy)
                                time_end = time.time()
                                returl_pearson['text3'] = f'Process time: {time_end - time_start}'
                                returl_pearson['text4'] = ''
    
                        #Spearman correlation
                        if _seleccionRadio.get() == 2:
                            time_start = time.time()
                            returl_spearman['text'] = f'spearman correlation of, "{valx}" and "{valy}"'
                            if _seleccionRadioFullView.get() == 1:
                                returl_spearman['text3'] = correlacion_test(self.data_file).spearman_cor(valx, valy)
                                returl_spearman['text2'] = logic_graphics().graphyc_scatter(self.data_file[valx], self.data_file[valy], returl_spearman['text'],valx,valy)
                                returl_spearman['image'] = returl_spearman['text2']
                                time_end = time.time()
                                returl_spearman['text4'] = f'Process time: {time_end - time_start}'
                                returl_spearman['text5'] = ''
                            else:
                                returl_spearman['text2'] = correlacion_test(self.data_file).spearman_cor(valx, valy)
                                time_end = time.time()
                                returl_spearman['text3'] = f'Process time: {time_end - time_start}'
                                returl_spearman['text4'] = ''
                            
                        self.data_result.append(returl_pearson)
                        self.data_result.append(returl_spearman)
            if _seleccionRadioFullView.get() == 1:
                time_start = time.time()
                heat_map = {}
                heat_map['image2'] = logic_graphics().graphyc_matshow(self.data_file[options])
                time_end = time.time()
                heat_map['text'] = f'Process time: {time_end - time_start}'
                self.data_result.append(heat_map)
        else:           
            returl_pearson = {}
            returl_pearson['text'] = f'Minimo seleccione 2 propiedades para generar la correlacion'
            self.data_result.append(returl_pearson)
                        
        self.toplevel.destroy()
            
        
    def show(self):           
        self.toplevel.deiconify()
        self.toplevel.wait_window()
        
        
    def get_result(self):        
        returl = self.data_result
        return returl