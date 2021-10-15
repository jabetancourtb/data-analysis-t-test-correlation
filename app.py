#!/usr/bin/python3
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from window.upload_file import upload_file, init
from core.correlations.__app import correlacion_app
from form_config import form_config
import pandas as pd
import os


class app(object):
    def __init__(self):
        # Configuración de la raíz
        self.root = Tk()
        self.root.geometry('800x500')

        self.config_panel = form_config(self.root)
        self._init()

        self.menubar = Menu(self.root)
        self.root.config(menu=self.menubar)
        self.load_menu()

        self.root.mainloop()

    def load_menu(self):
        # Menu Archivo
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Nuevo", command=lambda: self._new_form())
        filemenu.add_command(label="Cargar Archivo", command=lambda: self._load_file())
        filemenu.add_command(label="Guardar")
        filemenu.add_command(label="Cerrar")
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=lambda: self._destroy_root())

        # Menu editar
        editmenu = Menu(self.menubar, tearoff=0)
        editmenu.add_command(label="Cortar")
        editmenu.add_command(label="Copiar")
        editmenu.add_command(label="Pegar")

        # Menu ayuda
        helpmenu = Menu(self.menubar, tearoff=0)
        helpmenu.add_command(label="Ayuda")
        helpmenu.add_separator()
        helpmenu.add_command(label="Tutorial", command=lambda: self.config_panel.open_tutorial())

        self.menubar.add_cascade(label="Archivo", menu=filemenu)
        self.menubar.add_cascade(label="Editar", menu=editmenu)
        self.menubar.add_cascade(label="Ayuda", menu=helpmenu)

    def _load_file(self):
        self.config_panel.load_path_file()

    def _destroy_root(self):
        self.root.destroy()

    def _new_form(self):
        self.config_panel.destroy_form()
        self.config_panel = form_config(self.root)
        self._init()

    def _init(self):
        self.config_panel.load_header()
        self.config_panel.create_panel()
        self.config_panel.see_panel()
        self.config_panel.config_style()


app()
