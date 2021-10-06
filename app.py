from tkinter import *
from tkinter import filedialog
from tkinter import ttk  
import pandas as pd
import os

#https://www.pythontutorial.net/tkinter/tkinter-grid/
#https://www.tutorialspoint.com/how-to-create-a-modal-dialog-in-tkinter
#https://likegeeks.com/es/ejemplos-de-la-gui-de-python/

def BuscarArchivo():
    
    archivoAbierto = filedialog.askopenfilename(initialdir = "/", title = "Seleccione archivo",filetypes = (("CSV Files","*.csv"),))
    
    if len(archivoAbierto) > 0:  
        LblNombreRutaArchivo.set(archivoAbierto + "");  
        data = pd.read_csv (r'' + archivoAbierto)        
        DataHeader = data.columns
        

#def CargarMenu():
    
def choice(option):
   pop.destroy()
   if option == "yes":
      label.config(text="Hello, How are You?")
   else:
      label.config(text="You have selected No")
    
def ModalHeader():
   global pop
   pop = Toplevel(root)
   pop.title("Confirmation")
   pop.geometry("500x300")
   pop.config(bg="white")
   
   pop.columnconfigure(0, weight=1)
   pop.columnconfigure(1, weight=3)
      
   
   col = 1
   row = 1
   
   for dh in DataHeader:
       lbl = Label(pop, text=dh)
       lbl.grid(column = col, row = row)
       row += 1
       
   # Add Button for making selection
   button1 = Button(frame, text="Yes", command=lambda: choice("yes"), bg="blue", fg="white")
   button1.grid(row=0, column=1)
   button2 = Button(frame, text="No", command=lambda: choice("no"), bg="blue", fg="white")
   button2.grid(row=0, column=2)



    
def CargarMenu():    
    #Menu Archivo
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Nuevo", command=Nuevo)
    filemenu.add_command(label="Arrastrar Archivo", command=ModalHeader)
    filemenu.add_command(label="Guardar")
    filemenu.add_command(label="Cerrar")
    filemenu.add_separator()
    filemenu.add_command(label="Salir", command=root.quit)
    
    #Menu editar
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cortar")
    editmenu.add_command(label="Copiar")
    editmenu.add_command(label="Pegar")
    
    #Menu ayuda
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Ayuda")
    helpmenu.add_separator()
    helpmenu.add_command(label="Acerca de...")
    
    
    menubar.add_cascade(label="Archivo", menu=filemenu)
    menubar.add_cascade(label="Editar", menu=editmenu)
    menubar.add_cascade(label="Ayuda", menu=helpmenu)
    
def DefinirVariables():
    global DataHeader
    DataHeader = ["1","2","3"]
    
    
def Nuevo():
    FormularioHead()
    FormularioBody()
    
    
def FormularioHead():   
    
    global LblNombreRutaArchivo
    global BtnCargarArchivo
    
    LblNombreRutaArchivo = StringVar()
    
    BtnCargarArchivo = ttk.Button(root, text = "Cargar Archivo", command = BuscarArchivo)
    style = ttk.Style()
    style.theme_use('alt')
    style.configure('TButton', background = 'lime', foreground = 'black', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
    style.map('TButton', background=[('active','green')])
    BtnCargarArchivo.pack()  
    
    LblRutaArchivo = ttk.Label(root, textvariable=LblNombreRutaArchivo)
    LblRutaArchivo.pack()
    

def FormularioBody():
    
    global fram1
    global fram2
    
    #Create Panedwindow  
    panedwindow=ttk.Panedwindow(root, orient=HORIZONTAL)  
    panedwindow.pack(fill=BOTH, expand=True)  
    
    #Create Frams  
    fram1=ttk.Frame(panedwindow,width=100,height=300, relief=SUNKEN)  
    fram2=ttk.Frame(panedwindow,width=400,height=400, relief=SUNKEN)  
    panedwindow.add(fram1, weight=1)  
    panedwindow.add(fram2, weight=4) 
    


# Configuración de la raíz
root = Tk()

root.geometry('700x400')

menubar = Menu(root)
root.config(menu=menubar)

CargarMenu()
Nuevo()
DefinirVariables()

 
# Finalmente bucle de la aplicación
root.mainloop()




