import tkinter as tk
from tkinter import messagebox
from Bienvenida import Bienvenida


class Menu(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.quit = None
        self.master = master
        self.pack()
        self.inicializar()



    def salir_del_ciclo(self):
        self.quit()


    def inicializar(self):

        super(Bienvenida)

        lbl_menu = tk.Label(self, text="Menu\n"
                                     "1-Materias del Plan\n"
                                     "2-Estádo Académico\n"
                                     "3-Exámenes\n"
                                     "4-Correlatividad para cursar\n"
                                     "5-Correlatividad para rendir\n"
                                     "6-Avisos\n"
                                     "7-Salir", justify=tk.LEFT)
        lbl_menu.grid(row=0, column=0)

        self.entry = tk.Entry(self, width=20)
        self.entry.grid(row=0, column=1)


        self.btn_opcion = tk.Button(self, text="Opción", justify=tk.RIGHT)
        self.btn_opcion['command'] = self.menu
        self.btn_opcion.grid(row=0, column=2)


        self.boton_salir = tk.Button(self.quit, text="Salir", command=Menu.salir_del_ciclo)
        self.boton_salir.place(x=60, y=130)


    def menu(self):

        opcion = int((self.entry.get()))

        if opcion == 1:
            messagebox.showinfo('Materias del plan\n', """"
            Año    |   Dic.    |         Materia        | Se cursa | Se rinde  |
                 1    |    1c      |Matemática          |   Si          |    Si          |
                 1    |    1c      |Programación 1   |   Si          |    Si          |
                 1    |    1c      |Proc de Datos      |   Si          |    Si          |
                 1    |    1c      |Matemática          |   Si          |    Si          |
                 1    |    1c      |Ingles 1                |   Si          |    Si          |
                 1    |    1c      |Lab comp 1          |   Si          |    Si          |
                 1    |    2c      |Programación 2   |   Si          |    Si         |
                 1    |    2c      |Arq y Sist Op        |   Si          |    Si         |
                 1    |    2c      |Estadística            |   Si          |    Si         |
                 1    |    2c      |Ingles 2                 |   Si          |    Si        |
                 1    |    2c      |Lab comp 2           |   Si          |    Si        |
                 1    |    2c      |Met de la inv        |   Si          |    Si        |
                                        """)

        elif opcion == 2:
            messagebox.showinfo('Estado Académico\n', """"
                                          Año    |         Materia        | Estado | 
                                             1      |Matemática****    |cursa    |
                                             1      |Programación 1    |cursa    |
                                             1      |Proc de Datos*     |cursa    |
                                             1      |Matemática****    |cursa    |
                                             1      |Ingles 1******       |cursa    |
                                             1      |Lab comp 1****    |cursa    |
                                             1      |Programación 2   |cursa    |
                                             1      |Arq y Sist Op*      |cursa    |
                                             1      |Estadística***       |cursa    |
                                             1      |Ingles 2******       |cursa    |
                                             1      |Lab comp 2****    |cursa    |
                                             1      |Met de la inv*      |cursa    |
                                          """)

        elif opcion == 3:
            messagebox.showinfo("Próximos exámenes: 2do semestre julio/2023")
        elif opcion == 4:
            messagebox.showinfo('Correlatividad Cursar\n', """"
            Año    |         Materia        | Correlatividad  |
                1     |Matemática****    |  Puede cursar   |
                1     |Programación 1    |  Puede cursar   |
                1     |Proc de Datos*     |  Puede cursar   |
                1     |Matemática****    |  Puede cursar   |
                1     |Ingles 1******       |  Puede cursar   |
                1     |Lab comp 1****    |  Puede cursar   |
                1     |Programación 2   |  Puede cursar   |
                1     |Arq y Sist Op*      |  Puede cursar   |
                1     |Estadística***       |  Puede cursar   |
                1     |Ingles 2******       |  Puede cursar   |
                1     |Lab comp 2****    |  Puede cursar   |
                1     |Met de la inv*       |  Puede cursar   |
                                        """)
        elif opcion == 5:
            messagebox.showinfo('Correlatividad Rendir\n', """"
            Año    |         Materia        | Correlatividad |
                 1    |Matemática****    |     Regular     |
                 1    |Programación 1    |     Regular     |
                 1    |Proc de Datos*     |     Regular     |
                 1    |Matemática****    |     Regular     |
                 1    |Ingles 1******       |     Regular     |
                 1    |Lab comp 1****    |     Regular     |
                 1    |Programación 2   |     Regular     |
                 1    |Arq y Sist Op*      |     Regular     |
                 1    |Estadística***       |     Regular     |
                 1    |Ingles 2******       |     Regular     |
                 1    |Lab comp 2****    |     Regular     |
                 1    |Met de la inv*       |     Regular     |
                                        """)
        elif opcion == 6:
            messagebox.showinfo("No hay avisos importantes.")
        elif opcion == 7:
            messagebox.showinfo("Gracias por utilizar Sysacad")

        else:
            messagebox.showwarning("error", "ingrese una opción válida")


def main():

    app = tk.Tk()
    app.title('********Menu*******')
    app.geometry('450x200')
    ventana = Menu(app)
    ventana.mainloop()
    app.quit()


if __name__ == "__main__":
    main()


