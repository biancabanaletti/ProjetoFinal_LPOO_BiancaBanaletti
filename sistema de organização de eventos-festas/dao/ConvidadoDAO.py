from dao.conexao import conectar

class ConvidadoDAO:

    def inserir(self, convidado):

        conn = conectar()
        cursor = conn.cursor()

        sql = """
        INSERT INTO tb_convidados
        (nome, confirmado, evento_id)
        VALUES (%s, %s, %s)
        """

        cursor.execute(sql, (
            convidado.nome,
            convidado.confirmado,
            convidado.evento_id
        ))

        conn.commit()

        cursor.close()
        conn.close()

    def listar(self):

        conn = conectar()
        cursor = conn.cursor()

        sql = """
        SELECT
            c.id,
            c.nome,
            c.confirmado,
            e.nome
        FROM tb_convidados c
        INNER JOIN tb_eventos e
        ON c.evento_id = e.id
        ORDER BY c.id
        """

        cursor.execute(sql)

        convidados = cursor.fetchall()

        cursor.close()
        conn.close()

        return convidados

    def listar_por_evento(self, evento_id):

        conn = conectar()
        cursor = conn.cursor()

        sql = """
        SELECT
            id,
            nome,
            confirmado
        FROM tb_convidados
        WHERE evento_id = %s
        ORDER BY nome
        """

        cursor.execute(sql, (evento_id,))

        convidados = cursor.fetchall()

        cursor.close()
        conn.close()

        return convidados


    def buscar_por_id(self, id_convidado):

        conn = conectar()
        cursor = conn.cursor()

        sql = """
        SELECT *
        FROM tb_convidados
        WHERE id = %s
        """

        cursor.execute(sql, (id_convidado,))

        convidado = cursor.fetchone()

        cursor.close()
        conn.close()

        return convidado

    def atualizar(self, convidado):

        conn = conectar()
        cursor = conn.cursor()

        sql = """
        UPDATE tb_convidados
        SET
            nome = %s,
            confirmado = %s,
            evento_id = %s
        WHERE id = %s
        """

        cursor.execute(sql, (
            convidado.nome,
            convidado.confirmado,
            convidado.evento_id,
            convidado.id
        ))

        conn.commit()

        cursor.close()
        conn.close()

    def excluir(self, id_convidado):

        conn = conectar()
        cursor = conn.cursor()

        sql = """
        DELETE FROM tb_convidados
        WHERE id = %s
        """

        cursor.execute(sql, (id_convidado,))

        conn.commit()

        cursor.close()
        conn.close()