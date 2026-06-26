import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from controller.FornecedorController import FornecedorController
from controller.EventoController import EventoController


class TelaFornecedor:

    def __init__(self):

        self.controller = FornecedorController()
        self.controller_evento = EventoController()

        self.id_fornecedor = None
        self.eventos = {}

        self.janela = tk.Toplevel()
        self.janela.title("Gerenciamento de Fornecedores")
        self.janela.geometry("900x620")
        self.janela.configure(bg="#f2f2f2")

        titulo = tk.Label(
            self.janela,
            text="Cadastro de Fornecedores",
            font=("Arial",18,"bold"),
            bg="#f2f2f2"
        )
        titulo.pack(pady=10)

        frame = tk.Frame(self.janela,bg="#f2f2f2")
        frame.pack()

        # Nome

        tk.Label(
            frame,
            text="Nome:",
            bg="#f2f2f2",
            font=("Arial",10,"bold")
        ).grid(row=0,column=0,padx=10,pady=5,sticky="w")

        self.entry_nome = tk.Entry(frame,width=35)
        self.entry_nome.grid(row=0,column=1,pady=5)

        # Serviço

        tk.Label(
            frame,
            text="Serviço:",
            bg="#f2f2f2",
            font=("Arial",10,"bold")
        ).grid(row=1,column=0,padx=10,pady=5,sticky="w")

        self.entry_servico = tk.Entry(frame,width=35)
        self.entry_servico.grid(row=1,column=1,pady=5)

        # Valor

        tk.Label(
            frame,
            text="Valor:",
            bg="#f2f2f2",
            font=("Arial",10,"bold")
        ).grid(row=2,column=0,padx=10,pady=5,sticky="w")

        self.entry_valor = tk.Entry(frame,width=35)
        self.entry_valor.grid(row=2,column=1,pady=5)

        # Evento

        tk.Label(
            frame,
            text="Evento:",
            bg="#f2f2f2",
            font=("Arial",10,"bold")
        ).grid(row=3,column=0,padx=10,pady=5,sticky="w")

        self.combo_evento = ttk.Combobox(
            frame,
            width=32,
            state="readonly"
        )

        self.combo_evento.grid(
            row=3,
            column=1,
            pady=5
        )

        # Botões

        frame_botoes = tk.Frame(
            self.janela,
            bg="#f2f2f2"
        )

        frame_botoes.pack(pady=20)

        tk.Button(
            frame_botoes,
            text="Cadastrar",
            width=15,
            command=self.cadastrar_fornecedor
        ).grid(row=0,column=0,padx=5)

        tk.Button(
            frame_botoes,
            text="Excluir",
            width=15,
            command=self.excluir_fornecedor
        ).grid(row=0,column=1,padx=5)

        tk.Button(
            frame_botoes,
            text="Atualizar Lista",
            width=15,
            command=self.carregar_fornecedores
        ).grid(row=0,column=2,padx=5)

        tk.Button(
            frame_botoes,
            text="Limpar",
            width=15,
            command=self.limpar_campos
        ).grid(row=0,column=3,padx=5)

        # Treeview

        colunas = (
            "ID",
            "Nome",
            "Serviço",
            "Valor",
            "Evento"
        )

        self.tree = ttk.Treeview(
            self.janela,
            columns=colunas,
            show="headings",
            height=12
        )

        for coluna in colunas:

            self.tree.heading(
                coluna,
                text=coluna
            )

            self.tree.column(
                coluna,
                width=160,
                anchor="center"
            )

        self.tree.pack(
            fill="x",
            padx=20
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.selecionar_fornecedor
        )

        self.carregar_eventos()
        self.carregar_fornecedores()
        
    # Carregar Eventos

    def carregar_eventos(self):

        self.eventos.clear()

        lista = self.controller_evento.listar_eventos_combobox()

        nomes = []

        for evento in lista:
            self.eventos[evento[1]] = evento[0]
            nomes.append(evento[1])

        self.combo_evento["values"] = nomes

        if nomes:
            self.combo_evento.current(0)

    # Carregar Fornecedores
    
    def carregar_fornecedores(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        fornecedores = self.controller.listar_fornecedores()

        for fornecedor in fornecedores:

            self.tree.insert(
                "",
                tk.END,
                values=(
                    fornecedor[0],
                    fornecedor[1],
                    fornecedor[2],
                    f"R$ {fornecedor[3]:.2f}",
                    fornecedor[4]
                )
            )

    # Cadastrar
   
    def cadastrar_fornecedor(self):

        nome = self.entry_nome.get().strip()
        servico = self.entry_servico.get().strip()
        valor = self.entry_valor.get().strip()
        evento = self.combo_evento.get()

        if (
            nome == ""
            or servico == ""
            or valor == ""
            or evento == ""
        ):

            messagebox.showwarning(
                "Aviso",
                "Preencha todos os campos."
            )
            return

        try:
            valor = float(valor.replace(",", "."))
        except ValueError:

            messagebox.showerror(
                "Erro",
                "Valor inválido."
            )
            return

        evento_id = self.eventos[evento]

        self.controller.cadastrar_fornecedor(
            nome,
            servico,
            valor,
            evento_id
        )

        messagebox.showinfo(
            "Sucesso",
            "Fornecedor cadastrado!"
        )

        self.limpar_campos()
        self.carregar_fornecedores()

    # Selecionar
    
    def selecionar_fornecedor(self, event):

        item = self.tree.focus()

        if not item:
            return

        dados = self.tree.item(item, "values")

        self.id_fornecedor = dados[0]

        self.entry_nome.delete(0, tk.END)
        self.entry_nome.insert(0, dados[1])

        self.entry_servico.delete(0, tk.END)
        self.entry_servico.insert(0, dados[2])

        self.entry_valor.delete(0, tk.END)
        self.entry_valor.insert(
            0,
            str(dados[3]).replace("R$ ", "")
        )

        self.combo_evento.set(dados[4])

    # Excluir

    def excluir_fornecedor(self):

        if self.id_fornecedor is None:

            messagebox.showwarning(
                "Aviso",
                "Selecione um fornecedor."
            )
            return

        resposta = messagebox.askyesno(
            "Excluir",
            "Deseja realmente excluir este fornecedor?"
        )

        if resposta:

            self.controller.excluir_fornecedor(
                self.id_fornecedor
            )

            self.limpar_campos()
            self.carregar_fornecedores()

            messagebox.showinfo(
                "Sucesso",
                "Fornecedor excluído!"
            )

    # Limpar Campos

    def limpar_campos(self):

        self.entry_nome.delete(0, tk.END)
        self.entry_servico.delete(0, tk.END)
        self.entry_valor.delete(0, tk.END)

        if self.combo_evento["values"]:
            self.combo_evento.current(0)

        self.id_fornecedor = None