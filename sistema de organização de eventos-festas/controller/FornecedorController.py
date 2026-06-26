from dao.FornecedorDAO import FornecedorDAO
from model.Fornecedor import Fornecedor


class FornecedorController:

    def __init__(self):
        self.dao = FornecedorDAO()

    def cadastrar_fornecedor(
        self,
        nome,
        servico,
        valor,
        evento_id
    ):

        fornecedor = Fornecedor(
            nome=nome,
            servico=servico,
            valor=valor,
            evento_id=evento_id
        )

        self.dao.inserir(fornecedor)

        return fornecedor

    def listar_fornecedores(self):
        return self.dao.listar()

    def listar_por_evento(self, evento_id):
        return self.dao.listar_por_evento(evento_id)

    def buscar_fornecedor(self, id_fornecedor):
        return self.dao.buscar_por_id(id_fornecedor)

    def atualizar_fornecedor(
        self,
        id_fornecedor,
        nome,
        servico,
        valor,
        evento_id
    ):

        fornecedor = Fornecedor(
            nome=nome,
            servico=servico,
            valor=valor,
            evento_id=evento_id,
            id=id_fornecedor
        )

        self.dao.atualizar(fornecedor)

    def excluir_fornecedor(self, id_fornecedor):
        self.dao.excluir(id_fornecedor)