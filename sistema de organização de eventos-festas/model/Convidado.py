class Convidado:

    def __init__(
        self,
        nome: str,
        confirmado: bool = False
    ):

        self._id = None

        if not nome.strip(): #verifica se o nome do convidado foi informado
            raise ValueError(
                "o nome do convidado não pode ser vazio"
            )

        self.nome = nome #armazena os dados
        self.confirmado = confirmado

    @property
    def id(self):
        return self._id

    def confirmar(self):

        self.confirmado = True

    def cancelar_confirmacao(self):

        self.confirmado = False

    def resumo(self) -> str:

        status = (
            "confirmado"
            if self.confirmado
            else "não confirmado"
        )

        return (
            f"convidado: {self.nome} "
            f"({status})"
        )
        
    def __repr__(self):
        return self.resumo()
