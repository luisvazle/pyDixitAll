import pickle
import os
from tkinter import *
from tkinter.scrolledtext import ScrolledText


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("DixitAll")

        self.verificar_carpeta_datos()

        self.logo = PhotoImage(file="DixitAllLogo.png")  
        self.logo_label = Label(self.master, image=self.logo)
        self.logo_label.pack(side=LEFT)

        self.clave_label = Label(self.master, text="Término:")
        self.clave_label.pack()
        self.clave_entry = Entry(self.master)
        self.clave_entry.pack()

        self.valor_label = Label(self.master, text="Definición:")
        self.valor_label.pack()
        self.valor_entry = ScrolledText(self.master, wrap=WORD, width=50, height=10)
        self.valor_entry.pack()

        self.guardar_button = Button(self.master, text="Guardar", command=self.guardar)
        self.guardar_button.pack()

        self.modificar_button = Button(self.master, text="Modificar", command=self.modificar)
        self.modificar_button.pack()

        self.eliminar_button = Button(self.master, text="Eliminar", command=self.eliminar)
        self.eliminar_button.pack()

        self.consultar_label = Label(self.master, text="Término a consultar:")
        self.consultar_label.pack()
        self.consultar_entry = Entry(self.master)
        self.consultar_entry.pack()

        self.consultar_button = Button(self.master, text="Consultar", command=self.consultar)
        self.consultar_button.pack()

        self.salida_label = Label(self.master, text="Definición:")
        self.salida_label.pack()
        self.salida = ScrolledText(self.master, wrap=WORD, width=50, height=10)
        self.salida.pack()

        self.lista_label = Label(self.master, text="Términos almacenados:")
        self.lista_label.pack()
        self.lista_scroll = Scrollbar(self.master)
        self.lista_scroll.pack(side=RIGHT, fill=Y)
        self.lista = Listbox(self.master, width=50, yscrollcommand=self.lista_scroll.set, height=10)
        self.lista.pack()
        self.lista_scroll.config(command=self.lista.yview)

        try:
            with open("datos/datos.pickle", "rb") as f:
                self.datos = pickle.load(f)
        except FileNotFoundError:
            self.datos = {}

        self.actualizar_lista()

    def verificar_carpeta_datos(self):
        if not os.path.exists("datos"):
            os.makedirs("datos")

    def guardar(self):
        clave = self.clave_entry.get()
        valor = self.valor_entry.get("1.0", END)
        self.datos[clave] = valor
        with open("datos/datos.pickle", "wb") as f:
            pickle.dump(self.datos, f)
        self.actualizar_lista()

    def modificar(self):
        clave = self.clave_entry.get()
        valor = self.valor_entry.get("1.0", END)
        if clave in self.datos:
            self.datos[clave] = valor
            with open("datos/datos.pickle", "wb") as f:
                pickle.dump(self.datos, f)
            self.actualizar_lista()
        else:
            self.salida.delete("1.0", END)
            self.salida.insert(INSERT, "El término no existe")

    def eliminar(self):
        clave = self.clave_entry.get()
        if clave in self.datos:
            del self.datos[clave]
            with open("datos/datos.pickle", "wb") as f:
                pickle.dump(self.datos, f)
            self.actualizar_lista()
        else:
            self.salida.delete("1.0", END)
            self.salida.insert(INSERT, "El término no existe")

    def consultar(self):
        clave = self.consultar_entry.get()
        if clave in self.datos:
            self.salida.delete("1.0", END)
            self.salida.insert(INSERT, self.datos[clave])
        else:
            self.salida.delete("1.0", END)
            self.salida.insert(INSERT, "El término no existe")

    def close_window(self):
        with open("datos/datos.pickle", "wb") as f:
            pickle.dump(self.datos, f)
        self.master.destroy()

    def actualizar_lista(self):
        self.lista.delete(0, END)
        for clave in sorted(self.datos.keys()):
            self.lista.insert(END, clave)


root = Tk()
app = App(root)
root.protocol("WM_DELETE_WINDOW", app.close_window)
root.mainloop()
