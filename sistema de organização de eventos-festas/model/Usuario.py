class Usuario:

    def __init__(
        self,
        login: str,
        senha: str
    ):

        self._id = None

        if not login.strip(): #validar login e senha
            raise ValueError(
                "o login não pode ser vazio"
            )

        if len(senha) < 4:
            raise ValueError(
                "a senha deve possuir pelo menos 4 caracteres"
            )

        self.login = login
        self.senha = senha

    @property
    def id(self):
        return self._id

    def alterar_senha(
        self,
        nova_senha: str
    ):

        if len(nova_senha) < 4: #verifica se a senha tem tamanho minímo etc
            raise ValueError(
                "a nova senha deve possuir pelo menos 4 caracteres"
            )

        self.senha = nova_senha

    def resumo(self) -> str:

        return (
            f"usuário: {self.login}"
        )