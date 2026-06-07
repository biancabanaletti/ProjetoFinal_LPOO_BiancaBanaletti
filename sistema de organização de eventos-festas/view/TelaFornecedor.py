import tkinter as tk
from tkinter import messagebox

class TelaFornecedor:

    def __init__(self):
        self.janela = tk.Toplevel()
        self.janela.title("Gerenciamento de Fornecedores")
        self.janela.geometry("450x400")  # Aumentei um pouco a altura para caber os 3 campos
        self.janela.configure(bg="#f2f2f2")

        #título
        titulo = tk.Label(
            self.janela,
            text="Tela de Fornecedores",
            font=("Arial", 16, "bold"),
            bg="#f2f2f2"
        )
        titulo.pack(pady=20)

        #nome
        tk.Label(
            self.janela,
            text="Nome do Fornecedor:",
            bg="#f2f2f2",
            font=("Arial", 10, "bold")
        ).pack(pady=(5, 2))
        
        self.entry_nome = tk.Entry(self.janela, width=35)
        self.entry_nome.pack(pady=5)

        #serviço prestado
        tk.Label(
            self.janela,
            text="Serviço Prestado:",
            bg="#f2f2f2",
            font=("Arial", 10, "bold")
        ).pack(pady=(10, 2))
        
        self.entry_servico = tk.Entry(self.janela, width=35)
        self.entry_servico.pack(pady=5)

        #valor
        tk.Label(
            self.janela,
            text="Valor (R$):",
            bg="#f2f2f2",
            font=("Arial", 10, "bold")
        ).pack(pady=(10, 2))
        
        self.entry_valor = tk.Entry(self.janela, width=35)
        self.entry_valor.pack(pady=5)

        #botão cadastrar
        tk.Button(
            self.janela,
            text="Cadastrar",
            command=self.cadastrar_fornecedor,
            bg="#d9d9d9",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=5
        ).pack(pady=25)

    def cadastrar_fornecedor(self):
        nome = self.entry_nome.get()
        servico = self.entry_servico.get()
        valor = self.entry_valor.get()

        #verifica se algum dos campos ficou em branco
        if nome.strip() == "" or servico.strip() == "" or valor.strip() == "":
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos (Nome, Serviço e Valor)!")
        else:
            msg_sucesso = f"Fornecedor registrado!\n\nNome: {nome}\nServiço: {servico}\nValor: R$ {valor}"
            messagebox.showinfo("Sucesso", msg_sucesso)
            
            #limpa todos os campos para o próximo cadastro
            self.entry_nome.delete(0, tk.END)
            self.entry_servico.delete(0, tk.END)
            self.entry_valor.delete(0, tk.END)