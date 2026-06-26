from datetime import date

from model.Evento import (
    Casamento,
    FestaInfantil,
    EventoCorporativo,
    Evento
)

class EventoFactory: #factory com evento casamento festa de aniversário/infantil e evento corporativo

    @staticmethod
    def criar_evento(
        tipo: str,
        nome: str,
        data_evento: date,
        local: str
    ) -> Evento:

        tipo_formatado = tipo.strip().lower()

        if tipo_formatado in (
            "casamento",
            "wedding"
        ):

            return Casamento(
                nome=nome,
                data_evento=data_evento,
                local=local
            )

        elif tipo_formatado in (
            "festa infantil",
            "festa_infantil",
            "infantil",
            "aniversario"
        ):

            return FestaInfantil(
                nome=nome,
                data_evento=data_evento,
                local=local
            )

        elif tipo_formatado in (
            "corporativo",
            "evento corporativo",
            "empresa"
        ):

            return EventoCorporativo(
                nome=nome,
                data_evento=data_evento,
                local=local
            )

        class EventoGenerico(Evento):

            def descricao_tipo(self) -> str:
                return "generico"

        return EventoGenerico(
            nome=nome,
            data_evento=data_evento,
            local=local
        )