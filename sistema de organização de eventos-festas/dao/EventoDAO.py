from dao.conexao import conectar

class EventoDAO:

    def inserir(self, evento):

        conn = conectar()
        cursor = conn.cursor()
        #comando para inserir um novo evento
        sql = """
        INSERT INTO tb_eventos
        (nome, data_evento, local, tipo)
        VALUES (%s, %s, %s, %s)
        """
        #executa insert
        cursor.execute(sql, (
            evento.nome,
            evento.data_evento,
            evento.local,
            evento.descricao_tipo()
        ))

        conn.commit()

        cursor.close()
        conn.close()
        
    def listar(self):

        conn = conectar()
        cursor = conn.cursor()
        #consulta todos os eventos cadastrados
        sql = "SELECT * FROM tb_eventos"

        cursor.execute(sql)

        eventos = cursor.fetchall()

        cursor.close()
        conn.close()

        return eventos

    def excluir(self, id_evento):

        conn = conectar()
        cursor = conn.cursor()

        sql = "DELETE FROM tb_eventos WHERE id = %s"

        cursor.execute(sql, (id_evento,))

        conn.commit()

        cursor.close()
        conn.close()

    def atualizar(self, evento):

        conn = conectar()
        cursor = conn.cursor()
        #atualiza os dados de um evento existente
        sql = """
        UPDATE tb_eventos
        SET nome = %s,
            data_evento = %s,
            local = %s
        WHERE id = %s
        """

        cursor.execute(sql, (
            evento.nome,
            evento.data_evento,
            evento.local,
            evento.id
        ))

        conn.commit()

        cursor.close()
        conn.close()
        
#crud de eventos