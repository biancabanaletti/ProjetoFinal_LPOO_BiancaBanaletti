import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from controller.ConvidadoController import ConvidadoController
from controller.EventoController import EventoController


class TelaConvidado:

    def __init__(self):

        self.controller = ConvidadoController()
        self.controller_evento = EventoController()

        self.id_convidado = None
        self.eventos = {}

        self.janela = tk.Toplevel()

        self.janela.title("Gerenciamento de Convidados")
        self.janela.geometry("850x600")
        self.janela.configure(bg="#f2f2f2")

        titulo = tk.Label(
            self.janela,
            text="Cadastro de Convidados",
            font=("Arial", 18, "bold"),
            bg="#f2f2f2"
        )

        titulo.pack(pady=10)

        frame = tk.Frame(
            self.janela,
            bg="#f2f2f2"
        )

        frame.pack()

        # ----------------------------
        # Nome
        # ----------------------------

        tk.Label(
            frame,
            text="Nome:",
            font=("Arial",10,"bold"),
            bg="#f2f2f2"
        ).grid(row=0,column=0,padx=10,pady=5,sticky="w")

        self.entry_nome = tk.Entry(
            frame,
            width=35
        )

        self.entry_nome.grid(
            row=0,
            column=1,
            pady=5
        )

        tk.Label(
            frame,
            text="Evento:",
            font=("Arial",10,"bold"),
            bg="#f2f2f2"
        ).grid(row=1,column=0,padx=10,pady=5,sticky="w")

        self.combo_evento = ttk.Combobox(
            frame,
            width=32,
            state="readonly"
        )

        self.combo_evento.grid(
            row=1,
            column=1,
            pady=5
        )

        self.confirmado = tk.BooleanVar()

        tk.Checkbutton(
            frame,
            text="Presença Confirmada",
            variable=self.confirmado,
            bg="#f2f2f2"
        ).grid(
            row=2,
            column=1,
            sticky="w",
            pady=5
        )

        frame_botoes = tk.Frame(
            self.janela,
            bg="#f2f2f2"
        )

        frame_botoes.pack(pady=20)

        tk.Button(
            frame_botoes,
            text="Cadastrar",
            width=15,
            command=self.cadastrar_convidado
        ).grid(row=0,column=0,padx=5)

        tk.Button(
            frame_botoes,
            text="Excluir",
            width=15,
            command=self.excluir_convidado
        ).grid(row=0,column=1,padx=5)

        tk.Button(
            frame_botoes,
            text="Atualizar Lista",
            width=15,
            command=self.carregar_convidados
        ).grid(row=0,column=2,padx=5)

        tk.Button(
            frame_botoes,
            text="Limpar",
            width=15,
            command=self.limpar_campos
        ).grid(row=0,column=3,padx=5)

        colunas = (
            "ID",
            "Nome",
            "Confirmado",
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
                width=180,
                anchor="center"
            )

        self.tree.pack(
            fill="x",
            padx=20
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.selecionar_convidado
        )

        self.carregar_eventos()

        self.carregar_convidados()

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

    def carregar_convidados(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        convidados = self.controller.listar_convidados()

        for convidado in convidados:

            confirmado = "Sim" if convidado[2] else "Não"

            self.tree.insert(
                "",
                tk.END,
                values=(
                    convidado[0],
                    convidado[1],
                    confirmado,
                    convidado[3]
                )
            )

    def cadastrar_convidado(self):

        nome = self.entry_nome.get().strip()
        evento = self.combo_evento.get()

        if nome == "" or evento == "":

            messagebox.showwarning(
                "Aviso",
                "Preencha todos os campos."
            )

            return

        evento_id = self.eventos[evento]

        # ORDEM CORRETA DOS PARÂMETROS
        self.controller.cadastrar_convidado(
            nome,
            evento_id,
            self.confirmado.get()
        )

        messagebox.showinfo(
            "Sucesso",
            "Convidado cadastrado!"
        )

        self.limpar_campos()

        self.carregar_convidados()

    def selecionar_convidado(self, event):

        item = self.tree.focus()

        if not item:
            return

        dados = self.tree.item(
            item,
            "values"
        )

        self.id_convidado = dados[0]

        self.entry_nome.delete(0, tk.END)
        self.entry_nome.insert(0, dados[1])

        self.confirmado.set(
            dados[2] == "Sim"
        )

        self.combo_evento.set(
            dados[3]
        )

    def excluir_convidado(self):

        if self.id_convidado is None:

            messagebox.showwarning(
                "Aviso",
                "Selecione um convidado."
            )

            return

        resposta = messagebox.askyesno(
            "Excluir",
            "Deseja realmente excluir?"
        )

        if resposta:

            self.controller.excluir_convidado(
                self.id_convidado
            )

            self.limpar_campos()

            self.carregar_convidados()

            messagebox.showinfo(
                "Sucesso",
                "Convidado excluído."
            )

    def limpar_campos(self):

        self.entry_nome.delete(
            0,
            tk.END
        )

        self.confirmado.set(False)

        if self.combo_evento["values"]:
            self.combo_evento.current(0)

        self.id_convidado = None