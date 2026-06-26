from dao.ConvidadoDAO import ConvidadoDAO
from model.Convidado import Convidado


class ConvidadoController:

    def __init__(self):
        self.dao = ConvidadoDAO()

    def cadastrar_convidado(
        self,
        nome,
        evento_id,
        confirmado=False
    ):

        convidado = Convidado(
            nome=nome,
            confirmado=confirmado,
            evento_id=evento_id
        )

        self.dao.inserir(convidado)

        return convidado
    
    def listar_convidados(self):
        return self.dao.listar()

    def listar_por_evento(self, evento_id):
        return self.dao.listar_por_evento(evento_id)


    def buscar_convidado(self, id_convidado):
        return self.dao.buscar_por_id(id_convidado)
    
    def atualizar_convidado(
        self,
        id_convidado,
        nome,
        evento_id,
        confirmado
    ):

        convidado = Convidado(
            nome=nome,
            confirmado=confirmado,
            evento_id=evento_id,
            id=id_convidado
        )

        self.dao.atualizar(convidado)

    def excluir_convidado(self, id_convidado):
        self.dao.excluir(id_convidado)