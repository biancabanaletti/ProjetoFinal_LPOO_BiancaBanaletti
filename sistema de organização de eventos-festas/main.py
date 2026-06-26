from datetime import date

from model.Factory import EventoFactory
from model.Convidado import Convidado
from model.Fornecedor import Fornecedor
from model.Tarefa import Tarefa

from model.Strategy import (
    OrdenarPorDescricao,
    OrdenarPorResponsavel,
    OrdenarPorStatus,
)


def imprimir_tarefas(
    titulo,
    tarefas
):

    print(f"\n{titulo}")

    for t in tarefas:
        print(f" - {t}")


def imprimir_convidados(
    titulo,
    convidados
):

    print(f"\n{titulo}")

    for c in convidados:
        print(f" - {c}")


def imprimir_fornecedores(
    titulo,
    fornecedores
):

    print(f"\n{titulo}")

    for f in fornecedores:
        print(f" - {f}")


def main():

    print(
        "\n=== sistema de organização de eventos ===\n"
    )

    # factory casamento festa de aniversário/infantil evento corporativo
    casamento = EventoFactory.criar_evento(
        "casamento",
        nome="Casamento Ana & João",
        data_evento=date(2026, 3, 21),
        local="Chácara"
    )

    festa = EventoFactory.criar_evento(
        "festa infantil",
        nome="Aniversário do Pedro - 7 anos",
        data_evento=date(2025, 12, 5),
        local="Buffet"
    )

    corporativo = EventoFactory.criar_evento(
        "corporativo",
        nome="Reunião Anual da Empresa",
        data_evento=date(2025, 11, 30),
        local="Auditório Central"
    )

    # convidados casamento
    casamento.adicionar_convidado(
        Convidado("Ana")
    )

    casamento.adicionar_convidado(
        Convidado("João")
    )

    casamento.adicionar_convidado(
        Convidado("Maria")
    )

    casamento.confirmar_presenca("João")
    casamento.confirmar_presenca("Maria")

    # convidados festa
    festa.adicionar_convidado(
        Convidado("Pedro")
    )

    festa.adicionar_convidado(
        Convidado("Lucas")
    )

    festa.adicionar_convidado(
        Convidado("Julia")
    )

    festa.confirmar_presenca("Pedro")
    festa.confirmar_presenca("Julia")

    # convidados corporativo
    corporativo.adicionar_convidado(
        Convidado("Diretor Carlos")
    )

    corporativo.adicionar_convidado(
        Convidado("Gerente Marina")
    )

    corporativo.adicionar_convidado(
        Convidado("Equipe de TI")
    )

    corporativo.adicionar_convidado(
        Convidado("Financeiro")
    )

    corporativo.confirmar_presenca(
        "Gerente Marina"
    )

    corporativo.confirmar_presenca(
        "Financeiro"
    )

    # fornecedores
    casamento.adicionar_fornecedor(
        Fornecedor(
            "Buffet Livre",
            "buffet",
            3000.0
        )
    )

    festa.adicionar_fornecedor(
        Fornecedor(
            "Decoration Kids",
            "decoração",
            800.0
        )
    )

    corporativo.adicionar_fornecedor(
        Fornecedor(
            "Som & Luz",
            "equipamentos",
            1500.0
        )
    )

    # tarefas casamento
    casamento.adicionar_tarefa(
        Tarefa(
            "Enviar convites",
            "Ana"
        )
    )

    casamento.adicionar_tarefa(
        Tarefa(
            "Comprar alianças",
            "João"
        )
    )

    casamento.adicionar_tarefa(
        Tarefa(
            "Contratar fotógrafo",
            "Ana"
        )
    )

    casamento.tarefas[1].concluir()

    # tarefas festa
    festa.adicionar_tarefa(
        Tarefa(
            "Comprar bolo",
            "Mãe"
        )
    )

    festa.adicionar_tarefa(
        Tarefa(
            "Reservar brinquedos",
            "Pai"
        )
    )

    festa.adicionar_tarefa(
        Tarefa(
            "Montar lembrancinhas",
            "Mãe"
        )
    )

    festa.tarefas[0].concluir()

    # tarefas corporativo
    corporativo.adicionar_tarefa(
        Tarefa(
            "Organizar apresentação",
            "Marina"
        )
    )

    corporativo.adicionar_tarefa(
        Tarefa(
            "Checar equipamento de som",
            "Equipe de TI"
        )
    )

    corporativo.adicionar_tarefa(
        Tarefa(
            "Confirmar palestrantes",
            "Carlos"
        )
    )

    corporativo.tarefas[1].concluir()

    # casamento
    print(
        "\n==================== casamento ===================="
    )

    print(casamento.resumo())

    imprimir_convidados(
        "Convidados:",
        casamento.convidados
    )

    imprimir_fornecedores(
        "Fornecedores:",
        casamento.fornecedores
    )

    imprimir_tarefas(
        "Tarefas (ordenado por descrição):",
        OrdenarPorDescricao().ordenar(
            casamento.tarefas
        )
    )

    # festa infantil
    print(
        "\n==================== festa infantil ===================="
    )

    print(festa.resumo())

    imprimir_convidados(
        "Convidados:",
        festa.convidados
    )

    imprimir_fornecedores(
        "Fornecedores:",
        festa.fornecedores
    )

    imprimir_tarefas(
        "Tarefas (ordenado por responsável):",
        OrdenarPorResponsavel().ordenar(
            festa.tarefas
        )
    )

    # evento corporativo
    print(
        "\n==================== evento corporativo ===================="
    )

    print(corporativo.resumo())

    imprimir_convidados(
        "Convidados:",
        corporativo.convidados
    )

    imprimir_fornecedores(
        "Fornecedores:",
        corporativo.fornecedores
    )

    imprimir_tarefas(
        "Tarefas (ordenado por status):",
        OrdenarPorStatus().ordenar(
            corporativo.tarefas
        )
    )

    print("\n")


if __name__ == "__main__":
    main()