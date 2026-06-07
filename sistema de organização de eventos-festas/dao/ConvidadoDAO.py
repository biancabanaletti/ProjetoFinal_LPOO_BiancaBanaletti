from dao.conexao import conectar

class ConvidadoDAO:

    def inserir(self, convidado):

        conn = conectar() #conexão com banco de dados
        cursor = conn.cursor()
        #comando para inserir um novo convidado
        sql = """
        INSERT INTO tb_convidados
        (nome, confirmado)
        VALUES (%s, %s)
        """

        cursor.execute(sql, (
            convidado.nome,
            convidado.confirmado
        ))

        conn.commit()

        cursor.close()
        conn.close()