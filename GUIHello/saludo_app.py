import tkinter as tk
from tkinter import messagebox

class SaludoApp:
    def __init__(self, master):
        self.master = master
        master.title("Saludo App")
        master.configure(bg="#f9e1ff")  # Color de fondo rosita claro

        self.label = tk.Label(master, text="Ingrese su nombre:", bg="#c2cdec", fg="#ffdceb", font=("Arial", 12, "bold"))
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Arial", 12))
        self.entry.pack(pady=10)

        self.boton_saludar = tk.Button(master, text="Saludar", command=self.saludar,
                                       bg="#e6cff5", fg="white", font=("Arial", 11, "bold"))
        self.boton_saludar.pack(pady=10)

        self.boton_salir = tk.Button(master, text="Salir", command=master.quit,
                                     bg="#d0e5f7", fg="black", font=("Arial", 11))
        self.boton_salir.pack(pady=10)

    def saludar(self):
        nombre = self.entry.get()
        messagebox.showinfo("Saludo", f"Hola {nombre} 💖")

# Ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = SaludoApp(root)
    root.mainloop()