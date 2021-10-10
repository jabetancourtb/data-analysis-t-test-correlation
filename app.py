from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from window.upload_file import upload_file,init
from core.correlations.__app import  correlacion_app
import pandas as pd
import os


# https://www.pythontutorial.net/tkinter/tkinter-grid/
# https://www.tutorialspoint.com/how-to-create-a-modal-dialog-in-tkinter
# https://likegeeks.com/es/ejemplos-de-la-gui-de-python/

def find_file():
    archivoAbierto = filedialog.askopenfilename(initialdir="/", title="Seleccione archivo",
                                                filetypes=(("CSV Files", "*.csv"),))

    if len(archivoAbierto) > 0:
        _LblNombreRutaArchivo.set(archivoAbierto + "");


def inis():
     
     init()

def choice(option):
    pop.destroy()
    if option == "yes":
        label.config(text="Hello, How are You?")
    else:
        label.config(text="You have selected No")

def get_data_file():    
    data_file = upload_file(_LblNombreRutaArchivo.get())
    return data_file


def get_data_file_header():    
    data_file = get_data_file()
    _DataHeader= []
    for idx, valx in enumerate(data_file.columns):
        _DataHeader.append(valx)
    return _DataHeader

def load_correlation():
    data_file = get_data_file()    
    data_header = get_data_file_header()
    
    white_title_result("Cargando Correlación")
    result = correlacion_app(root,data_header, data_file).show()
    #select_correlation(root)
    print(result)
    #result = return_correlation()
    whire_result(result)



def load_menu():
    # Menu Archivo
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Nuevo", command=new)
    filemenu.add_command(label="Arrastrar Archivo")
    filemenu.add_command(label="Guardar", command=inis)
    filemenu.add_command(label="Cerrar")
    filemenu.add_separator()
    filemenu.add_command(label="Salir", command=root.quit)

    # Menu editar
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cortar")
    editmenu.add_command(label="Copiar")
    editmenu.add_command(label="Pegar")

    # Menu ayuda
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Ayuda")
    helpmenu.add_separator()
    helpmenu.add_command(label="Acerca de...")

    menubar.add_cascade(label="Archivo", menu=filemenu)
    menubar.add_cascade(label="Editar", menu=editmenu)
    menubar.add_cascade(label="Ayuda", menu=helpmenu)


def white_title_result(title):
    _message_result.set(_message_result.get() + "\n\n\n" + title + "\n")

def whire_result(text):
    _message_result.set(_message_result.get() + "\n" + text)
    
def new():
    define_variables()
    form_head()
    form_body()

def define_variables():
    global _message_result
    _message_result = StringVar()

def form_head():
    global _LblNombreRutaArchivo
    global _BtnCargarArchivo

    _LblNombreRutaArchivo = StringVar()

    _BtnCargarArchivo = ttk.Button(root, text="Cargar Archivo", command=find_file)
    style = ttk.Style()
    style.theme_use('alt')
    style.configure('TButton', background='lime', foreground='black', width=20, borderwidth=1, focusthickness=3,
                    focuscolor='none')
    style.map('TButton', background=[('active', 'green')])
    _BtnCargarArchivo.pack()

    LblRutaArchivo = ttk.Label(root, textvariable=_LblNombreRutaArchivo)
    LblRutaArchivo.pack()


def form_body():
    global _fram1
    global _fram2

    # Create Panedwindow
    panedwindow = ttk.Panedwindow(root, orient=HORIZONTAL)
    panedwindow.pack(fill=BOTH, expand=True)

    # Create Frams
    _fram1 = ttk.Frame(panedwindow, width=100, height=300, relief=SUNKEN)
    
    
    button_correlation = Button(_fram1, text="Correlation Test", command=load_correlation, bg="blue", fg="white")
    button_correlation.grid(row=1, column=1)
    
    _fram2 = ttk.Frame(panedwindow, width=400, height=400, relief=SUNKEN)
    panedwindow.add(_fram1, weight=1)
    panedwindow.add(_fram2, weight=4)
        
    form2 = ttk.Label(_fram2, textvariable=_message_result)
    form2.pack()


# Configuración de la raíz
root = Tk()

root.geometry('700x400')

menubar = Menu(root)
root.config(menu=menubar)

load_menu()
new()


# Finalmente bucle de la aplicación
root.mainloop()
