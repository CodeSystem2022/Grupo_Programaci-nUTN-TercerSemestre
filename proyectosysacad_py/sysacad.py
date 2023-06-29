import tkinter as tk
from tkinter import messagebox
import psycopg2


class Bienvenida(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Bienvenido")
        self.geometry("400x200")
        self.resizable(False, False)
        self.config(bg="blue")

        label_bienvenida = tk.Label(self, text="¡Bienvenido!", font=("Arial", 16), bg="blue", fg="white")
        label_bienvenida.pack(pady=20)

        button_aceptar = tk.Button(self, text="Aceptar", command=self.cerrar_ventana)
        button_aceptar.pack(pady=10)

    def cerrar_ventana(self):
        self.destroy()


   def mostrar_opcion1(self):
        self.withdraw()  # Ocultar la ventana del menú
        opcion1_window = Opcion1Window(self)  # Crear una nueva ventana para la opción 1

    def mostrar_opcion2(self):
        self.withdraw()
        opcion2_window = Opcion2Window(self)  # Crear una nueva ventana para la opción 2

    def mostrar_opcion3(self):
        self.withdraw()
        opcion3_window = Opcion3Window(self)  # Crear una nueva ventana para la opción 3

    def mostrar_opcion4(self):
        self.withdraw()
        opcion3_window = Opcion4Window(self)  # Crear una nueva ventana para la opción 4

    def mostrar_opcion5(self):
        self.withdraw()
        opcion3_window = Opcion5Window(self)  # Crear una nueva ventana para la opción 5

    def mostrar_opcion6(self):
        self.destroy()
        self.master.deiconify()
