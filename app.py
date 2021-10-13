from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from window.upload_file import upload_file,init
from core.correlations.__app import  correlacion_app
from form_config import  form_config
import pandas as pd
import os


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


def _init():    
    config_panel.load_header()
    config_panel.create_panel()
    config_panel.see_panel()
    config_panel.config_style()
    
    
# Configuración de la raíz
root = Tk()

root.geometry('800x500')

menubar = Menu(root)
root.config(menu=menubar)

config_panel = form_config(root)
    
_init()


# Finalmente bucle de la aplicación
root.mainloop()
