class Pagamento:

    def __init__(
        self,
        valor: float,
        forma_pagamento: str
    ):

        self._id = None

        if valor <= 0: #verifica se o valor informado é válido
            raise ValueError(
                "o valor do pagamento deve ser maior que zero"
            )

        if not forma_pagamento.strip():
            raise ValueError(
                "a forma de pagamento não pode ser vazia"
            )

        self.valor = valor
        self.forma_pagamento = forma_pagamento
        self.status = "pendente"

    @property
    def id(self):
        return self._id

    def confirmar_pagamento(self):

        self.status = "pago"

    def cancelar_pagamento(self):

        self.status = "cancelado"

    def resumo(self) -> str:

        return (
            f"valor: r$ {self.valor:.2f} | "
            f"forma de pagamento: {self.forma_pagamento} | "
            f"status: {self.status}"
        )