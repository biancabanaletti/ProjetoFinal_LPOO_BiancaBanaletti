class Tarefa:

    def __init__(
        self,
        descricao: str,
        responsavel: str
    ):

        self._id = None

        if not descricao.strip(): #verifica descrição da tarefa
            raise ValueError(
                "a descrição da tarefa não pode ser vazia"
            )

        if not responsavel.strip():
            raise ValueError(
                "o responsável não pode ser vazio"
            )

        self.descricao = descricao
        self.responsavel = responsavel
        self.concluida = False

    @property
    def id(self):
        return self._id

    def concluir(self): #se a tarefa foi concluída

        self.concluida = True

    def reabrir(self):

        self.concluida = False

    def resumo(self) -> str:

        status = (
            "concluída"
            if self.concluida
            else "pendente"
        )

        return (
            f"tarefa: {self.descricao} | "
            f"responsável: {self.responsavel} | "
            f"status: {status}"
        )
        
    def __repr__(self):
        return self.resumo()