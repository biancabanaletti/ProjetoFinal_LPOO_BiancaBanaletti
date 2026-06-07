class Fornecedor:

    def __init__(
        self,
        nome: str,
        servico: str,
        valor: float
    ):

        self._id = None

        if not nome.strip(): #verifica se o nome e o serviço foram informados
            raise ValueError(
                "o nome do fornecedor não pode ser vazio"
            )

        if not servico.strip():
            raise ValueError(
                "o serviço não pode ser vazio"
            )

        self.nome = nome
        self.servico = servico
        self.valor = valor

    @property
    def id(self):
        return self._id

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