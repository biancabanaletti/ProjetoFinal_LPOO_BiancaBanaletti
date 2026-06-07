from abc import ABC, abstractmethod
from typing import List

from model.Tarefa import Tarefa


class OrdenacaoStrategy(ABC): #strategy ordenação por descrição responsável e tarefa

    @abstractmethod
    def ordenar(
        self,
        tarefas: List[Tarefa]
    ) -> List[Tarefa]:

        pass


class OrdenarPorDescricao(
    OrdenacaoStrategy
):

    def ordenar(
        self,
        tarefas: List[Tarefa]
    ) -> List[Tarefa]:

        return sorted(
            tarefas,
            key=lambda t:
            t.descricao.lower()
        )


class OrdenarPorResponsavel(
    OrdenacaoStrategy
):

    def ordenar(
        self,
        tarefas: List[Tarefa]
    ) -> List[Tarefa]:

        return sorted(
            tarefas,
            key=lambda t:
            (t.responsavel or "zzz").lower()
        )


class OrdenarPorStatus(
    OrdenacaoStrategy
):

    def ordenar(
        self,
        tarefas: List[Tarefa]
    ) -> List[Tarefa]:

        return sorted(
            tarefas,
            key=lambda t:
            t.concluida
        )