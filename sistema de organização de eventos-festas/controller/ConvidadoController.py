from dao.ConvidadoDAO import ConvidadoDAO
from model.Convidado import Convidado

class ConvidadoController:

    def __init__(self):
        self.dao = ConvidadoDAO() #instância do DAO

    def cadastrar_convidado(self, nome, confirmado=False):
    #cria um novo objeto convidado com os dados informados
        convidado = Convidado(nome, confirmado)

        self.dao.inserir(convidado)

        return convidado

    def listar_convidados(self):
        return self.dao.listar() #retorna a lista de todos os convidados cadastrados