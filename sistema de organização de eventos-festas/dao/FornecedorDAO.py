from dao.conexao import conectar

class FornecedorDAO:

    def inserir(self, fornecedor):

        conn = conectar()
        cursor = conn.cursor()

        sql = """
        INSERT INTO tb_fornecedores
        (nome, servico, valor, evento_id)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(sql, (
            fornecedor.nome,
            fornecedor.servico,
            fornecedor.valor,
            fornecedor.evento_id
        ))

        conn.commit()

        cursor.close()
        conn.close()

    def listar(self):

        conn = conectar()
        cursor = conn.cursor()

        sql = """
        SELECT
            f.id,
            f.nome,
            f.servico,
            f.valor,
            e.nome
        FROM tb_fornecedores f
        INNER JOIN tb_eventos e
            ON f.evento_id = e.id
        ORDER BY f.id
        """

        cursor.execute(sql)

        fornecedores = cursor.fetchall()

        cursor.close()
        conn.close()

        return fornecedores

    def listar_por_evento(self, evento_id):

        conn = conectar()
        cursor = conn.cursor()

        sql = """
        SELECT
            id,
            nome,
            servico,
            valor
        FROM tb_fornecedores
        WHERE evento_id = %s
        ORDER BY nome
        """

        cursor.execute(sql, (evento_id,))

        fornecedores = cursor.fetchall()

        cursor.close()
        conn.close()

        return fornecedores

    def buscar_por_id(self, id_fornecedor):

        conn = conectar()
        cursor = conn.cursor()

        sql = """
        SELECT *
        FROM tb_fornecedores
        WHERE id = %s
        """

        cursor.execute(sql, (id_fornecedor,))

        fornecedor = cursor.fetchone()

        cursor.close()
        conn.close()

        return fornecedor

    def atualizar(self, fornecedor):

        conn = conectar()
        cursor = conn.cursor()

        sql = """
        UPDATE tb_fornecedores
        SET
            nome = %s,
            servico = %s,
            valor = %s,
            evento_id = %s
        WHERE id = %s
        """

        cursor.execute(sql, (
            fornecedor.nome,
            fornecedor.servico,
            fornecedor.valor,
            fornecedor.evento_id,
            fornecedor.id
        ))

        conn.commit()

        cursor.close()
        conn.close()

    def excluir(self, id_fornecedor):

        conn = conectar()
        cursor = conn.cursor()

        sql = """
        DELETE FROM tb_fornecedores
        WHERE id = %s
        """

        cursor.execute(sql, (id_fornecedor,))

        conn.commit()

        cursor.close()
        conn.close()