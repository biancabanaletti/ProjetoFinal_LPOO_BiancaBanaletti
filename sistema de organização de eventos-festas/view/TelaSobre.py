import tkinter as tk

class TelaSobre:

    def __init__(self):
        self.janela = tk.Toplevel()
        self.janela.title("Sobre")
        self.janela.geometry("350x250")
        self.janela.configure(bg="#f2f2f2")

        texto = (
            "Sistema de Organização de Eventos e Festas\n\n"
            "Projeto Final - LPOO\n\n"
            "Aluna:\n"
            "Bianca Banaletti" #tela sobre o projeto com nome do projeto matéria e aluna responsável
        )

        tk.Label(
            self.janela,
            text=texto,
            bg="#f2f2f2",
            font=("Arial", 11),
            justify="center"
        ).pack(expand=True, padx=20, pady=20)