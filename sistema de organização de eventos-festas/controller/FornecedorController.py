from dao.FornecedorDAO import FornecedorDAO
from model.Fornecedor import Fornecedor

class FornecedorController:

    def __init__(self):
        self.dao = FornecedorDAO()

    def cadastrar_fornecedor(self, nome, servico, valor):
        #criaum novo objeto Fornecedor com os dados informados
        fornecedor = Fornecedor(nome, servico, valor)

        self.dao.inserir(fornecedor)

        return fornecedor

    def listar_fornecedores(self):
        return self.dao.listar()