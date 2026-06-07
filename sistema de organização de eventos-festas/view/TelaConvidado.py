import tkinter as tk
from tkinter import messagebox  # Importa a caixinha de mensagem

class TelaConvidado:

    def __init__(self):
        self.janela = tk.Toplevel()
        self.janela.title("Convidados")
        self.janela.geometry("400x300")
        self.janela.configure(bg="#f2f2f2")

        titulo = tk.Label(
            self.janela, #tela para cadastro dos convidados - adicionar o nome
            text="Tela de Convidados",
            font=("Arial", 16, "bold"),
            bg="#f2f2f2"
        )
        titulo.pack(pady=20)

        tk.Label(
            self.janela,
            text="Nome do Convidado:",
            bg="#f2f2f2",
            font=("Arial", 10)
        ).pack(pady=2)

        self.entry_nome = tk.Entry(
            self.janela,
            width=30
        )
        self.entry_nome.pack(pady=10)

        tk.Button(
            self.janela,
            text="Adicionar",
            command=self.adicionar_convidado,
            bg="#d9d9d9",
            font=("Arial", 10, "bold"),
            padx=10
        ).pack(pady=15)

    def adicionar_convidado(self):
        nome_convidado = self.entry_nome.get()

        #valida se o usuário não digitou apenas espaços ou deixou em branco
        if nome_convidado.strip() == "":
            messagebox.showwarning("Aviso", "Por favor, digite o nome do convidado!")
        else:
            # Exibe a mensagem de sucesso na tela
            messagebox.showinfo("Sucesso", f"Convidado '{nome_convidado}' cadastrado com sucesso!")
            
            self.entry_nome.delete(0, tk.END)