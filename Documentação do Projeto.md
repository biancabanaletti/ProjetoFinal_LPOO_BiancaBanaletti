Projeto Final: Linguagem de Programação Orientada a Objetos e Análise e Projeto de Sistemas

Nome: Bianca Banaletti

Tema: Sistema de Organização de Eventos e Festas

1. Descrição e Delimitação do Escopo

Sistema que gerencia diferentes tipos de eventos e festas: festa infantil, evento corporativo e casamento.

Utilizado para organização e controle, como a parte de decoração e fornecedores.

Público-alvo: pessoas que querem contratar serviços de eventos e festas.

2. Fase de Análise
a) Requisitos Funcionais

RF01: O sistema deve listar todos os eventos cadastrados (Festa Infantil, Evento Corporativo, Casamento);

RF02: O sistema deve atualizar a lista de convidados e fornecedores;

RF03: O Sistema deve permitir a criação, leitura, exclusão e atualização dos dados;

RF04: O sistema deve armazenar o nome do convidado e controlar a presença (confirmada ou não);

RF05: O sistema deve mostrar as tarefas que serão realizadas no evento, bem como o responsável pela tarefa;

RF06: O sistema armazena o nome dos prestadores contratados para o evento e o tipo de serviço;

RF07: O sistema atualiza a data e o local do evento;

RF08: O sistema deve permitir cadastrar novos eventos com informações como nome, data, local e tipo do evento;

RF09: O sistema deve permitir consultar a quantidade de convidados confirmados para cada evento;

RF10: O sistema deve permitir consultar os fornecedores cadastrados em cada evento.

b) Requisitos Não Funcionais

RNF01: O sistema deve possuir interface gráfica desenvolvida utilizando a biblioteca Tkinter.

RNF02: O sistema deve possuir interface gráfica simples e de fácil utilização;

RNF03: O sistema deve armazenar os dados de forma persistente em banco de dados ou arquivos;

RNF04: As alterações realizadas devem ser refletidas imediatamente na interface do sistema.

RNF05: O sistema deve garantir a integridade e segurança dos dados cadastrados;

c) Regras de Negócio

RN01: Um convidado não pode confirmar presença mais de uma vez para o mesmo evento;

RN02: Todo evento deve possuir nome, data e local obrigatoriamente.

d) Documento de Requisitos

[Documento de Definição de Requisitos.pdf](https://github.com/user-attachments/files/28656694/Documento.de.Definicao.de.Requisitos.pdf)

e) Diagrama de Casos de Uso

<img width="684" height="506" alt="image" src="https://github.com/user-attachments/assets/9b2df9ba-969f-4154-98db-9ea6ff29fef1" />



f) Documentação dos Casos de Uso

[Documentação do Caso de Uso.pdf](https://github.com/user-attachments/files/28656693/Documentacao.do.Caso.de.Uso.pdf)


g) Diagrama de Classes – Modelo Conceitual

<img width="523" height="373" alt="image" src="https://github.com/user-attachments/assets/4c22eb80-678d-4c3d-b996-6c151d33acfd" />


3. Fase de Projeto

a) Diagrama de Classes

[Diagrama de Classes.pdf](https://github.com/user-attachments/files/28656689/Diagrama.de.Classes.pdf)


b) Segundo Diagrama UML - Diagrama de Sequência

<img width="1215" height="556" alt="image" src="https://github.com/user-attachments/assets/322bd6d7-e8a8-4e0a-a316-6c3193732748" />


4. Considerações Finais

Principais desafios encontrados: Os principais desafios foram modelar o sistema utilizando Linguagem de Programação Orientada a Objetos, integrar a interface gráfica com o banco de dados e aplicar corretamente os padrões de projeto exigidos. Também foi necessário realizar testes e ajustes para garantir o funcionamento adequado das funcionalidades desenvolvidas.

Aprendizados obtidos: o desenvolvimento do projeto permitiu compreender de forma prática a relação entre as etapas de análise, projeto e implementação de software. A elaboração dos diagramas UML auxiliou na modelagem do sistema antes da codificação, tornando a implementação mais organizada.

Possíveis melhorias futuras: o sistema poderá receber novas funcionalidades, como autenticação de usuários, gerenciamento completo de tarefas pela interface gráfica, geração de relatórios em PDF, pesquisa e filtragem de eventos, edição e exclusão de registros diretamente pelas telas e integração mais completa com o banco de dados.

5. Referências

Ferramentas utilizadas para construção dos diagramas: Astah e PlantUML.

• Declaração de uso de IA:

Foi utilizada a ferramenta ChatGPT (OpenAI GPT-5.5) como apoio para esclarecimento de dúvidas, correção de erros, explicação de conceitos e auxílio na revisão de trechos de código. Todo o desenvolvimento, adaptação e validação final da solução foram realizados pela autora do trabalho.
