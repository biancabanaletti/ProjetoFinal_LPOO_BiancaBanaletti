drop table if exists tb_tarefas cascade;
drop table if exists tb_fornecedores cascade;
drop table if exists tb_convidados cascade;
drop table if exists tb_eventos cascade;

create table tb_eventos (
    id serial primary key,
    nome varchar(100) not null,
    data_evento date not null,
    local varchar(100) not null,
    tipo varchar(50) not null,
    status varchar(30) default 'planejado'
);

create table tb_convidados (
    id serial primary key,
    nome varchar(100) not null,
    confirmado boolean default false,
    evento_id integer references tb_eventos(id)
);

create table tb_fornecedores (
    id serial primary key,
    nome varchar(100) not null,
    servico varchar(100) not null,
    valor numeric(10,2),
    evento_id integer references tb_eventos(id)
);

create table tb_tarefas (
    id serial primary key,
    descricao varchar(200) not null,
    responsavel varchar(100) not null,
    concluida boolean default false,
    evento_id integer references tb_eventos(id)
);

insert into tb_eventos
(
    nome,
    data_evento,
    local,
    tipo,
    status
)
values
(
    'Casamento - Maria e Pedro',
    current_date + 30,
    'Passo Fundo',
    'Casamento',
    'Planejado'
);

insert into tb_convidados
(
    nome,
    confirmado,
    evento_id
)
values
(
    'Ana',
    true,
    1
);

insert into tb_fornecedores
(
    nome,
    servico,
    valor,
    evento_id
)
values
(
    'Buffet X',
    'Buffet',
    3500,
    1
);

insert into tb_tarefas
(
    descricao,
    responsavel,
    concluida,
    evento_id
)
values
(
    'Organizar Decoração',
    'João',
    true,
    1
);

select * from tb_eventos;
select * from tb_convidados;
select * from tb_fornecedores;
select * from tb_tarefas;

select current_database();