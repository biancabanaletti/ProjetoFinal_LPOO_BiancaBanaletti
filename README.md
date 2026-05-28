# ProjetoFinal_LPOO_BiancaBanaletti
Projeto Final: Linguagem de Programação Orientada a Objetos e Análise e Projeto de Sistemas

Nome: Bianca Banaletti

Tema: Sistema de Organização de Eventos e Festas

Descrição geral do sistema.

Permite gerenciar e organizar diferentes tipos de eventos e festas, incluindo: Cadastro de eventos (Casamento, Festa Infantil, Evento Corporativo, entre outros); Lista de convidados; Lista de fornecedores; Controle de tarefas; Ordenação de tarefas utilizando Strategy; Criação dos eventos utilizando Factory.

Descrição de cada classe:

/controller - Responsável por intermediar a comunicação entre a interface gráfica, os models e os DAOs. Controla as regras de negócio e coordena as operações do sistema.

ConvidadoController: Responsável por controlar as operações relacionadas aos convidados do sistema. Intermedia a comunicação entre a interface gráfica, o model Convidado e o ConvidadoDAO. Permite cadastrar convidados, listar convidados, confirmar presença e remover convidados.

EventoController: Responsável pelo controle das operações relacionadas aos eventos. Faz a ligação entre a interface gráfica, o model Evento e o EventoDAO. Permite criar eventos, listar eventos, atualizar informações, excluir eventos e controlar funcionalidades relacionadas aos convidados, fornecedores e tarefas do evento.

FornecedorController: Responsável pelo gerenciamento dos fornecedores do sistema. Realiza a comunicação entre a interface gráfica, o model Fornecedor e o FornecedorDAO. Permite cadastrar fornecedores, listar fornecedores, atualizar dados e remover fornecedores.

/dao - 

EventoDAO: Responsável pelas operações de persistência dos eventos no banco de dados PostgreSQL. Implementa operações de CRUD: inserir, listar, atualizar e excluir eventos.

ConvidadoDAO: Responsável pela persistência dos convidados no banco de dados. Realiza cadastro, listagem, atualização e remoção de convidados.

FornecedorDAO: Responsável pela persistência dos fornecedores no banco de dados PostgreSQL. Gerencia operações de cadastro, consulta, atualização e exclusão de fornecedores.

Convidados: Representa uma pessoa convidada para o evento. Armazena o nome do convidado; Controla a presença confirmada (True/False); Permite confirmar presença; Define uma saída organizada quando impresso (repr).

Tarefa: Representa uma tarefa que deve ser realizada no evento. Descrição da tarefa; Responsável pela tarefa; Status de conclusão (True/False).

Fornecedor: Representa empresas ou prestadores contratados para o evento. Armazena: nome do fornecedor, tipo de serviço (buffet, decoração, etc) e custo estimado do serviço.

Evento: É a classe principal dos eventos. Armazena: nome do evento, data, local, lista de convidados, lista de tarefas e lista de fornecedores. Possui métodos para: adicionar convidados, confirmar presença, adicionar tarefas e adicionar fornecedores.

Factory: Implementa o Factory no projeto. Cria eventos de: casamento, festa infantil e corporativo.

Strategy: Define ordenação para listas de tarefas. Ordenar por: descrição, responsável e status.

Main: Arquivo principal do sistema. É usado para executar o programa e demonstrar as funcionalidades.


• Instruções de execução.

Certificar que todos os arquivos.py estão na pasta

Abra o terminal na pasta do projeto (main.py)

Execute: phyton main.py

A saída mostrará: Criação dos eventos, Adição de convidados, fornecedores e tarefas, Ordenação das tarefas com diferentes estratégias, Saída formatada e organizada.


• Diagrama de classes (imagem) — gerado pelo próprio aluno. 
• Link para o arquivo Documentação do Projeto.md (artefatos APS, quando aplicável).  
• Declaração de uso de IA (se houver) — ferramenta/modelo utilizado e em quais partes.

Documentação do Projeto.md
