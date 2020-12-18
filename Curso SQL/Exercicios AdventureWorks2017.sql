/*EXERCICIOS AdventureWorks2017*/ 
/*Exercicio 1 - Ver as tabelas "FirstName" e "LastName" - Tabela "Person.Person"*/
select [FirstName], [LastName] from [AdventureWorks2017].[Person].[Person]

/*Exercicio 2 - Saber quantos nomes na coluna "LastName" existem sem os nomes repetidos/duplicados - Tabela "Person.Person"*/
select distinct [LastName] from [AdventureWorks2017].[Person].[Person]

/*Exercicio 3 - Ver o nome de todas as peças que pesam mais de 500Kg e igual ou inferior a 700Kg - Tabela "Person.Product"*/
select [Name] FROM [AdventureWorks2017].[Production].[Product] where Weight > 500 and Weight <= 700

/*Exercicio 4 - Ver todos os empregados(employees) que são casados(married (m)) e são assalariados(salaried) - Tabela "Person.Employee"*/
select * from [AdventureWorks2017].[HumanResources].[Employee] where MaritalStatus = 'm' and SalariedFlag = 'true'

/*Exercicio 5*/
/*Execicio 5.1 - Ver o número que fica na coluna "BusinessEntityID" de Peter Krebs - Tabela "Person.Person"*/
select BusinessEntityID FROM [AdventureWorks2017].[Person].[Person] where FirstName = 'Peter' and LastName = 'krebs'
/*Execicio 5.2* - Ver o email cujo "BusinessEntityID" corresponde ao do Peter Krebs(5.1) - Tabela "Person.EmailAddress"*/
SELECT EmailAddress FROM [AdventureWorks2017].[Person].[EmailAddress] where BusinessEntityID = '26'

/*Exercicio 6 - Ver quantos produtos temos registados - Tabela "Person.Product"*/
select COUNT(*) FROM [AdventureWorks2017].[Production].[Product]

/*Exercico 7 - Ver quantos produtos temos registados - coluna "Size" - Tabela "Person.Product"*/
select COUNT(Size) FROM [AdventureWorks2017].[Production].[Product]

/*Exercicio 8 - Ver quantos produtos diferentes temos registados - coluna "Size" - Tabela "Person.Product"*/
select COUNT(DISTINCT Size) FROM [AdventureWorks2017].[Production].[Product]

/*Exercicio 9 - Ver os 10 primeiros produtos da coluna "ProductID", ordenando a coluna "ListPrice"
por ordem decrescente - Tabela "Person.Product"*/
select Top 10 ProductID from [AdventureWorks2017].[Production].[Product] order by ListPrice desc

/*Exercicio 10 - Ver as colunas "Nome" e "Numero" onde a coluna "ProductID" seja entre 1 e 4 - Tabela "Person.Product"*/
select TOP 4 Name,ProductNumber from [AdventureWorks2017].[Production].[Product] order by ProductID asc
select Name,ProductNumber from [AdventureWorks2017].[Production].[Product] where ProductID >= '1' and ProductID <= '4'
select Name,ProductNumber from [AdventureWorks2017].[Production].[Product] where ProductID between 1 and 4

/*Exercicio 11 - Ver quantos produtos estão registados na coluna "ListPrice" que custam mais do que 1500 - Tabela "Person.Product"*/
select COUNT(ListPrice) from [AdventureWorks2017].[Production].[Product] where ListPrice > 1500

/*Exercicio 12 - Ver quantas pessoas tem o sobrenome que inicia com a letra P - Tabela "Person.Person"*/
select COUNT(LastName) from [AdventureWorks2017].[Person].[Person] where LastName like 'P%'

/*Exercicio 13 - Ver quantas cidades únicas estão registadas - Tabela "Person.Address"*/
select COUNT(DISTINCT City) from [AdventureWorks2017].[Person].[Address]

/*Exercicio 14 - Ver quais cidades únicas estão registadas - Tabela "Person.Address"*/
select DISTINCT City from [AdventureWorks2017].[Person].[Address]

/*Exercicio 15 - Quantos produtos vermelhos tem preço entre 500 a 1000 - Tabela "Person.Product"*/
select COUNT(*) from [AdventureWorks2017].[Production].[Product] where Color = 'red' and ListPrice between 500 and 1000

/*Exercicio 16 - Quantos produtos registados tem a palvra 'road' no nome deles - Tabela "Person.Product*/
select COUNT(*) from [AdventureWorks2017].[Production].[Product] where Name like '%road%'

/*Exercicio 17 - Quantas pessoas tem o mesmo MiddleName (agrupadas por MiddleName) - Tabela "Person.Person"*/
select MiddleName, COUNT(firstname) as "Quantidade" from [AdventureWorks2017].[Person].[Person] group by MiddleName

/*Exercicico 18 - Média da quantidade(quantity) que cada produto é vendido na loja - Tabela*/
select ProductID, AVG(OrderQty) as "Media" from [AdventureWorks2017].[Sales].[SalesOrderDetail] group by ProductID

/*Exercicio 19 - As 10 vendas que no total tiveram os maiores valores de venda (line total) por produto por ordem descendente
Tabela "Sales.SaleOrderDetail"*/
select TOP 10 ProductID, SUM(LineTotal) as "Soma" from [AdventureWorks2017].[Sales].[SalesOrderDetail] group by ProductID 
order by SUM(linetotal) DESC

/*Exercicio 20 - Quantos produtos e qual a quantidade media de produtos temos registados nas ordens de serviço(WorkOrders),
agrupadas por productID - Tabela "Production.WorkOrder"*/
select ProductID, COUNT(ProductID) "Contagem", AVG(orderqty) as "Media" from [AdventureWorks2017].[Production].[WorkOrder]
group by ProductID

/*Exercicio 21 - Ver as provincias(stateProvinceID) com o mair número de registos no sistema, então é preciso encontrar
quais provincias(stateProvinceID) estão registadas na tabela mais de 1000 vezes - Tabela "Person.Address"*/
select StateProvinceID,COUNT(StateProvinceID) as "Quantidades" from [AdventureWorks2017].[Person].[Address]
group by StateProvinceID having COUNT(StateProvinceID) > 1000

/*Exercicio 22 - Ver quais produtos(productID) não estão trazendo em média no minimo 1 milhão em total de vendas(lineTotal)
Tabela "Sales.SaleOrderDetail"*/
select ProductID,AVG(LineTotal) as "Quantidades" from [AdventureWorks2017].[Sales].[SalesOrderDetail] group by ProductID
having AVG(LineTotal) < 1000000

/*Exercicio 23 - Ver e alterar  os nomes das colunas "FirstName" "LastName" - Tabela Person.Person*/
select FirstName as "Nome", LastName as "Apelido" from [AdventureWorks2017].[Person].[Person]

/*Exercicio 24 - Ver e alterar o nome da coluna "ProductNumber" - Tabela "Production.Product"*/
select ProductNumber as "Numero_Produto" from [AdventureWorks2017].[Production].[Product]

/*Exercicio 25 - Ver e alterar o nome da coluna "unitPrice" - Tabela "Sales.SalesOrderDetail"*/
select unitPrice as "Preco_Unitario" from [AdventureWorks2017].[Sales].[SalesOrderDetail]

/*Exercicio 26 - Junção da tabela "Person.PhoneNumberType" e "Person.PersonPhone"*/
select pp.BusinessEntityId, pt.name, pt.PhoneNumberTypeId, pp.PhoneNumber from [AdventureWorks2017].[Person].[PersonPhone] PP
inner join [AdventureWorks2017].[Person].[PhoneNumberType] PT on PT.PhoneNumberTypeID = PP.PhoneNumberTypeID

/*Exercicio 27 - Junção da tabela "Person.Adress" e "Person.StateProvince"*/
select Top 10 PA.AddressID, PA.City, PS.StateProvinceID, PS.Name from [AdventureWorks2017].[Person].[Address] PA
inner join [AdventureWorks2017].[Person].[StateProvince] PS on PS.StateProvinceID = PA.StateProvinceID

/*Exercicio 28 - Ver os dados todos da tabela "Person.Addrress" onde na tabela "Person.StateProvince" os dados da coluna "Nome" são "Alberta"
E onde os dados da coluna "StateProvinceID" das duas tabelas forem iguais*/
select * from [AdventureWorks2017].[Person].[Address] where StateProvinceID IN(select StateProvinceID from 
[AdventureWorks2017].[Person].[StateProvince] where Name = 'Alberta')