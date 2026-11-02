import customtkinter as ctk

# Configuración del tema visual
ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("blue")

# Ventana principal
app = ctk.CTk()
app.geometry("450x300")
app.title("Mi primera app moderna")

# Texto de bienvenida
etiqueta = ctk.CTkLabel(app, text="¡Hola, Javier!", font=("Arial", 20, "bold"))
etiqueta.pack(pady=40)

# Botón interactivo
def accion_boton():
    etiqueta.configure(text="¡Funciona perfectamente!")

boton = ctk.CTkButton(app, text="Haz clic aquí", command=accion_boton)
boton.pack(pady=10)

app.mainloop()