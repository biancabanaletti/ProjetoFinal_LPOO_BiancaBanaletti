from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import date
from typing import List

from model.Convidado import Convidado
from model.Fornecedor import Fornecedor
from model.Tarefa import Tarefa

from model.Strategy import (
    OrdenacaoStrategy,
    OrdenarPorDescricao
)


class Evento(ABC):

    def __init__(
        self,
        nome: str,
        data_evento: date,
        local: str
    ):

        self._id = None

        if not nome.strip():
            raise ValueError(
                "o nome do evento não pode ser vazio"
            )

        if not local.strip():
            raise ValueError(
                "o local do evento não pode ser vazio"
            )
        #dados principais do evento
        self.nome = nome
        self.data_evento = data_evento
        self.local = local

        self.status = "planejado"
        #listas
        self.convidados: List[Convidado] = []
        self.fornecedores: List[Fornecedor] = []
        self.tarefas: List[Tarefa] = []
        #ordenação de tarefas
        self.ordenacao_strategy = OrdenarPorDescricao()

    @property
    def id(self):
        return self._id

    def adicionar_convidado(
        self,
        convidado: Convidado
    ) -> None:

        self.convidados.append(convidado)

    def remover_convidado(
        self,
        nome: str
    ) -> bool:

        for c in self.convidados:

            if c.nome == nome:
                self.convidados.remove(c)
                return True

        return False

    def confirmar_presenca(
        self,
        nome: str
    ) -> bool:

        for c in self.convidados:

            if c.nome == nome:
                c.confirmar()
                return True

        return False

    def listar_confirmados(
        self
    ) -> List[Convidado]:

        return [
            c for c in self.convidados
            if c.confirmado
        ]

    def adicionar_fornecedor(
        self,
        fornecedor: Fornecedor
    ) -> None:

        self.fornecedores.append(fornecedor)

    def remover_fornecedor(
        self,
        nome: str
    ) -> bool:

        for f in self.fornecedores:

            if f.nome == nome:
                self.fornecedores.remove(f)
                return True

        return False

    def adicionar_tarefa(
        self,
        tarefa: Tarefa
    ) -> None:

        self.tarefas.append(tarefa)

    def remover_tarefa(
        self,
        descricao: str
    ) -> bool:

        for t in self.tarefas:

            if t.descricao == descricao:
                self.tarefas.remove(t)
                return True

        return False

    def tarefas_pendentes(
        self
    ) -> List[Tarefa]:

        return [
            t for t in self.tarefas
            if not t.concluida
        ]

    def ordenar_tarefas(
        self
    ) -> List[Tarefa]:

        return self.ordenacao_strategy.ordenar(
            self.tarefas
        )

    def set_ordenacao_strategy(
        self,
        strategy: OrdenacaoStrategy
    ) -> None:

        self.ordenacao_strategy = strategy

    def cancelar_evento(self):

        self.status = "cancelado"

    def finalizar_evento(self):

        self.status = "finalizado"

    @abstractmethod
    def descricao_tipo(self) -> str:
        pass

    def resumo(self) -> str:

        return (
            f"\n===== evento =====\n"
            f"id: {self.id}\n"
            f"nome: {self.nome}\n"
            f"tipo: {self.descricao_tipo()}\n"
            f"data: {self.data_evento.strftime('%d/%m/%Y')}\n"
            f"local: {self.local}\n"
            f"status: {self.status}\n"
            f"convidados: {len(self.convidados)}\n"
            f"fornecedores: {len(self.fornecedores)}\n"
            f"tarefas pendentes: "
            f"{len(self.tarefas_pendentes())}"
        )


class Casamento(Evento):

    def descricao_tipo(self) -> str:
        return "casamento"


class FestaInfantil(Evento):

    def descricao_tipo(self) -> str:
        return "festa infantil"


class EventoCorporativo(Evento):

    def descricao_tipo(self) -> str:
        return "evento corporativo"