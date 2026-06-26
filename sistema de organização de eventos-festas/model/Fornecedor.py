class Fornecedor:

    def __init__(
        self,
        nome,
        servico,
        valor,
        evento_id=None,
        id=None
    ):

        self.id = id
        self.nome = nome
        self.servico = servico
        self.valor = valor
        self.evento_id = evento_id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, valor):
        self._id = valor

    def atualizar_valor(
        self,
        novo_valor: float
    ):

        self.valor = novo_valor

    def resumo(self) -> str:

        return ( #retorna com os dados do fornecedor
            f"fornecedor: {self.nome} | "
            f"serviço: {self.servico} | "
            f"valor: r$ {self.valor:.2f}"
        )
        
    def __repr__(self):
        return self.resumo()