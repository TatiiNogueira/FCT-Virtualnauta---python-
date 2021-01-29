 /*Escrever o código com letra maiuscula ou minuscula é indiferente*
 Apenas os nomes das coisas é que tem de ser escritos exatamente da mesma forma*/
 
 /* Criar uma Base de dados
 O Nome pode ser o que quisermos mas não pode conter espaços */
 create database Nome;

 /* Eliminar uma Base de dados
 Em Nome colocamos o nome da Base de Dados que queremos eliminar*/
 drop database Nome;

 /*Restaurar uma Base de Dados
 RECOMENDAÇÂO: Colocar o ficheiro dentro da pasta "C:\Users\Pubblic\Downloads"
 1 - Clicamos com o botão direito do rato em Databases
 2 - Selecionamos "Restore DataBase..."
 3 - Clicamos em "Device"
 4 - Clicamos no botão "..." que fica no final da linha de "Device"
 5 - Clicamos em "Add"
 6 - Procuramos pelo ficheiro, para isso em "Backup File Location" colocamos o caminho da pasta "C:\Users\Pubblic"
 para selecionarmo o ficheiro clicamos 2x sobre o ficheiro OU clicamos uma vez sobre o ficheiro e depois em "OK"
 7 - Clicamos em "OK" e novamente em "OK"
 8 -Irá aparecer a mensagem "Database 'Nome_da_Base_de__Dados' restored sucessfully" clicamos em "OK"
 E está feita a restauração da Base de Dados
 */

 /* Retornar todas as colunas de uma tabela
 O * significa todas a colunas*/
 SELECT * FROM [Nome_da_Base_De_Dados][Nome_Tabela]

 /*Ver os dados, fazendo com que não apareça os nomes repetidos*/
 SELECT DISTINCT Nome_da_Coluna FROM [Nome_da_Base_De_Dados][Nome_Tabela]

 /*Saber o número de Rows da tabela
 Se quisere saber o número de Rows mas que não conte os valores repetido/duplicados batsa colocar count(DISTINCT e o resto*/
 select COUNT(*) from [Nome_da_Base_De_Dados][Nome_Tabela]

 /*Saber o número de Rows de uma ou várias colunas em especifico da tabela
 Se quisere saber o número de Rows mas que não conte os valores repetido/duplicados batsa colocar count(DISTINCT e o resto*/
 select COUNT(Nome_da_Coluna, Nome_De_Outra_Coluna,....) from [Nome_da_Base_De_Dados][Nome_Tabela]
      
 /*Between - Significa entre
 Também podemos utilizar para datas (Formato da data 0000-00-00)*/
 select * from [Nome_da_Base_De_Dados][Nome_Tabela] where Nome_da_Coluna between valor_1 and valor_2
 select * from [Nome_da_Base_De_Dados][Nome_Tabela] where Nome_da_Coluna between data_1 and data_2

 /*IN - Significa igual*/
 select * from [Nome_da_Base_De_Dados][Nome_Tabela] where Nome_da_Coluna IN (Valor_1,Valor_2....)

 /*% - O que vier a seguir do % não interessa, retorna me tudo o que começar por o que eu indiquei
 No exemplo 1 irá retornar tudo o que começar por 'Ar', não me interessa o que vem depois
 No exemplo 2 irá retornar tudo o que tiver no meio 'essa' não me interessa o que vem antes nem o que vem depois
 No exemplo 3 irá retornar tudo o que tiver no meio 'ro', não me interessa o que vem antes, mas depois do 'ro' só pode ter uma letra/numero*/
 select * from [Nome_da_Base_De_Dados][Nome_Tabela] where Nome_da_Coluna like  /*Exemplo1*/ 'Ar%'
									       /*Exemplo2*/ '%essa%'
									       /*Exemplo3*/ '%ro_'

/*Atribuir nome a uma tabela*/
/*Inicio do Código*/ AS "Nome_que_queremos_dar_à_Coluna" /*Fim do Código*/

/*Somar valores*/
select SUM(nome_coluna) from [Nome_da_Base_De_Dados][Nome_Tabela]

/*Média dos valores de uma coluna*/
select AVG(nome_coluna) from [Nome_da_Base_De_Dados][Nome_Tabela]

/*UNION - Permite juntar os dados de duas tabela
Junta a primeira coluna que indicamos da tabela 1 e a a primeira coluna que indicamos da tabela 2 na mesma coluna e assim por diante
Mas o datatype das colunas tem de ser o mesmo ou seja se na tabela 1 a primeira coluna que indicamos for inta primeira coluna que indicamos da tabela 2 
também tem de ser int e assim por diante e apenas junta os dados que não são repetidos*/
Select nome_coluna1,nome_coluna2, .... from [Nome_da_Base_De_Dados][Nome_Tabela_1]
UNION
Select nome_coluna1,nome_coluna2, .... from [Nome_da_Base_De_Dados][Nome_Tabela_2]
/*Se quiseremos ver todos os dados incluindo os repetidos basta escrevermo à frente de "UNION" "ALL"*/
Select nome_coluna1,nome_coluna2, .... from [Nome_da_Base_De_Dados][Nome_Tabela_1]
UNION ALL
Select nome_coluna1,nome_coluna2, .... from [Nome_da_Base_De_Dados][Nome_Tabela_2]

/*Transferir dados de uma tabela para outra tabela*/
INSERT INTO [Nome_da_Base_De_Dados][Nome_Tabela_1] (nome_coluna1,nome_coluna2)(SELECT nome_coluna1,nome_coluna2 FROM [Nome_da_Base_De_Dados][Nome_Tabela_2])
