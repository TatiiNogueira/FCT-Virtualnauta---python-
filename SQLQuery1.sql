/*Criar Tabela*/
Create table dados(
Número char(50),
Nome varchar(20) not null,
Apelido varchar(20) not null,
);

/*Introduzir valores na tabela*/
INSERT INTO dados (Número, Nome, Apelido)
VALUES 
('1', 'Maria', 'Paula'),
('2', 'João', 'Carlos'),
('3', 'Rute', 'Cardoso')
