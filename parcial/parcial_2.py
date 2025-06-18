import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os
#creo una funcion para guardar los datos en un archivo json
ARCHIVO_DATOS = "data.json"
CATEGORIAS = ["ciencia", "literatura", "ingeniería"]

def cargar_datos():
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return []
#creo varias funcuies las cuales llamare mas adelante
def guardar_datos(libros):
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
        json.dump(libros, f, indent=4, ensure_ascii=False)

def agregar_libro(libros, titulo, autor, categoria):
    nuevo = {"titulo": titulo, "autor": autor, "categoria": categoria, "disponible": True}
    return libros + [nuevo]

def buscar_libros(libros, termino):
    termino_lower = termino.lower()
    return [libro for libro in libros if termino_lower in libro["titulo"].lower() or termino_lower in libro["autor"].lower()]

def cambiar_estado(libros, titulo):
    titulo_lower = titulo.lower()
    found = False
    for i, libro in enumerate(libros):
        if libro["titulo"].lower() == titulo_lower:
            libros[i]["disponible"] = not libros[i]["disponible"]
            found = True
            break
    return libros, found 

#creo la blioteca y llamo las funciones

class BibliotecaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("inventario de la Biblioteca")
        self.libros = cargar_datos()

        tk.Button(root, text="registrar libro", command=self.registrar).pack(pady=5)
        tk.Button(root, text="buscar libro", command=self.buscar).pack(pady=5)
        tk.Button(root, text="marcar prestado/Devuelto", command=self.marcar).pack(pady=5)
        tk.Button(root, text="salir y guardar", command=self.salir).pack(pady=10)

        self.lista = tk.Text(root, width=80, height=20)
        self.lista.pack()

        self.actualizar_lista(self.libros)

    def registrar(self):
        titulo = simpledialog.askstring("registrar libro", "ingrese el título del libro:")
        if not titulo:
            messagebox.showwarning("el título no puede estar vacío.")
            return

        autor = simpledialog.askstring("registrar libro", "ingrese el autor del libro:")
        if not autor:
            messagebox.showwarning("el autor no puede estar vacío.")
            return

        categoria = simpledialog.askstring("registrar Libro", f"ingrese la categoría ({', '.join(CATEGORIAS)}):")
        if not categoria or categoria not in CATEGORIAS:
            messagebox.showerror("categoría inválida o vacía.")
            return

        self.libros = agregar_libro(self.libros, titulo, autor, categoria)
        self.actualizar_lista(self.libros)
        messagebox.showinfo("exito", f"libro '{titulo}' registrado exitosamente.")

    def buscar(self):
        termino = simpledialog.askstring("buscar libro", "ingrese título o autor a buscar:")
        if not termino:
            self.actualizar_lista(self.libros)
            return

        resultados = buscar_libros(self.libros, termino)
        if resultados:
            self.actualizar_lista(resultados)
            messagebox.showinfo("búsqueda", f"se encontraron {len(resultados)} resultados.")
        else:
            self.actualizar_lista([])
            messagebox.showinfo("búsqueda", "no se encontraron libros con ese término.")


    def marcar(self):
        titulo_a_marcar = simpledialog.askstring("marcar Estado", "ingrese el título del libro a marcar (prestado/devuelto):")
        if not titulo_a_marcar:
            return

        self.libros, found = cambiar_estado(self.libros, titulo_a_marcar)
        if found:
            self.actualizar_lista(self.libros)
            messagebox.showinfo("estado actualizado", f"el estado de '{titulo_a_marcar}' ha sido cambiado.")
        else:
            messagebox.showerror("error", f"no se encontró el libro con título '{titulo_a_marcar}'.")

    def salir(self):
        guardar_datos(self.libros)
        messagebox.showinfo("guardado", "datos guardados")
        self.root.destroy()

    def actualizar_lista(self, libros_a_mostrar):
        self.lista.delete("1.0", tk.END)
        if not libros_a_mostrar:
            self.lista.insert(tk.END, "no hay libros para mostrar")
            return

        for l in libros_a_mostrar:
            estado = "disponible" if l["disponible"] else "Prestado"
            self.lista.insert(tk.END, f"título: {l['titulo']}\nAutor: {l['autor']}\ncategoría: {l['categoria']}\nestado: {estado}\n\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaGUI(root)
    root.mainloop()