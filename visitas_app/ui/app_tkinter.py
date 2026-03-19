import tkinter as tk
from tkinter import ttk, messagebox
from modelos.visitante import Visitante


class AppTkinter:
    def __init__(self, servicio):
        self.servicio = servicio

        self.root = tk.Tk()
        self.root.title("Sistema de Registro de Visitantes")
        self.root.geometry("600x400")

        self.crear_widgets()

    def crear_widgets(self):
        frame_form = tk.LabelFrame(self.root, text="Datos del Visitante")
        frame_form.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_form, text="Cédula:").grid(row=0, column=0)
        self.entry_cedula = tk.Entry(frame_form)
        self.entry_cedula.grid(row=0, column=1)

        tk.Label(frame_form, text="Nombre:").grid(row=1, column=0)
        self.entry_nombre = tk.Entry(frame_form)
        self.entry_nombre.grid(row=1, column=1)

        tk.Label(frame_form, text="Motivo:").grid(row=2, column=0)
        self.entry_motivo = tk.Entry(frame_form)
        self.entry_motivo.grid(row=2, column=1)

        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Registrar", command=self.registrar).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Eliminar", command=self.eliminar).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Limpiar", command=self.limpiar_campos).grid(row=0, column=2, padx=5)

        self.tree = ttk.Treeview(self.root, columns=("cedula", "nombre", "motivo"), show="headings")
        self.tree.heading("cedula", text="Cédula")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("motivo", text="Motivo")

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    def registrar(self):
        cedula = self.entry_cedula.get().strip()
        nombre = self.entry_nombre.get().strip()
        motivo = self.entry_motivo.get().strip()

        if not cedula or not nombre or not motivo:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        visitante = Visitante(cedula, nombre, motivo)
        resultado = self.servicio.registrar_visitante(visitante)

        if resultado:
            messagebox.showinfo("Éxito", "Visitante registrado")
            self.actualizar_tabla()
            self.limpiar_campos()
        else:
            messagebox.showerror("Error", "La cédula ya existe")

    def actualizar_tabla(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for i, v in enumerate(self.servicio.obtener_visitantes()):
            self.tree.insert("", "end", iid=i, values=(v.cedula, v.nombre, v.motivo))

    def eliminar(self):
        seleccion = self.tree.selection()

        if not seleccion:
            messagebox.showwarning("Error", "Seleccione un registro")
            return

        indice = int(seleccion[0])

        confirmar = messagebox.askyesno("Confirmar", "¿Desea eliminar este registro?")
        if not confirmar:
            return

        eliminado = self.servicio.eliminar_por_indice(indice)

        if eliminado:
            messagebox.showinfo("Éxito", "Registro eliminado")
            self.actualizar_tabla()
        else:
            messagebox.showerror("Error", "No se pudo eliminar")

    def limpiar_campos(self):
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_motivo.delete(0, tk.END)

    def run(self):
        self.root.mainloop()