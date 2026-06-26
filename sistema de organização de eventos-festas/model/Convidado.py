class Convidado:

    def __init__(
        self,
        nome,
        confirmado=False,
        evento_id=None,
        id=None
    ):

        self.id = id
        self.nome = nome
        self.confirmado = confirmado
        self.evento_id = evento_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

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
