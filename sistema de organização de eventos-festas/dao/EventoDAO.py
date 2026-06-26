from dao.conexao import conectar

class EventoDAO:

    def inserir(self, evento):

        conn = conectar()
        cursor = conn.cursor()

        sql = """
        INSERT INTO tb_eventos
        (nome, data_evento, local, tipo, status)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            evento.nome,
            evento.data_evento,
            evento.local,
            evento.descricao_tipo(),
            evento.status
        ))

        conn.commit()

        cursor.close()
        conn.close()

    def listar(self):

        conn = conectar()
        cursor = conn.cursor()

        sql = """
        SELECT
            id,
            nome,
            data_evento,
            local,
            tipo,
            status
        FROM tb_eventos
        ORDER BY id
        """

        cursor.execute(sql)

        eventos = cursor.fetchall()

        cursor.close()
        conn.close()

        return eventos

    def buscar_por_id(self, id_evento):

        conn = conectar()
        cursor = conn.cursor()

        sql = """
        SELECT *
        FROM tb_eventos
        WHERE id = %s
        """

        cursor.execute(sql, (id_evento,))

        evento = cursor.fetchone()

        cursor.close()
        conn.close()

        return evento

    def atualizar(self, evento):

        conn = conectar()
        cursor = conn.cursor()

        sql = """
        UPDATE tb_eventos
        SET
            nome = %s,
            data_evento = %s,
            local = %s,
            tipo = %s,
            status = %s
        WHERE id = %s
        """

        cursor.execute(sql, (
            evento.nome,
            evento.data_evento,
            evento.local,
            evento.descricao_tipo(),
            evento.status,
            evento.id
        ))

        conn.commit()

        cursor.close()
        conn.close()

    def excluir(self, id_evento):

        conn = conectar()
        cursor = conn.cursor()

        sql = """
        DELETE FROM tb_eventos
        WHERE id = %s
        """

        cursor.execute(sql, (id_evento,))

        conn.commit()

        cursor.close()
        conn.close()

    def listar_para_combobox(self):

        conn = conectar()
        cursor = conn.cursor()

        sql = """
        SELECT
            id,
            nome
        FROM tb_eventos
        ORDER BY nome
        """

        cursor.execute(sql)

        eventos = cursor.fetchall()

        cursor.close()
        conn.close()

        return eventos