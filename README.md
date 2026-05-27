# ProjetoFinal_LPOO_BiancaBanaletti
Projeto Final: Linguagem de Programação Orientada a Objetos e Análise e Projeto de Sistemas

Nome: Bianca Banaletti

Tema: Sistema de Organização de Eventos e Festas

Descrição geral do sistema.

Permite gerenciar e organizar diferentes tipos de eventos e festas, incluindo: Cadastro de eventos (Casamento, Festa Infantil, Evento Corporativo, entre outros); Lista de convidados; Lista de fornecedores; Controle de tarefas; Ordenação de tarefas utilizando Strategy; Criação dos eventos utilizando Factory.

Descrição de cada classe:

Convidados: Representa uma pessoa convidada para o evento. Armazena o nome do convidado; Controla a presença confirmada (True/False); Permite confirmar presença; Define uma saída organizada quando impresso (repr).

Tarefa: Representa uma tarefa que deve ser realizada no evento. Descrição da tarefa; Responsável pela tarefa; Status de conclusão (True/False).

Fornecedor: Representa empresas ou prestadores contratados para o evento. Armazena: nome do fornecedor, tipo de serviço (buffet, decoração, etc) e custo estimado do serviço.

Evento: É a classe principal dos eventos. Armazena: nome do evento, data, local, lista de convidados, lista de tarefas e lista de fornecedores. Possui métodos para: adicionar convidados, confirmar presença, adicionar tarefas e adicionar fornecedores.

Factory: Implementa o Factory no projeto. Cria eventos de: casamento, festa infantil e corporativo.

Strategy: Define ordenação para listas de tarefas. Ordenar por: descrição, responsável e status.

Main: Arquivo principal do sistema. É usado para executar o programa e demonstrar as funcionalidades.


• Instruções de execução.



• Diagrama de classes (imagem) — gerado pelo próprio aluno. 
• Link para o arquivo Documentação do Projeto.md (artefatos APS, quando aplicável).  
• Declaração de uso de IA (se houver) — ferramenta/modelo utilizado e em quais partes.

Documentação do Projeto.md
