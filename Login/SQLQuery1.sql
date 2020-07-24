CREATE TABLE Facebook(

	Email VARCHAR(80) primary key,
	Password NVARCHAR(50) NULL
);

GO
INSERT INTO Facebook(Email,Password) VALUES('testes.programacao.teste@gmail.com','testes1234' )

go 

CREATE TABLE Username(

	Name VARCHAR(80) NULL,
);

GO