import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

from controller.EventoController import EventoController
from view.TelaConvidado import TelaConvidado
from view.TelaFornecedor import TelaFornecedor
from view.TelaSobre import TelaSobre


class TelaEvento:

    def __init__(self):

        self.controller = EventoController()

        self.janela = tk.Tk()
        self.janela.title("Sistema de Eventos e Festas")
        self.janela.geometry("900x650")
        self.janela.configure(bg="#f2f2f2")

        self.id_evento = None

        barra_menu = tk.Menu(self.janela)

        menu_gerenciar = tk.Menu(
            barra_menu,
            tearoff=0
        )

        menu_gerenciar.add_command(
            label="Convidados",
            command=self.abrir_convidados
        )

        menu_gerenciar.add_command(
            label="Fornecedores",
            command=self.abrir_fornecedores
        )


        menu_ajuda = tk.Menu(
            barra_menu,
            tearoff=0
        )

        menu_ajuda.add_command(
            label="Sobre",
            command=self.abrir_sobre
        )


        barra_menu.add_cascade(
            label="Gerenciar",
            menu=menu_gerenciar
        )

        barra_menu.add_cascade(
            label="Ajuda",
            menu=menu_ajuda
        )

        self.janela.config(menu=barra_menu)

        tk.Label(
            self.janela,
            text="Cadastro de Eventos",
            font=("Arial",18,"bold"),
            bg="#f2f2f2"
        ).pack(pady=10)



        frame = tk.Frame(
            self.janela,
            bg="#f2f2f2"
        )

        frame.pack()

        tk.Label(
            frame,
            text="Nome",
            bg="#f2f2f2",
            font=("Arial",10,"bold")
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=5,
            sticky="w"
        )


        self.entry_nome = tk.Entry(
            frame,
            width=30
        )

        self.entry_nome.grid(
            row=0,
            column=1
        )

        tk.Label(
            frame,
            text="Local",
            bg="#f2f2f2",
            font=("Arial",10,"bold")
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=5,
            sticky="w"
        )


        self.entry_local = tk.Entry(
            frame,
            width=30
        )

        self.entry_local.grid(
            row=1,
            column=1
        )

        tk.Label(
            frame,
            text="Data (AAAA-MM-DD)",
            bg="#f2f2f2",
            font=("Arial",10,"bold")
        ).grid(
            row=2,
            column=0,
            padx=10,
            pady=5,
            sticky="w"
        )


        self.entry_data = tk.Entry(
            frame,
            width=30
        )

        self.entry_data.grid(
            row=2,
            column=1
        )

        tk.Label(
            frame,
            text="Tipo",
            bg="#f2f2f2",
            font=("Arial",10,"bold")
        ).grid(
            row=3,
            column=0,
            padx=10,
            pady=5,
            sticky="w"
        )


        self.combo_tipo = ttk.Combobox(
            frame,
            width=27,
            state="readonly"
        )


        self.combo_tipo["values"] = (
            "Casamento",
            "Festa Infantil",
            "Evento Corporativo"
        )


        self.combo_tipo.current(0)


        self.combo_tipo.grid(
            row=3,
            column=1,
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
            command=self.cadastrar_evento
        ).grid(
            row=0,
            column=0,
            padx=5
        )


        tk.Button(
            frame_botoes,
            text="Editar",
            width=15,
            command=self.editar_evento
        ).grid(
            row=0,
            column=1,
            padx=5
        )


        tk.Button(
            frame_botoes,
            text="Excluir",
            width=15,
            command=self.excluir_evento
        ).grid(
            row=0,
            column=2,
            padx=5
        )


        tk.Button(
            frame_botoes,
            text="Atualizar Lista",
            width=15,
            command=self.carregar_eventos
        ).grid(
            row=0,
            column=3,
            padx=5
        )


        tk.Button(
            frame_botoes,
            text="Limpar",
            width=15,
            command=self.limpar_campos
        ).grid(
            row=0,
            column=4,
            padx=5
        )

        colunas = (
            "ID",
            "Nome",
            "Data",
            "Local",
            "Tipo",
            "Status"
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
                width=130,
                anchor="center"
            )


        self.tree.pack(
            fill="x",
            padx=20
        )


        self.tree.bind(
            "<<TreeviewSelect>>",
            self.selecionar_evento
        )


        self.carregar_eventos()


        self.janela.mainloop()
        

    def carregar_eventos(self):

        for item in self.tree.get_children():
            self.tree.delete(item)


        eventos = self.controller.listar_eventos()


        for evento in eventos:

            self.tree.insert(
                "",
                tk.END,
                values=evento
            )

    def cadastrar_evento(self):

        nome = self.entry_nome.get().strip()
        local = self.entry_local.get().strip()
        data = self.entry_data.get().strip()
        tipo = self.combo_tipo.get()


        if nome == "" or local == "" or data == "":

            messagebox.showwarning(
                "Aviso",
                "Preencha todos os campos."
            )

            return


        try:

            data_evento = datetime.strptime(
                data,
                "%Y-%m-%d"
            ).date()


            self.controller.criar_evento(
                tipo,
                nome,
                data_evento,
                local
            )


            messagebox.showinfo(
                "Sucesso",
                "Evento cadastrado com sucesso!"
            )


            self.limpar_campos()

            self.carregar_eventos()



        except Exception as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )

    def selecionar_evento(self, event):

        selecionado = self.tree.focus()


        if not selecionado:
            return


        dados = self.tree.item(
            selecionado,
            "values"
        )


        self.id_evento = dados[0]


        self.entry_nome.delete(
            0,
            tk.END
        )

        self.entry_nome.insert(
            0,
            dados[1]
        )


        self.entry_data.delete(
            0,
            tk.END
        )

        self.entry_data.insert(
            0,
            dados[2]
        )


        self.entry_local.delete(
            0,
            tk.END
        )

        self.entry_local.insert(
            0,
            dados[3]
        )


        self.combo_tipo.set(
            dados[4]
        )

    def editar_evento(self):


        if self.id_evento is None:

            messagebox.showwarning(
                "Aviso",
                "Selecione um evento para editar."
            )

            return



        nome = self.entry_nome.get().strip()
        local = self.entry_local.get().strip()
        data = self.entry_data.get().strip()
        tipo = self.combo_tipo.get()



        if nome == "" or local == "" or data == "":

            messagebox.showwarning(
                "Aviso",
                "Preencha todos os campos."
            )

            return



        try:


            data_evento = datetime.strptime(
                data,
                "%Y-%m-%d"
            ).date()



            self.controller.atualizar_evento(
                self.id_evento,
                tipo,
                nome,
                data_evento,
                local
            )



            messagebox.showinfo(
                "Sucesso",
                "Evento atualizado com sucesso!"
            )



            self.limpar_campos()

            self.carregar_eventos()



        except Exception as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )

    def excluir_evento(self):


        if self.id_evento is None:


            messagebox.showwarning(
                "Aviso",
                "Selecione um evento."
            )


            return



        resposta = messagebox.askyesno(
            "Excluir",
            "Deseja realmente excluir este evento?"
        )



        if resposta:


            try:


                self.controller.excluir_evento(
                    self.id_evento
                )


                messagebox.showinfo(
                    "Sucesso",
                    "Evento excluído."
                )


                self.id_evento = None


                self.limpar_campos()

                self.carregar_eventos()



            except Exception as erro:


                messagebox.showerror(
                    "Erro",
                    str(erro)
                )

    def limpar_campos(self):


        self.entry_nome.delete(
            0,
            tk.END
        )


        self.entry_local.delete(
            0,
            tk.END
        )


        self.entry_data.delete(
            0,
            tk.END
        )


        self.combo_tipo.current(
            0
        )


        self.id_evento = None

    # Abrir Telas

    def abrir_convidados(self):

        TelaConvidado()



    def abrir_fornecedores(self):

        TelaFornecedor()



    def abrir_sobre(self):

        TelaSobre()