import tkinter as tk


class TelaSobre:

    def __init__(self):

        self.janela = tk.Toplevel()

        self.janela.title("Sobre o Sistema")
        self.janela.geometry("800x500")
        self.janela.configure(bg="#f2f2f2")

        tk.Label(
            self.janela,
            text="Sistema de Organização de Eventos e Festas",
            bg="#f2f2f2",
            font=("Arial", 18, "bold")
        ).pack(
            pady=20
        )

        texto = (
            "Sobre o Sistema\n\n"

            "O sistema tem como objetivo auxiliar na organização "
            "e gerenciamento de eventos e festas.\n\n"

            "Funcionalidades disponíveis:\n"
            "• Cadastro e gerenciamento de eventos;\n"
            "• Diferentes tipos de eventos:\n"
            "   - Casamento;\n"
            "   - Festa Infantil;\n"
            "   - Evento Corporativo;\n"
            "• Controle de convidados;\n"
            "• Gerenciamento de fornecedores;\n"
            "• Controle de tarefas;\n"
            "• Utilização do padrão Factory para criação dos eventos.\n\n"

            "Projeto desenvolvido para a disciplina de LPOO.\n\n"

            "Aluna responsável:\n"
            "Bianca Banaletti"
        )


        tk.Label(
            self.janela,
            text=texto,
            bg="#f2f2f2",
            font=("Arial", 11),
            justify="left",
            anchor="w"
        ).pack(
            padx=40,
            pady=10,
            fill="both",
            expand=True
        )

        # BOTÃO FECHAR

        tk.Button(
            self.janela,
            text="Fechar",
            width=15,
            command=self.janela.destroy
        ).pack(
            pady=15
        )