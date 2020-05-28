IF OBJECT_ID('NewsInfo') IS NOT NULL
BEGIN
    SELECT * FROM FinancialDB.dbo.NewsInfo
END
ELSE
BEGIN
    CREATE TABLE FinancialDB.dbo.NewsInfo (
    Id int IDENTITY(1,1) PRIMARY KEY,
    Fecha  smalldatetime NOT NULL,
    Seccion  varchar(100),
    Encabezado varchar(500),
    Web  varchar(500)
    )
END