/*Exercicios Northwind*/

/*Exercicio 1 - Ver todos os que clientes que moram na mesma região - Tabela "Customers"*/
select A.ContactName,B.ContactName
from [Northwind].[dbo].[Customers] A, [Northwind].[dbo].[Customers] B
where A.Region = B.Region

/*Exercicio 2 - Ver nome e data de todos os funcionários que forama contratados no mes anterior*/
select A.firstname, A.hiredate, B.firstname, B.hiredate
From [Northwind].[dbo].[Employees] A, [Northwind].[dbo].[Employees] B
where DATEPART(YEAR,A.HireDate) = DATEPART(year, B.hiredate)

/*Exercicio 3 - Ver os produtos que tem o mesmo percentual de desconto - Tabela "Order Details"*/
select A.productID, A.Discount, B.productID, B.Discount
From [Northwind].[dbo].[Order Details] A, [Northwind].[dbo].[Order Details] B
where A.Discount = B.Discount