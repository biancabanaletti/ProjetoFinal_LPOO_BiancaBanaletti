class Decoracao:

    def __init__(
        self,
        tema: str,
        cor_principal: str,
        orcamento: float
    ):

        self._id = None

        if not tema.strip(): #verifica se o tema foi informado
            raise ValueError(
                "o tema da decoração não pode ser vazio"
            )

        if not cor_principal.strip():
            raise ValueError(
                "a cor principal não pode ser vazia"
            )

        self.tema = tema
        self.cor_principal = cor_principal
        self.orcamento = orcamento

    @property
    def id(self):
        return self._id

    def atualizar_orcamento(
        self,
        novo_orcamento: float
    ):

        self.orcamento = novo_orcamento

    def resumo(self) -> str:
         #retorna um resumo das informações da decoração
        return (
            f"tema: {self.tema} | "
            f"cor principal: {self.cor_principal} | "
            f"orçamento: r$ {self.orcamento:.2f}"
        )