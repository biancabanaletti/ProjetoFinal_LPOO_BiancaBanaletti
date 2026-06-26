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

/dao - Camada responsável pela comunicação com o banco de dados PostgreSQL. Realiza operações de persistência, como cadastro, consulta, atualização e exclusão de informações no banco. Os arquivos DAO utilizam a conexão criada em Conexao.py para executar comandos SQL.

Conexao: Responsável por estabelecer conexão com o banco de dados PostgreSQL utilizado pelo sistema.

EventoDAO: Responsável pelas operações de persistência dos eventos no banco de dados PostgreSQL. Implementa operações de CRUD: inserir, listar, atualizar e excluir eventos.

ConvidadoDAO: Responsável pela persistência dos convidados no banco de dados. Realiza cadastro, listagem, atualização e remoção de convidados.

FornecedorDAO: Responsável pela persistência dos fornecedores no banco de dados PostgreSQL. Gerencia operações de cadastro, consulta, atualização e exclusão de fornecedores.

/database - lpoo_projeto_biancabanaletti.sql

Arquivo responsável pela criação das tabelas do banco de dados PostgreSQL. Define as tabelas de eventos, convidados, fornecedores e tarefas, além de inserir dados iniciais de teste e relacionamentos entre entidades.

/model - Camada responsável pela lógica e estrutura dos dados do sistema. Contém as classes principais da aplicação, como Evento, Convidado, Fornecedor, Tarefa, Pagamento e Decoracao. Também implementa regras de negócio e padrões de projeto utilizados no sistema, como Factory e Strategy.

Convidado: Representa uma pessoa convidada para o evento. Armazena o nome do convidado; Controla a presença confirmada (True/False); Permite confirmar presença; Define uma saída organizada quando impresso (repr).

Decoracao: Representa a decoração do evento. Armazena: tema da decoração, cor principal e orçamento estimado. Permite atualizar o orçamento e definir uma saída organizada com resumo das informações.

Evento: É a classe principal dos eventos. Armazena: nome do evento, data, local, status do evento, lista de convidados, lista de tarefas e lista de fornecedores. Possui métodos para: adicionar e remover convidados, confirmar presença, adicionar e remover tarefas, adicionar e remover fornecedores, listar convidados confirmados, ordenar tarefas e finalizar/cancelar eventos.

Factory: Implementa o Factory no projeto. Cria eventos de: casamento, festa infantil e corporativo.

Fornecedor: Representa empresas ou prestadores contratados para o evento. Armazena: nome do fornecedor, tipo de serviço (buffet, decoração, etc) e custo estimado do serviço.

Pagamento: Representa os pagamentos relacionados ao evento. Armazena: valor, forma de pagamento e status do pagamento. Permite confirmar ou cancelar pagamentos.

Strategy: Define ordenação para listas de tarefas. Ordenar por: descrição, responsável e status.

Tarefa: Representa uma tarefa que deve ser realizada no evento. Descrição da tarefa; Responsável pela tarefa; Status de conclusão (True/False).

TipoEvento: Implementa um Enum para representar os tipos de eventos do sistema. Define categorias padronizadas como: casamento, festa infantil, evento corporativo, formatura e aniversário.

Usuario: Representa os usuários do sistema. Armazena: login e senha do usuário. Permite alterar senha e realizar validações básicas de acesso.

/view - Camada responsável pela interface gráfica do sistema utilizando Tkinter. Contém as telas da aplicação, permitindo a interação do usuário com o sistema através de janelas, botões, campos de texto e menus.

TelaEvento: Responsável pela interface principal do sistema utilizando Tkinter. Permite acessar as funcionalidades relacionadas aos eventos, como cadastro, visualização e gerenciamento. Também possui botões para abrir as telas de convidados, fornecedores e informações do sistema.

TelaConvidado: Responsável pela interface gráfica de gerenciamento dos convidados do evento. Permite visualizar informações dos convidados e controlar funcionalidades relacionadas à confirmação de presença.

TelaFornecedor: Responsável pela interface gráfica de gerenciamento dos fornecedores contratados para o evento. Permite visualizar e organizar informações como nome do fornecedor, serviço prestado e valores.

TelaSobre: Tela informativa do sistema. Exibe informações sobre o projeto, disciplina, objetivo do sistema e identificação da aluna responsável pelo desenvolvimento.

/Run

Janela.py: Arquivo responsável por iniciar a interface gráfica do sistema. Executa a janela principal da aplicação e realiza a abertura da TelaEvento, funcionando como ponto inicial do programa utilizando Tkinter.

Tela de Início:

<img width="892" height="693" alt="image" src="https://github.com/user-attachments/assets/c7f31cf8-9ab7-4e44-80aa-7e89da52dd9d" />


Evento cadastrado:

<img width="892" height="694" alt="image" src="https://github.com/user-attachments/assets/737ce028-ff82-492d-8859-8acf915c3e1c" />


Tela de Convidados:

<img width="844" height="623" alt="image" src="https://github.com/user-attachments/assets/339996b2-f4cf-497c-9b4c-a2d5a2b28ea2" />

Convidado cadastrado:

<img width="840" height="621" alt="image" src="https://github.com/user-attachments/assets/a6c9fb2f-da69-4e9c-99c2-5f5ac5347a12" />


Tela de Fornecedores:

<img width="891" height="641" alt="image" src="https://github.com/user-attachments/assets/e7dfb3da-fbbd-458e-ae23-329b197fa849" />


Fornecedor cadastrado:

<img width="894" height="641" alt="image" src="https://github.com/user-attachments/assets/0fd1e71d-0ca0-4bfe-a15f-87d2d869a377" />


Tela Sobre:

<img width="791" height="522" alt="image" src="https://github.com/user-attachments/assets/2e35b10a-752b-4e7c-a5bb-b4fc33ca8aba" />



Main: Arquivo principal do sistema. É usado para executar o programa e demonstrar as funcionalidades aplicadas.


• Instruções de execução.

#Banco de Dados
lpoo_projeto_biancabanaletti.sql

O PostgreSQL foi utilizado como sistema gerenciador de banco de dados do projeto, sendo responsável pelo armazenamento persistente das informações do sistema de organização de eventos.

No arquivo SQL, foram executadas as seguintes etapas:

1. Remoção das tabelas existentes utilizando drop table if exists, permitindo recriar o banco sem conflitos durante os testes do sistema.

2. Criação das tabelas principais do sistema:
tb_eventos
tb_convidados
tb_fornecedores
tb_tarefas

3. Definição das chaves primárias (primary key) e relacionamentos entre tabelas utilizando foreign key, permitindo associar convidados, fornecedores e tarefas a um evento específico.

4. Definição dos tipos de dados adequados para cada atributo, como:
varchar
date
boolean
numeric

5. Inserção de dados de teste utilizando comandos insert into, permitindo validar o funcionamento do sistema e testar consultas.

6. Realização de consultas utilizando select * from, utilizadas para verificar os dados cadastrados nas tabelas.

• No VSCode:

Certificar que todos os arquivos.py estão na pasta.

Abra o terminal na pasta do projeto (main.py).

Execute: phyton main.py

Ao executar o arquivo main.py, o sistema realiza uma demonstração das funcionalidades implementadas utilizando os padrões de projeto Factory e Strategy. O padrão Factory é utilizado para criar diferentes tipos de eventos (casamento, festa infantil e evento corporativo) por meio da classe EventoFactory, centralizando e simplificando o processo de criação dos objetos.

Após a criação dos eventos, são adicionados convidados, fornecedores e tarefas, além da confirmação de presença de alguns convidados. Também é demonstrada a alteração do status de tarefas concluídas e a utilização do padrão Strategy para ordenar as tarefas de diferentes formas, como por descrição, responsável e status.

Ao final da execução, o sistema exibe no terminal um resumo completo de cada evento, apresentando suas informações, convidados, fornecedores e tarefas organizadas conforme a estratégia de ordenação aplicada.

Abra o terminal na pasta do projeto (janela.py).

Execute: python janela.py (ou apenas Run Python File).

O arquivo janela.py é responsável por iniciar a interface gráfica do sistema. Ao ser executado, ele abre a tela principal de gerenciamento de eventos (TelaEvento), desenvolvida com a biblioteca Tkinter.

A tela principal permite o cadastro de eventos por meio do preenchimento do nome do evento e do local de realização. Também possui uma barra de menus com opções para gerenciamento de convidados, fornecedores e acesso à tela de informações do sistema ("Sobre"). O sistema realiza validação dos campos obrigatórios e apresenta mensagens de aviso ou confirmação para o usuário através de caixas de diálogo.

• Diagrama de classes (imagem)

<img width="1520" height="475" alt="image" src="https://github.com/user-attachments/assets/49f78c26-2b89-41b5-8045-0b7956808503" />


• Seção de Conclusão / Aprendizado:

Principais desafios encontrados: Os principais desafios foram modelar o sistema utilizando Linguagem de Programação Orientada a Objetos, integrar a interface gráfica com o banco de dados e aplicar corretamente os padrões de projeto exigidos. Também foi necessário realizar testes e ajustes para garantir o funcionamento adequado das funcionalidades desenvolvidas.

Aprendizados obtidos: o desenvolvimento do projeto permitiu compreender de forma prática a relação entre as etapas de análise, projeto e implementação de software. A elaboração dos diagramas UML auxiliou na modelagem do sistema antes da codificação, tornando a implementação mais organizada.

• Declaração de uso de IA:

Foi utilizada a ferramenta ChatGPT (OpenAI GPT-5.5) como apoio para esclarecimento de dúvidas, correção de erros, explicação de conceitos e auxílio na revisão de trechos de código. Todo o desenvolvimento, adaptação e validação final da solução foram realizados pela autora do trabalho.
