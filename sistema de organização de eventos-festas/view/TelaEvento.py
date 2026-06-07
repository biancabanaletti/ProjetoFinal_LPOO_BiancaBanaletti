import tkinter as tk
from tkinter import messagebox
from view.TelaConvidado import TelaConvidado
from view.TelaFornecedor import TelaFornecedor
from view.TelaSobre import TelaSobre

class TelaEvento:

    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Sistema de Eventos e Festas")
        self.janela.geometry("500x400")
        self.janela.configure(bg="#f2f2f2")

        #criação menu superior
        barra_menu = tk.Menu(self.janela)
        
        menu_gerenciar = tk.Menu(barra_menu, tearoff=0)
        menu_gerenciar.add_command(label="Convidados", command=self.abrir_convidados)
        menu_gerenciar.add_command(label="Fornecedores", command=self.abrir_fornecedores)
        
        menu_ajuda = tk.Menu(barra_menu, tearoff=0)
        menu_ajuda.add_command(label="Sobre", command=self.abrir_sobre)
        
        barra_menu.add_cascade(label="Gerenciar", menu=menu_gerenciar)
        barra_menu.add_cascade(label="Ajuda", menu=menu_ajuda)
        
        self.janela.config(menu=barra_menu)

        #componentes da tela
        tk.Label(
            self.janela, 
            text="Nome do Evento: ", 
            bg="#f2f2f2", 
            font=("Arial", 10, "bold")
        ).pack(pady=(20, 2))
        
        self.entry_nome = tk.Entry(self.janela, width=40)
        self.entry_nome.pack(pady=5)

        tk.Label(
            self.janela, 
            text="Local:", 
            bg="#f2f2f2", 
            font=("Arial", 10, "bold")
        ).pack(pady=(10, 2))
        
        self.entry_local = tk.Entry(self.janela, width=40)
        self.entry_local.pack(pady=5)

        tk.Button(
            self.janela,
            text="Cadastrar Evento",
            command=self.cadastrar_evento,
            bg="#d9d9d9",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5
        ).pack(pady=25)

        self.janela.mainloop()

    #métodos de ação
    def cadastrar_evento(self):
        nome = self.entry_nome.get()
        local = self.entry_local.get()
        
        if nome.strip() == "" or local.strip() == "":
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos!")
        else:
            messagebox.showinfo("Sucesso", f"Evento '{nome}' cadastrado com sucesso em '{local}'!")

    def abrir_convidados(self):
        TelaConvidado()

    def abrir_fornecedores(self):
        TelaFornecedor()

    def abrir_sobre(self):
        TelaSobre()