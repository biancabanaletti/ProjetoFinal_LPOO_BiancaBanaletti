from model.Evento import Casamento, FestaInfantil, EventoCorporativo
from dao.EventoDAO import EventoDAO

class EventoController:

    def __init__(self):
        self.dao = EventoDAO()

    def criar_evento(self, tipo, nome, data, local):

        if tipo == "Casamento":
            evento = Casamento(nome, data, local)

        elif tipo == "Festa Infantil":
            evento = FestaInfantil(nome, data, local)

        else:
            evento = EventoCorporativo(nome, data, local)

        self.dao.inserir(evento)

        return evento

    def listar_eventos(self):
        return self.dao.listar()

    def excluir_evento(self, id_evento):
        self.dao.excluir(id_evento)
        
#cadastrar evento; listar; excluir; atualizar