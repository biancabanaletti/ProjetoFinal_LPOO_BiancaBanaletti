from dao.conexao import conectar

class FornecedorDAO:

    def inserir(self, fornecedor):

        conn = conectar()
        cursor = conn.cursor()
        #comando para inserir um novo fornecedor
        sql = """
        INSERT INTO tb_fornecedores
        (nome, servico, valor)
        VALUES (%s, %s, %s)
        """

        cursor.execute(sql, (
            fornecedor.nome,
            fornecedor.servico,
            fornecedor.valor
        ))

        conn.commit()

        cursor.close()
        conn.close()