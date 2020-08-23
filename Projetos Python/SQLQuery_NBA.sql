--Comando para vizualizar os dados da tabela Excel que foi importada

--Visualizar os dados das 10 primeiras linhas da tabela e das colunas indicadas
SELECT TOP 10 [Rk], [Player], [Pos], [Age]
--Base de dados e o nome da tabela
FROM [Estudos].[dbo].[Sheet1$]

--Visualizar a informação da tabela toda
SELECT * FROM [Estudos].[dbo].[Sheet1$]
