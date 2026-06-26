from model.Factory import EventoFactory
from dao.EventoDAO import EventoDAO


class EventoController:

    def __init__(self):
        self.dao = EventoDAO()

    def criar_evento(self, tipo, nome, data, local):

        evento = EventoFactory.criar_evento(
            tipo,
            nome,
            data,
            local
        )

        self.dao.inserir(evento)

        return evento

    def listar_eventos(self):
        return self.dao.listar()

    def buscar_evento(self, id_evento):
        return self.dao.buscar_por_id(id_evento)

    def atualizar_evento(
        self,
        id_evento,
        tipo,
        nome,
        data,
        local
):

        evento = EventoFactory.criar_evento(
        tipo,
        nome,
        data,
        local
    )

        evento.id = id_evento

        self.dao.atualizar(evento)

    def excluir_evento(self, id_evento):
        self.dao.excluir(id_evento)

    def listar_eventos_combobox(self):
        return self.dao.listar_para_combobox()